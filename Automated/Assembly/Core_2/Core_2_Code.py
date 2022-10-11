import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class CORE_2_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        pass

    def _calculate_checksum(self):
        crc1 = 0
        crc2 = 0xFFFFFFFF
        for val in self._mmap:
            byte = int.from_bytes(val, "big")
            crc1 = crc1 + byte
            crc2 = crc2 ^ (byte << (crc1 & 0x17))
        return crc2

    #######################
    ### SPIRAL MOUNTAIN ###
    #######################

    def _sm_bridge_completion_requirements(self, move_value_list):
        self._write_byte(0x53517, move_value_list[0])
        self._write_byte(0x5352B, move_value_list[1])
        self._write_byte(0x5353F, move_value_list[2])
        self._write_byte(0x53553, move_value_list[3])
        self._write_bytes(0x53564, 3, 0x240400)
        self._write_byte(0x53567, move_value_list[4])
        self._write_byte(0x5357B, move_value_list[5])
        self._write_byte(0x5358F, move_value_list[6])
        self._write_byte(0x535A3, move_value_list[7])
        self._write_byte(0x535B7, move_value_list[8])
    
    #######################
    ### TRANSFORMATIONS ###
    #######################

    def _termite_transformation_cost(self, transform_cost):
        self._write_byte(0x4A7E7, transform_cost)
    
    def _crocodile_transformation_cost(self, transform_cost):
        self._write_byte(0x4A7EF, transform_cost)
    
    def _walrus_transformation_cost(self, transform_cost):
        self._write_byte(0x4A7F7, transform_cost)
    
    def _pumpkin_transformation_cost(self, transform_cost):
        self._write_byte(0x4A7FF, transform_cost)
    
    def _bee_transformation_cost(self, transform_cost):
        self._write_byte(0x4A807, transform_cost)
    
    ###########################
    ### CARRYING CAPACITIES ###
    ###########################

    def _starting_inventory_counts(self, start_val):
        '''Using the value for air and giving it to blue eggs, red feathers, and gold feathers'''
        if(start_val > 0):
            self._write_bytes(0xBF51E, 2, start_val)
            self._write_byte(0xBF521, 0x59)
            self._write_byte(0xBF525, 0x59)
            self._write_byte(0xBF529, 0x59)
        else:
            print("Cannot Have Zero For Starting Value")
            exit(0)

    def _blue_egg_before_cheato_limit(self, capacity_limit):
        self._write_byte(0xBF21F, capacity_limit)
    
    def _blue_egg_after_cheato_limit(self, capacity_limit):
        self._write_byte(0xBF217, capacity_limit)
    
    def _red_feather_before_cheato_limit(self, capacity_limit):
        self._write_byte(0xBF23F, capacity_limit)
    
    def _red_feather_after_cheato_limit(self, capacity_limit):
        self._write_byte(0xBF237, capacity_limit)
    
    def _gold_feather_before_cheato_limit(self, capacity_limit):
        self._write_byte(0xBF25B, capacity_limit)
    
    def _gold_feather_after_cheato_limit(self, capacity_limit):
        self._write_byte(0xBF257, capacity_limit)
    
    ######################
    ### HEALTH & LIVES ###
    ######################

    def _starting_max_health(self, start_val):
        self._write_byte(0xBF517, start_val)
        self._write_byte(0xC097B, 8 - start_val)
        self._write_byte(0xC097F, start_val)

    def _empty_honeycombs_for_extra_health(self, eh_val):
        '''
        Doesn't give health until you go through warp.
        And even then, you don't get a health refill
        '''
        self._write_byte(0xC091F, eh_val)
        self._write_byte(0xC095F, eh_val)

    def _starting_lives(self, start_val):
        self._write_byte(0xBF51B, start_val)
    
    def _infinite_lives(self):
        self._write_bytes(0xBF72C, 8, 0x0000000000000000)

    ######################
    ### STARTING AREAS ###
    ######################

    def _new_game_starting_area(self):
        pass

    def _after_lair_cutscene_starting_area(self):
        pass

    #################
    ### COLLISION ###
    #################

    def _modify_object_collision(self, collision_dict):
        pass

    ################
    ### BK MODEL ###
    ################

    def _always_high_poly_bk_model(self):
        self._write_bytes(0x11722, 2, 0x34E)
        self._write_bytes(0x1172A, 2, 0x34E)

    def _always_wishywashy_model(self):
        self._write_bytes(0x116C2, 2, 0x34E)
        self._write_bytes(0x11722, 2, 0x356)
        self._write_bytes(0x1172A, 2, 0x356)
        self._write_bytes(0x1172E, 2, 0x356)
    
    def _replace_bk_model_with_asset(self, asset):
        self._write_bytes(0x11722, 2, asset)
        self._write_bytes(0x1172A, 2, asset)
        self._write_bytes(0x1172E, 2, asset)
    
    ##################
    ### PAUSE MENU ###
    ##################

    def _exit_to_witchs_lair(self):
        # Disable Exit To Witch's Lair From TRUE to FALSE
        self._write_bytes(0x8BBF8, 4, 0x00001025)
        # Disable Debug Byte
        self._write_byte(0x8BCE7, 0x00)
    
    def _default_totals_screen(self):
        self._write_bytes(0x8B0D0, 4, 0x24020000)
        self._write_bytes(0x8B0D8, 4, 0x24020000)
        self._write_bytes(0x8B0E0, 4, 0x24020000)
        self._write_bytes(0x8B0E8, 4, 0x24020000)
        self._write_bytes(0x8B0F0, 4, 0x24020000)
        self._write_bytes(0x8B0F8, 4, 0x24020000)
        self._write_bytes(0x8B100, 4, 0x24020000)
    
    #################
    ### FALLPROOF ###
    #################

    def _fallproof(self):
        self._write_bytes(0x2D69C, 4, 0x00000000)
        self._write_bytes(0x2D6A0, 4, 0x00000000)
    
    ################################
    ### ALTERNATE WIN CONDITIONS ###
    ################################
    
    def _remove_defeating_gruntilda_check(self):
        # Instance
        self._write_bytes(0x15C94, 4, 0x00000000)
        self._write_bytes(0x15C98, 4, 0x00000000)
        self._write_bytes(0x15C9C, 4, 0x00000000)
        # Instance
        self._write_bytes(0x15D00, 4, 0x00000000)
        self._write_bytes(0x15D04, 4, 0x00000000)
        self._write_bytes(0x15D08, 4, 0x00000000)
        # Instance
        self._write_bytes(0x15DB0, 4, 0x00000000)
        self._write_bytes(0x15DB4, 4, 0x00000000)
        self._write_bytes(0x15DB8, 4, 0x00000000)
        # Instance
        self._write_bytes(0x29E28, 4, 0x00000000)
        self._write_bytes(0x29E2C, 4, 0x00000000)
        self._write_bytes(0x29E30, 4, 0x00000000)
        # Instance
        self._write_bytes(0x29FB8, 4, 0x00000000)
        self._write_bytes(0x29FBC, 4, 0x00000000)
        self._write_bytes(0x29FC0, 4, 0x00000000)
        # Instance
        self._write_bytes(0x98B34, 4, 0x00000000)
        self._write_bytes(0x98B38, 4, 0x00000000)
        self._write_bytes(0x98B3C, 4, 0x00000000)

    def _jiggy_count_win_condition(self, item_count):
        # Instance
        self._write_byte(0x15C8B, item_count)
        # Instance
        self._write_byte(0x15CF7, item_count)
        # Instance
        self._write_byte(0x15DA7, item_count)
        # Instance
        self._write_byte(0x29E1F, item_count)
        # Instance
        self._write_byte(0x29FAF, item_count)
        # Instance
        self._write_byte(0x98B4F, item_count)
    
    def _note_count_win_condition(self, item_count):
        # Note Requirement
        self._write_bytes(0xBFE70, 4, 0x0C0D1BBB)
        self._write_bytes(0xBFE78, 3, 0x240100)
        self._write_byte(0xBFE7B, item_count)
        self._write_bytes(0xBFE7C, 4, 0x1441000A)
        self._write_bytes(0xBFE80, 4, 0x00000000)
        self._write_bytes(0xBFE84, 4, 0x00000000)
        self._write_bytes(0xBFE88, 4, 0x00000000)
        # Cutscene
        self._write_bytes(0xBFE8C, 4, 0x24040002)
        self._write_bytes(0xBFE90, 4, 0x24040095)
        self._write_bytes(0xBFE94, 4, 0x00002825)
        self._write_bytes(0xBFE98, 4, 0x0C0B901E)
        self._write_bytes(0xBFE9C, 4, 0x24060001)
        self._write_bytes(0xBFEA0, 4, 0x0C0A6299)
    
    #################
    ### CUTSCENES ###
    #################
    
    def _skippable_intro_and_lair_cutscenes(self):
        self._write_bytes(0x9573C, 4, 0x24020001)
    
    def _skippable_game_over_cutscene(self):
        self._write_bytes(0x95770, 4, 0x00000000)

    ############################
    ### TRANSFORMATION COSTS ###
    ############################

    def _read_transformation_costs(self):
        transformation_cost_list = []
        for curr_index in range(0x4A7E7, 0x4A808, 0x8):
            transformation_cost_list.append(self._read_byte(curr_index))
        return transformation_cost_list

    def _modify_transformation_costs(self, replacement_list):
        for index_count, curr_index in enumerate(range(0x4A7E7, 0x4A808, 0x8)):
            if(replacement_list[index_count] != None):
                self._write_byte(curr_index, replacement_list[index_count])
    
    ###########################
    ### NEW GAME START AREA ###
    ###########################

    def _new_game_start_area(self, area_id):
        self._write_byte(0x986FA, area_id)