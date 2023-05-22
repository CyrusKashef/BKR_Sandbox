import sys
sys.path.append(".")

from Data_Files.Enums.Transformation_Enums import TRANSFORMATION_ENUMS
from Data_Files.Enums.Jigsaw_Puzzle_Enums import JIGSAW_PUZZLE_ENUMS
from Data_Files.Enums.Note_Door_Enums import NOTE_DOOR_ENUMS

from Data_Files.Logic.Requirements.Area_Requirements import AREA_REQUIREMENT_DICT

WARP = "WARPS"
AREA = "AREAS"
ABILITIES = "ABILITIES"

class LOGIC_CLASS():
    def __init__(self):
        # Default Jigsaw Puzzle Costs
        self._jigsaw_puzzle_cost_dict = {
            0: 1, 1: 2, 2: 5, 3: 6,
            4: 7, 5: 8, 6: 9, 7: 10,
            8: 12, 9: 25, 10: 4,
        }
        # Default Transformation Costs
        self._transformation_cost_dict = {
            TRANSFORMATION_ENUMS.TERMITE_BK: 5,
            TRANSFORMATION_ENUMS.CROCODILE_BK: 10,
            TRANSFORMATION_ENUMS.WALRUS_BK: 15,
            TRANSFORMATION_ENUMS.PUMPKIN_BK: 20,
            TRANSFORMATION_ENUMS.BEE_BK: 25,
        }
        # Default Note Door Costs
        self._note_door_cost_dict = {
            NOTE_DOOR_ENUMS.NOTE_DOOR_ONE: 50, NOTE_DOOR_ENUMS.NOTE_DOOR_TWO: 180,
            NOTE_DOOR_ENUMS.NOTE_DOOR_THREE: 260, NOTE_DOOR_ENUMS.NOTE_DOOR_FOUR: 350,
            NOTE_DOOR_ENUMS.NOTE_DOOR_FIVE: 450, NOTE_DOOR_ENUMS.NOTE_DOOR_SIX: 640,
            NOTE_DOOR_ENUMS.NOTE_DOOR_SEVEN: 765, NOTE_DOOR_ENUMS.NOTE_DOOR_EIGHT: 810,
            NOTE_DOOR_ENUMS.NOTE_DOOR_NINE: 828, NOTE_DOOR_ENUMS.NOTE_DOOR_TEN: 846,
            NOTE_DOOR_ENUMS.NOTE_DOOR_ELEVEN: 864, NOTE_DOOR_ENUMS.NOTE_DOOR_TWELVE: 882,
        }
        # Default Starting Area
        self._unreached_areas = list(AREA_REQUIREMENT_DICT.keys())
        self._reached_areas = []
        # Default Warps
        self._accessible_warps = []
        # Default Health
        self._current_health = 5
        # Default Moves
        self._current_moves = []
        # Default Speed
        self._super_banjo = False
        # Default Win Conditions
        self._note_score_win_count = None
        self._jiggy_score_win_count = None
        # Default Settings
        self._coupled_warps = True

    ##################
    ### WARP LOGIC ###
    ##################

    def _warp_logic(self):
        pass

    ##################
    ### INITIALIZE ###
    ##################

    def _set_jigsaw_puzzle_costs(self, jigsaw_puzzle_cost_dict):
        self._jigsaw_puzzle_cost_dict = {
            0: jigsaw_puzzle_cost_dict[0], # World 1
            1: jigsaw_puzzle_cost_dict[1], # World 2
            2: jigsaw_puzzle_cost_dict[2], # World 3
            3: jigsaw_puzzle_cost_dict[3], # World 4
            4: jigsaw_puzzle_cost_dict[4], # World 5
            5: jigsaw_puzzle_cost_dict[5], # World 6
            6: jigsaw_puzzle_cost_dict[6], # World 7
            7: jigsaw_puzzle_cost_dict[7], # World 8
            8: jigsaw_puzzle_cost_dict[8], # World 9
            9: jigsaw_puzzle_cost_dict[9], # Gruntilda Puzzle
            10: jigsaw_puzzle_cost_dict[10], # Double Health Puzzle
        }

    def _set_transformation_costs(self, transformation_cost_dict):
        self._transformation_cost_dict = {
            TRANSFORMATION_ENUMS.TERMITE_BK: transformation_cost_dict[TRANSFORMATION_ENUMS.TERMITE_BK],
            TRANSFORMATION_ENUMS.CROCODILE_BK: transformation_cost_dict[TRANSFORMATION_ENUMS.CROCODILE_BK],
            TRANSFORMATION_ENUMS.WALRUS_BK: transformation_cost_dict[TRANSFORMATION_ENUMS.WALRUS_BK],
            TRANSFORMATION_ENUMS.PUMPKIN_BK: transformation_cost_dict[TRANSFORMATION_ENUMS.PUMPKIN_BK],
            TRANSFORMATION_ENUMS.BEE_BK: transformation_cost_dict[TRANSFORMATION_ENUMS.BEE_BK],
        }
    
    def _set_note_door_costs(self, note_door_cost_dict):
        self._note_door_cost_dict = {
            0: note_door_cost_dict[0], # 50
            1: note_door_cost_dict[1], # 180
            2: note_door_cost_dict[2], # 260
            3: note_door_cost_dict[3], # 350
            4: note_door_cost_dict[4], # 450
            5: note_door_cost_dict[5], # 640
            6: note_door_cost_dict[6], # 765
            7: note_door_cost_dict[7], # 810
            8: note_door_cost_dict[8], # 828
            9: note_door_cost_dict[9], # 846
            10: note_door_cost_dict[10], # 864
            11: note_door_cost_dict[11], # 882
        }

    def _set_starting_location(self, area_enum):
        self._reached_areas = [area_enum]
        self._unreached_areas.remove(area_enum)

    def _set_starting_health(self, starting_health=5):
        self._current_health = starting_health

    def _set_starting_moves(self, starting_moves=[]):
        self._current_moves = starting_moves
    
    def _set_super_banjo(self, super_banjo_bool=False):
        self._super_banjo = super_banjo_bool
    
    def _set_coupled_warps_setting(self, coupled_warps_setting=True):
        self._coupled_warps = coupled_warps_setting

    #######################
    ### REACHABLE AREAS ###
    #######################

    def _check_reachable_locations(self):
        added_location = True
        while(added_location):
            now_reachable_area_list = []
            for unreached_area_enum in self._unreached_areas:
                if(self._is_area_reachable(unreached_area_enum)):
                    now_reachable_area_list.append(unreached_area_enum)
            if(not now_reachable_area_list):
                added_location = False
                continue
            for now_reachable_area in now_reachable_area_list:
                self._reached_areas.append(now_reachable_area)
                self._unreached_areas.remove(now_reachable_area)

    def _is_area_reachable(self, unreached_area_enum):
        for requirement_list_index in range(len(AREA_REQUIREMENT_DICT[unreached_area_enum])):
            if(WARP in AREA_REQUIREMENT_DICT[unreached_area_enum][requirement_list_index]):
                if(AREA_REQUIREMENT_DICT[unreached_area_enum][requirement_list_index][WARP] not in self._accessible_warps):
                    continue
            if(AREA in AREA_REQUIREMENT_DICT[unreached_area_enum][requirement_list_index]):
                if(AREA_REQUIREMENT_DICT[unreached_area_enum][requirement_list_index][AREA] not in self._reached_areas):
                    continue
            if(ABILITIES in AREA_REQUIREMENT_DICT[unreached_area_enum][requirement_list_index]):
                for ability in AREA_REQUIREMENT_DICT[unreached_area_enum][requirement_list_index][ABILITIES]:
                    if(ability not in self._current_moves):
                        continue
            return True
        return False

    ########################
    ### OBTAINABLE ITEMS ###
    ########################

    def _obtain_area_items(self):
        pass

    def _can_player_transform(self):
        pass

    def _can_player_obtain_jiggy(self):
        pass

    def _can_player_obtain_note(self):
        pass

    def _can_player_obtain_move(self):
        pass

    def _add_token_to_current_reachable_area(self):
        pass

    def _add_jiggy_to_current_reachable_area(self):
        pass

    def _add_note_to_current_reachable_area(self):
        pass

    def _add_move_to_current_reachable_area(self):
        pass

    def _add_empty_honeycomb_to_current_reachable_area(self):
        pass

    def _add_jinjo_to_current_reachable_area(self):
        pass

    def _add_misc_items_to_current_reachable_area(self):
        pass

    def _add_extra_lives_to_current_reachable_area(self):
        pass

    def _add_eggs_feathers_to_current_reachable_area(self):
        pass

    ###############################
    ### FEATURE DEPENDENT LOGIC ###
    ###############################

    def _adjust_sandcastle_move_cheats(self):
        pass

# if __name__ == '__main__':
#     logic_obj = LOGIC_CLASS()
#     starting_location = AREA_ENUMS.SM_MAIN
#     logic_obj._set_starting_location(starting_location)
#     starting_moves_list = [ABILITY_ENUMS.HIGH_JUMP, ABILITY_ENUMS.FEATHERY_FLAP, ABILITY_ENUMS.FLAP_FLIP,
#                            ABILITY_ENUMS.CLAW_SWIPE, ABILITY_ENUMS.ROLL_ATTACK, ABILITY_ENUMS.RAT_A_TAP_RAP,
#                            ABILITY_ENUMS.DIVE, ABILITY_ENUMS.CLIMB, ABILITY_ENUMS.BEAK_BARGE,
#                            ABILITY_ENUMS.CAMERA_CONTROL]
#     logic_obj._set_starting_moves(starting_moves_list)
#     print("Before:")
#     print(logic_obj._reached_areas)
#     logic_obj._check_reachable_locations()
#     print("After:")
#     print(logic_obj._reached_areas)