from Data_Files.Enums import Move_Enums, Area_Enums
from Data_Files.Enums.Warp_Ids import WARP_IDS

AREA_REQUIREMENT_DICT = {
    #######################
    ### Spiral Mountain ###
    #######################
    Area_Enums.SM_MAIN: [
        [WARP_IDS.SM_BANJOS_HOUSE_TO_SM_MAIN],
        [WARP_IDS.GL_MM_ENTRANCE_TO_SM_MAIN],
    ],
    Area_Enums.SM_HOUSE_ROOF: [
        [Area_Enums.SM_MAIN, Move_Enums.FLAP_FLIP],
    ],
    Area_Enums.SM_STUMP_UP_LEFT: [
        [Area_Enums.SM_MAIN, Move_Enums.FLAP_FLIP],
    ],
    Area_Enums.SM_STUMP_UP_MIDDLE: [
        [Area_Enums.SM_MAIN, Move_Enums.FLAP_FLIP],
    ],
    Area_Enums.SM_STUMP_UP_RIGHT: [
        [Area_Enums.SM_MAIN, Move_Enums.FLAP_FLIP],
    ],
    Area_Enums.SM_STUMP_DOWN_LEFT: [
        [Area_Enums.SM_MAIN, Move_Enums.FLAP_FLIP],
    ],
    Area_Enums.SM_STUMP_DOWN_MIDDLE: [
        [Area_Enums.SM_MAIN, Move_Enums.HIGH_JUMP],
        [Area_Enums.SM_MAIN, Move_Enums.FLAP_FLIP],
        [Area_Enums.SM_MAIN, Move_Enums.TALON_TROT],
    ],
    Area_Enums.SM_STUMP_DOWN_RIGHT: [
        [Area_Enums.SM_MAIN, Move_Enums.FLAP_FLIP],
    ],
    Area_Enums.SM_TREE_NEAR_HOUSE: [
        [Area_Enums.SM_MAIN, Move_Enums.CLIMB],
    ],
    Area_Enums.SM_TREE_NEAR_SWIM: [
        [Area_Enums.SM_MAIN, Move_Enums.CLIMB],
    ],
    Area_Enums.SM_TREE_NEAR_CLIMB: [
        [Area_Enums.SM_MAIN, Move_Enums.CLIMB],
    ],
    Area_Enums.SM_TREE_UNDER_BRIDGE: [
        [Area_Enums.SM_MAIN, Move_Enums.CLIMB],
    ],
    Area_Enums.SM_WATERFALL_LEDGE_1: [
        [Area_Enums.SM_MAIN, Move_Enums.HIGH_JUMP],
        [Area_Enums.SM_MAIN, Move_Enums.TALON_TROT],
    ],
    Area_Enums.SM_WATERFALL_LEDGE_2: [
        [Area_Enums.SM_WATERFALL_LEDGE_1, Move_Enums.HIGH_JUMP],
        [Area_Enums.SM_WATERFALL_LEDGE_1, Move_Enums.TALON_TROT],
    ],
    Area_Enums.SM_WATERFALL_LEDGE_3: [
        [Area_Enums.SM_WATERFALL_LEDGE_2, Move_Enums.HIGH_JUMP, Move_Enums.FEATHERY_FLAP],
        [Area_Enums.SM_WATERFALL_LEDGE_2, Move_Enums.TALON_TROT],
    ],
    Area_Enums.SM_WATERFALL_ALCOVE: [
        [Area_Enums.SM_WATERFALL_LEDGE_3, Move_Enums.HIGH_JUMP, Move_Enums.FEATHERY_FLAP],
        [Area_Enums.SM_WATERFALL_LEDGE_3, Move_Enums.TALON_TROT],
    ],
    Area_Enums.SM_WATERFALL_POND: [
        [Area_Enums.SM_MAIN, Move_Enums.DIVE],
    ],
    Area_Enums.SM_SPIRAL_MOAT: [
        [Area_Enums.SM_MAIN, Move_Enums.DIVE],
    ],
    Area_Enums.SM_BH_MAIN: [
        [WARP_IDS.SM_MAIN_TO_SM_BANJOS_HOUSE],
    ]
    #######################
    ### Mumbos Mountain ###
    #######################
    ###########################
    ### Treasure Trove Cove ###
    ###########################
    #######################
    ### Clankers Cavern ###
    #######################
    #########################
    ### Bubblegloop Swamp ###
    #########################
    ######################
    ### Freezeezy Peak ###
    ######################
    ####################
    ### Gobis Valley ###
    ####################
    ###########################
    ### Mad Monster Mansion ###
    ###########################
    ########################
    ### Rusty Bucket Bay ###
    ########################
    ########################
    ### Click Clock Wood ###
    ########################
    #######################
    ### GRUNTILDAS LAIR ###
    #######################
}