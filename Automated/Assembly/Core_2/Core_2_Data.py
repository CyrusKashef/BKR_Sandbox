import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class CORE_2_DATA_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._LIST_OF_SKYBOXES = [0x7BD, 0x7BF, 0x7C1, 0x7C2, 0x7C3, 0x7C4,
                            0x7C5, 0x7C6, 0x7C9, 0x7CA, 0x7CC, 0x7CD]
        self._LIST_OF_CLOUDS = [0x7BE, 0x7C0, 0x7C7, 0x7C8, 0x7CB]
        self._SKYBOX_CLOUD_START_INDEX = 0x87B0
        self._MUSIC_START_INDEX = 0xA8F0

    ################
    ### CHECKSUM ###
    ################

    def _calculate_checksum(self):
        '''Runs through algorithm to calculate the new checksum (Might not work?)'''
        crc1 = 0
        crc2 = 0xFFFFFFFF
        for val in self._mmap:
            byte = int.from_bytes(val, "big")
            crc1 = crc1 + byte
            crc2 = crc2 ^ (byte << (crc1 & 0x17))
        return crc2

    def _set_checksum(self, crc):
        '''Sets the checksum located in Core 2's Data'''
        self._write_bytes(0xF264, 4, crc)
    
    ###########################
    ### SKYBOXES AND CLOUDS ###
    ###########################
    # Starting Index: 0x87B0
    # 0x00: MAP
    # 0x02: 00 00
    # 0x04: Skybox ID
    # 0x06: 00 00 (padding)
    # 0x08: Scale (float)
    # 0x0C: Rotation Speed (float)
    # 0x10: Cloud 1 ID
    # 0x12: 00 00 (padding)
    # 0x14: Scale (float)
    # 0x18: Rotation Speed (float)
    # 0x1C: Cloud 2 ID
    # 0x1E: 00 00 (padding)
    # 0x20: Scale (float)
    # 0x24: Rotation Speed (float)
    # Map Intervals: 0x28

    def _set_skybox_and_clouds(self, map_count, new_skybox=None, new_cloud1=None, new_cloud2=None):
        '''Sets a new skybox and new clouds for each area that allows skyboxes/clouds'''
        map_start_index = self._SKYBOX_CLOUD_START_INDEX + map_count * 0x28
        self._write_bytes(map_start_index + 0x04, 2, new_skybox)
        cloud1 = self._read_byte_list_to_int(map_start_index + 0x10, 2)
        if(new_cloud1 and (cloud1 > 0)):
            self._write_bytes(map_start_index + 0x10, 2, cloud1)
        cloud2 = self._read_byte_list_to_int(map_start_index + 0x1C, 2)
        if(new_cloud2 and (cloud2 > 1)):
            self._write_bytes(map_start_index + 0x1C, 2, cloud2)
    
    #############
    ### MUSIC ###
    #############
    # 0x00: Map
    # 0x02: Music 1
    # 0x04: Music 2
    # 0x06: Music 3
    # Music Intervals: 0x08

    def _set_music(self, map_count, new_music1=None, new_music2=None, new_music3=None):
        '''Sets new music for each area with music'''
        music_start_index = self._MUSIC_START_INDEX + map_count * 0x8
        music1 = self._read_byte_list_to_int(music_start_index + 0x2, 2)
        if((new_music1 != None) and (music1 < 0x100) and (music1 > 0)):
            self._write_bytes(music_start_index + 0x2, 2, new_music1)
        music2 = self._read_byte_list_to_int(music_start_index + 0x4, 2)
        if((new_music2 != None) and (music2 < 0x100) and (music2 > 1)):
            self._write_bytes(music_start_index + 0x4, 2, new_music2)
        music3 = self._read_byte_list_to_int(music_start_index + 0x6, 2)
        if((new_music3 != None) and (music3 < 0x100) and (music3 > 1)):
            self._write_bytes(music_start_index + 0x6, 2, new_music3)
    
    #########################
    ### MARKER COLLISIONS ###
    #########################
    ### Structure ###
    # 0x00: Marker ID
    # 0x02: Or Parameter (Whatever is below gets OR'd with this)
    # 0x04: Claw Swipe Collision Parameters
    # 0x06: Roll Attack Collision Parameters
    # 0x08: Jumping On Them Collision Parameters
    # 0x0A: Rat-A-Tap Rap Collision Parameters
    # 0x0C: Beak Barge Collision Parameters
    # 0x0E: Beak Buster Collision Parameters
    # 0x10: Beak Bomb Collision Parameters
    # 0x12: Egg Firing Collision Parameters
    # 0x14: Wonderwing Collision Parameters
    # 0x16: Croc Bite Collision Parameters
    # 0x18: Other Contact Collision Parameters
    # Marker Intervals: 0x1A
    ### Collisions Parameter Format ###
    # (Bitwise): aaaa bb ccc dd eee ff
    # aaaa = Does BK Bounce Off Or Take Damage? And By How Much?
    #   0 | 0000 Nothing
    #   1 | 0001 Damage BK, Tiny Push Back
    #   2 | 0010 Damage BK, Small Push Back
    #   3 | 0011 Damage BK, Decent Push Back
    #   4 | 0100 Damage BK, Far Push Back
    #   5 | 0101 Damage BK, Very Far Push Back
    #   6 | 0110 Nothing
    #   7 | 0111 Bounce Off, Tiny Push Back
    #   8 | 1000 Bounce Off, Small Push Back
    #   9 | 1001 Bounce Off, Decent Push Back
    #   A | 1010 Bounce Off, Far Push Back
    #   B | 1011 Bounce Off, Very Far Push Back
    #   C | 1100 Nothing
    #   D | 1101 Nothing
    #   E | 1110 Nothing
    #   F | 1111 Nothing
    # bb = State When Collision Is Triggered?
    #   01 = Alternate State
    #   10 = Killed
    # ccc = Sound Effect When Collision Is Triggered?
    # dd = How Much Damage Does BK Take?
    # eee = How Many Hits To Trigger?
    # ff = Number Of Honeycombs Spawned When Triggered?

    def _create_collision_parameter_value(self, effect_to_bk, next_state, sound_effect,
                                                bk_damage, hit_count, num_of_honeycombs):
        '''Creates a two byte collision value from a series of bit parameters'''
        int_val = ((effect_to_bk << 12) + (next_state << 10) + (sound_effect << 7) +
                   (bk_damage << 5) + (hit_count << 2) + num_of_honeycombs)
        return int_val
    
    def _get_bitwise_collision_parameter_values(self, index_start):
        '''Returns a series of bit parameters from a two byte collision value'''
        int_val = self._read_byte_list_to_int(index_start, 2)
        effect_to_bk = (int_val >> 12) & 0b1111
        next_state = (int_val >> 10) & 0b11
        sound_effect = (int_val >> 7) & 0b111
        bk_damage = (int_val >> 5) & 0b11
        hit_count = (int_val >> 2) & 0b111
        num_of_honeycombs = int_val & 0b11
        return effect_to_bk, next_state, sound_effect, bk_damage, hit_count, num_of_honeycombs
    
    def _set_collision_parameter(self, index_start, effect_to_bk, next_state, sound_effect,
                                       bk_damage, hit_count, num_of_honeycombs):
        '''Sets a new collision value using a series of bit parameters'''
        int_val = self._create_collision_parameter_value(effect_to_bk, next_state, sound_effect,
                                               bk_damage, hit_count, num_of_honeycombs)
        self._write_bytes(index_start, 2, int_val)
    
    #######################
    ### ACTOR STRUCTURE ###
    #######################
    # In some parts of the game, when an object breaks/dies, something is left behind.
    # Example: MM Hut notes
    # Start Index: 0x2ED0
    # 0x00: unk0
    # 0x02: padding?
    # 0x04: Actor ID
    # 0x08: Count
    # 0x0C: unkC
    # 0x0E: unkE
    # 0x10: unk10
    # 0x14: unk14
    # 0x18: unk18
    # 0x1C: unk1C
    # 0x20: unk20
    # 0x24: unk24
    # 0x28: unk28
    # 0x2C: unk2C
    # 0x30: unk30
    # Actor Intervals: 0x34

    def _set_actor_list(self, start_index, unk0=None, actor_id=None, count=None, unkC=None,
                        unkE=None, unk10=None, unk14=None, unk18=None, unk1C=None, unk20=None,
                        unk24=None, unk28=None, unk2C=None, unk30=None):
        '''Modifies what item(s) drop from breaking/killing an object'''
        if(unk0 != None):
            self._write_bytes(start_index, 2, unk0)
        if(actor_id != None):
            self._write_bytes(start_index + 0x4, 4, actor_id)
        if(count != None):
            self._write_bytes(start_index + 0x8, 4, count)
        if(unkC != None):
            self._write_bytes(start_index + 0xC, 2, unkC)
        if(unkE != None):
            self._write_bytes(start_index + 0xE, 4, unkE)
        if(unk10 != None):
            self._write_bytes(start_index + 0x10, 4, unk10)
        if(unk14 != None):
            self._write_bytes(start_index + 0x14, 4, unk14)
        if(unk18 != None):
            self._write_bytes(start_index + 0x18, 4, unk18)
        if(unk1C != None):
            self._write_bytes(start_index + 0x1C, 4, unk1C)
        if(unk20 != None):
            self._write_bytes(start_index + 0x20, 4, unk20)
        if(unk24 != None):
            self._write_bytes(start_index + 0x24, 4, unk24)
        if(unk28 != None):
            self._write_bytes(start_index + 0x28, 4, unk28)
        if(unk2C != None):
            self._write_bytes(start_index + 0x2C, 4, unk2C)
        if(unk30 != None):
            self._write_bytes(start_index + 0x30, 4, unk30)
    
    ##################
    ### ANIMATIONS ###
    ##################

    def _get_animation_functions_dict(self, start_index):
        '''Gets the animation functions for a particular object'''
        animation_dict = {
            "ID": self._read_byte_list_to_int(start_index, 4),
            "INIT": self._read_byte_list_to_int(start_index + 0x04, 4),
            "Update": self._read_byte_list_to_int(start_index + 0x08, 4),
            "End": self._read_byte_list_to_int(start_index + 0x0C, 4),
            "Interrupt": self._read_byte_list_to_int(start_index + 0x10, 4),
            }
        return animation_dict

    def _get_all_animation_functions_dict(self):
        '''Gets the animation functions for all objects'''
        animations_dict = {}
        for start_index in range(0x294, 0xE9C, 0x14):
            animations_dict[start_index] = self._get_animation_functions(start_index)
    
    def _set_animation_functions(self, start_index, animation_dict):
        '''Sets the animation functions for a particular object'''
        self._write_bytes(start_index + 0x04, 4, animation_dict["INIT"])
        self._write_bytes(start_index + 0x08, 4, animation_dict["Update"])
        self._write_bytes(start_index + 0x0C, 4, animation_dict["End"])
        self._write_bytes(start_index + 0x10, 4, animation_dict["Interrupt"])

    ############
    ### MISC ###
    ############
    
    def _adjust_menu_for_witchs_lair(self):
        '''Changes the positioning, ordering, and sprite of the pause menu when 'Exit To Witch's Lair' is added'''
        # Positioning
        self._write_bytes(0x8F5C, 2, 0x2D) # "RETURN TO GAME"
        self._write_bytes(0x8F6C, 2, 0x4C) # "EXIT TO WITCH'S LAIR"
        self._write_bytes(0x8F7C, 2, 0x6B) # "VIEW TOTALS"
        self._write_bytes(0x8F8C, 2, 0x8A) # "SAVE AND QUIT"
        # Ordering
        self._write_bytes(0x8F60, 4, 0x3DCCCCCD) # "EXIT TO WITCH'S LAIR"
        self._write_bytes(0x8F70, 4, 0x3E4CCCCD) # "VIEW TOTALS"
        self._write_bytes(0x8F80, 4, 0x3E99999A) # "SAVE AND QUIT"
        # Sprite
        self._write_byte(0x8F6E, 0x05) # Give "EXIT TO WITCH'S LAIR" the Gruntilda Sprite
    
    ###################
    ### BANJO SPEED ###
    ###################

    # Termite
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/ant.c#L10

    def _get_termite_speed_dict(self):
        '''Gets the values for the Termite BK's speed'''
        speed_dict = {
            "Termite_Unk0": self._read_byte_list_to_float(0x13D0, 4),
            "Termite_Unk1": self._read_byte_list_to_float(0x13D4, 4),
            "Termite_Unk2": self._read_byte_list_to_float(0x13D8, 4),
            "Termite_Unk3": self._read_byte_list_to_float(0x13DC, 4),
            "Termite_Unk4": self._read_byte_list_to_float(0x13E0, 4),
            "Termite_Unk5": self._read_byte_list_to_float(0x13E4, 4),
        }
        return speed_dict

    def _set_termite_speed_dict(self, speed_dict):
        '''Sets the values for the Termite BK's speed'''
        self._write_float_bytes(0x13D0, speed_dict["Termite_Unk0"])
        self._write_float_bytes(0x13D4, speed_dict["Termite_Unk1"])
        self._write_float_bytes(0x13D8, speed_dict["Termite_Unk2"])
        self._write_float_bytes(0x13DC, speed_dict["Termite_Unk3"])
        self._write_float_bytes(0x13E0, speed_dict["Termite_Unk4"])
        self._write_float_bytes(0x13E4, speed_dict["Termite_Unk5"])

    # Crocodile
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/croc.c#L10

    def _get_crocodile_speed_dict(self):
        '''Gets the values for the Crocodile BK's speed'''
        speed_dict = {
            "Crocodile_Unk0": self._read_byte_list_to_float(0x1570, 4),
            "Crocodile_Unk1": self._read_byte_list_to_float(0x1574, 4),
            "Crocodile_Unk2": self._read_byte_list_to_float(0x1578, 4),
            "Crocodile_Unk3": self._read_byte_list_to_float(0x157C, 4),
            "Crocodile_Unk4": self._read_byte_list_to_float(0x1580, 4),
            "Crocodile_Unk5": self._read_byte_list_to_float(0x1584, 4),
            "Crocodile_Unk6": self._read_byte_list_to_float(0x1588, 4),
            "Crocodile_Unk7": self._read_byte_list_to_float(0x158C, 4),
        }
        return speed_dict

    def _set_crocodile_speed_dict(self, speed_dict):
        '''Sets the values for the Crocodile BK's speed'''
        self._write_float_bytes(0x1570, speed_dict["Crocodile_Unk0"])
        self._write_float_bytes(0x1574, speed_dict["Crocodile_Unk1"])
        self._write_float_bytes(0x1578, speed_dict["Crocodile_Unk2"])
        self._write_float_bytes(0x157C, speed_dict["Crocodile_Unk3"])
        self._write_float_bytes(0x1580, speed_dict["Crocodile_Unk4"])
        self._write_float_bytes(0x1584, speed_dict["Crocodile_Unk5"])
        self._write_float_bytes(0x1588, speed_dict["Crocodile_Unk6"])
        self._write_float_bytes(0x158C, speed_dict["Crocodile_Unk7"])

    # Pumpkin
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/pumpkin.c#L11

    def _get_pumpkin_speed_dict(self):
        '''Gets the values for the Pumpkin BK's speed'''
        speed_dict = {
            "Pumpkin_Unk0": self._read_byte_list_to_float(0x1760, 4),
            "Pumpkin_Unk1": self._read_byte_list_to_float(0x1764, 4),
            "Pumpkin_Unk2": self._read_byte_list_to_float(0x1768, 4),
            "Pumpkin_Unk3": self._read_byte_list_to_float(0x176C, 4),
            "Pumpkin_Unk4": self._read_byte_list_to_float(0x1770, 4),
            "Pumpkin_Unk5": self._read_byte_list_to_float(0x1774, 4),
        }
        return speed_dict

    def _set_pumpkin_speed_dict(self, speed_dict):
        '''Sets the values for the Pumpkin BK's speed'''
        self._write_float_bytes(0x1760, speed_dict["Pumpkin_Unk0"])
        self._write_float_bytes(0x1764, speed_dict["Pumpkin_Unk1"])
        self._write_float_bytes(0x1768, speed_dict["Pumpkin_Unk2"])
        self._write_float_bytes(0x176C, speed_dict["Pumpkin_Unk3"])
        self._write_float_bytes(0x1770, speed_dict["Pumpkin_Unk4"])
        self._write_float_bytes(0x1774, speed_dict["Pumpkin_Unk5"])

    # Walrus
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/walrus.c#L10

    def _get_walrus_speed_dict(self):
        '''Gets the values for the Walrus BK's speed'''
        speed_dict = {
            "Walrus_Unk0": self._read_byte_list_to_float(0x1830, 4),
            "Walrus_Unk1": self._read_byte_list_to_float(0x1834, 4),
            "Walrus_Unk2": self._read_byte_list_to_float(0x1838, 4),
            "Walrus_Unk3": self._read_byte_list_to_float(0x183C, 4),
            "Walrus_Unk4": self._read_byte_list_to_float(0x1840, 4),
            "Walrus_Unk5": self._read_byte_list_to_float(0x1844, 4),
            "Walrus_Unk6": self._read_byte_list_to_float(0x1848, 4),
            "Walrus_Unk7": self._read_byte_list_to_float(0x184C, 4),
            "Walrus_Unk8": self._read_byte_list_to_float(0x1850, 4),
            "Walrus_Unk9": self._read_byte_list_to_float(0x1854, 4),
            "Walrus_UnkA": self._read_byte_list_to_float(0x1858, 4),
            "Walrus_UnkB": self._read_byte_list_to_float(0x185C, 4),
        }
        return speed_dict

    def _set_walrus_speed_dict(self, speed_dict):
        '''Sets the values for the Walrus BK's speed'''
        self._write_float_bytes(0x1830, speed_dict["Walrus_Unk0"])
        self._write_float_bytes(0x1834, speed_dict["Walrus_Unk1"])
        self._write_float_bytes(0x1838, speed_dict["Walrus_Unk2"])
        self._write_float_bytes(0x183C, speed_dict["Walrus_Unk3"])
        self._write_float_bytes(0x1840, speed_dict["Walrus_Unk4"])
        self._write_float_bytes(0x1844, speed_dict["Walrus_Unk5"])
        self._write_float_bytes(0x1848, speed_dict["Walrus_Unk6"])
        self._write_float_bytes(0x184C, speed_dict["Walrus_Unk7"])
        self._write_float_bytes(0x1850, speed_dict["Walrus_Unk8"])
        self._write_float_bytes(0x1854, speed_dict["Walrus_Unk9"])
        self._write_float_bytes(0x1858, speed_dict["Walrus_UnkA"])
        self._write_float_bytes(0x185C, speed_dict["Walrus_UnkB"])

    # BK Talon Trot
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/bTrot.c#L9

    def _get_bk_talon_trot_speed_dict(self):
        '''Gets the values for the BK's speed in Talon Trot'''
        speed_dict = {
            "Talon_Trot_Unk0": self._read_byte_list_to_float(0x1500, 4),
            "Talon_Trot_Unk1": self._read_byte_list_to_float(0x1504, 4),
            "Talon_Trot_Unk2": self._read_byte_list_to_float(0x1508, 4),
            "Talon_Trot_Unk3": self._read_byte_list_to_float(0x150C, 4),
            "Talon_Trot_Unk4": self._read_byte_list_to_float(0x1510, 4),
            "Talon_Trot_Unk5": self._read_byte_list_to_float(0x1514, 4),
            "Talon_Trot_Unk6": self._read_byte_list_to_float(0x1518, 4),
            "Talon_Trot_Unk7": self._read_byte_list_to_float(0x151C, 4),
            "Talon_Trot_Unk8": self._read_byte_list_to_float(0x1520, 4),
            "Talon_Trot_Unk9": self._read_byte_list_to_float(0x1524, 4),
            "Talon_Trot_UnkA": self._read_byte_list_to_float(0x1528, 4),
            "Talon_Trot_UnkB": self._read_byte_list_to_float(0x152C, 4),
            "Talon_Trot_UnkC": self._read_byte_list_to_float(0x1530, 4),
        }
        return speed_dict

    def _set_bk_talon_trot_speed_dict(self, speed_dict):
        '''Sets the values for the BK's speed in Talon Trot'''
        self._write_float_bytes(0x1500, speed_dict["Talon_Trot_Unk0"])
        self._write_float_bytes(0x1504, speed_dict["Talon_Trot_Unk1"])
        self._write_float_bytes(0x1508, speed_dict["Talon_Trot_Unk2"])
        self._write_float_bytes(0x150C, speed_dict["Talon_Trot_Unk3"])
        self._write_float_bytes(0x1510, speed_dict["Talon_Trot_Unk4"])
        self._write_float_bytes(0x1514, speed_dict["Talon_Trot_Unk5"])
        self._write_float_bytes(0x1518, speed_dict["Talon_Trot_Unk6"])
        self._write_float_bytes(0x151C, speed_dict["Talon_Trot_Unk7"])
        self._write_float_bytes(0x1520, speed_dict["Talon_Trot_Unk8"])
        self._write_float_bytes(0x1524, speed_dict["Talon_Trot_Unk9"])
        self._write_float_bytes(0x1528, speed_dict["Talon_Trot_UnkA"])
        self._write_float_bytes(0x152C, speed_dict["Talon_Trot_UnkB"])
        self._write_float_bytes(0x1530, speed_dict["Talon_Trot_UnkC"])

    # Banjo Surface Swim
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/swim.c#L11

    def _get_banjo_surface_swim_speed_dict(self):
        '''Gets the values for the BK's speed while swimming above water'''
        speed_dict = {
            "Swim_Min_Horz_Velocity": self._read_byte_list_to_float(0x17B0, 4),
            "Swim_Max_Horz_Velocity": self._read_byte_list_to_float(0x17B4, 4),
            "Swim_Min_Duration": self._read_byte_list_to_float(0x17B8, 4),
            "Swim_Max_Duration": self._read_byte_list_to_float(0x17BC, 4),
        }
        return speed_dict

    def _set_banjo_surface_swim_speed_dict(self, speed_dict):
        '''Sets the values for the BK's speed while swimming above water'''
        self._write_float_bytes(0x17B0, speed_dict["Swim_Min_Horz_Velocity"])
        self._write_float_bytes(0x17B4, speed_dict["Swim_Max_Horz_Velocity"])
        self._write_float_bytes(0x17B8, speed_dict["Swim_Min_Duration"])
        self._write_float_bytes(0x17BC, speed_dict["Swim_Max_Duration"])

    # Banjo Walk
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/walk.c#L20

    def _get_banjo_walk_speed_dict(self):
        '''Gets the values for the BK's walking speed'''
        speed_dict = {
            "Creep_Min_Velocity": self._read_byte_list_to_float(0x17E0, 4),
            "Creep_Max/Slow_Walk_Min_Velocity_Threshold": self._read_byte_list_to_float(0x17E4, 4),
            "Slow_Walk_Max/Walk_Min_Threshold": self._read_byte_list_to_float(0x17E8, 4),
            "Walk_Max/Walk_Fast_Min_Threshold": self._read_byte_list_to_float(0x17EC, 4),
            "Walk_Fast_Max_Velocity": self._read_byte_list_to_float(0x17F0, 4),
            "Mud_Min_Velocity": self._read_byte_list_to_float(0x17F4, 4),
            "Mud_Max_Velocity": self._read_byte_list_to_float(0x17F8, 4),
            "Skid_Velocity": self._read_byte_list_to_float(0x17FC, 4),
            "Walk_Slowest_Slow_Duration": self._read_byte_list_to_float(0x1800, 4),
            "Walk_Fastest_Slow_Duration": self._read_byte_list_to_float(0x1804, 4),
            "Creep_Slowest_Duration": self._read_byte_list_to_float(0x1808, 4),
            "Creep_Fastest_Duration": self._read_byte_list_to_float(0x180C, 4),
            "Walk_Slowest_Duration": self._read_byte_list_to_float(0x1810, 4),
            "Walk_Fast_Duration": self._read_byte_list_to_float(0x1814, 4),
            "Walk_Slowest_Fast_Walk_Duration": self._read_byte_list_to_float(0x1818, 4),
            "Walk_Fastest_Fast_Walk_Duration": self._read_byte_list_to_float(0x181C, 4),
            "Mud_Slowest_Duration": self._read_byte_list_to_float(0x1820, 4),
            "Mud_Fastest_Duration": self._read_byte_list_to_float(0x1824, 4),
        }
        return speed_dict

    def _set_banjo_walk_speed_dict(self, speed_dict):
        '''Sets the values for the BK's walking speed'''
        self._write_float_bytes(0x17E0, speed_dict["Creep_Min_Velocity"])
        self._write_float_bytes(0x17E4, speed_dict["Creep_Max/Slow_Walk_Min_Velocity_Threshold"])
        self._write_float_bytes(0x17E8, speed_dict["Slow_Walk_Max/Walk_Min_Threshold"])
        self._write_float_bytes(0x17EC, speed_dict["Walk_Max/Walk_Fast_Min_Threshold"])
        self._write_float_bytes(0x17F0, speed_dict["Walk_Fast_Max_Velocity"])
        self._write_float_bytes(0x17F4, speed_dict["Mud_Min_Velocity"])
        self._write_float_bytes(0x17F8, speed_dict["Mud_Max_Velocity"])
        self._write_float_bytes(0x17FC, speed_dict["Skid_Velocity"])
        self._write_float_bytes(0x1800, speed_dict["Walk_Slowest_Slow_Duration"])
        self._write_float_bytes(0x1804, speed_dict["Walk_Fastest_Slow_Duration"])
        self._write_float_bytes(0x1808, speed_dict["Creep_Slowest_Duration"])
        self._write_float_bytes(0x180C, speed_dict["Creep_Fastest_Duration"])
        self._write_float_bytes(0x1810, speed_dict["Walk_Slowest_Duration"])
        self._write_float_bytes(0x1814, speed_dict["Walk_Fast_Duration"])
        self._write_float_bytes(0x1818, speed_dict["Walk_Slowest_Fast_Walk_Duration"])
        self._write_float_bytes(0x181C, speed_dict["Walk_Fastest_Fast_Walk_Duration"])
        self._write_float_bytes(0x1820, speed_dict["Mud_Slowest_Duration"])
        self._write_float_bytes(0x1824, speed_dict["Mud_Fastest_Duration"])
    
    # Long Legs
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/bLongLeg.c#L9

    # Flight
    # Possibly: https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/bFly.c#L185

    ##############################
    ### LEVEL MODEL ASSIGNMENT ###
    ##############################
    # Decomp: https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/mapModel.c#L28
    # Start Index: 0x7650
    # 0x00: Map Id
    # 0x02: Side A Id
    # 0x04: Side B Id
    # 0x06: Unk3
    # 0x08: unk4
    # 0x0A: unk5
    # 0x0C: unk6
    # 0x0E: unk7
    # 0x10: unk8
    # 0x12: padding
    # 0x14: Scale
    # Actor Intervals: 0x18

    def _get_level_models(self, start_index):
        '''Gets the level models for a particular map'''
        level_models_dict = {
            "Map": self._read_byte_list_to_int(start_index, 2),
            "Side_A": self._read_byte_list_to_int(start_index + 0x2, 2),
            "Side_B": self._read_byte_list_to_int(start_index + 0x4, 2),
            "Unk3": self._read_byte_list_to_int(start_index + 0x6, 2),
            "Unk4": self._read_byte_list_to_int(start_index + 0x8, 2),
            "Unk5": self._read_byte_list_to_int(start_index + 0xA, 2),
            "Unk6": self._possible_negative(self._read_byte_list_to_int(start_index + 0xC, 2), 2),
            "Unk7": self._possible_negative(self._read_byte_list_to_int(start_index + 0xE, 2), 2),
            "Unk8": self._possible_negative(self._read_byte_list_to_int(start_index + 0x10, 2), 2),
            "Scale": self._read_byte_list_to_float(start_index + 0x14, 4),
        }
        return level_models_dict
    
    def _get_all_level_models(self):
        '''
        Gets the level models for every map
        '''
        level_models_dict = {}
        for level_count, start_index in enumerate(range(0x7650, 0x8250, 0x18)):
            level_models_dict[level_count] = self._get_level_models(start_index)
        return level_models_dict

    def _set_level_models(self, start_index, replacement_dict):
        '''Sets the level models for a particular map'''
        self._write_bytes(start_index, 2, replacement_dict["Map"])
        self._write_bytes(start_index + 0x2, 2, replacement_dict["Side_A"])
        self._write_bytes(start_index + 0x4, 2, replacement_dict["Side_B"])
        self._write_bytes(start_index + 0x6, 2, replacement_dict["Unk3"])
        self._write_bytes(start_index + 0x8, 2, replacement_dict["Unk4"])
        self._write_bytes(start_index + 0xA, 2, replacement_dict["Unk5"])
        self._write_bytes(start_index + 0xC, 2, self._possible_negative_to_positive(replacement_dict["Unk6"], 2))
        self._write_bytes(start_index + 0xE, 2, self._possible_negative_to_positive(replacement_dict["Unk7"], 2))
        self._write_bytes(start_index + 0x10, 2, self._possible_negative_to_positive(replacement_dict["Unk8"], 2))
        self._write_float_bytes(start_index + 0x14, replacement_dict["Scale"])
    
    def _set_all_level_models(self, replacement_dict):
        '''Sets the level models for every map'''
        for level_count, start_index in enumerate(range(0x7650, 0x8250, 0x18)):
            self._set_level_models(start_index, replacement_dict[level_count])
    
    ################
    ### SECTIONS ###
    ################
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/gc/section.c#L19

    def _get_gc_section_info(self, section_num):
        # 0x8280 GC Section Min
        # 0x8680 GC Section Max
        curr_index = 0x8280 + 0x8 * section_num
        curr_map = self._read_byte_list_to_int(curr_index, 2)
        curr_level = self._read_byte_list_to_int(curr_index + 0x2, 2)
        curr_dev_string_offset = self._read_byte_list_to_int(curr_index + 0x4, 4)
        return curr_map, curr_level, curr_dev_string_offset
    
    def _set_gc_section_info(self, section_num, map_id=None, new_level_id=None, new_dev_string_offset=None):
        curr_index = 0x8280 + 0x8 * section_num
        if(map_id != None):
            self._write_bytes(curr_index, 2, map_id)
        if(new_level_id != None):
            self._write_bytes(curr_index + 0x2, 2, new_level_id)
        if(new_dev_string_offset != None):
            self._write_bytes(curr_index + 0x4, 4, new_dev_string_offset)

    def _get_gc_section_info_dict(self):
        gc_section_info_dict = {}
        for section_num in range(0x1, 0x9B):
            curr_map, curr_level, curr_dev_string_offset = self._get_gc_section_info(section_num)
            gc_section_info_dict[section_num] = {
                "Map": curr_map,
                "Level": curr_level,
                "Dev_String_Offset": curr_dev_string_offset,
            }
        return gc_section_info_dict
    
    def _set_gc_section_info_dict(self, gc_section_info_dict):
        for section_num in range(0x1, 0x9B):
            curr_map = gc_section_info_dict[section_num]["Map"]
            curr_level = gc_section_info_dict[section_num]["Level"]
            curr_dev_string_offset = gc_section_info_dict[section_num]["Dev_String_Offset"]
            self._set_gc_section_info(section_num, curr_map, curr_level, curr_dev_string_offset)

    
    #############################
    ### WARP PAD DESTINATIONS ###
    #############################

    def _mm_warp_pad(self, new_map_id, new_exit_id):
        '''When exiting MM via the warp pad/'Exit To Witch's Lair', this is the map and entry the player is warped to'''
        # Default 0x69, 0x2
        self._write_bytes(0x8FD0, 2, new_map_id)
        self._write_bytes(0x8FD2, 2, new_exit_id)

    def _ttc_warp_pad(self, new_map_id, new_exit_id):
        '''When exiting TTC via the warp pad/'Exit To Witch's Lair', this is the map and entry the player is warped to'''
        # Default 0x6D, 0x4
        self._write_bytes(0x8FD4, 2, new_map_id)
        self._write_bytes(0x8FD6, 2, new_exit_id)

    def _cc_warp_pad(self, new_map_id, new_exit_id):
        '''When exiting CC via the warp pad/'Exit To Witch's Lair', this is the map and entry the player is warped to'''
        # Default 0x70, 0x2
        self._write_bytes(0x8FD8, 2, new_map_id)
        self._write_bytes(0x8FDA, 2, new_exit_id)

    def _bgs_warp_pad(self, new_map_id, new_exit_id):
        '''When exiting BGS via the warp pad/'Exit To Witch's Lair', this is the map and entry the player is warped to'''
        # Default 0x72, 0x2
        self._write_bytes(0x8FDC, 2, new_map_id)
        self._write_bytes(0x8FDE, 2, new_exit_id)

    def _fp_warp_pad(self, new_map_id, new_exit_id):
        '''When exiting FP via the warp pad/'Exit To Witch's Lair', this is the map and entry the player is warped to'''
        # Default 0x6F, 0x6
        self._write_bytes(0x8FE0, 2, new_map_id)
        self._write_bytes(0x8FE2, 2, new_exit_id)
    
    # 0x8FE4 has -1 -1 here? Probably scrapped level

    def _gv_warp_pad(self, new_map_id, new_exit_id):
        '''When exiting GV via the warp pad/'Exit To Witch's Lair', this is the map and entry the player is warped to'''
        # Default 0x6E, 0x3
        self._write_bytes(0x8FE8, 2, new_map_id)
        self._write_bytes(0x8FEA, 2, new_exit_id)

    def _ccw_warp_pad(self, new_map_id, new_exit_id):
        '''When exiting CCW via the warp pad/'Exit To Witch's Lair', this is the map and entry the player is warped to'''
        # Default 0x79, 0x6
        self._write_bytes(0x8FEC, 2, new_map_id)
        self._write_bytes(0x8FEE, 2, new_exit_id)

    def _rbb_warp_pad(self, new_map_id, new_exit_id):
        '''When exiting RBB via the warp pad/'Exit To Witch's Lair', this is the map and entry the player is warped to'''
        # Default 0x77, 0x2
        self._write_bytes(0x8FF0, 2, new_map_id)
        self._write_bytes(0x8FF2, 2, new_exit_id)

    def _mmm_warp_pad(self, new_map_id, new_exit_id):
        '''When exiting MMM via the warp pad/'Exit To Witch's Lair', this is the map and entry the player is warped to'''
        # Default 0x75, 0x2
        self._write_bytes(0x8FF4, 2, new_map_id)
        self._write_bytes(0x8FF6, 2, new_exit_id)

    def _sm_warp_pad(self, new_map_id, new_exit_id):
        '''When exiting SM via the warp pad/'Exit To Witch's Lair', this is the map and entry the player is warped to'''
        # Default 0x69, 0x12
        self._write_bytes(0x8FD0, 2, new_map_id)
        self._write_bytes(0x8FD2, 2, new_exit_id)
    
    ########################################
    ### NON SPIRAL MOUNTAIN MOVE CAMERAS ###
    ########################################
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/ch/mole.c#L33

    def _get_move_camera_dict(self):
        move_camera_dict = {}
        starting_index = 0x4834
        ending_index = 0x4870
        for count, curr_index in enumerate(range(starting_index, ending_index, 0x6)):
            move_camera_dict[count] = {
                "Learn_Text": self._read_byte_list_to_int(curr_index, 2),
                "Refresher_Text": self._read_byte_list_to_int(curr_index + 0x2, 2),
                "Camera": self._read_byte(curr_index + 0x4),
                "Ability": self._read_byte(curr_index + 0x5),
            }
        return move_camera_dict

    def _set_move_camera_dict(self, move_camera_dict):
        starting_index = 0x4834
        ending_index = 0x4870
        for count, curr_index in enumerate(range(starting_index, ending_index, 0x6)):
            self._write_bytes(curr_index, 2, move_camera_dict[count]["Learn_Text"])
            self._write_bytes(curr_index + 0x2, 2, move_camera_dict[count]["Refresher_Text"])
            self._write_byte(curr_index + 0x4, move_camera_dict[count]["Camera"])
            self._write_byte(curr_index + 0x5, move_camera_dict[count]["Ability"])

    ###################
    ### MODEL SWAPS ###
    ###################

    def _replace_sir_slush_model(self, asset_id):
        self._write_bytes(0x50E4, 2, asset_id)

if __name__ == '__main__':
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    FILE_NAME = "FCF698"
    core_2_data_obj = CORE_2_DATA_CLASS(FILE_DIR, FILE_NAME)