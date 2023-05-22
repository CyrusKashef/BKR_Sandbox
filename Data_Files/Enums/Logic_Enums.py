from enum import IntEnum, auto

class LOGIC_ENUMS(IntEnum):
    
    @classmethod
    def get_debug_name(self, note_door):
        return note_door.name

    @classmethod
    def get_int_val_enum(self, note_door):
        return note_door.value
    
    ####################
    ### HEALTH COUNT ###
    ####################

    ONE_HEALTH = 1
    TWO_HEALTH = auto()
    THREE_HEALTH = auto()
    FOUR_HEALTH = auto()
    FIVE_HEALTH = auto()
    SIX_HEALTH = auto()
    SEVEN_HEALTH = auto()
    EIGHT_HEALTH = auto()
    DOUBLE_HEALTH = auto()
    
    #################
    ### ABILITIES ###
    #################

    BEAK_BARGE = auto()
    BEAK_BOMB = auto()
    BEAK_BUSTER = auto()
    CAMERA_CONTROL = auto()
    CLAW_SWIPE = auto()
    CLIMB = auto()
    EGG_FIRING = auto()
    FEATHERY_FLAP = auto()
    FLAP_FLIP = auto()
    FLIGHT = auto()
    HIGH_JUMP = auto()
    RAT_A_TAP_RAP = auto()
    ROLL_ATTACK = auto()
    SHOCK_SPRING_JUMP = auto()
    STILT_STRIDE = auto()
    DIVE = auto()
    TALON_TROT = auto()
    TURBO_TALON_TROT = auto()
    WONDERWING = auto()
    OPEN_NOTE_DOORS = auto()

    #######################
    ### TRANSFORMATIONS ###
    #######################

    TERMITE_BK = auto()
    CROCODILE_BK = auto()
    WALRUS_BK = auto()
    PUMPKIN_BK = auto()
    BEE_BK = auto()

    ##############
    ### JINJOS ###
    ##############
    # MM
    MM_BLUE_JINJO = auto()
    MM_MAGENTA_JINJO = auto()
    MM_YELLOW_JINJO = auto()
    MM_GREEN_JINJO = auto()
    MM_ORANGE_JINJO = auto()
    # TTC
    TTC_BLUE_JINJO = auto()
    TTC_MAGENTA_JINJO = auto()
    TTC_YELLOW_JINJO = auto()
    TTC_GREEN_JINJO = auto()
    TTC_ORANGE_JINJO = auto()
    # CC
    CC_BLUE_JINJO = auto()
    CC_MAGENTA_JINJO = auto()
    CC_YELLOW_JINJO = auto()
    CC_GREEN_JINJO = auto()
    CC_ORANGE_JINJO = auto()
    # BGS
    BGS_BLUE_JINJO = auto()
    BGS_MAGENTA_JINJO = auto()
    BGS_YELLOW_JINJO = auto()
    BGS_GREEN_JINJO = auto()
    BGS_ORANGE_JINJO = auto()
    # FP
    FP_BLUE_JINJO = auto()
    FP_MAGENTA_JINJO = auto()
    FP_YELLOW_JINJO = auto()
    FP_GREEN_JINJO = auto()
    FP_ORANGE_JINJO = auto()
    # GV
    GV_BLUE_JINJO = auto()
    GV_MAGENTA_JINJO = auto()
    GV_YELLOW_JINJO = auto()
    GV_GREEN_JINJO = auto()
    GV_ORANGE_JINJO = auto()
    # MMM
    MMM_BLUE_JINJO = auto()
    MMM_MAGENTA_JINJO = auto()
    MMM_YELLOW_JINJO = auto()
    MMM_GREEN_JINJO = auto()
    MMM_ORANGE_JINJO = auto()
    # RBB
    RBB_BLUE_JINJO = auto()
    RBB_MAGENTA_JINJO = auto()
    RBB_YELLOW_JINJO = auto()
    RBB_GREEN_JINJO = auto()
    RBB_ORANGE_JINJO = auto()
    # CCW
    CCW_BLUE_JINJO = auto()
    CCW_MAGENTA_JINJO = auto()
    CCW_YELLOW_JINJO = auto()
    CCW_GREEN_JINJO = auto()
    CCW_ORANGE_JINJO = auto()

    #######################
    ### SPAWNED JIGGIES ###
    #######################
    # MM
    MM_JINJOS_JIGGY = auto()
    MM_CHIMPY_JIGGY = auto()
    MM_CONGA_JIGGY = auto()
    MM_JUJU_JIGGY = auto()
    MM_ORANGE_PADS_JIGGY = auto()
    MM_HUTS_JIGGY = auto()
    # TTC
    TTC_JINJOS_JIGGY = auto()
    TTC_BLUBBER_JIGGY = auto()
    TTC_LITTLE_LOCKUP_JIGGY = auto()
    # CC
    CC_JINJOS_JIGGY = auto()
    CC_FREE_CLANKER_JIGGY = auto()
    CC_TOOTH_JIGGY = auto()
    CC_RINGS_JIGGY = auto()
    CC_SNIPPETS_JIGGY = auto()
    # BGS
    BGS_JINJOS_JIGGY = auto()
    BGS_CENTRAL_SWITCH_JIGGY = auto()
    BGS_MAZE_SWITCH_JIGGY = auto()
    BGS_YELLOW_FLIBBIT_JIGGY = auto()
    BGS_HUTS_JIGGY = auto()
    BGS_TANKTUP_JIGGY = auto()
    BGS_TIPTUP_JIGGY = auto()
    BGS_MR_VILE_JIGGY = auto()
    BGS_CROCTUS_JIGGY = auto()
    BGS_EGG_JIGGY = auto()
    # FP
    FP_JINJOS_JIGGY = auto()
    FP_SIR_SLUSH_JIGGY = auto()
    FP_WOZZA_JIGGY = auto()
    FP_SNOWMAN_BUTTONS_JIGGY = auto()
    FP_BOGGY_1_JIGGY = auto()
    FP_BOGGY_2_JIGGY = auto()
    FP_BOGGY_3_JIGGY = auto()
    FP_PRESENTS_JIGGY = auto()
    FP_CHRISTMAS_TREE_JIGGY = auto()
    # GV
    GV_JINJOS_JIGGY = auto()
    GV_GRABBA_JIGGY = auto()
    GV_MATCHING_PUZZLE_JIGGY = auto()
    GV_ANCIENT_ONES_JIGGY = auto()
    GV_GOBI_JIGGY = auto()
    GV_TRUNKER_JIGGY = auto()
    GV_GOBI_HONEYCOMB = auto()
    GV_CACTUS_HONEYCOMB = auto()
    # MMM
    MMM_JINJOS_JIGGY = auto()
    MMM_MOTZAND_JIGGY = auto()
    MMM_FLOWER_POTS = auto()
    # RBB
    RBB_JINJOS_JIGGY = auto()
    RBB_WHISTLE_JIGGY = auto()
    # CCW
    CCW_JINJOS_JIGGY = auto()
    CCW_GNAWTY_JIGGY = auto()
    CCW_EYRIE_JIGGY = auto()
    CCW_NABNUT_JIGGY = auto()
    CCW_PLANT_JIGGY = auto()
    # GL
    GL_JINJOS_JIGGY = auto()
    GL_MM_WITCH_SWITCH_JIGGY = auto()
    GL_TTC_WITCH_SWITCH_JIGGY = auto()
    GL_CC_WITCH_SWITCH_JIGGY = auto()
    GL_MMM_WITCH_SWITCH_JIGGY = auto()
    GL_RBB_WITCH_SWITCH_JIGGY = auto()
    GL_CCW_WITCH_SWITCH_JIGGY = auto()

    ################################
    ### SPAWNED EMPTY HONEYCOMBS ###
    ################################

    GV_GOBI_EMPTY_HONEYCOMB = auto()
    GV_CACTUS_EMPTY_HONEYCOMB = auto()
    RBB_BOAT_EMPTY_HONEYCOMB = auto()

    ##################
    ### WORLD KEYS ###
    ##################

    SPIRAL_MOUNTAIN = auto()
    MUMBOS_MOUNTAIN = auto()
    TREASURE_TROVE_COVE = auto()
    CLANKERS_CAVERN = auto()
    BUBBLEGLOOP_SWAMP = auto()
    FREEZEEZY_PEAK = auto()
    GOBIS_VALLEY = auto()
    MAD_MONSTER_MANSION = auto()
    RUSTY_BUCKET_BAY = auto()
    CLICK_CLOCK_WOOD_HUB = auto()
    CLICK_CLOCK_WOOD_SPRING = auto()
    CLICK_CLOCK_WOOD_SUMMER = auto()
    CLICK_CLOCK_WOOD_AUTUMN = auto()
    CLICK_CLOCK_WOOD_WINTER = auto()
    GRUNTILDAS_LAIR = auto()

    #########################
    ### COMPLEX ITEM KEYS ###
    #########################

    JIGGY = auto()
    EMPTY_HONEYCOMB = auto()
    MUMBO_TOKEN = auto()
    JINJOS = auto()
    EXTRA_LIVES = auto()
    ORANGE = auto()
    BLUBBERS_GOLD = auto()
    PRESENTS = auto()
    RED_PRESENT = auto()
    BLUE_PRESENT = auto()
    GREEN_PRESENT = auto()
    CATERPILLAR = auto()
    ACORN = auto()
    HONEYCOMB = auto()

    ########################
    ### SIMPLE ITEM KEYS ###
    ########################

    NOTE = auto()
    BLUE_EGG = auto()
    RED_FEATHER = auto()
    GOLD_FEATHER = auto()
    BLUE_FLOWER = auto()
    ORANGE_YELLOW_FLOWER = auto()
    RED_FLOWER = auto()
    SEASHELL = auto()
    SEAWEED = auto()

    ######################
    ### WITCH SWITCHES ###
    ######################

    MM_WITCH_SWITCH = auto()
    TTC_WITCH_SWITCH = auto()
    CC_WITCH_SWITCH = auto()
    MMM_WITCH_SWITCH = auto()
    RBB_WITCH_SWITCH = auto()
    CCW_WITCH_SWITCH = auto()

    ###################
    ### WATER LEVEL ###
    ###################

    WATER_LEVEL_1 = auto()
    WATER_LEVEL_2 = auto()
    WATER_LEVEL_3 = auto()

    #########################
    ### OTHER PROGRESSION ###
    #########################

    GL_SHED_GATE = auto()