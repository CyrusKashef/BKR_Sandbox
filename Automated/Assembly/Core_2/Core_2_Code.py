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

    def _reassign_banjos_house_warp(self, warp_id):
        '''
        Replaces going into Banjo's house warp with a new warp
        '''
        # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/code_956B0.c
        # https://hack64.net/wiki/doku.php?id=banjo_kazooie:enums#map_exit_indices
        self._write_bytes(0x986D6, 2, warp_id)
    
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