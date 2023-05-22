from Data_Files.Enums.Ability_Enums import ABILITY_ENUMS
from Data_Files.Enums.IntEnums.Area_Enums import AREA_ENUMS
from Data_Files.Enums.IntEnums.Warp_Ids import WARP_IDS

WARP = "WARPS"
AREA = "AREAS"
ABILITIES = "ABILITIES"

AREA_REQUIREMENT_DICT = {
    #######################
    ### Spiral Mountain ###
    #######################
    AREA_ENUMS.SM_MAIN: [
        {
            WARP: WARP_IDS.SM_BANJOS_HOUSE_TO_SM_MAIN,
        },
        {
            WARP: WARP_IDS.GL_MM_ENTRANCE_TO_SM_MAIN,
        },
    ],
    AREA_ENUMS.SM_HOUSE_ROOF: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.FLAP_FLIP]
        },
    ],
    AREA_ENUMS.SM_STUMP_UP_LEFT: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.FLAP_FLIP]
        },
    ],
    AREA_ENUMS.SM_STUMP_UP_MIDDLE: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.FLAP_FLIP]
        },
    ],
    AREA_ENUMS.SM_STUMP_UP_RIGHT: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.FLAP_FLIP]
        },
    ],
    AREA_ENUMS.SM_STUMP_DOWN_LEFT: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.FLAP_FLIP]
        },
    ],
    AREA_ENUMS.SM_STUMP_DOWN_MIDDLE: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.FLAP_FLIP]
        },
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.HIGH_JUMP]
        },
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.TALON_TROT]
        },
    ],
    AREA_ENUMS.SM_STUMP_DOWN_RIGHT: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.FLAP_FLIP]
        },
    ],
    AREA_ENUMS.SM_TREE_NEAR_HOUSE: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.CLIMB]
        },
    ],
    AREA_ENUMS.SM_TREE_NEAR_SWIM: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.CLIMB]
        },
    ],
    AREA_ENUMS.SM_TREE_NEAR_CLIMB: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.CLIMB]
        },
    ],
    AREA_ENUMS.SM_TREE_UNDER_BRIDGE: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.CLIMB]
        },
    ],
    AREA_ENUMS.SM_WATERFALL_LEDGE_1: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.HIGH_JUMP]
        },
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.TALON_TROT]
        },
    ],
    AREA_ENUMS.SM_WATERFALL_LEDGE_2: [
        {
            AREA: AREA_ENUMS.SM_WATERFALL_LEDGE_1,
            ABILITIES: [ABILITY_ENUMS.HIGH_JUMP]
        },
        {
            AREA: AREA_ENUMS.SM_WATERFALL_LEDGE_1,
            ABILITIES: [ABILITY_ENUMS.TALON_TROT]
        },
    ],
    AREA_ENUMS.SM_WATERFALL_LEDGE_3: [
        {
            AREA: AREA_ENUMS.SM_WATERFALL_LEDGE_2,
            ABILITIES: [ABILITY_ENUMS.HIGH_JUMP, ABILITY_ENUMS.FEATHERY_FLAP]
        },
        {
            AREA: AREA_ENUMS.SM_WATERFALL_LEDGE_2,
            ABILITIES: [ABILITY_ENUMS.TALON_TROT]
        },
    ],
    AREA_ENUMS.SM_WATERFALL_ALCOVE: [
        {
            AREA: AREA_ENUMS.SM_WATERFALL_LEDGE_3,
            ABILITIES: [ABILITY_ENUMS.HIGH_JUMP, ABILITY_ENUMS.FEATHERY_FLAP]
        },
        {
            AREA: AREA_ENUMS.SM_WATERFALL_LEDGE_3,
            ABILITIES: [ABILITY_ENUMS.TALON_TROT]
        },
    ],
    AREA_ENUMS.SM_WATERFALL_POND: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.DIVE]
        },
    ],
    AREA_ENUMS.SM_SPIRAL_MOAT: [
        {
            AREA: AREA_ENUMS.SM_MAIN,
            ABILITIES: [ABILITY_ENUMS.DIVE]
        },
    ],
    AREA_ENUMS.SM_BH_MAIN: [
        {
            WARP: WARP_IDS.SM_MAIN_TO_SM_BANJOS_HOUSE,
        },
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