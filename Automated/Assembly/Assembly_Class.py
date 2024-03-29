import sys
from random import seed, randint, uniform, choice, triangular

sys.path.append(".")
from Automated.Assembly.Core_1.Core_1_Code import CORE_1_CODE_CLASS
from Automated.Assembly.Core_1.Core_1_Data import CORE_1_DATA_CLASS
from Automated.Assembly.Core_2.Core_2_Code import CORE_2_CODE_CLASS
from Automated.Assembly.Core_2.Core_2_Data import CORE_2_DATA_CLASS
from Automated.Assembly.Spiral_Mountain.Spiral_Mountain_Code import SPIRAL_MOUNTAIN_CODE_CLASS
from Automated.Assembly.Spiral_Mountain.Spiral_Mountain_Data import SPIRAL_MOUNTAIN_DATA_CLASS
from Automated.Assembly.Mumbos_Mountain.Mumbos_Mountain_Code import MUMBOS_MOUNTAIN_CODE_CLASS
from Automated.Assembly.Treasure_Trove_Cove.Treasure_Trove_Cove_Code import TREASURE_TROVE_COVE_CODE_CLASS
from Automated.Assembly.Treasure_Trove_Cove.Treasure_Trove_Cove_Data import TREASURE_TROVE_COVE_DATA_CLASS
from Automated.Assembly.Clankers_Cavern.Clankers_Cavern_Code import CLANKERS_CAVERN_CODE_CLASS
from Automated.Assembly.Bubblegloop_Swamp.Bubblegloop_Swamp_Code import BUBBLEGLOOP_SWAMP_CODE_CLASS
from Automated.Assembly.Freezeezy_Peak.Freezeezy_Peak_Code import FREEZEEZY_PEAK_CODE_CLASS
from Automated.Assembly.Gobis_Valley.Gobis_Valley_Code import GOBIS_VALLEY_CODE_CLASS
from Automated.Assembly.Gobis_Valley.Gobis_Valley_Data import GOBIS_VALLEY_DATA_CLASS
from Automated.Assembly.Mad_Monster_Mansion.Mad_Monster_Mansion_Code import MAD_MONSTER_MANSION_CODE_CLASS
from Automated.Assembly.Mad_Monster_Mansion.Mad_Monster_Mansion_Data import MAD_MONSTER_MANSION_DATA_CLASS
from Automated.Assembly.Rusty_Bucket_Bay.Rusty_Bucket_Bay_Code import RUSTY_BUCKET_BAY_CODE_CLASS
from Automated.Assembly.Click_Clock_Wood.Click_Clock_Wood_Code import CLICK_CLOCK_WOOD_CODE_CLASS
from Automated.Assembly.Gruntildas_Lair.Gruntildas_Lair_Code import GRUNTILDAS_LAIR_CODE_CLASS
from Automated.Assembly.Gruntildas_Lair.Gruntildas_Lair_Data import GRUNTILDAS_LAIR_DATA_CLASS
from Automated.Assembly.Final_Battle.Final_Battle_Code import FINAL_BATTLE_CODE_CLASS
from Automated.Assembly.Cutscenes.Cutscenes_Code import CUTSCENES_CODE_CLASS

from Data_Files.Marker_Dict import ENEMY_MARKER_DICT
from Data_Files.Move_Dict import MOVE_DICT
from Data_Files.Sandcastle_Cheat_Dict import SIMPLIFIED_CHEAT_DICT, MOVE_CHEAT_DICT
from Data_Files.Static_Markers_Dict import BANJO_SOULIE_MARKERS
from Data_Files.Setups.Bottles_Dict import BOTTLES_DICT, SEPARATED_BOTTLES_DICT

class ASSEMBLY_CLASS():
    def __init__(self, file_dir):
        # CONSTANTS
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        self._DECOMPRESSED_EXTENSION = "-Decompressed"
        self._LIST_OF_SKYBOXES = [0x7BD, 0x7BF, 0x7C1, 0x7C2, 0x7C3, 0x7C4,
                                  0x7C5, 0x7C6, 0x7C9, 0x7CA, 0x7CC, 0x7CD]
        self._LIST_OF_CLOUDS = [0x7BE, 0x7C0, 0x7C7, 0x7C8, 0x7CB]
        self._SKYBOX_CLOUD_START_INDEX = 0x87B0
        self._MARKER_INDEX_START = 0xD530
        self._COLLECTIBLE_MAX_DICT = {
            "Jiggy": 100,
            "Token": 115,
            "Honeycomb": 24,
            "Note": 900,
        }

        # CLASSES
        self._core_1_code = CORE_1_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}F19250{self._DECOMPRESSED_EXTENSION}")
        self._core_1_data = CORE_1_DATA_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}F362EB{self._DECOMPRESSED_EXTENSION}")
        self._core_2_code = CORE_2_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}F37F90{self._DECOMPRESSED_EXTENSION}")
        self._core_2_data = CORE_2_DATA_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}F9CAE0{self._DECOMPRESSED_EXTENSION}")
        self._spiral_mountain_code = SPIRAL_MOUNTAIN_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FC4810{self._DECOMPRESSED_EXTENSION}")
        self._spiral_mountain_data = SPIRAL_MOUNTAIN_DATA_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FC6C0F{self._DECOMPRESSED_EXTENSION}")
        self._mumbos_mountain_code = MUMBOS_MOUNTAIN_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FB24A0{self._DECOMPRESSED_EXTENSION}")
        self._mumbos_mountain_data = None
        self._treasure_trove_cove_code = TREASURE_TROVE_COVE_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FAE860{self._DECOMPRESSED_EXTENSION}")
        self._treasure_trove_cove_data = TREASURE_TROVE_COVE_DATA_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FB1AEB{self._DECOMPRESSED_EXTENSION}")
        self._clankers_cavern_code = CLANKERS_CAVERN_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FA3FD0{self._DECOMPRESSED_EXTENSION}")
        self._clankers_cavern_data = None
        self._bubblegloop_swamp_code = BUBBLEGLOOP_SWAMP_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FB44E0{self._DECOMPRESSED_EXTENSION}")
        self._bubblegloop_swamp_data = None
        self._freezeezy_peak_code = FREEZEEZY_PEAK_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FBEBE0{self._DECOMPRESSED_EXTENSION}")
        self._freezeezy_peak_data = None
        self._gobis_valley_code = GOBIS_VALLEY_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FA9150{self._DECOMPRESSED_EXTENSION}")
        self._gobis_valley_data = GOBIS_VALLEY_DATA_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FAE27E{self._DECOMPRESSED_EXTENSION}")
        self._mad_monster_mansion_code = MAD_MONSTER_MANSION_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FA5F50{self._DECOMPRESSED_EXTENSION}")
        self._mad_monster_mansion_data = MAD_MONSTER_MANSION_DATA_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FA8CE6{self._DECOMPRESSED_EXTENSION}")
        self._rusty_bucket_bay_code = RUSTY_BUCKET_BAY_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FB9A30{self._DECOMPRESSED_EXTENSION}")
        self._rusty_bucket_bay_data = None
        self._click_clock_wood_code = CLICK_CLOCK_WOOD_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FD6190{self._DECOMPRESSED_EXTENSION}")
        self._click_clock_wood_data = None
        self._gruntildas_lair_code = GRUNTILDAS_LAIR_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FC9150{self._DECOMPRESSED_EXTENSION}")
        self._gruntildas_lair_data = GRUNTILDAS_LAIR_DATA_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FCF698{self._DECOMPRESSED_EXTENSION}")
        self._final_battle_code = FINAL_BATTLE_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FD0420{self._DECOMPRESSED_EXTENSION}")
        self._final_battle_data = None
        self._cutscenes_code = CUTSCENES_CODE_CLASS(file_dir, f"{self._EXTRACTED_FILES_DIR}FC6F20{self._DECOMPRESSED_EXTENSION}")
        self._cutscenes_data = None

    ########################
    ### RANDOM FUNCTIONS ###
    ########################

    def _set_seed(self, seed_val):
        self._seed = seed_val

    def _rand_int(self, lower, upper, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return randint(lower, upper)

    def _rand_int_triangular(self, lower, upper, mode, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return round(triangular(lower, upper, mode))
    
    def _rand_float(self, lower, upper, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return uniform(lower, upper)
    
    def _rand_choice(self, list, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return choice(list)
    
    #############################
    ### RANDOMIZATION OPTIONS ###
    #############################
    
    def _patch_yum_yum_crash_fix(self):
        self._core_1_code._patch_yum_yum_crash_fix()
        self._treasure_trove_cove_code._patch_yum_yum_crash_fix()
    
    def _sm_starting_moves(self, starting_move_list):
        move_value_list = []
        for move in starting_move_list:
            for move_value in MOVE_DICT[move]:
                move_value_list.append(move_value)
        if(len(move_value_list) > 9):
            print(f"Attempting To Start With Too Many Moves: {len(move_value_list)}")
            raise SystemError(f"Attempting To Start With Too Many Moves: {len(move_value_list)}")
        elif(len(move_value_list) < 9):
            sorted(move_value_list)
            while(len(move_value_list) < 9):
                move_value_list.append(move_value_list[0])
        self._spiral_mountain_code._bottles_skip_tutorial_moves(move_value_list)
        self._spiral_mountain_code._check_moves_as_used(move_value_list)
        self._core_2_code._sm_bridge_completion_requirements(move_value_list)
    
    def _jump_pad_cheat_code_move(self, new_move):
        if(new_move in ["Jumps", "Attacks"]):
            raise SystemError(f"Cannot Make These Into Sandcastle Cheats: {new_move}")
        self._core_2_code._jump_pad_cheat_code_move(MOVE_DICT[new_move][0])

    def _fly_pad_cheat_code_move(self, new_move):
        if(new_move in ["Jumps", "Attacks"]):
            raise SystemError(f"Cannot Make These Into Sandcastle Cheats: {new_move}")
        self._core_2_code._fly_pad_cheat_code_move(MOVE_DICT[new_move][0])
    
    def _remove_known_anti_tampering(self):
        self._core_1_code._disable_anti_tamper()
        # self._core_2_code._disable_anti_tamper()
        self._spiral_mountain_code._disable_anti_tamper()
        self._mumbos_mountain_code._disable_anti_tamper()
        self._treasure_trove_cove_code._disable_anti_tamper()
        self._clankers_cavern_code._disable_anti_tamper()
        self._bubblegloop_swamp_code._disable_anti_tamper()
        # self._freezeezy_peak_code._disable_anti_tamper()
        self._gobis_valley_code._disable_anti_tamper()
        self._mad_monster_mansion_code._disable_anti_tamper()
        # self._rusty_bucket_bay_code._disable_anti_tamper()
        # self._click_clock_wood_code._disable_anti_tamper()
    
    def _adjust_core_checksums(self):
        # ASM_ENGINE_CODE ->  0xF37F90
        #     CRC2 -> ASM_ENGINE_VARS @ 0xF264
        # ASM_ENGINE_VARS ->  0xF9CAE0
        #     CRC2 -> ASM_LIBRARY_VARS @ 0xF64
        # ASM_LIBRARY_CODE -> 0xF19250
        #     CRC1 -> ROM @ 0x5E78
        #     CRC2 -> ROM @ 0x5E7C
        # ASM_LIBRARY_VARS -> 0xF362EB
        #     CRC1 -> ROM @ 0x5E80
        #     CRC2 -> ROM @ 0x5E84
        crc2 = self._core_2_code._calculate_checksum()
        self._core_2_data._set_checksum(crc2)
        crc2 = self._core_2_data._calculate_checksum()
        self._core_1_data._set_checksum(crc2)
        code_crc1, code_crc2 = self._core_1_code._calculate_checksum()
        vars_crc1, vars_crc2 = self._core_1_data._calculate_checksum()
        core_checksum_dict = {
            "Code_CRC1": code_crc1,
            "Code_CRC2": code_crc2,
            "Vars_CRC1": vars_crc1,
            "Vars_CRC2": vars_crc2,
        }
        return core_checksum_dict

    def _transformation_costs(self, transformation_cost_dict):
        self._core_2_code._termite_transformation_cost(transformation_cost_dict["Termite"])
        self._core_2_code._crocodile_transformation_cost(transformation_cost_dict["Crocodile"])
        self._core_2_code._walrus_transformation_cost(transformation_cost_dict["Walrus"])
        self._core_2_code._pumpkin_transformation_cost(transformation_cost_dict["Pumpkin"])
        self._core_2_code._bee_transformation_cost(transformation_cost_dict["Bee"])
    
    def _carrying_capacity(self, capacity_dict):
        # self._core_2_code._starting_blue_egg_count(capacity_dict["Blue_Eggs"]["Starting"])
        self._core_2_code._blue_egg_count_bottles_tutorial(capacity_dict["Blue_Eggs"]["Before_Cheato"] // 2)
        self._core_2_code._blue_egg_before_cheato_limit(capacity_dict["Blue_Eggs"]["Before_Cheato"])
        self._core_2_code._blue_egg_after_cheato_limit(capacity_dict["Blue_Eggs"]["After_Cheato"])
        # self._core_2_code._starting_red_feather_count(capacity_dict["Red_Feathers"]["Starting"])
        self._core_2_code._red_feather_count_bottles_tutorial(capacity_dict["Red_Feathers"]["Before_Cheato"] // 2)
        self._core_2_code._red_feather_before_cheato_limit(capacity_dict["Red_Feathers"]["Before_Cheato"])
        self._core_2_code._red_feather_after_cheato_limit(capacity_dict["Red_Feathers"]["After_Cheato"])
        # self._core_2_code._starting_gold_feather_count(capacity_dict["Gold_Feathers"]["Starting"])
        self._core_2_code._gold_feather_count_bottles_tutorial(capacity_dict["Gold_Feathers"]["Before_Cheato"] // 2)
        self._core_2_code._gold_feather_before_cheato_limit(capacity_dict["Gold_Feathers"]["Before_Cheato"])
        self._core_2_code._gold_feather_after_cheato_limit(capacity_dict["Gold_Feathers"]["After_Cheato"])
    
    def _starting_lives(self, starting_life_count):
        if(starting_life_count == "Infinite"):
            self._core_2_code._infinite_lives()
            self._core_2_code._starting_lives(255)
        else:
            self._core_2_code._starting_lives(starting_life_count)
    
    def _replace_bk_model_with_asset(self, asset):
        if(asset == 0x34E):
            self._core_2_code._always_high_poly_bk_model()
        elif(asset == 0x356):
            self._core_2_code._always_wishywashy_model()
        else:
            self._core_2_code._replace_bk_model_with_asset(asset)
    
    def _replace_bk_termite_model_with_asset(self, asset):
        self._core_2_code._replace_bk_termite_model_with_asset(asset)
    
    def _replace_bk_crocodile_model_with_asset(self, asset):
        self._core_2_code._replace_bk_crocodile_model_with_asset(asset)
    
    def _replace_bk_walrus_model_with_asset(self, asset):
        self._core_2_code._replace_bk_walrus_model_with_asset(asset)
    
    def _replace_bk_pumpkin_model_with_asset(self, asset):
        self._core_2_code._replace_bk_pumpkin_model_with_asset(asset)
    
    def _replace_bk_bee_model_with_asset(self, asset):
        self._core_2_code._replace_bk_bee_model_with_asset(asset)
    
    def _replace_bk_wishywashy_model_with_asset(self, asset):
        self._core_2_code._replace_bk_wishywashy_model_with_asset(asset)
    
    def _set_skybox_and_clouds(self, map_count, new_skybox=None, new_cloud1=None, new_cloud2=None):
        self._core_2_data._set_skybox_and_clouds(map_count, new_skybox, new_cloud1, new_cloud2)

    def _randomize_skybox_and_clouds(self, seed=None):
        if(seed):
            self._set_seed(seed)
        for map_count in range(25):
            map_start_index = self._SKYBOX_CLOUD_START_INDEX + map_count * 0x28
            new_skybox = self._rand_choice(self._LIST_OF_SKYBOXES, add_val=(self._SKYBOX_CLOUD_START_INDEX + map_start_index + 0x04))
            new_cloud1 = self._rand_choice(self._LIST_OF_CLOUDS, add_val=(self._SKYBOX_CLOUD_START_INDEX + map_start_index + 0x10))
            new_cloud2 = self._rand_choice(self._LIST_OF_CLOUDS, add_val=(self._SKYBOX_CLOUD_START_INDEX + map_start_index + 0x1C))
            self._core_2_data._set_skybox_and_clouds(map_count, new_skybox, new_cloud1, new_cloud2)
    
    def _randomize_music(self):
        '''Test this'''
        for map_count in range(0x83):
            music_start_index = self._MUSIC_START_INDEX + map_count * 0x8
            new_music1 = self._rand_choice(LOOPING_LEVEL_MUSIC_DICT, add_val=(self._MUSIC_START_INDEX + music_start_index + 0x2))
            new_music2 = self._rand_choice(LOOPING_LEVEL_MUSIC_DICT, add_val=(self._MUSIC_START_INDEX + music_start_index + 0x4))
            new_music3 = self._rand_choice(LOOPING_LEVEL_MUSIC_DICT, add_val=(self._MUSIC_START_INDEX + music_start_index + 0x6))
            self._core_2_data._set_music(map_count, new_music1=new_music1, new_music2=new_music2, new_music3=new_music3)
    
    def _set_all_music(self, new_music1, new_music2, new_music3):
        for map_count in range(0x83):
            self._core_2_data._set_music(map_count, new_music1, new_music2, new_music3)
    
    def _starting_max_health(self, start_val, default_cap=True):
        self._core_2_code._starting_max_health(start_val, default_cap)
        self._core_2_code._remove_game_select_health_display(start_val)
    
    def _empty_honeycombs_for_extra_health(self, eh_val):
        self._core_2_code._empty_honeycombs_for_extra_health(eh_val)
    
    def _starting_inventory_counts(self, start_val):
        self._core_2_code._starting_inventory_counts(start_val)
    
    def _modify_collision_markers(self, seed=None, effect_to_bk_option=None, sound_effect_option=None,
                                        bk_damage_option=None, hit_count_option=None, num_of_honeycombs_option=None):
        # Currently the issue is that when all of these values are randomized,
        # the compressed file grows in size and ends up messing up the later
        # ASM files. Will revisit this.
        if(seed):
            self._set_seed(seed)
        for marker_count in ENEMY_MARKER_DICT:
            index_start = self._MARKER_INDEX_START + marker_count * 0x1A
            killable_state = False
            for collision_index in range(0x04, 0x12, 0x2):
                effect_to_bk, next_state, sound_effect, bk_damage, hit_count, num_of_honeycombs = self._core_2_data._get_bitwise_collision_parameter_values(index_start + collision_index)
                # Num Of Dropped Honeycombs
                #   Checking if a killable state exists
                num_of_honeycombs = 0
                if(next_state == 2):
                    killable_state = True
                self._core_2_data._set_collision_parameter(index_start + collision_index, effect_to_bk, next_state, sound_effect,
                                                           bk_damage, hit_count, num_of_honeycombs)
            effect_to_bk, next_state, sound_effect, bk_damage, hit_count, num_of_honeycombs = self._core_2_data._get_bitwise_collision_parameter_values(index_start + 0x2)
            # Num Of Dropped Honeycombs
            #   If at any point killable, drop at least 1 honeycomb (random if selected)
            #   If not killable, drop no honeycombs
            if(killable_state or (next_state == 2)):
                if(num_of_honeycombs_option == "Randomize"):
                    num_of_honeycombs = self._rand_int_triangular(0, 3, mode=1, add_val=(index_start + collision_index + 5))
                elif(num_of_honeycombs == 0):
                    num_of_honeycombs = 1
            else:
                num_of_honeycombs = 0
            self._core_2_data._set_collision_parameter(index_start + 0x2, effect_to_bk, next_state, sound_effect,
                                                       bk_damage, hit_count, num_of_honeycombs)
    
    def _soulie_collision_markers(self):
        for index_start in BANJO_SOULIE_MARKERS:
            for collision_index in BANJO_SOULIE_MARKERS[index_start]:
                self._core_2_data._set_collision_parameter(index_start + collision_index,
                                                           BANJO_SOULIE_MARKERS[index_start][collision_index][0],
                                                           BANJO_SOULIE_MARKERS[index_start][collision_index][1],
                                                           BANJO_SOULIE_MARKERS[index_start][collision_index][2],
                                                           BANJO_SOULIE_MARKERS[index_start][collision_index][3],
                                                           BANJO_SOULIE_MARKERS[index_start][collision_index][4],
                                                           BANJO_SOULIE_MARKERS[index_start][collision_index][5])
    
    def _remove_hut_notes(self):
        # Mumbos Mountain
        self._core_2_data._set_actor_list(start_index=0x2ED0, actor_id=0x52, unkC=0x21, unk14=0x42C80000,
                                          unk18=0x42480000, unk1C=0x43FA0000, unk20=0x437A0000,
                                          unk24=0x42C80000, unk28=0x42480000)
        # Bubblegloop Swamp
        self._core_2_data._set_actor_list(start_index=0x310C, actor_id=0x52, unkC=0x21, unk14=0x42C80000,
                                          unk18=0x42480000, unk1C=0x43FA0000, unk20=0x437A0000,
                                          unk24=0x42C80000, unk28=0x42480000)
    
    def _enemy_note_drops(self, note_count1, note_count2, note_count3):
        self._core_2_data._set_actor_list(start_index=0x3348, actor_id=0x51, count=note_count1, unk10=0x3E800000,
                                          unk14=0x42FA0000, unk18=0x41C80000, unk1C=0x44354000,
                                          unk20=0x42FA0000, unk24=0x42FA0000, unk28=0x41C80000)
        self._core_2_data._set_actor_list(start_index=0x337C, actor_id=0x51, count=note_count2, unk10=0x3E800000,
                                          unk14=0x42FA0000, unk18=0x41C80000, unk1C=0x44354000,
                                          unk20=0x42FA0000, unk24=0x42FA0000, unk28=0x41C80000)
        self._core_2_data._set_actor_list(start_index=0x33B0, actor_id=0x51, count=note_count3, unk10=0x3E800000,
                                          unk14=0x42FA0000, unk18=0x41C80000, unk1C=0x44354000,
                                          unk20=0x42FA0000, unk24=0x42FA0000, unk28=0x41C80000)
    
    def _banjo_soulie_enemy_drops(self):
        # 1 Note (Counts As 5)
        self._core_2_data._set_actor_list(start_index=0x3348, actor_id=0x0051, count=0x01, unk10=0x46500000,
                                          unk14=0x00000000, unk18=0x00000000, unk1C=0x443B8000,
                                          unk20=0x437A0000, unk24=0x00000000, unk28=0x00000000)
        # 3 Blue Eggs
        self._core_2_data._set_actor_list(start_index=0x337C, actor_id=0x0052, count=0x03, unk10=0x3E800000,
                                          unk14=0x42FA0000, unk18=0x41C80000, unk1C=0x44354000,
                                          unk20=0x42FA0000, unk24=0x42FA0000, unk28=0x41C80000)
        # 1 Gold Feather
        self._core_2_data._set_actor_list(start_index=0x33B0, actor_id=0x0370, count=0x01, unk10=0x46500000,
                                          unk14=0x00000000, unk18=0x00000000, unk1C=0x443B8000,
                                          unk20=0x437A0000, unk24=0x00000000, unk28=0x00000000)
    
    def _increase_note_pickup_count(self, note_pickup_count):
        self._core_2_code._increase_note_pickup_count(note_pickup_count)

    def _exit_to_witchs_lair(self):
        self._core_2_code._exit_to_witchs_lair()
        self._core_2_data._adjust_menu_for_witchs_lair()
    
    def _replace_note_doors(self, collectable_type, new_max):
        scaling = new_max / self._COLLECTIBLE_MAX_DICT["Note"]
        note_door_list = self._gruntildas_lair_data._read_note_door_values()
        replacement_list = []
        for note_val in note_door_list:
            replacement_list.append(int(note_val * scaling))
        self._gruntildas_lair_data._modify_note_door_values(replacement_list)
        if(collectable_type == "Jiggy"):
            self._gruntildas_lair_code._note_door_to_jiggy_doors()
        elif(collectable_type == "Honeycomb"):
            self._gruntildas_lair_code._note_doors_to_honeycomb_doors()
        elif(collectable_type != "Note"):
            print(f"Unknown Collectable Type: {collectable_type}")
            raise SystemError(f"Unknown Collectable Type: {collectable_type}")
    
    def _set_note_door_values(self, note_door_value_list):
        self._gruntildas_lair_data._modify_note_door_values(note_door_value_list)
    
    def _replace_jigsaw_puzzles(self, collectable_type, new_max):
        scaling = new_max / self._COLLECTIBLE_MAX_DICT["Jiggy"]
        jigsaw_puzzle_list = self._gruntildas_lair_data._read_jigsaw_puzzle_costs()
        replacement_list = []
        for note_val in jigsaw_puzzle_list:
            replacement_list.append(int(note_val * scaling))
        self._gruntildas_lair_data._modify_jigsaw_puzzle_costs(replacement_list)

    def _set_jigsaw_puzzle_costs(self, jigsaw_puzzle_cost_list):
        self._gruntildas_lair_data._modify_jigsaw_puzzle_costs(jigsaw_puzzle_cost_list)
    
    def _replace_transformation_costs(self, collectable_type, new_max):
        scaling = new_max / self._COLLECTIBLE_MAX_DICT["Token"]
        transformation_cost_list = self._core_2_code._read_transformation_costs()
        replacement_list = []
        for note_val in transformation_cost_list:
            replacement_list.append(int(note_val * scaling))
        self._core_2_code._modify_transformation_costs(replacement_list)
    
    def _set_transformation_costs(self, transformation_cost_list):
        self._core_2_code._modify_transformation_costs(transformation_cost_list)
    
    def _fallproof(self):
        self._core_2_code._fallproof()

    def _remove_animation(self, start_index):
        '''Makes You Immobile; Probably Will Never Use'''
        animation_dict = self._core_2_data._get_animation_functions_dict(start_index)
        for key in ["INIT", "Update", "End", "Interrupt"]:
            animation_dict[key] = 0x00000000
        self._core_2_data._set_animation_functions(start_index, animation_dict)

    def _jiggy_win_condition(self, jiggy_count):
        self._core_2_code._remove_defeating_gruntilda_check()
        self._core_2_code._jiggy_count_win_condition(jiggy_count)
    
    def _note_count_win_condition(self, note_count):
        self._core_2_code._note_count_win_condition(note_count)
    
    def _skippable_cutscenes(self):
        self._core_2_code._skippable_intro_and_lair_cutscenes()
        self._core_2_code._skippable_game_over_cutscene()
    
    def _boot_to_game_select(self):
        self._core_1_code._booting_up_map(0x91)
        self._core_2_code._booting_up_map(0x91)
    
    def _scale_termite_speed(self, scaling):
        # Limiting it to positive numbers
        speed_dict = self._core_2_data._get_termite_speed_dict()
        for item in ["Termite_Unk0", "Termite_Unk1"]:
            speed_dict[item] = max(min(int(speed_dict[item] * scaling), 0x7F0FFFFF), 0x00000001)
        self._core_2_data._set_termite_speed_dict(speed_dict)
    
    def _scale_crocodile_speed(self, scaling):
        # Limiting it to positive numbers
        speed_dict = self._core_2_data._get_crocodile_speed_dict()
        for item in ["Crocodile_Unk0", "Crocodile_Unk1", "Crocodile_Unk2"]:
            speed_dict[item] = max(min(int(speed_dict[item] * scaling), 0x7F0FFFFF), 0x00000001)
        self._core_2_data._set_crocodile_speed_dict(speed_dict)
    
    def _scale_pumpkin_speed(self, scaling):
        # Limiting it to positive numbers
        speed_dict = self._core_2_data._get_pumpkin_speed_dict()
        for item in ["Pumpkin_Unk0", "Pumpkin_Unk1"]:
            speed_dict[item] = max(min(int(speed_dict[item] * scaling), 0x7F0FFFFF), 0x00000001)
        self._core_2_data._set_pumpkin_speed_dict(speed_dict)
    
    def _scale_walrus_speed(self, scaling):
        # Limiting it to positive numbers
        speed_dict = self._core_2_data._get_walrus_speed_dict()
        for item in ["Walrus_Unk0", "Walrus_Unk1", "Walrus_Unk6", "Walrus_Unk7"]:
            speed_dict[item] = max(min(int(speed_dict[item] * scaling), 0x7F0FFFFF), 0x00000001)
        self._core_2_data._set_walrus_speed_dict(speed_dict)
    
    def _scale_bk_talon_trot_speed(self, scaling):
        # Limiting it to positive numbers
        speed_dict = self._core_2_data._get_bk_talon_trot_speed_dict()
        for item in ["Talon_Trot_Unk0", "Talon_Trot_Unk1", "Talon_Trot_Unk2", "Talon_Trot_Unk3", "Talon_Trot_Unk4"]:
            speed_dict[item] = max(min(int(speed_dict[item] * scaling), 0x7F0FFFFF), 0x00000001)
        self._core_2_data._set_bk_talon_trot_speed_dict(speed_dict)
    
    def _scale_banjos_surface_swim_speed(self, scaling):
        # Limiting it to positive numbers
        speed_dict = self._core_2_data._get_banjo_surface_swim_speed_dict()
        for item in ["Swim_Min_Horz_Velocity", "Swim_Max_Horz_Velocity"]:
            speed_dict[item] = max(min(int(speed_dict[item] * scaling), 0x7F0FFFFF), 0x00000001)
        self._core_2_data._set_banjo_surface_swim_speed_dict(speed_dict)
    
    def _scale_banjos_walk_speed(self, scaling):
        # Limiting it to positive numbers
        speed_dict = self._core_2_data._get_banjo_walk_speed_dict()
        for item in ["Creep_Min_Velocity", "Walk_Fast_Max_Velocity", "Mud_Min_Velocity", "Mud_Max_Velocity",
                     "Creep_Max/Slow_Walk_Min_Velocity_Threshold", "Slow_Walk_Max/Walk_Min_Threshold", "Walk_Max/Walk_Fast_Min_Threshold"]:
            speed_dict[item] = max(min(int(speed_dict[item] * scaling), 0x7F0FFFFF), 0x00000001)
        self._core_2_data._set_banjo_walk_speed_dict(speed_dict)
    
    def _remove_slope_slide_timer(self):
        self._core_2_code._remove_regular_slope_slide_timer()
        self._core_2_code._remove_steep_slope_slide_timer()
    
    def _default_totals_screen(self):
        self._core_2_code._default_totals_screen()
    
    def _replace_level_model(self, first_level_count, second_level_count, parameter_list):
        level_models_dict = self._core_2_data._get_all_level_models()
        for parameter in parameter_list:
            level_models_dict[first_level_count][parameter] = level_models_dict[second_level_count][parameter]
        self._core_2_data._set_all_level_models(level_models_dict)
    
    def _modify_level_model_by_dict(self, new_level_model_dict):
        curr_level_model_dict = self._core_2_data._get_all_level_models()
        for level_count in curr_level_model_dict:
            curr_map = curr_level_model_dict[level_count]["Map"]
            if(curr_map in new_level_model_dict):
                for parameter in new_level_model_dict[curr_map]:
                    curr_level_model_dict[level_count][parameter] = new_level_model_dict[curr_map][parameter]
        self._core_2_data._set_all_level_models(curr_level_model_dict)
    
    def _snacker_everywhere(self):
        self._core_2_code._snacker_remove_ttc_boundaries()
        self._core_2_code._snacker_all_maps()

    def _mm_fix_honeycomb_flags(self):
        self._core_2_code._mm_fix_honeycomb_flags()
    
    def _mmm_anyones_empty_honeycomb(self):
        self._core_2_code._mmm_anyones_empty_honeycomb()

    def _remove_tutorial_option(self):
        self._spiral_mountain_code._remove_tutorial_option()

    def _adjust_final_battle_phases(self,
                                    phase1_hits=None,
                                    phase2_hits=None, phase2_spots=None,
                                    phase3_hits=None,
                                    phase4_num_of_jinjos=None, phase4_egg_per_jinjo=None,
                                    phase5_eggs_per_hole=None):
        self._final_battle_code._adjust_final_battle_phases(phase1_hits,
                                                            phase2_hits, phase2_spots,
                                                            phase3_hits,
                                                            phase4_num_of_jinjos, phase4_egg_per_jinjo,
                                                            phase5_eggs_per_hole)
    
    def _one_round_vile(self):
        self._bubblegloop_swamp_code._one_round_vile()
    
    def _reassign_ff_tile_types(self, ff_tile_dict):
        self._TILE_TRANSLATOR_DICT = {
            "Blank_Tile": 0,
            "BK_Tile": 1,
            "Eye_Tile": 2,
            "Sound_Tile": 3,
            "Timer_Tile": 4,
            "Gruntilda_Tile": 5,
            "Skull_Tile": 6,
            "Joker_Tile": 8,
        }
        board_dict = self._gruntildas_lair_data._get_board_dict()
        for count in board_dict:
            board_dict[count]["Tile_Type"] = self._TILE_TRANSLATOR_DICT[ff_tile_dict[count]]
        self._gruntildas_lair_data._set_board_dict(board_dict)
    
    def _reassign_gv_matching_puzzle_tile_types(self, gv_mp_tile_dict):
        matching_puzzle_dict = self._gobis_valley_data._get_matching_puzzle_dict()
        for tile_count, puzzle_count in enumerate(matching_puzzle_dict):
            matching_puzzle_dict[puzzle_count]["Tile_Value"] = gv_mp_tile_dict[tile_count]
        self._gobis_valley_data._set_matching_puzzle_dict(matching_puzzle_dict)
    
    def _reassign_motzands_songs(self, first_song_list=None, second_song_list=None):
        if(first_song_list):
            self._mad_monster_mansion_data._set_motzands_first_song(first_song_list)
        if(second_song_list):
            self._mad_monster_mansion_data._set_motzands_second_song(second_song_list)
    
    def _reassign_tumblars_tiles(self, mm_t_tile_dict):
        tumblar_tile_dict = self._mad_monster_mansion_data._get_tumblar_tile_dict()
        for tile_count, puzzle_count in enumerate(tumblar_tile_dict):
            if(puzzle_count not in [0x4, 0xC, 0x14, 0x1C]):
                tumblar_tile_dict[puzzle_count]["Tile_Value"] = mm_t_tile_dict[tile_count]
        self._mad_monster_mansion_data._set_tumblar_tile_dict(tumblar_tile_dict)
    
    def _reassign_sm_main_to_sm_banjos_house_warp(self, map_id, exit_id):
        self._core_2_code._reassign_sm_main_to_sm_banjos_house_warp(map_id, exit_id)
    
    def _new_game_start_area(self, map_id, entry_id):
        self._core_2_code._new_game_start_area(map_id, entry_id)
    
    def _stonehenge_conga(self):
        self._mumbos_mountain_code._stonehenge_conga()
    
    def _unlimited_cheat_codes(self):
        self._treasure_trove_cove_code._unlimited_cheat_codes()
    
    def _simplified_cheat_codes(self, jump_pad_cheat_move="Shock_Jump", fly_pad_cheat_move="Flight"):
        self._treasure_trove_cove_data._obtain_sandcastle_cheats()
        for cheat_num in SIMPLIFIED_CHEAT_DICT:
            self._treasure_trove_cove_data._edit_sandcastle_cheat(cheat_num, SIMPLIFIED_CHEAT_DICT[cheat_num])
        self._treasure_trove_cove_data._edit_sandcastle_cheat(48, MOVE_CHEAT_DICT[jump_pad_cheat_move])
        self._core_2_code._jump_pad_cheat_code_move(new_move=MOVE_DICT[jump_pad_cheat_move][0])
        self._treasure_trove_cove_data._edit_sandcastle_cheat(52, MOVE_CHEAT_DICT[fly_pad_cheat_move])
        self._core_2_code._fly_pad_cheat_code_move(new_move=MOVE_DICT[fly_pad_cheat_move][0])
        self._treasure_trove_cove_data._set_sandcastle_cheats()
    
    def _water_level_one_automatically(self):
        self._core_2_code._water_level_one_automatically()

    def _water_level_two_automatically(self):
        self._core_2_code._water_level_two_automatically()
    
    def _adjusted_bottles_cameras(self, sm_moves, non_sm_moves):
        script_id_dict = {}
        script_id = 0x010C
        # Spiral Mountain Moves
        move_camera_dict = self._spiral_mountain_data._get_move_camera_dict()
        for count in move_camera_dict:
            move_camera_dict[count]["Learn_Text"] = BOTTLES_DICT[sm_moves[count]]["Learn_Text"]
            move_camera_dict[count]["Refresher_Text"] = BOTTLES_DICT[sm_moves[count]]["Refresher_Text"]
            move_camera_dict[count]["Camera"] = BOTTLES_DICT[sm_moves[count]]["New_Camera"]
            move_camera_dict[count]["Ability"] = sm_moves[count]
            script_id_dict[sm_moves[count]] = script_id
            script_id += 0x80
        self._spiral_mountain_data._set_move_camera_dict(move_camera_dict)
        script_id += 0x80
        # Non-Spiral Mountain Moves
        move_camera_dict = self._core_2_data._get_move_camera_dict()
        for count in move_camera_dict:
            move_camera_dict[count]["Learn_Text"] = BOTTLES_DICT[non_sm_moves[count]]["Learn_Text"]
            move_camera_dict[count]["Refresher_Text"] = BOTTLES_DICT[non_sm_moves[count]]["Refresher_Text"]
            move_camera_dict[count]["Camera"] = BOTTLES_DICT[non_sm_moves[count]]["New_Camera"]
            move_camera_dict[count]["Ability"] = non_sm_moves[count]
            script_id_dict[non_sm_moves[count]] = script_id
            script_id += 0x80
        self._core_2_data._set_move_camera_dict(move_camera_dict)
        return script_id_dict
    
    def _adjusted_seperated_bottles_cameras(self, sm_moves, non_sm_moves):
        script_id_dict = {}
        script_id = 0x010C
        # Spiral Mountain Moves
        move_camera_dict = self._spiral_mountain_data._get_move_camera_dict()
        for count in move_camera_dict:
            move_camera_dict[count]["Learn_Text"] = SEPARATED_BOTTLES_DICT[sm_moves[count]]["Learn_Text"]
            move_camera_dict[count]["Refresher_Text"] = SEPARATED_BOTTLES_DICT[sm_moves[count]]["Refresher_Text"]
            # move_camera_dict[count]["Camera"] = SEPARATED_BOTTLES_DICT[sm_moves[count]]["New_Camera"]
            move_camera_dict[count]["Camera"] = SEPARATED_BOTTLES_DICT[sm_moves[count]]["Old_Camera"]
            move_camera_dict[count]["Ability"] = sm_moves[count]
            script_id_dict[sm_moves[count]] = script_id
            script_id += 0x80
        self._spiral_mountain_data._set_move_camera_dict(move_camera_dict)
        script_id += 0x80
        # Non-Spiral Mountain Moves
        move_camera_dict = self._core_2_data._get_move_camera_dict()
        for count in move_camera_dict:
            move_camera_dict[count]["Learn_Text"] = SEPARATED_BOTTLES_DICT[non_sm_moves[count]]["Learn_Text"]
            move_camera_dict[count]["Refresher_Text"] = SEPARATED_BOTTLES_DICT[non_sm_moves[count]]["Refresher_Text"]
            # move_camera_dict[count]["Camera"] = SEPARATED_BOTTLES_DICT[non_sm_moves[count]]["New_Camera"]
            move_camera_dict[count]["Camera"] = SEPARATED_BOTTLES_DICT[non_sm_moves[count]]["Old_Camera"]
            move_camera_dict[count]["Ability"] = non_sm_moves[count]
            script_id_dict[non_sm_moves[count]] = script_id
            script_id += 0x80
        self._core_2_data._set_move_camera_dict(move_camera_dict)
        return script_id_dict
    
    def _set_swim_a_speed(self, swim_a_speed):
        self._core_2_code._set_swim_a_speed(swim_a_speed)
    
    def _set_swim_b_speed(self, swim_b_speed):
        self._core_2_code._set_swim_b_speed(swim_b_speed)
    
    def _set_roll_speed(self, roll_speed):
        self._core_2_code._set_roll_speed(roll_speed)
    
    def _raise_sharkfood_island(self):
        self._treasure_trove_cove_code._raise_sharkfood_island()
    
    def _remove_tutorial_vegetable_despawn(self):
        '''Does not work'''
        self._spiral_mountain_code._remove_tutorial_vegetable_despawn()
    
    def _forgiving_deaths(self):
        '''Does not work'''
        self._core_2_code._forgiving_deaths()
    
    def _adjust_gc_section_info_by_level(self, new_gc_section_info_dict):
        curr_gc_section_info_dict = self._core_2_data._get_gc_section_info_dict()
        for section_num in curr_gc_section_info_dict:
            curr_level = curr_gc_section_info_dict[section_num]["Map"]
            if(curr_level in new_gc_section_info_dict):
                curr_gc_section_info_dict[section_num]["Level"] = new_gc_section_info_dict[curr_level]
        self._core_2_data._set_gc_section_info_dict(curr_gc_section_info_dict)
    
    def _replace_sir_slush_model(self, asset_id, marker_data_dict=None):
        self._core_2_data._replace_sir_slush_model(asset_id)
        if(marker_data_dict == None):
            marker_data_dict = {
                0xD8F2: { # Sir Slush (Body)
                    0x02: [0, 0, 0, 0, 0, 3],
                    0x04: [9, 0, 2, 0, 0, 0],
                    0x06: [9, 0, 2, 0, 0, 0],
                    0x08: [5, 0, 0, 1, 0, 0],
                    0x0A: [0, 2, 2, 0, 1, 0],
                    0x0C: [0, 2, 2, 0, 1, 0],
                    0x0E: [0, 0, 0, 0, 0, 0],
                    0x10: [0, 0, 0, 0, 0, 0],
                    0x12: [0, 0, 0, 0, 1, 0],
                    0x14: [9, 0, 2, 0, 0, 0],
                    0x16: [0, 0, 0, 0, 0, 0],
                    0x18: [5, 0, 0, 1, 0, 0],
                }
            }
        for index_start in marker_data_dict:
            for collision_index in marker_data_dict[index_start]:
                self._core_2_data._set_collision_parameter(index_start + collision_index,
                                                            marker_data_dict[index_start][collision_index][0],
                                                            marker_data_dict[index_start][collision_index][1],
                                                            marker_data_dict[index_start][collision_index][2],
                                                            marker_data_dict[index_start][collision_index][3],
                                                            marker_data_dict[index_start][collision_index][4],
                                                            marker_data_dict[index_start][collision_index][5])