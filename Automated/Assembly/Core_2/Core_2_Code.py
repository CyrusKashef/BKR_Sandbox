import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class CORE_2_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        '''No known anti-tampering for Core 2'''
        pass

    def _calculate_checksum(self):
        '''Runs through algorithm to calculate the new checksum (Might not work?)'''
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
        '''
        This function checks if certain moves have been learned.
        Primary (and possibly only) uses for this function are SM's bridge completion and Bottle's text flag
        '''
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
    
    ######################
    ### LEARNING MOVES ###
    ######################

    def _remove_shoes_camera_transitions(self):
        '''
        Decomp: https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/ch/mole.c#L171
        Removes the camera showing off the Wading Boots and the Turbo Trainers when learning the move
        Needs Testing
        '''
        # Solution 1
        self._write_bytes(0x52900, 4, 0x00000000) # Wading Boots
        self._write_bytes(0x52940, 4, 0x00000000) # Turbo Trainers
        # Solution 2
        # self._write_byte(0x52907, wading_boots_cam) # Wading Boots
        # self._write_bytes(0x52947, turbo_trainers_cam) # Turbo Trainers

    def _set_bottles_given_blue_eggs(self, blue_egg_count):
        '''Sets how many blue eggs Bottles gives you when learning egg firing'''
        self._write_byte(0x52987, blue_egg_count)

    def _set_bottles_given_red_feathers(self, red_feather_count):
        '''Sets how many red feathers Bottles gives you when learning flight'''
        self._write_byte(0x5299B, red_feather_count)

    def _set_bottles_given_gold_feathers(self, gold_feather_count):
        '''Sets how many gold feathers Bottles gives you when learning wonderwing'''
        self._write_byte(0x529AB, gold_feather_count)

    def _jump_pad_cheat_code_move(self, new_move):
        '''
        Decomp: https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/code_43A40.c#L48
        The jump pad actor has a function that checks the sandcastle cheat code.
        If changed to a different move, whenever the jump pad actor is loaded,
          the move is given to the player, even if they don't know shock jump.
        Possibly need to put a shock jump pad in the sandcastle?
        '''
        self._write_byte(0x43A77, new_move)

    def _fly_pad_cheat_code_move(self, new_move):
        '''
        Decomp: https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/code_43A40.c#L62
        The flight pad actor has a function that checks the sandcastle cheat code.
        If changed to a different move, whenever the flight pad actor is loaded,
          the move is given to the player, even if they don't know flight.
        Possibly need to put a flight pad in the sandcastle?
        '''
        self._write_byte(0x43AEF, new_move)
    
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
            print("Cannot Have Zero For Starting Air Value, Player Will Die LMAO")
            exit(0)
    
    def _blue_egg_count_bottles_tutorial(self, blue_egg_count):
        self._write_byte(0x52987, blue_egg_count)

    def _blue_egg_before_cheato_limit(self, capacity_limit):
        '''Modifies the blue egg carrying capacity before inputting Cheato's code'''
        self._write_byte(0xBF21F, capacity_limit)
    
    def _blue_egg_after_cheato_limit(self, capacity_limit):
        '''Modifies the blue egg carrying capacity after inputting Cheato's code'''
        self._write_byte(0xBF217, capacity_limit)
    
    def _red_feather_count_bottles_tutorial(self, red_feather_count):
        self._write_byte(0x5299B, red_feather_count)
    
    def _red_feather_before_cheato_limit(self, capacity_limit):
        '''Modifies the red feather carrying capacity before inputting Cheato's code'''
        self._write_byte(0xBF23F, capacity_limit)
    
    def _red_feather_after_cheato_limit(self, capacity_limit):
        '''Modifies the red feather carrying capacity after inputting Cheato's code'''
        self._write_byte(0xBF237, capacity_limit)
    
    def _gold_feather_count_bottles_tutorial(self, gold_feather_count):
        self._write_byte(0x529AF, gold_feather_count)
    
    def _gold_feather_before_cheato_limit(self, capacity_limit):
        '''Modifies the gold feather carrying capacity before inputting Cheato's code'''
        self._write_byte(0xBF25B, capacity_limit)
    
    def _gold_feather_after_cheato_limit(self, capacity_limit):
        '''Modifies the gold feather carrying capacity after inputting Cheato's code'''
        self._write_byte(0xBF257, capacity_limit)
    
    ######################
    ### HEALTH & LIVES ###
    ######################

    def _starting_max_health(self, start_health_val):
        '''Modifies the player's starting health total'''
        # D_80385F30[ITEM_14_HEALTH] = D_80385F30[ITEM_15_HEALTH_TOTAL] = start_health_val;
        self._write_byte(0xBF517, start_health_val)
        # D_80385F30[ITEM_15_HEALTH_TOTAL] =  start_health_val + MIN(8 - start_health_val, (honeycombscore_get_total() / eh_val));
        self._write_byte(0xC096B, 9 - start_health_val) # Adjusts MIN function itself
        self._write_byte(0xC097B, 8 - start_health_val) # Adjusts parameter within MIN function
        self._write_byte(0xC097F, start_health_val)
    
    def _remove_game_select_health_display(self, start_health_val):
        '''
        Modifies when the player's health is under constant display.
        For some reason, the game select will display the player's health for that player's file.
        '''
        self._write_byte(0xBF763, start_health_val)

    def _empty_honeycombs_for_extra_health(self, eh_val):
        '''
        Modifies the number of empty honeycombs for the player to receive extra health
        NOTE: These adjustment work once per warp use. If you don't warp,
        the player will go into a state where they can't pause and their
        health will increase at the wrong rate, but will be adjusted after
        they warp.
        FIX: When decomp is finished, add "D_803815C0 = 0;" to "case 2://L802FECD4"
        '''
        # Disables Pausing To Not Interrupt Next Step
        # If interrupted, the player won't receive the updated health until warp
        # if(!(item_getCount(ITEM_13_EMPTY_HONEYCOMB) < 6))
        self._write_byte(0x5863, eh_val)
        
        # Health Upgrade Animation & Updating Health
        # if(eh_val <= D_803815D4...
        byte_list = self._float_to_byte_list(eh_val)
        self._write_byte(0x77AC6, byte_list[0])
        self._write_byte(0x77AC7, byte_list[1])
        
        # Removes Current Empty Honeycomb Count
            # func_803463D4(ITEM_13_EMPTY_HONEYCOMB, -eh_val);
        self._write_bytes(0x77C9A, 2, 0x8000 - eh_val)
        
        # Total Health Calculation (Loading Game/Zone)
        # D_80385F30[ITEM_13_EMPTY_HONEYCOMB] = honeycombscore_get_total() % eh_val;
        self._write_byte(0xC091F, eh_val)
        # D_80385F30[ITEM_15_HEALTH_TOTAL] =  start_health + MIN(8 - start_val, (honeycombscore_get_total() / eh_val));
        self._write_byte(0xC095F, eh_val)

    def _starting_lives(self, start_val):
        '''Modifies the player's starting life count, and lives upon re-entering the game'''
        self._write_byte(0xBF51B, start_val)
    
    def _infinite_lives(self):
        '''Removes the life count decrease function upon death'''
        self._write_bytes(0xBF72C, 8, 0x0000000000000000)

    #################
    ### COLLISION ###
    #################

    def _modify_object_collision(self, collision_dict):
        pass

    ################
    ### BK MODEL ###
    ################

    def _always_high_poly_bk_model(self):
        '''Replaces all instances of the low poly BK model with the high poly BK model'''
        self._write_bytes(0x11722, 2, 0x34E)
        self._write_bytes(0x1172A, 2, 0x34E)

    def _always_wishywashy_model(self):
        '''Replaces all instances of the BK model with the WishyWashy BK model'''
        self._write_bytes(0x116C2, 2, 0x34E)
        self._write_bytes(0x11722, 2, 0x356)
        self._write_bytes(0x1172A, 2, 0x356)
        self._write_bytes(0x1172E, 2, 0x356)
    
    def _replace_bk_model_with_asset(self, asset):
        '''Replaces all instances of the BK model with another model'''
        self._write_bytes(0x11722, 2, asset)
        self._write_bytes(0x1172A, 2, asset)
        self._write_bytes(0x1172E, 2, asset)
    
    ####################
    ### OTHER MODELS ###
    ####################
    
    def _replace_bk_termite_model_with_asset(self, asset):
        '''Replaces instance of the BK Termite model with another model'''
        self._write_bytes(0x1169A, 2, asset)
    
    def _replace_bk_crocodile_model_with_asset(self, asset):
        '''Replaces instance of the BK Crocodile model with another model'''
        self._write_bytes(0x116AA, 2, asset)
    
    def _replace_bk_walrus_model_with_asset(self, asset):
        '''Replaces instance of the BK Walrus model with another model'''
        self._write_bytes(0x116B2, 2, asset)
    
    def _replace_bk_pumpkin_model_with_asset(self, asset):
        '''Replaces instance of the BK Pumpkin model with another model'''
        self._write_bytes(0x116A2, 2, asset)
    
    def _replace_bk_bee_model_with_asset(self, asset):
        '''Replaces instance of the BK Bee model with another model'''
        self._write_bytes(0x116BA, 2, asset)
    
    def _replace_bk_wishywashy_model_with_asset(self, asset):
        '''Replaces instance of the BK WishyWashy model with another model'''
        self._write_bytes(0x116C2, 2, asset)
    
    ##################
    ### PAUSE MENU ###
    ##################

    def _exit_to_witchs_lair(self):
        '''Enables the 'Exit To Witch's Lair' pause menu option'''
        # Disable Exit To Witch's Lair From TRUE to FALSE
        self._write_bytes(0x8BBF8, 4, 0x00001025)
        # Disable Debug Byte
        self._write_byte(0x8BCE7, 0x00)
    
    def _default_totals_screen(self):
        '''When viewing totals, the default page will be the totals page instead of the current map's page'''
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
        '''Player will not receive fall damage when in tumble state'''
        self._write_bytes(0x2D69C, 4, 0x00000000)
        self._write_bytes(0x2D6A0, 4, 0x00000000)
    
    ################################
    ### ALTERNATE WIN CONDITIONS ###
    ################################
    
    def _remove_defeating_gruntilda_check(self):
        '''
        Conditions that would warp the player to the Beach 100 Jiggies cutscene,
        player is no longer required to defeat Gruntilda
        '''
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
        '''
        Modifies the number of Jiggies required to warp the player to the Beach 100 Jiggies cutscene
        Typically used with 'Remove Defeated Gruntilda Check' function
        '''
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
        '''Replaces the Jiggy count that warps the player to the Beach 100 Jiggies cutscene with a Note count'''
        # Note Requirement
        self._write_bytes(0xBFE70, 4, 0x0C0D1BBB)
        self._write_bytes(0xBFE78, 2, 0x2401)
        self._write_byte(0xBFE7A, 2, item_count)
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
        '''Pressing Start will allow the player to skip the intro and lair cutscenes'''
        self._write_bytes(0x9573C, 4, 0x24020001)
    
    def _skippable_game_over_cutscene(self):
        '''Pressing Start will allow the player to skip the game over cutscene'''
        self._write_bytes(0x95770, 4, 0x00000000)
    
    def _booting_up_map(self, map_id):
        '''
        When loading the game, this is the location the player boots up at
        Typically used to skip the Rareware & N64 logo cutscene and the concert
        '''
        self._write_byte(0x1467F, map_id)
        self._write_byte(0x9580B, map_id)

    ############################
    ### TRANSFORMATION COSTS ###
    ############################
    # I have two sets of functions, but they are not all needed
    # Will need to remove/modify functions

    def _termite_transformation_cost(self, transform_cost):
        '''Modifies the number of tokens Mumbo requires for the termite transformation'''
        self._write_byte(0x4A7E7, transform_cost)
    
    def _crocodile_transformation_cost(self, transform_cost):
        '''Modifies the number of tokens Mumbo requires for the crocodile transformation'''
        self._write_byte(0x4A7EF, transform_cost)
    
    def _walrus_transformation_cost(self, transform_cost):
        '''Modifies the number of tokens Mumbo requires for the walrus transformation'''
        self._write_byte(0x4A7F7, transform_cost)
    
    def _pumpkin_transformation_cost(self, transform_cost):
        '''Modifies the number of tokens Mumbo requires for the pumpkin transformation'''
        self._write_byte(0x4A7FF, transform_cost)
    
    def _bee_transformation_cost(self, transform_cost):
        '''Modifies the number of tokens Mumbo requires for the bee transformation'''
        self._write_byte(0x4A807, transform_cost)

    def _read_transformation_costs(self):
        '''Bulk function to read transformation costs'''
        transformation_cost_list = []
        for curr_index in range(0x4A7E7, 0x4A808, 0x8):
            transformation_cost_list.append(self._read_byte(curr_index))
        return transformation_cost_list

    def _modify_transformation_costs(self, replacement_list):
        '''Bulk function to modify transformation costs'''
        for index_count, curr_index in enumerate(range(0x4A7E7, 0x4A808, 0x8)):
            if(replacement_list[index_count] != None):
                self._write_byte(curr_index, replacement_list[index_count])
    
    ###########################
    ### NEW GAME START AREA ###
    ###########################

    def _new_game_start_area(self, map_id, entry_id):
        '''
        Changes the map location and entry point where the player begins their game.
        Not implemented yet.
        '''
        # 0x3E17B - Intro Cutscene
        # 0x986FA - New Game Start
        # starting pointer = 0x9778
        # new_start_level_id = (level_pointer - starting pointer) // 8
        # new_start_level_id = Game_Engine[new_start_level_name]
        # self.core2_obj._modify_byte(0x986FA, start_level_ids[new_start_level_name])
        # if(skip_intro_cutscene):
        #     self.core2_obj._modify_byte(0x3E17B, start_level_ids[new_start_level_name])
        self._write_byte(0x3E17B, map_id)
        self._write_byte(0x986FA, map_id)
        self._write_byte(0x986FB, entry_id)

    def _after_lair_cutscene_starting_area(self):
        '''
        Changes the map location and entry point after the player has watched the 'Enter the lair cutscene'.
        Not implemented yet.
        '''
        pass
        # 0x98BAE - Load Game Start
        # starting pointer = 0x9778
        # new_start_level_id = (level_pointer - starting pointer) // 8
        # new_start_level_id = Game_Engine[new_start_level_name]
        # self.core2_obj._modify_byte(0x98BAE, start_level_ids[load_game_start_level_name])
    
    ##########################
    ### SNACKER EVERYWHERE ###
    ##########################

    def _snacker_remove_ttc_boundaries(self):
        '''
        For TTC, Snacker is typically not allowed near Blubber's ship or at specific heights
        This makes all of the 'not allowed' boundaries extremely small, essentially ignoring the boundaries
        '''
        # Boundaries Are Basically Zero
        self._write_bytes(0x34FC, 4, 0x3C014416)
        self._write_bytes(0x3508, 4, 0x3C060000)
        self._write_bytes(0x3548, 4, 0x3C060000)

    def _snacker_all_maps(self):
        '''Uses the Snacker TTC spawn function for all maps'''
        # Remove Case Statements
        self._write_bytes(0x3950, 4, 0x00000000)
        self._write_bytes(0x3954, 4, 0x00000000)
        self._write_bytes(0x3958, 4, 0x00000000)
        self._write_bytes(0x395C, 4, 0x00000000)
        self._write_bytes(0x3960, 4, 0x00000000)
        self._write_bytes(0x3964, 4, 0x00000000)
        self._write_bytes(0x3968, 4, 0x00000000)
        self._write_bytes(0x396C, 4, 0x00000000)
    
    ########################
    ### EMPTY HONEYCOMBS ###
    ########################
    
    def _mm_fix_honeycomb_flags(self):
        '''
        For most Empty Honeycombs, the ID is determined by the associated flag
        For MM, the ID is determined by height instead of a flag
        Altered the condition of the height mechanic to a map that doesn't exist in order to remove the function
        '''
        # Point To Non-Existing Map
        self._write_bytes(0x42CC0, 4, 0x240100A0)

    def _mmm_anyones_empty_honeycomb(self):
        '''
        MMM's Empty Honeycomb is typically only collectable by the Pumpkin BK
        This allows any transformation to collect the Empty Honeycomb
        '''
        # Remove The Branch For Pumpkin
        self._write_bytes(0x581C, 4, 0x14410000)
    
    #############
    ### WARPS ###
    #############
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/code_956B0.c
    # https://hack64.net/wiki/doku.php?id=banjo_kazooie:enums#map_exit_indices

    def _convert_warp_id(self, map_id, exit_id):
        warp_id = map_id * 0x100 + exit_id
        return warp_id

    def _reassign_sm_main_to_sm_banjos_house_warp(self, map_id, exit_id):
        '''
        Replaces going into Banjo's house warp with a new warp
        0x8c01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x986D6, 2, warp_id)

    def _reassign_sm_main_to_gl_mm_entrance_warp(self, map_id, exit_id):
        '''
        0x6912
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9871E, 2, warp_id)
        # Lair Cutscene If Statement
        self._write_bytes(0x98BAE, 2, warp_id)

    def _reassign_sm_banjos_house_to_sm_main_warp(self, map_id, exit_id):
        '''
        0x112
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x986FA, 2, warp_id)

    def _reassign_gl_mm_entrance_to_sm_main_warp(self, map_id, exit_id):
        '''
        0x113
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98742, 2, warp_id)

    def _reassign_gl_mm_entrance_to_mm_main_warp(self, map_id, exit_id):
        '''
        0x205
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96E8A, 2, warp_id)

    def _reassign_gl_mm_entrance_to_gl_ttc_cc_puzzles_warp(self, map_id, exit_id):
        '''
        0x6a01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97FC6, 2, warp_id)

    def _reassign_gl_ttc_cc_puzzles_to_gl_mm_entrance_warp(self, map_id, exit_id):
        '''
        0x6901
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97EEE, 2, warp_id)

    def _reassign_gl_ttc_cc_puzzles_to_gl_ccw_puzzle_warp(self, map_id, exit_id):
        '''
        0x6b01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98032, 2, warp_id)

    def _reassign_gl_ccw_puzzle_to_gl_ttc_cc_puzzles_warp(self, map_id, exit_id):
        '''
        0x6a02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9800E, 2, warp_id)

    def _reassign_gl_ccw_puzzle_to_gl_ttc_entrance_warp(self, map_id, exit_id):
        '''
        0x6d01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x980C2, 2, warp_id)

    def _reassign_gl_ccw_puzzle_to_gl_pipe_room_warp(self, map_id, exit_id):
        '''
        0x6c01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9807A, 2, warp_id)

    def _reassign_gl_ccw_puzzle_to_gl_cc_entrance_warp(self, map_id, exit_id):
        '''
        0x7001
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9810A, 2, warp_id)

    def _reassign_gl_ccw_puzzle_to_gl_grunty_statue_warp(self, map_id, exit_id):
        '''
        0x7102
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x981E2, 2, warp_id)

    def _reassign_gl_pipe_room_to_gl_ccw_puzzle_warp(self, map_id, exit_id):
        '''
        0x6b02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98056, 2, warp_id)

    def _reassign_gl_ttc_entrance_to_gl_ccw_puzzle_warp(self, map_id, exit_id):
        '''
        0x6b03
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9809E, 2, warp_id)

    def _reassign_gl_ttc_entrance_to_ttc_main_warp(self, map_id, exit_id):
        '''
        0x704
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x965D2, 2, warp_id)
        self._write_bytes(0x978E2, 2, warp_id)

    def _reassign_gl_cc_entrance_to_gl_ccw_puzzle_warp(self, map_id, exit_id):
        '''
        0x6b04
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x980E6, 2, warp_id)

    def _reassign_gl_cc_entrance_to_cc_main_warp(self, map_id, exit_id):
        '''
        0xb05
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97906, 2, warp_id)

    def _reassign_gl_grunty_statue_to_gl_ccw_puzzle_warp(self, map_id, exit_id):
        '''
        0x6b05
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x981BE, 2, warp_id)

    def _reassign_gl_grunty_statue_to_gl_bgs_entrance_warp(self, map_id, exit_id):
        '''
        0x7201
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x982BA, 2, warp_id)

    def _reassign_gl_grunty_statue_to_gl_gv_entrance_warp(self, map_id, exit_id):
        '''
        0x6e01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97ECA, 2, warp_id)

    def _reassign_gl_bgs_entrance_to_bgs_main_warp(self, map_id, exit_id):
        '''
        0xd02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9792A, 2, warp_id)

    def _reassign_gl_bgs_entrance_to_gl_grunty_statue_warp(self, map_id, exit_id):
        '''
        0x7103
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98296, 2, warp_id)

    def _reassign_gl_gv_entrance_to_gl_grunty_statue_note_door_warp(self, map_id, exit_id):
        '''
        0x7101
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97FEA, 2, warp_id)

    def _reassign_gl_gv_entrance_to_gl_grunty_statue_witch_switch_warp(self, map_id, exit_id):
        '''
        0x7104
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98BFE, 2, warp_id)

    def _reassign_gl_gv_entrance_to_gl_fp_entrance_warp(self, map_id, exit_id):
        '''
        0x6f01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97F12, 2, warp_id)

    def _reassign_gl_gv_entrance_to_gv_main_warp(self, map_id, exit_id):
        '''
        0x1208
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9794E, 2, warp_id)

    def _reassign_gl_fp_entrance_to_fp_main_warp(self, map_id, exit_id):
        '''
        0x2701
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98152, 2, warp_id)

    def _reassign_gl_fp_entrance_to_gl_gv_entrance_warp(self, map_id, exit_id):
        '''
        0x6e02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97F36, 2, warp_id)

    def _reassign_gl_fp_entrance_to_gl_gv_puzzle_warp(self, map_id, exit_id):
        '''
        0x7402
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9824E, 2, warp_id)

    def _reassign_gl_fp_entrance_to_gl_water_three_switch_warp(self, map_id, exit_id):
        '''
        0x7601
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x983BA, 2, warp_id)

    def _reassign_gl_gv_puzzle_to_gl_fp_entrance_warp(self, map_id, exit_id):
        '''
        0x6f05
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98272, 2, warp_id)

    def _reassign_gl_gv_puzzle_to_gl_mmm_entrance_warp(self, map_id, exit_id):
        '''
        0x7501
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9822A, 2, warp_id)

    def _reassign_gl_mmm_entrance_to_gl_gv_puzzle_warp(self, map_id, exit_id):
        '''
        0x7401
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98206, 2, warp_id)

    def _reassign_gl_mmm_entrance_to_gl_crypt_warp(self, map_id, exit_id):
        '''
        0x7a01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x982F2, 2, warp_id)

    def _reassign_gl_mmm_entrance_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b14
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97972, 2, warp_id)

    def _reassign_gl_crypt_to_gl_mmm_entrance_warp(self, map_id, exit_id):
        '''
        0x7503
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9832A, 2, warp_id)

    def _reassign_gl_water_three_switch_to_gl_fp_entrance_warp(self, map_id, exit_id):
        '''
        0x6f02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x985B6, 2, warp_id)

    def _reassign_gl_water_three_switch_to_gl_rbb_entrance_warp(self, map_id, exit_id):
        '''
        0x7701
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9844A, 2, warp_id)

    def _reassign_gl_water_three_switch_to_gl_ccw_entrance_note_door_warp(self, map_id, exit_id):
        '''
        0x7901
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9846E, 2, warp_id)

    def _reassign_gl_water_three_switch_to_gl_ccw_entrance_token_warp(self, map_id, exit_id):
        '''
        0x7902
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98492, 2, warp_id)

    def _reassign_gl_rbb_entrance_to_gl_water_three_switch_warp(self, map_id, exit_id):
        '''
        0x7604
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98426, 2, warp_id)

    def _reassign_gl_rbb_entrance_to_gl_mmm_puzzle_warp(self, map_id, exit_id):
        '''
        0x7801
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98646, 2, warp_id)

    def _reassign_gl_rbb_entrance_to_gl_rbb_puzzle_warp(self, map_id, exit_id):
        '''
        0x7802
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9866A, 2, warp_id)

    def _reassign_gl_rbb_entrance_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3110
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97996, 2, warp_id)

    def _reassign_gl_mmm_puzzle_to_gl_rbb_entrance_warp(self, map_id, exit_id):
        '''
        0x7704
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98622, 2, warp_id)

    def _reassign_gl_rbb_puzzle_to_gl_rbb_entrance_warp(self, map_id, exit_id):
        '''
        0x7703
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x985FE, 2, warp_id)

    def _reassign_gl_ccw_entrance_to_gl_water_three_switch_note_door_warp(self, map_id, exit_id):
        '''
        0x7603
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98402, 2, warp_id)

    def _reassign_gl_ccw_entrance_to_gl_water_three_switch_token_warp(self, map_id, exit_id):
        '''
        0x7602
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x983DE, 2, warp_id)

    def _reassign_gl_ccw_entrance_to_gl_path_to_ff_warp(self, map_id, exit_id):
        '''
        0x8001
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x986B2, 2, warp_id)

    def _reassign_gl_ccw_entrance_to_ccw_main_warp(self, map_id, exit_id):
        '''
        0x4007
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x988FA, 2, warp_id)

    def _reassign_gl_path_to_ff_to_gl_ccw_entrance_warp(self, map_id, exit_id):
        '''
        0x7903
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9868E, 2, warp_id)

    def _reassign_gl_ff_to_gl_door_of_grunty_warp(self, map_id, exit_id):
        '''
        0x9305
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98AEE, 2, warp_id)

    def _reassign_gl_door_of_grunty_to_gl_ff_warp(self, map_id, exit_id):
        '''
        0x8e05
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98B12, 2, warp_id)

    def _reassign_gl_door_of_grunty_to_final_battle_warp(self, map_id, exit_id):
        '''
        0x9001
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98B72, 2, warp_id)

    def _reassign_mm_main_to_gl_mm_entrance_warp(self, map_id, exit_id):
        '''
        0x6902
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97F7E, 2, warp_id)

    def _reassign_mm_main_to_mm_mumbos_skull_warp(self, map_id, exit_id):
        '''
        0xe01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9619E, 2, warp_id)

    def _reassign_mm_main_to_mm_lower_tickers_warp(self, map_id, exit_id):
        '''
        0xc02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x961E6, 2, warp_id)

    def _reassign_mm_main_to_mm_upper_tickers_warp(self, map_id, exit_id):
        '''
        0xc01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9622E, 2, warp_id)

    def _reassign_mm_mumbos_skull_to_mm_main_warp(self, map_id, exit_id):
        '''
        0x201
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x961C2, 2, warp_id)

    def _reassign_mm_lower_tickers_to_mm_main_warp(self, map_id, exit_id):
        '''
        0x202
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9620A, 2, warp_id)

    def _reassign_mm_upper_tickers_to_mm_main_warp(self, map_id, exit_id):
        '''
        0x203
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96252, 2, warp_id)

    def _reassign_ttc_main_to_gl_ttc_entrance_warp(self, map_id, exit_id):
        '''
        0x6d04
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x988B2, 2, warp_id)

    def _reassign_ttc_main_to_ttc_sandcastle_warp(self, map_id, exit_id):
        '''
        0xa01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x964D6, 2, warp_id)

    def _reassign_ttc_main_to_ttc_nipper_warp(self, map_id, exit_id):
        '''
        0x601
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96DD6, 2, warp_id)

    def _reassign_ttc_main_to_ttc_salty_hippo_side_warp(self, map_id, exit_id):
        '''
        0x506
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96566, 2, warp_id)

    def _reassign_ttc_main_to_ttc_salty_hippo_top_warp(self, map_id, exit_id):
        '''
        0x505
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96542, 2, warp_id)

    def _reassign_ttc_alcove_lower_to_ttc_alcove_upper_warp(self, map_id, exit_id):
        '''
        0x70e
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9651E, 2, warp_id)

    def _reassign_ttc_alcove_upper_to_ttc_alcove_lower_warp(self, map_id, exit_id):
        '''
        0x70f
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x964FA, 2, warp_id)

    def _reassign_ttc_lighthouse_lower_to_ttc_lighthouse_upper_warp(self, map_id, exit_id):
        '''
        0x708
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9658A, 2, warp_id)
        self._write_bytes(0x96662, 2, warp_id)

    # def _reassign_ttc_lighthouse_upper_to_ttc_lighthouse_lower_warp(self, map_id, exit_id):
    #     '''
    #     0x70c # I can't find this? But it works in game...
    #     '''
    #     warp_id = self._convert_warp_id(map_id, exit_id)
    #     self._write_bytes(0x00000, 2, warp_id)

    def _reassign_ttc_sandcastle_to_ttc_main_warp(self, map_id, exit_id):
        '''
        0x703
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x965AE, 2, warp_id)

    def _reassign_ttc_nipper_to_ttc_main_warp(self, map_id, exit_id):
        '''
        0x70a
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x979BA, 2, warp_id)

    def _reassign_ttc_salty_hippo_side_to_ttc_main_warp(self, map_id, exit_id):
        '''
        0x707
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9663E, 2, warp_id)

    def _reassign_ttc_salty_hippo_top_to_ttc_main_warp(self, map_id, exit_id):
        '''
        0x706
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9661A, 2, warp_id)

    def _reassign_ttc_sharkfood_island_to_ttc_main_warp(self, map_id, exit_id):
        '''
        0x780
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98A82, 2, warp_id)

    def _reassign_cc_main_to_gl_cc_entrance_warp(self, map_id, exit_id):
        '''
        0x7002
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9812E, 2, warp_id)

    def _reassign_cc_clanker_wonderwing_to_cc_clanker_belly_warp(self, map_id, exit_id):
        '''
        0x2203
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96DFA, 2, warp_id)

    def _reassign_cc_clanker_blowhole_to_cc_clanker_mouth_warp(self, map_id, exit_id):
        '''
        0x2202
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96E42, 2, warp_id)

    def _reassign_cc_clanker_blowhole_to_cc_clanker_belly_warp(self, map_id, exit_id):
        '''
        0x2201
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96E1E, 2, warp_id)

    def _reassign_cc_clanker_belly_to_cc_clanker_wonderwing_warp(self, map_id, exit_id):
        '''
        0x2301
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96E66, 2, warp_id)

    def _reassign_bgs_main_to_gl_bgs_entrance_warp(self, map_id, exit_id):
        '''
        0x7202
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98396, 2, warp_id)

    def _reassign_bgs_main_to_bgs_mumbos_skull_warp(self, map_id, exit_id):
        '''
        0x4701
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x978BE, 2, warp_id)

    def _reassign_bgs_main_to_bgs_tanktup_warp(self, map_id, exit_id):
        '''
        0x1101
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96446, 2, warp_id)
        self._write_bytes(0x96DA2, 2, warp_id)

    def _reassign_bgs_mumbos_skull_to_bgs_main_warp(self, map_id, exit_id):
        '''
        0xd06
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9789A, 2, warp_id)

    def _reassign_bgs_tanktup_to_bgs_main_warp(self, map_id, exit_id):
        '''
        0xd03
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9646A, 2, warp_id)

    def _reassign_bgs_main_to_bgs_vile_left_warp(self, map_id, exit_id):
        '''
        Issue: Conflicts with BGS Vile Right Warp
        0x1004
        '''
        self._write_bytes(0x96D26, 2, map_id)
        self._write_bytes(0x96D6E, 2, exit_id)

    def _reassign_bgs_main_to_bgs_vile_right_warp(self, map_id, exit_id):
        '''
        Issue: Conflicts with BGS Vile Left Warp
        0x1003
        '''
        self._write_bytes(0x96D26, 2, map_id)
        self._write_bytes(0x96D4A, 2, exit_id)

    def _reassign_bgs_vile_left_to_bgs_main_warp(self, map_id, exit_id):
        '''
        0xd05
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x964B2, 2, warp_id)

    def _reassign_bgs_vile_right_to_bgs_main_warp(self, map_id, exit_id):
        '''
        0xd04
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9648E, 2, warp_id)

    def _reassign_fp_main_to_gl_fp_entrance_warp(self, map_id, exit_id):
        '''
        0x6f06
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9891E, 2, warp_id)

    def _reassign_fp_main_to_fp_igloo_warp(self, map_id, exit_id):
        '''
        0x4101
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97E16, 2, warp_id)

    def _reassign_fp_main_to_fp_tree_warp(self, map_id, exit_id):
        '''
        0x5301
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97E3A, 2, warp_id)

    def _reassign_fp_main_to_fp_mumbos_skull_warp(self, map_id, exit_id):
        '''
        0x4801
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97DF2, 2, warp_id)

    def _reassign_fp_main_to_fp_wozzas_cave_warp(self, map_id, exit_id):
        '''
        0x7f01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98372, 2, warp_id)

    def _reassign_fp_igloo_to_fp_main_warp(self, map_id, exit_id):
        '''
        0x2708
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97E82, 2, warp_id)

    def _reassign_fp_tree_to_fp_main_warp(self, map_id, exit_id):
        '''
        0x2709
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97EA6, 2, warp_id)

    def _reassign_fp_mumbos_skull_to_fp_main_warp(self, map_id, exit_id):
        '''
        0x2707
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97E5E, 2, warp_id)

    def _reassign_fp_wozzas_cave_to_fp_main_warp(self, map_id, exit_id):
        '''
        0x2706
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9834E, 2, warp_id)

    def _reassign_gv_main_to_gl_gv_entrance_warp(self, map_id, exit_id):
        '''
        0x6e03
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97F5A, 2, warp_id)

    def _reassign_gv_main_to_gv_jinxy_warp(self, map_id, exit_id):
        '''
        0x1a02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96EAE, 2, warp_id)

    def _reassign_gv_main_to_gv_rubee_warp(self, map_id, exit_id):
        '''
        0x1607
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x962DA, 2, warp_id)

    def _reassign_gv_main_to_gv_water_pyramid_upper_warp(self, map_id, exit_id):
        '''
        0x1502
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96352, 2, warp_id)

    def _reassign_gv_main_to_gv_water_pyramid_lower_warp(self, map_id, exit_id):
        '''
        0x1506
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9629A, 2, warp_id)

    def _reassign_gv_main_to_gv_matching_pyramid_warp(self, map_id, exit_id):
        '''
        0x1301
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96312, 2, warp_id)

    def _reassign_gv_main_to_king_sandybutt_warp(self, map_id, exit_id):
        '''
        0x1401
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96392, 2, warp_id)

    def _reassign_gv_main_to_gv_sns_room_warp(self, map_id, exit_id):
        '''
        0x9205
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98AA6, 2, warp_id)

    def _reassign_gv_jinxy_to_gv_main_warp(self, map_id, exit_id):
        '''
        0x1202
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96ED2, 2, warp_id)

    def _reassign_gv_rubee_to_gv_main_warp(self, map_id, exit_id):
        '''
        0x1206
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96422, 2, warp_id)

    def _reassign_gv_water_pyramid_lower_to_gv_main_warp(self, map_id, exit_id):
        '''
        0x1205
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x963FE, 2, warp_id)
        # self._write_bytes(0x98AA6, 2, warp_id)

    def _reassign_gv_matching_pyramid_to_gv_main_warp(self, map_id, exit_id):
        '''
        0x1203
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x963B6, 2, warp_id)

    def _reassign_gv_king_sandybutt_front_to_gv_main_warp(self, map_id, exit_id):
        '''
        0x1204
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x963DA, 2, warp_id)

    def _reassign_gv_king_sandybutt_back_to_gv_main_warp(self, map_id, exit_id):
        '''
        0x1207
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97876, 2, warp_id)

    def _reassign_gv_sns_room_to_gv_main_warp(self, map_id, exit_id):
        '''
        0x120a
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98ACA, 2, warp_id)

    def _reassign_mmm_main_to_gl_mmm_entrance_warp(self, map_id, exit_id):
        '''
        0x7502
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9888E, 2, warp_id)

    def _reassign_mmm_main_to_mmm_napper_front_warp(self, map_id, exit_id):
        '''
        0x2601
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x966F2, 2, warp_id)

    def _reassign_mmm_main_to_mmm_napper_chimney_warp(self, map_id, exit_id):
        '''
        0x2602
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96716, 2, warp_id)

    def _reassign_mmm_main_to_mmm_egg_room_warp(self, map_id, exit_id):
        '''
        0x2801
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x967CA, 2, warp_id)

    def _reassign_mmm_main_to_mmm_red_feather_room_warp(self, map_id, exit_id):
        '''
        0x2a01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x967A6, 2, warp_id)

    def _reassign_mmm_main_to_mmm_honeycomb_room_warp(self, map_id, exit_id):
        '''
        0x2e01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96812, 2, warp_id)

    def _reassign_mmm_main_to_mmm_loggo_room_warp(self, map_id, exit_id):
        '''
        0x2c01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9685A, 2, warp_id)

    def _reassign_mmm_main_to_mmm_bedroom_warp(self, map_id, exit_id):
        '''
        0x2d01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96836, 2, warp_id)

    def _reassign_mmm_main_to_mmm_note_room_warp(self, map_id, exit_id):
        '''
        0x2901
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x967EE, 2, warp_id)

    def _reassign_mmm_main_to_mmm_church_warp(self, map_id, exit_id):
        '''
        0x1c01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96BB2, 2, map_id)
        self._write_bytes(0x96BBA, 2, exit_id)

    def _reassign_mmm_main_to_mmm_secret_room_warp(self, map_id, exit_id):
        '''
        0x2b01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96B06, 2, warp_id)

    def _reassign_mmm_main_to_mmm_cellar_warp(self, map_id, exit_id):
        '''
        0x1d01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96782, 2, warp_id)

    def _reassign_mmm_main_to_mmm_well_top_warp(self, map_id, exit_id):
        '''
        0x2501
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9673A, 2, warp_id)

    def _reassign_mmm_main_to_mmm_mumbos_skull_warp(self, map_id, exit_id):
        '''
        0x3001
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96BE6, 2, warp_id)
        self._write_bytes(0x96C0A, 2, warp_id)

    def _reassign_mmm_main_to_mmm_tumblar_warp(self, map_id, exit_id):
        '''
        0x2401
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9675E, 2, warp_id)

    def _reassign_mmm_church_lower_to_mmm_church_upper_warp(self, map_id, exit_id):
        '''
        0x1b10
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96A9A, 2, warp_id)

    def _reassign_mmm_church_upper_to_mmm_church_lower_warp(self, map_id, exit_id):
        '''
        0x1b11
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96ABE, 2, warp_id)

    def _reassign_mmm_napper_front_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9687E, 2, warp_id)

    def _reassign_mmm_egg_room_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b0b
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x969E6, 2, warp_id)

    def _reassign_mmm_red_feather_room_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b0a
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x969C2, 2, warp_id)

    def _reassign_mmm_honeycomb_room_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b0d
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96A2E, 2, warp_id)

    def _reassign_mmm_loggo_room_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b0c
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96A0A, 2, warp_id)

    def _reassign_mmm_bedroom_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b0e
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96A52, 2, warp_id)

    def _reassign_mmm_note_room_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b0f
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96A76, 2, warp_id)

    def _reassign_mmm_church_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b05
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9690E, 2, warp_id)

    def _reassign_mmm_secret_room_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b06
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96932, 2, warp_id)

    def _reassign_mmm_cellar_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b09
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9699E, 2, warp_id)

    def _reassign_mmm_well_top_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b03
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x968C6, 2, warp_id)

    def _reassign_mmm_mumbos_skull_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b12
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96AE2, 2, warp_id)

    def _reassign_mmm_tumblar_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b04
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x968EA, 2, warp_id)

    def _reassign_mmm_main_to_mmm_gutter_top_warp(self, map_id, exit_id):
        '''
        0x2f01
        '''
        self._write_bytes(0x96C62, 2, map_id)
        self._write_bytes(0x96C66, 2, exit_id)

    def _reassign_mmm_main_to_mmm_gutter_bottom_warp(self, map_id, exit_id):
        '''
        0x2f02
        '''
        self._write_bytes(0x96C46, 2, map_id * 0x100)
        self._write_bytes(0x96CEA, 2, exit_id)

    def _reassign_mmm_main_to_mmm_well_bottom_warp(self, map_id, exit_id):
        '''
        0x2504
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x987C2, 2, warp_id)

    def _reassign_mmm_loggo_room_to_mmm_inside_loggo_warp(self, map_id, exit_id):
        '''
        0x8d04
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9886A, 2, warp_id)

    def _reassign_mmm_gutter_bottom_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b08
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9697A, 2, warp_id)

    def _reassign_mmm_well_bottom_to_mmm_main_warp(self, map_id, exit_id):
        '''
        0x1b13
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x987FA, 2, warp_id)

    def _reassign_mmm_inside_loggo_to_mmm_loggo_room_warp(self, map_id, exit_id):
        '''
        0x2c04
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98832, 2, warp_id)

    def _reassign_rbb_main_to_gl_rbb_entrance_warp(self, map_id, exit_id):
        '''
        0x7702
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x985DA, 2, warp_id)

    def _reassign_rbb_main_to_rbb_big_fish_warehouse_top_warp(self, map_id, exit_id):
        '''
        0x3502
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96FF2, 2, warp_id)

    def _reassign_rbb_main_to_rbb_big_fish_warehouse_bottom_warp(self, map_id, exit_id):
        '''
        0x3501
        '''
        self._write_bytes(0x97336, 2, map_id)
        self._write_bytes(0x9733E, 2, exit_id)

    def _reassign_rbb_main_to_rbb_boat_room_warp(self, map_id, exit_id):
        '''
        0x3601
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97016, 2, warp_id)

    def _reassign_rbb_main_to_rbb_boom_box_container_warp(self, map_id, exit_id):
        '''
        0x3801
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97082, 2, warp_id)

    def _reassign_rbb_main_to_rbb_seaman_grublin_container_warp(self, map_id, exit_id):
        '''
        0x3e01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9705E, 2, warp_id)

    def _reassign_rbb_main_to_rbb_chompa_container_warp(self, map_id, exit_id):
        '''
        0x3701
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9703A, 2, warp_id)

    def _reassign_rbb_main_to_rbb_kitchen_pipe_warp(self, map_id, exit_id):
        '''
        0x3c01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96F86, 2, warp_id)

    def _reassign_rbb_main_to_rbb_boom_box_pipe_warp(self, map_id, exit_id):
        '''
        0x3b01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96FCE, 2, warp_id)

    def _reassign_rbb_main_to_rbb_engine_room_pipe_warp(self, map_id, exit_id):
        '''
        0x3404
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96F3E, 2, warp_id)

    def _reassign_rbb_main_to_rbb_engine_room_main_warp(self, map_id, exit_id):
        '''
        0x3401
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96F62, 2, warp_id)

    def _reassign_rbb_main_to_rbb_control_room_window_warp(self, map_id, exit_id):
        '''
        0x3d01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96FAA, 2, warp_id)

    def _reassign_rbb_main_to_rbb_captains_room_window_warp(self, map_id, exit_id):
        '''
        0x3f01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96EF6, 2, warp_id)

    def _reassign_rbb_main_to_rbb_cabin_window_warp(self, map_id, exit_id):
        '''
        0x3901
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x96F1A, 2, warp_id)

    def _reassign_rbb_main_to_rbb_boss_boom_box_warp(self, map_id, exit_id):
        '''
        0x3a01
        '''
        self._write_bytes(0x9725A, 2, map_id)
        self._write_bytes(0x97256, 2, exit_id)

    def _reassign_rbb_main_to_rbb_anchor_warp(self, map_id, exit_id):
        '''
        0x8b04
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9878A, 2, warp_id)

    def _reassign_rbb_big_fish_warehouse_bottom_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x310d
        '''
        self._write_bytes(0x9735E, 2, map_id)
        self._write_bytes(0x97366, 2, exit_id)

    def _reassign_rbb_boat_room_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3108
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x971A2, 2, warp_id)

    def _reassign_rbb_boom_box_container_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x310b
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9720E, 2, warp_id)

    def _reassign_rbb_seaman_grublin_container_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x310a
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x971EA, 2, warp_id)

    def _reassign_rbb_chompa_container_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3109
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x971C6, 2, warp_id)

    def _reassign_rbb_kitchen_pipe_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3104
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97112, 2, warp_id)

    def _reassign_rbb_boom_box_pipe_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3106
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9715A, 2, warp_id)

    def _reassign_rbb_engine_room_pipe_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3103
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x970EE, 2, warp_id)

    def _reassign_rbb_engine_room_main_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3107
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9717E, 2, warp_id)

    def _reassign_rbb_control_room_window_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3105
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97136, 2, warp_id)

    def _reassign_rbb_captains_room_window_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3101
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x970A6, 2, warp_id)

    def _reassign_rbb_cabin_window_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3102
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x970CA, 2, warp_id)

    def _reassign_rbb_boss_boom_box_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x310c
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97232, 2, warp_id)

    def _reassign_rbb_anchor_to_rbb_main_warp(self, map_id, exit_id):
        '''
        0x3113
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98766, 2, warp_id)

    def _reassign_ccw_main_to_gl_ccw_entrance_warp(self, map_id, exit_id):
        '''
        0x7906
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x988D6, 2, warp_id)

    def _reassign_ccw_main_to_ccw_spring_main_warp(self, map_id, exit_id):
        '''
        0x4301
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9780A, 2, warp_id)

    def _reassign_ccw_main_to_ccw_summer_main_warp(self, map_id, exit_id):
        '''
        0x4401
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9782E, 2, warp_id)

    def _reassign_ccw_main_to_ccw_autumn_main_warp(self, map_id, exit_id):
        '''
        0x4501
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97852, 2, warp_id)

    def _reassign_ccw_main_to_ccw_winter_main_warp(self, map_id, exit_id):
        '''
        0x4601
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x977E6, 2, warp_id)

    def _reassign_ccw_spring_main_to_ccw_main_warp(self, map_id, exit_id):
        '''
        0x4002
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9777A, 2, warp_id)

    def _reassign_ccw_spring_main_to_ccw_spring_mumbos_skull_warp(self, map_id, exit_id):
        '''
        0x4a01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x979DE, 2, warp_id)

    def _reassign_ccw_spring_main_to_ccw_spring_nabnut_door_warp(self, map_id, exit_id):
        '''
        0x5e01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97C1E, 2, warp_id)

    def _reassign_ccw_spring_main_to_ccw_spring_nabnut_window_warp(self, map_id, exit_id):
        '''
        0x5e02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98942, 2, warp_id)

    def _reassign_ccw_spring_main_to_ccw_spring_whipcracks_warp(self, map_id, exit_id):
        '''
        0x6501
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97AFE, 2, warp_id)

    def _reassign_ccw_spring_mumbos_skull_to_ccw_spring_main_warp(self, map_id, exit_id):
        '''
        0x4309
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97A6E, 2, warp_id)

    def _reassign_ccw_spring_nabnut_door_to_ccw_spring_main_warp(self, map_id, exit_id):
        '''
        0x4307
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97C8A, 2, warp_id)

    def _reassign_ccw_spring_nabnut_window_to_ccw_spring_main_warp(self, map_id, exit_id):
        '''
        0x4304
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x989D2, 2, warp_id)

    def _reassign_ccw_spring_whipcracks_to_ccw_spring_main_warp(self, map_id, exit_id):
        '''
        0x4308
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97B8E, 2, warp_id)

    def _reassign_ccw_spring_main_to_ccw_spring_zubba_warp(self, map_id, exit_id):
        '''
        0x5b01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9857E, 2, warp_id)

    def _reassign_ccw_spring_zubba_to_ccw_spring_main_warp(self, map_id, exit_id):
        '''
        0x4306
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x984FE, 2, warp_id)

    def _reassign_ccw_summer_main_to_ccw_main_warp(self, map_id, exit_id):
        '''
        0x4003
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9779E, 2, warp_id)

    def _reassign_ccw_summer_main_to_ccw_summer_mumbos_skull_warp(self, map_id, exit_id):
        '''
        0x4b01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97A02, 2, warp_id)

    def _reassign_ccw_summer_main_to_ccw_summer_zubba_warp(self, map_id, exit_id):
        '''
        0x5a02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x984B6, 2, warp_id)

    def _reassign_ccw_summer_main_to_ccw_summer_nabnut_door_warp(self, map_id, exit_id):
        '''
        0x5f01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97C42, 2, warp_id)

    def _reassign_ccw_summer_main_to_ccw_summer_nabnut_window_warp(self, map_id, exit_id):
        '''
        0x5f02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98966, 2, warp_id)

    def _reassign_ccw_summer_main_to_ccw_summer_whipcracks_warp(self, map_id, exit_id):
        '''
        0x6601
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97B22, 2, warp_id)

    def _reassign_ccw_summer_mumbos_skull_to_ccw_summer_main_warp(self, map_id, exit_id):
        '''
        0x4409
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97A92, 2, warp_id)

    def _reassign_ccw_summer_zubba_to_ccw_summer_main_warp(self, map_id, exit_id):
        '''
        0x4406
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98522, 2, warp_id)

    def _reassign_ccw_summer_nabnut_door_to_ccw_summer_main_warp(self, map_id, exit_id):
        '''
        0x4407
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97CAE, 2, warp_id)

    def _reassign_ccw_summer_nabnut_window_to_ccw_summer_main_warp(self, map_id, exit_id):
        '''
        0x4404
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x989F6, 2, warp_id)

    def _reassign_ccw_summer_whipcracks_to_ccw_summer_main_warp(self, map_id, exit_id):
        '''
        0x4408
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97BB2, 2, warp_id)

    def _reassign_ccw_autumn_main_to_ccw_main_warp(self, map_id, exit_id):
        '''
        0x4004
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x977C2, 2, warp_id)

    def _reassign_ccw_autumn_main_to_ccw_autumn_mumbos_skull_warp(self, map_id, exit_id):
        '''
        0x4c01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97A26, 2, warp_id)

    def _reassign_ccw_autumn_main_to_ccw_autumn_zubba_warp(self, map_id, exit_id):
        '''
        0x5c02
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x984DA, 2, warp_id)

    def _reassign_ccw_autumn_main_to_ccw_autumn_nabnut_door_warp(self, map_id, exit_id):
        '''
        0x6001
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97C66, 2, warp_id)

    def _reassign_ccw_autumn_main_to_ccw_autumn_nabnut_window_warp(self, map_id, exit_id):
        '''
        0x6002
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x9898A, 2, warp_id)

    def _reassign_ccw_autumn_main_to_ccw_autumn_flooded_attic_warp(self, map_id, exit_id):
        '''
        0x6301
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97D3E, 2, warp_id)

    def _reassign_ccw_autumn_main_to_ccw_autumn_whipcracks_warp(self, map_id, exit_id):
        '''
        0x6701
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97B46, 2, warp_id)

    def _reassign_ccw_autumn_mumbos_skull_to_ccw_autumn_main_warp(self, map_id, exit_id):
        '''
        0x4509
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97AB6, 2, warp_id)

    def _reassign_ccw_autumn_zubba_to_ccw_autumn_main_warp(self, map_id, exit_id):
        '''
        0x4505
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98546, 2, warp_id)

    def _reassign_ccw_autumn_nabnut_door_to_ccw_autumn_main_warp(self, map_id, exit_id):
        '''
        0x4507
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97CD2, 2, warp_id)

    def _reassign_ccw_autumn_nabnut_window_to_ccw_autumn_main_warp(self, map_id, exit_id):
        '''
        0x4504
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98A1A, 2, warp_id)

    def _reassign_ccw_autumn_flooded_attic_to_ccw_autumn_main_warp(self, map_id, exit_id):
        '''
        0x4506
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97DAA, 2, warp_id)

    def _reassign_ccw_autumn_whipcracks_to_ccw_autumn_main_warp(self, map_id, exit_id):
        '''
        0x4508
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97BD6, 2, warp_id)

    def _reassign_ccw_winter_main_to_ccw_main_warp(self, map_id, exit_id):
        '''
        0x4001
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97756, 2, warp_id)

    def _reassign_ccw_winter_main_to_ccw_winter_mumbos_skull_warp(self, map_id, exit_id):
        '''
        0x4d01
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97A4A, 2, warp_id)

    def _reassign_ccw_winter_main_to_ccw_winter_nabnut_window_warp(self, map_id, exit_id):
        '''
        0x6102
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x989AE, 2, warp_id)

    def _reassign_ccw_winter_main_to_ccw_winter_acorn_storage_warp(self, map_id, exit_id):
        '''
        0x6201
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x00000, 2, warp_id)

    def _reassign_ccw_winter_main_to_ccw_winter_flooded_attic_warp(self, map_id, exit_id):
        '''
        0x6401
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97D1A, 2, warp_id)

    def _reassign_ccw_winter_main_to_ccw_winter_whipcracks_warp(self, map_id, exit_id):
        '''
        0x6801
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97B6A, 2, warp_id)

    def _reassign_ccw_winter_mumbos_skull_to_ccw_winter_main_warp(self, map_id, exit_id):
        '''
        0x4609
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97ADA, 2, warp_id)

    def _reassign_ccw_winter_nabnut_window_to_ccw_winter_main_warp(self, map_id, exit_id):
        '''
        0x4604
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x98A3E, 2, warp_id)

    def _reassign_ccw_winter_acorn_storage_to_ccw_winter_main_warp(self, map_id, exit_id):
        '''
        0x4606
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97D86, 2, warp_id)

    def _reassign_ccw_winter_flooded_attic_to_ccw_winter_main_warp(self, map_id, exit_id):
        '''
        0x4605
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97DCE, 2, warp_id)

    def _reassign_ccw_winter_whipcracks_to_ccw_winter_main_warp(self, map_id, exit_id):
        '''
        0x4608
        '''
        warp_id = self._convert_warp_id(map_id, exit_id)
        self._write_bytes(0x97BFA, 2, warp_id)
    
    ##############
    ### TIMERS ###
    ##############

    def _remove_regular_slope_slide_timer(self):
        '''
        Removes the slope timer for slopes that require talon trot or transformations.
        Banjo still slows as he goes up, but the player can jump their way to the top.
        * Changed the "STATE_TIMER_5_UNKNOWN" to a "STATE_TIMER_1_THROW".
        * Get_Slope_Timer function always returns zero.
        '''
        # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/code_39D0.c#L213
        self._write_byte(0x43B7, 0x01)
        # self._write_bytes(0x43CE, 2, 0xBFF0)
        # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/code_D9B0.c#L51
        self._write_bytes(0xDA4E, 2, 0x0000)
    
    def _remove_steep_slope_slide_timer(self):
        '''
        Removes the slope timer for slopes that require transformations.
        * Changed the "STATE_TIMER_6_UNKNOWN" to a "STATE_TIMER_1_THROW".
        * Get_Slope_Timer function always returns zero.
        '''
        # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/code_39D0.c#L200
        self._write_byte(0x425F, 0x01)
        # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/code_D9B0.c#L51
        self._write_bytes(0xDA4E, 2, 0x0000)
    
    ######################
    ### WATER SWITCHES ###
    ######################

    def _water_level_one_automatically(self):
        # What Is The Water Level?
        self._write_bytes(0x4E5BC, 4, 0x24020001)
        self._write_bytes(0x4E5C0, 4, 0x24030001)
        self._write_bytes(0x4E5C4, 4, 0x24020001)
        # When Entering 640 Note Door Room,
        # Should The Player Be Swimming Or Walking?
        self._write_bytes(0x4F14C, 4, 0x24020001)
        self._write_bytes(0x4F160, 4, 0x24020001)
        self._write_bytes(0x4F170, 4, 0x24020001)

    def _water_level_two_automatically(self):
        # What Is The Water Level?
        self._write_bytes(0x4E5B8, 4, 0x24020002)
        self._write_bytes(0x4E5BC, 4, 0x24020002)
        self._write_bytes(0x4E5C0, 4, 0x24030002)
        self._write_bytes(0x4E5C4, 4, 0x24020002)
        # When Exiting RBB,
        # Should The Player Be Swimming Or Walking?
        self._write_bytes(0x4F110, 4, 0x24020001)
        self._write_bytes(0x4F120, 4, 0x24020001)
        # When Entering 640 Note Door Room,
        # Should The Player Be Swimming Or Walking?
        self._write_bytes(0x4F160, 4, 0x24020001)
        self._write_bytes(0x4F170, 4, 0x24020001)
    
    ###################
    ### BANJO SPEED ###
    ###################
    
    # Swim Speed A
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/bSwim.c#L239

    def _set_swim_a_speed(self, swim_b_speed):
        self._write_float_bytes(0x20AEA, swim_b_speed, 2)
    
    # Swim Speed B
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/bSwim.c#L196

    def _set_swim_b_speed(self, swim_b_speed):
        self._write_float_bytes(0x20942, swim_b_speed, 2)
    
    # Roll Speed
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/bs/twirl.c#L32

    def _set_roll_speed(self, roll_speed):
        self._write_float_bytes(0x2FB8E, roll_speed, 2)
    
    ####################
    ### FIRST PERSON ###
    ####################

    def _remove_first_person_check(self):
        '''Does not work'''
        # Does the BUTTON_C_UP check twice
        self._write_bytes(0xE010, 4, 0x01C01025)
    
    ###################
    ### DEATH RESET ###
    ###################

    def _forgiving_deaths(self):
        # mapSavestate_init()
        self._write_bytes(0x9A7C8, 4, 0x00000000)
        # itemscore_levelReset(D_80383300.level)
        self._write_bytes(0x9A7D0, 4, 0x00000000)
        self._write_bytes(0x9A7D4, 4, 0x00000000)
        self._write_bytes(0x9A7D8, 4, 0x00000000)
        # jiggyscore_clearAllSpawned()
        self._write_bytes(0x9A7DC, 4, 0x00000000)
        # levelSpecificFlags_clear()
        self._write_bytes(0x9A7E4, 4, 0x00000000)
        # # func_803204E4()
        # self._write_bytes(0x9A83C, 4, 0x00000000)
        # mm_resetHuts()
        self._write_bytes(0x9A88C, 4, 0x00000000)
        # ttc_resetTresureHunt()
        self._write_bytes(0x9A89C, 4, 0x00000000)
        # mmm_resetFlowerPots()
        self._write_bytes(0x9A8AC, 4, 0x00000000)
    
    ###############
    ### MARKERS ###
    ###############

    def _increase_note_pickup_count(self, note_pickup_count):
        # Instead increase by 1, change to increase multiple
        # func_803463F4 -> D18F5
        self._write_bytes(0x4AB8, 4, 0x0C0D18F5)
        # How much do you wanna increase the note count?
        self._write_bytes(0x4ABC, 2, 0x2405)
        self._write_bytes(0x4ABE, 2, note_pickup_count)
    
    ###############
    ### TESTING ###
    ###############

    # Environmental
    # Decomp: https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/code_16010.c
    def _remove_bubblegloop_swamp_piranha_sound(self):
        self._write_bytes(0x162F8, 4, 0x244EFFF4)

    def _taking_damage_testing(self):
        self._write_bytes(0x160B4, 2, 0xA020D212)

    def _remove_bubblegloop_swamp_environmental_effects(self):
        self._write_bytes(0x16884, 4, 0x244EFFF4)

    def _super_deadly_bubblegloop_swamp_piranha_damage(self):
        self._write_byte(0x16AEB, 0x0C)
        self._write_bytes(0x16AF2, 2, 0x4140)