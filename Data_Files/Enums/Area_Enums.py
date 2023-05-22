import sys
sys.path.append(".")

from enum import IntEnum, auto
from Data_Files.Enums.Map_Enums import MAP_ENUMS

class AREA_ENUMS(IntEnum):

    #######################
    ### SPIRAL MOUNTAIN ###
    #######################

    ### SM MAIN 0x01
    
    SM_MAIN = MAP_ENUMS.SM_MAIN * 0x100 + 0x01
    SM_HOUSE_ROOF = auto()
    SM_STUMP_UP_LEFT = auto()
    SM_STUMP_UP_MIDDLE = auto()
    SM_STUMP_UP_RIGHT = auto()
    SM_STUMP_DOWN_LEFT = auto()
    SM_STUMP_DOWN_MIDDLE = auto()
    SM_STUMP_DOWN_RIGHT = auto()
    SM_TREE_NEAR_HOUSE = auto()
    SM_TREE_NEAR_SWIM = auto()
    SM_TREE_NEAR_CLIMB = auto()
    SM_TREE_UNDER_BRIDGE = auto()
    SM_WATERFALL_LEDGE_1 = auto()
    SM_WATERFALL_LEDGE_2 = auto()
    SM_WATERFALL_LEDGE_3 = auto()
    SM_WATERFALL_ALCOVE = auto()
    SM_WATERFALL_POND = auto()
    SM_SPIRAL_MOAT = auto()

    ### SM BANJOS HOUSE 0x8C

    SM_BH_MAIN = MAP_ENUMS.SM_BANJOS_HOUSE * 0x100 + 0x01

    #######################
    ### MUMBOS MOUNTAIN ###
    #######################

    ### MM MAIN 0x02

    MM_MAIN = MAP_ENUMS.MM_MAIN * 0x100 + 0x01
    MM_PINK_JINJO = auto()
    MM_TREE_NEAR_PINK_JINJO = auto()
    MM_TREE_NEAR_BLUE_JINJO = auto()
    MM_BEEHIVE_HEXAGON = auto()
    MM_STONEHENGE_JIGGY = auto()
    MM_ATOP_STONEHENGE = auto()
    MM_CHIMPY_STUMP = auto()
    MM_EGG_FIRING = auto()
    MM_STUMP_TO_WITCH_SWITCH_1 = auto()
    MM_STUMP_TO_WITCH_SWITCH_2 = auto()
    MM_STUMP_TO_WITCH_SWITCH_3 = auto()
    MM_STUMP_WITH_WITCH_SWITCH = auto()
    MM_EMPTY_HONEYCOMB_ALCOVE = auto()
    MM_ATOP_HUTS = auto()
    MM_JUJU_PLATFORM = auto()
    MM_MUMBOS_SKULL_EYE = auto()
    MM_ATOP_MUMBOS_SKULL = auto()
    MM_ATOP_TICKERS_TOWER = auto()
    MM_BLUE_JINJO = auto()
    MM_UNDERWATER = auto()

    ### MM TICKERS TOWER 0x0C

    MM_TT_FLOOR_1 = MAP_ENUMS.MM_TICKERS * 0x100 + 0x01
    MM_TT_SLOPE_LEDGE_1 = auto()
    MM_TT_UPPER_FLOORS = auto()

    ### MM INSIDE MUMBOS SKULL 0x0E

    MM_MS_MAIN = MAP_ENUMS.MM_MUMBOS_SKULL * 0x100 + 0x01
    MM_MS_SHELF = auto()

    ###########################
    ### TREASURE TROVE COVE ###
    ###########################

    # TTC MAIN 0x07

    TTC_MAIN = MAP_ENUMS.TTC_MAIN * 0x100 + 0x01
    TTC_UNDERWATER = auto()
    TTC_TREE_NEAR_ENTRANCE_LEFT = auto()
    TTC_TREE_NEAR_ENTRANCE_RIGHT = auto()
    TTC_SANDCASTLE_WATER_AREA = auto()
    TTC_TREE_NEAR_SANDCASTLE_1 = auto()
    TTC_TREE_NEAR_SANDCASTLE_2 = auto()
    TTC_TREE_NEAR_SANDCASTLE_3 = auto()
    TTC_TREE_NEAR_SANDCASTLE_4 = auto()
    TTC_TREE_NEAR_SANDCASTLE_5 = auto()
    TTC_TREE_NEAR_SANDCASTLE_6 = auto()
    TTC_SHOCK_JUMP_PAD_PLATFORM_1 = auto()
    TTC_SHOCK_JUMP_PAD_PLATFORM_2 = auto()
    TTC_SHOCK_JUMP_PAD_PLATFORM_3 = auto()
    TTC_SHOCK_JUMP_PAD_PLATFORM_4 = auto()
    TTC_SHOCK_JUMP_PAD_PLATFORM_5 = auto()
    TTC_SHOCK_JUMP_PAD_PLATFORM_6 = auto()
    TTC_SHOCK_JUMP_LEDGE_1 = auto()
    TTC_SHOCK_JUMP_LEDGE_2 = auto()
    TTC_SHOCK_JUMP_JIGGY_LEDGE = auto()
    TTC_TREE_NEAR_LOCKUPS_1 = auto()
    TTC_TREE_NEAR_LOCKUPS_2 = auto()
    TTC_TREE_NEAR_LOCKUPS_3 = auto()
    TTC_QUESTION_MARK_AREA = auto()
    TTC_PLATFORM_TO_FIRST_X_1 = auto()
    TTC_PLATFORM_TO_FIRST_X_2 = auto()
    TTC_FIRST_X_PLATFORM = auto()
    TTC_POOL_WITH_JIGGY = auto()
    TTC_POOL_WITH_TOKEN = auto()
    TTC_EXTRA_LIFE_POOL = auto()
    TTC_BLUBBERS_SHIP_DECK = auto()
    TTC_BLUBBERS_SHIP_CROWS_NEST = auto()
    TTC_LOCKUP_JIGGY_ALCOVE = auto()
    TTC_STAIRS_ALCOVE = auto()
    TTC_ATOP_MOUNTAIN_MAIN = auto()
    TTC_ATOP_MOUNTAIN_TREE_1 = auto()
    TTC_ATOP_MOUNTAIN_TREE_2 = auto()
    TTC_ATOP_MOUNTAIN_TREE_3 = auto()
    TTC_ATOP_MOUNTAIN_TREE_4 = auto()
    TTC_YELLOW_JINJO_TREE = auto()
    TTC_ATOP_MOUNTAIN_LEDGE_1 = auto()
    TTC_ATOP_MOUNTAIN_LEDGE_2 = auto()
    TTC_ATOP_MOUNTAIN_LEDGE_3 = auto()
    TTC_ATOP_MOUNTAIN_LEDGE_4 = auto()
    TTC_ATOP_MOUNTAIN_LEDGE_5 = auto()
    TTC_ATOP_MOUNTAIN_LEDGE_6 = auto()
    TTC_ATOP_MOUNTAIN_SHOCK_JUMP_LEDGE = auto()
    TTC_ATOP_MOUNTAIN_FROM_SHOCK_JUMP_LEDGE = auto()
    TTC_ATOP_MOUNTAIN_LIGHTHOUSE_BASE = auto()
    TTC_LIGHTHOUSE_UPPER = auto()
    TTC_ATOP_LIGHTHOUSE = auto()

    ### BLUBBERS SHIP 0x05

    TTC_BS_SIDE_UNDERWATER = MAP_ENUMS.TTC_SALTY_HIPPO * 0x100 + 0x01
    TTC_BS_SIDE_ABOVE_WATER = auto()
    TTC_BS_TOP_UNDERWATER = auto()
    TTC_BS_TOP_ABOVE_WATER = auto()

    ### NIPPERS 0x06

    TTC_INSIDE_NIPPERS_SHELL = MAP_ENUMS.TTC_NIPPER * 0x100 + 0x01

    ### SANDCASTLE

    TTC_INSIDE_SANDCASTLE = MAP_ENUMS.TTC_SANDCASTLE + 0x100 + 0x01

    ### SHARKFOOD ISLAND

    TTC_SI_MAIN = MAP_ENUMS.TTC_SHARKFOOD_ISLAND * 0x100 + 0x01
    TTC_SI_ALCOVE_1 = auto()
    TTC_SI_ALCOVE_2 = auto()
    TTC_SI_ALCOVE_3 = auto()
    TTC_SI_ALCOVE_4 = auto()
    TTC_SI_ALCOVE_5 = auto()
    TTC_SI_ALCOVE_6 = auto()
    TTC_SI_ALCOVE_7 = auto()
    TTC_SI_ALCOVE_8 = auto()
    TTC_SI_ALCOVE_9 = auto()
    TTC_SI_ALCOVE_10 = auto()
    TTC_SI_ALCOVE_11 = auto()
    TTC_SI_ALCOVE_12 = auto()
    TTC_SI_ALCOVE_13 = auto()
    TTC_SI_ALCOVE_14 = auto()
    TTC_SI_ALCOVE_15 = auto()
    TTC_SI_ALCOVE_16 = auto()
    TTC_SI_LEDGE = auto()
    TTC_SI_TOP = auto()

    #######################
    ### CLANKERS CAVERN ###
    #######################

    ### CLANKERS CAVERN MAIN

    CC_ENTRANCE_INSIDE_PIPE = MAP_ENUMS.CC_MAIN * 0x100 + 0x01
    CC_ENTRANCE_ATOP_PIPE = auto()
    CC_ENTRANCE_LEFT_GOLD_FEATHER_PIPE = auto()
    CC_ENTRANCE_RIGHT_GOLD_FEATHER_PIPE = auto()
    CC_ENTRANCE_LEFT_CHOMPA_PIPE = auto()
    CC_ENTRANCE_RIGHT_CHOMPA_PIPE_1 = auto()
    CC_ENTRANCE_RIGHT_CHOMPA_PIPE_2 = auto()
    CC_ENTRANCE_LADDER_PLATFORM = auto()
    CC_YELLOW_JINJO = auto()
    CC_ENTRANCE_UNREACHABLE_PIPE = auto()
    CC_WATER_BELOW_ENTRANCE = auto()
    CC_WATER_MAIN = auto()
    CC_MUTIE_SNIPPETS = auto()
    CC_GOLD_FEATHER_PLATFORM = auto()
    CC_BEEHIVE_PLATFORM = auto()
    CC_ALTERNATING_COLLECTABLES_ALCOVE_1 = auto()
    CC_ALTERNATING_COLLECTABLES_ALCOVE_2 = auto()
    CC_ALTERNATING_COLLECTABLES_ALCOVE_3 = auto()
    CC_ALTERNATING_COLLECTABLES_ALCOVE_REST = auto()
    CC_BLUE_EGGS_PLATFORM = auto()
    CC_EXTRA_LIFE_PLATFORM = auto()
    CC_HONEYCOMB_PIPE = auto()
    CC_CLIMBABLE_PIPE_WITH_NOTES = auto()
    CC_CLIMBABLE_PIPE_ALCOVE_1 = auto()
    CC_CLIMBABLE_PIPE_ALCOVE_2 = auto()
    CC_CLIMBABLE_PIPE_WITHOUT_NOTES = auto()
    CC_ATOP_SLIDING_PIPE = auto()
    CC_INSIDE_SLIDING_PIPE = auto()
    CC_ATOP_HONEYCOMB_GRATE = auto()
    CC_INSIDE_HONEYCOMB_GRATE = auto()
    CC_UNDER_HONEYCOMB_GRATE_PLATFORM = auto()
    CC_LEFT_TOOTH_PLATFORM = auto()
    CC_RIGHT_TOOTH_PLATFORM = auto()
    CC_CLANKERS_LEFT_FIN = auto()
    CC_CLANKERS_RIGHT_FIN = auto()
    CC_ATOP_CLANKER = auto()
    CC_ABOVE_CLANKERS_HEAD_WALKWAY = auto()
    CC_ABOVE_CLANKERS_HEAD_GRATE = auto()
    CC_BEHIND_CLANKERS_TAIL_PLATFORM = auto()
    CC_BEHIND_CLANKERS_TAIL_GRATE = auto()
    CC_BEHIND_CLANKERS_TAIL_BETWEEN_GRATE_AND_PLATFORM = auto()
    CC_BEHIND_CLANKERS_TAIL_LONG_PIPE = auto()

    ### BLOWHOLE
    CC_BLOWHOLE_MAIN = MAP_ENUMS.CC_CLANKER_BLOWHOLE * 0x100 + 0x01

    ### MOUTH/BELLY
    CC_MOUTH_MAIN = MAP_ENUMS.CC_CLANKER_MOUTH_BELLY * 0x100 + 0x01
    CC_MOUTH_LEFT_TOOTH = auto()
    CC_MOUTH_RIGHT_TOOTH = auto()
    CC_MOUTH_BELLY_UNDERWATER = auto()
    CC_BELLY_MAIN = auto()
    CC_BELLY_FLIGHT_PAD = auto()
    CC_BELLY_JIGGY_SPAWN = auto()
    CC_BELLY_WONDERWING_ENTRANCE = auto()
    CC_LEFT_GILL_UNDERWATER = auto()
    CC_LEFT_GILL_ABOVE_WATER = auto()

    ### WONDERWING
    CC_WONDERWING_MAIN = MAP_ENUMS.CC_CLANKER_WONDERWING * 0x100 + 0x01

    #########################
    ### BUBBLEGLOOP SWAMP ###
    #########################

    ### MAIN
    ### VILE
    ### TANKTUP

    ######################
    ### FREEZEEZY PEAK ###
    ######################

    ### MAIN
    ### IGLOO
    ### MUMBOS
    ### TREE
    ### WOZZAS

    ####################
    ### GOBIS VALLEY ###
    ####################

    ### MAIN
    ### MATCHING PYRAMID
    ### WATER PYRAMID
    ### RUBEE
    ### JINXY
    ### SNS ROOM

    ###########################
    ### MAD MONSTER MANSION ###
    ###########################

    ### MAIN
    ### CHURCH
    ### CELLAR
    ### TUMBLAR
    ### WELL
    ### NAPPER
    ### EGG ROOM
    ### NOTE ROOM
    ### RED FEATHER ROOM
    ### SECRET ROOM
    ### LOGGO ROOM
    ### BEDROOM
    ### HONEYCOMB ROOM
    ### GUTTER
    ### MUMBOS
    ### INSIDE LOGGO

    ########################
    ### RUSTY BUCKET BAY ###
    ########################

    ### MAIN
    ### ENGINE ROOM
    ### BIG FISH WAREHOUSE
    ### BOAT ROOM
    ### CHOMPA CONTAINER
    ### MINI KABOOM CONTAINER
    ### CABIN WINDOW
    ### BOSS KABOOM BOSS
    ### MINI KABOOM PIPE
    ### KITCHEN PIPE
    ### CONTROL ROOM WINDOW
    ### SEAMAN GRUBLIN CONTAINER
    ### CAPTAINS ROOM WINDOW
    ### RBB ANCHOR

    ########################
    ### CLICK CLOCK WOOD ###
    ########################
    
    ### CCW MAIN

    ### CCW SPRING MAIN
    ### CCW SPRING MUMBOS
    ### CCW SPRING ZUBBAS
    ### CCW SPRING NABNUT
    ### CCW SPRING WHIPCRACKS

    ### CCW SUMMER MAIN
    ### CCW SUMMER MUMBOS
    ### CCW SUMMER ZUBBAS
    ### CCW SUMMER NABNUT
    ### CCW SUMMER WHIPCRACKS

    ### CCW AUTUMN MAIN
    ### CCW AUTUMN MUMBOS
    ### CCW AUTUMN ZUBBAS
    ### CCW AUTUMN NABNUT
    ### CCW AUTUMN WHIPCRACKS
    ### CCW AUTUMN FLOODED ATTIC

    ### CCW WINTER MAIN
    ### CCW WINTER MUMBOS
    ### CCW WINTER NABNUT
    ### CCW WINTER WHIPCRACKS
    ### CCW WINTER FLOODED ATTIC
    ### CCW WINTER ACORN STORAGE

    #######################
    ### GRUNTILDAS LAIR ###
    #######################

    ### MM ENTRANCE
    ### TTC CC PUZZLES
    ### CCW PUZZLE
    ### PIPE ROOM
    ### TTC ENTRANCE
    ### GV ENTRANCE
    ### FP ENTRANCE
    ### CC ENTRANCE
    ### GRUNTY STATUE
    ### BGS ENTRANCE
    ### GV PUZZLE
    ### MMM ENTRANCE
    ### WATER THREE SWITCH
    ### RBB ENTRANCE
    ### MMM RBB PUZZLE
    ### CCW ENTRANCE
    ### CRYPT
    ### PATH TO FF
    ### FF
    ### DOOR OF GRUNTY