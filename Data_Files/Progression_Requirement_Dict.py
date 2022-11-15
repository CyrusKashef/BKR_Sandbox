from BK_Enums import *
from Rooms import *

############################
### SPAWNED REQUIREMENTS ###
############################
# LEGEND:
# () = At least one of these
# [] = Must have all of these
# {} = Count of item

CASUAL_SPAWNED_REQUIREMENTS_DICT = {
    # MM
    MM_JINJOS_JIGGY: [MM_BLUE_JINJO, MM_PINK_JINJO, MM_YELLOW_JINJO, MM_GREEN_JINJO, MM_ORANGE_JINJO],
    MM_CHIMPY_JIGGY: [MM_MAIN, MM_ORANGE_JINJO],
    MM_CONGA_JIGGY: [MM_MAIN, EGG_FIRING],
    MM_JUJU_JIGGY: [MM_MAIN, EGG_FIRING],
    MM_ORANGE_PADS_JIGGY: [MM_MAIN],
    MM_HUTS_JIGGY: [MM_MAIN, BEAK_BUSTER],
    # TTC
    TTC_JINJOS_JIGGY: [TTC_BLUE_JINJO, TTC_PINK_JINJO, TTC_YELLOW_JINJO, TTC_GREEN_JINJO, TTC_ORANGE_JINJO],
    TTC_BLUBBER_JIGGY: {BLUBBERS_GOLD: 2}, # DEPENDS
    TTC_LITTLE_LOCKUP_JIGGY: [TTC_MAIN, BEAK_BUSTER],
    # CC
    CC_JINJOS_JIGGY: [CC_BLUE_JINJO, CC_PINK_JINJO, CC_YELLOW_JINJO, CC_GREEN_JINJO, CC_ORANGE_JINJO],
    CC_FREE_CLANKER_JIGGY: [CC_MAIN, DIVE],
    CC_TOOTH_JIGGY: [CC_MAIN, CC_BELLY_MOUTH, EGG_FIRING],
    CC_RINGS_JIGGY: [CC_BELLY_MOUTH, DIVE],
    CC_SNIPPETS_JIGGY: [CC_MAIN, DIVE, (CLAW_SWIPE, ROLL_ATTACK, RAT_A_TAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING)],
    # BGS
    BGS_JINJOS_JIGGY: [BGS_BLUE_JINJO, BGS_PINK_JINJO, BGS_YELLOW_JINJO, BGS_GREEN_JINJO, BGS_ORANGE_JINJO],
    BGS_CENTRAL_SWITCH_JIGGY: [BGS_MAIN, BEAK_BUSTER, TALON_TROT],
    BGS_MAZE_SWITCH_JIGGY: [BGS_MAIN, BEAK_BUSTER, (STILT_STRIDE, EIGHT_HEALTH, [WONDERWING, EIGHT_HEALTH])], # CHECK THIS
    BGS_YELLOW_FLIBBIT_JIGGY: [BGS_MAIN, (CLAW_SWIPE, ROLL_ATTACK, RAT_A_TAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING)],
    BGS_HUTS_JIGGY: [BGS_MAIN, BEAK_BUSTER, HIGH_JUMP, SHOCK_SPRING_JUMP],
    BGS_TANKTUP_JIGGY: [BGS_MAIN, BEAK_BUSTER],
    BGS_TIPTUP_JIGGY: [BGS_TANKTUP, BEAK_BUSTER],
    BGS_MR_VILE_JIGGY: [BGS_MR_VILE, CROCODILE_BK],
    BGS_CROCTUS_JIGGY: [BGS_MAIN, EGG_FIRING, BEAK_BUSTER, HIGH_JUMP, SHOCK_SPRING_JUMP],
    BGS_EGG_JIGGY: [BEAK_BUSTER, RAT_A_TAP_RAP, BEAK_BARGE, ([HIGH_JUMP, SHOCK_SPRING_JUMP], [CLIMB, TALON_TROT])],
    # FP
    FP_JINJOS_JIGGY: [FP_BLUE_JINJO, FP_PINK_JINJO, FP_YELLOW_JINJO, FP_GREEN_JINJO, FP_ORANGE_JINJO],
    FP_SIR_SLUSH_JIGGY: [FP_MAIN, FLIGHT, BEAK_BOMB],
    FP_WOZZA_JIGGY: [FP_MAIN, WALRUS_BK],
    FP_SNOWMAN_BUTTONS_JIGGY: [FP_MAIN, FLIGHT, BEAK_BOMB],
    FP_BOGGY_1_JIGGY: [FP_MAIN, (FLIGHT, TALON_TROT)],
    FP_BOGGY_2_JIGGY: [FP_MAIN, FP_BOGGY_1_JIGGY, WALRUS_BK],
    FP_BOGGY_3_JIGGY: [FP_MAIN, FP_BOGGY_2_JIGGY, TURBO_TALON_TROT],
    FP_PRESENTS_JIGGY: [FP_IGLOO, RED_PRESENT, BLUE_PRESENT, GREEN_PRESENT],
    FP_CHRISTMAS_TREE_JIGGY: [FP_MAIN, BEAK_BUSTER, EGG_FIRING, FLIGHT],
    # GV
    GV_JINJOS_JIGGY: [GV_BLUE_JINJO, GV_PINK_JINJO, GV_YELLOW_JINJO, GV_GREEN_JINJO, GV_ORANGE_JINJO],
    GV_GRABBA_JIGGY: [GV_MAIN, (TURBO_TALON_TROT, [TALON_TROT, FLIGHT, BEAK_BOMB])],
    GV_MATCHING_PUZZLE_JIGGY: [GV_MATCHING_PUZZLE, BEAK_BUSTER],
    GV_ANCIENT_ONES_JIGGY: [GV_MAIN, (TALON_TROT, TURBO_TALON_TROT), FLIGHT],
    GV_GOBI_JIGGY: [GV_MAIN, (TALON_TROT, TURBO_TALON_TROT), (BEAK_BARGE, BEAK_BUSTER, BEAK_BOMB, EGG_FIRING, WONDERWING)],
    GV_TRUNKER_JIGGY: [GV_GOBI_JIGGY, BEAK_BUSTER],
    GV_GOBI_HONEYCOMB: [GV_TRUNKER_JIGGY, BEAK_BUSTER],
    GV_CACTUS_HONEYCOMB: [GV_MAIN, (TALON_TROT, TURBO_TALON_TROT), BEAK_BUSTER, FLIGHT],
    # MMM
    MMM_JINJOS_JIGGY: [MMM_BLUE_JINJO, MMM_PINK_JINJO, MMM_YELLOW_JINJO, MMM_GREEN_JINJO, MMM_ORANGE_JINJO],
    MMM_MOTZAND_JIGGY: [MMM_CHURCH, FLAP_FLIP, HIGH_JUMP, SHOCK_SPRING_JUMP, BEAK_BUSTER],
    MMM_FLOWER_POTS: [MMM_MAIN, EGG_FIRING], # DEPENDS
    # RBB
    RBB_JINJOS_JIGGY: [RBB_BLUE_JINJO, RBB_PINK_JINJO, RBB_YELLOW_JINJO, RBB_GREEN_JINJO, RBB_ORANGE_JINJO],
    RBB_WHISTLE_JIGGY: [RBB_MAIN, BEAK_BUSTER],
    # CCW
    CCW_JINJOS_JIGGY: [CCW_BLUE_JINJO, CCW_PINK_JINJO, CCW_YELLOW_JINJO, CCW_GREEN_JINJO, CCW_ORANGE_JINJO],
    CCW_GNAWTY_JIGGY: [CCW_SUMMER_MAIN, (CCW_AUTUMN_MAIN, CCW_WINTER_MAIN), DIVE, (EGG_FIRING, BEAK_BARGE, BEAK_BUSTER, WONDERWING)],
    CCW_EYRIE_JIGGY: [CCW_SPRING_MAIN, CCW_SUMMER_MAIN, CCW_AUTUMN_MAIN, CCW_WINTER_MAIN, HIGH_JUMP, SHOCK_SPRING_JUMP, BEAK_BUSTER, {CATERPILLAR: 15}],
    CCW_NABNUT_JIGGY: [CCW_AUTUMN_MAIN, {ACORN: 15}], # DEPENDS
    CCW_PLANT_JIGGY: [CCW_SPRING_MAIN, CCW_SUMMER_MAIN, CCW_AUTUMN_MAIN, EGG_FIRING, BEAK_BUSTER],
    # GL
    GL_JINJOS_JIGGY: [GL_BLUE_JINJO, GL_PINK_JINJO, GL_YELLOW_JINJO, GL_GREEN_JINJO, GL_ORANGE_JINJO],
    GL_MM_WITCH_SWITCH_JIGGY: [MM_WITCH_SWITCH, GL_MM_ENTRANCE, TERMITE_BK],
    GL_TTC_WITCH_SWITCH_JIGGY: [TTC_WITCH_SWITCH, GL_TTC_ENTRANCE, FLAP_FLIP],
    GL_CC_WITCH_SWITCH_JIGGY: [CC_WITCH_SWITCH, BEAK_BUSTER],
    GL_MMM_WITCH_SWITCH_JIGGY: [MMM_WITCH_SWITCH, GL_FP_ENTRANCE, (RAT_A_TAP_RAP, [FLIGHT, BEAK_BOMB], EGG_FIRING, WONDERWING)],
    GL_RBB_WITCH_SWITCH_JIGGY: [RBB_WITCH_SWITCH, GL_640_NOTE_DOOR, WATER_LEVEL_2],
    GL_CCW_WITCH_SWITCH_JIGGY: [CCW_WITCH_SWITCH, GL_CCW_ENTRANCE, BEE_BK],
    # OTHER STATIC PROGRESSION
    GL_SHED_GATE: [GL_MMM_ENTRANCE, (RAT_A_TAP_RAP, EGG_FIRING, BEAK_BARGE, WONDERWING)],
    WATER_LEVEL_1: [GL_SHED_GATE, PUMPKIN_BK, BEAK_BUSTER],
    WATER_LEVEL_2: [GL_RBB_ENTRANCE, WATER_LEVEL_1, BEAK_BUSTER, ([TALON_TROT], [HIGH_JUMP, FEATHERY_FLAP])], # CHECK THIS
}

#############################
### LOCATION REQUIREMENTS ###
#############################

CASUAL_LOCATION_REQUIREMENTS_DICT = {
    # SM
    SM_MAIN: {
        (-7108, 1200, -3079): [], # Waterfall Extra Life
        (3656, 339, 6552): [], # House Extra Life
        (3271, -110, -2673): [], # Bottles Beak Barge
        (4675, 400, 511): [], # Bottles Attacks
        (-1999, 342, -2545): [], # Bottles Climb
        (-164, -190, 3313): [], # Bottles Jumps
        (3802, -500, 5259): [], # Bottles Start
        (-2336, 302, 973): [], # Bottles Dive
        (0, 1800, 0): [], # Bottles Top
        (-6725, 1300, -1803): [], # Waterfall Honeycomb
        (-2752, 1299, 37): [], # Tree Honeycomb
        (-1400, 99, 4824): [], # Stump Honeycomb
        (-264, -442, -651): [], # Underwater Honeycomb
        (3594, -105, -3473): [], # Quarrie
        (2559, -105, -3414): [], # Quarrie
        (3948, -108, -1785): [], # Quarrie
        (4223, -105, -2699): [], # Quarrie
    },
    SM_BANJOS_HOUSE: {},
    # MM
    MM_MAIN: {
        (223, 3563, -382): [], # Extra Life
        (1702, -125, 2941): [], # Blue Jinjo
        (3943, 2155, -3422): [], # Bottles Beak Buster
        (-5926, 200, 6213): [], # Bottles Egg Firing
        (-2550, 2255, -1217): [], # Bottles Talon Trot
        (985, 484, 1681): [], # Alcove Honeycomb
        (4302, 2900, -1490): [], # Juju Honeycomb
        (373, 4221, -906): [], # Tickers Tower Jiggy
        (4335, 1485, 794): [], # Slope Jiggy
        (5580, 2756, -2708): [], # Mumbo's Eye Jiggy
        (-3699, 2438, -2113): [], # Stonehenge Jiggy
        (-4431, 475, 6183): [], # Conga Token
        (-4869, 225, -2506): [], # Stonehenge Token
        (5150, 2168, -2447): [], # Mumbo Bridge Token
        (5855, 0, 2169): [], # Level Start Token
        (-4126, 145, 4566): [], # Orange
        (-3297, 2755, -1421): [], # Orange Jinjo
        (5876, 299, 2369): [], # Pink Jinjo
        (-3465, 650, 5629): [], # Witch Switch
        (-4060, 1355, 1092): [], # Yellow Jinjo
    },
    MM_TICKERS_TOWER: {
        (-343, 345, -518): [], # Tickers Tower Token
    },
    MM_MUMBOS_SKULL: {},
    # TTC
    TTC_MAIN: {
        (-2442, 3158, -1706): [], # Ledge Extra Life
        (4710, 323, -6007): [], # Underwater Extra Life
        (5864, 677, 7898): [], # Sharkfood Island Life
        (-875, 242, 7206): [], # Blue Jinjo
        (-288, 2161, 1314): [], # Bottles Fly
        (2698, 1517, 3338): [], # Bottles Shock Jump
        (8473, 844, -2684): [], # Crate Honeycomb
        (-4303, 46, 115): [], # Underwater Honeycomb
        (-179, 3062, 889): [], # Green Jinjo
        (2832, 2152, -1797): [], # Shock Spring Jiggy
        (479, 8500, -2709): [], # Lighthouse Jiggy
        (-5116, 1417, -3915): [], # Brick Alcove Jiggy
        (-1575, 2597, -2500): [], # Arch Alcove Jiggy
        (-2760, 2053, -4733): [], # Pool Jiggy
        (-2660, 2447, -6079): [], # Lockup Token 1
        (-2646, 2447, -6223): [], # Lockup Token 2
        (2462, 2217, 2957): [], # Shock Jump Token
        (478, 6917, -2712): [], # Lighthouse Token
        (-221, 2029, 929): [], # Crows Nest Token
        (-783, 745, -3872): [], # Crate Token
        (6480, 597, -258): [], # Treasure Hunt Token
        (-4932, 1122, -1063): [], # Pool Token
        (-6620, 510, 4621): [], # Nipper Token
        (-5626, 3112, -2856): [], # Orange Jinjo
        (4848, 1340, -240): [], # Pink Jinjo
        (153, 6917, -2705): [], # Witch Switch
        (-968, 5358, -776): [], # Yellow Jinjo
    },
    TTC_BLUBBERS: {
        (254, -748, -175): [], # Blubber's Gold 1
        (-145, -748, 221): [], # Blubber's Gold 2
        (610, -412, 31): [], # Blubbers Token
    },
    TTC_NIPPERS: {
        (385, 227, 31): [], # Nipper Jiggy
    },
    TTC_SANDCATLE: {
        (0, 350, -987): [], # Sandcastle Jiggy
    },
    TTC_SHARKFOOD_ISLAND: {
        (0, 1950, 0): [], # Pink SNS Egg
    },
    # CC
    CC_MAIN: {
        (7309, 4267, 2286): [], # Green Pipe Extra Life
        (4570, 3727, 2783): [], # Shock Jump Extra Life
        (1752, 5270, -2214): [], # Alcove Extra Life
        (4326, 2146, -4080): [], # Blue Jinjo
        (3718, 3311, 2519): [], # Underwater Pipe Honeycomb
        (7886, 4272, 1969): [], # Above Water Pipe Honeycomb
        (5017, -3085, -13): [], # Green Jinjo
        (10061, 5112, 3): [], # Behind Clanker Jiggy
        (90, 5962, -12): [], # In Front Of Clanker Jiggy
        (4629, 2151, 3082): [], # Long Pipe Jiggy
        (2028, 5456, 2344): [], # Alcove Token
        (-9694, 5272, 1607): [], # Entrance Token
        (9823, 4225, -19): [], # Behind Clanker Token
        (870, 2146, -3148): [], # Gold Pipe Token
        (6138, 5087, 2637): [], # Orange Jinjo
        (-4726, 5337, -110): [], # Yellow Jinjo
    },
    CC_BELLY_MOUTH: {
        (532, 1424, 6632): [], # Tooth Token
        (3644, -474, 48): [], # Pink Jinjo
    },
    CC_BLOWHOLE: {
        (10, -391, -2185): [], # Blowhole Jiggy
        (0, -425, 1910): [], # Witch Switch
    },
    CC_GOLD_FEATHER: {
        (-259, -500, 1413): [], # Bottles Wonderwing
        (0, -340, -1604): [], # Gold Feather Jiggy
    },
    # BGS
    BGS_MAIN: {
        (-4382, 985, 2799): [], # Pink Egg Extra Life
    }
    # FP
    # GV
    # MMM
    # RBB
    # CCW
    # GL
}

PSUEDO_RANDOM_LOCATION_REQUIREMENTS_DICT = {
    # SM
    SM_MAIN: {
        (-2975, 1291, -1821): [], # Tree 1
        (-344, 835, -2224): [], # Tree 2
        (966, 750, 1807): [], # Tree 3
        (3, 49, 4847): [], # Stump 1
        (1018, 99, 4770): [], # Stump 2
        (1181, 49, 3994): [], # Stump 3
        (-2, -50, 3977): [], # Stump 4
        (-779, 49, 3581): [], # Stump 5
        (-3429, 575, -1015): [], # Under Stone Bridge
        (-5765, 50, -1681): [], # In Pond
    },
    SM_BANJOS_HOUSE: {
        (61, 6, -66): [], # Rug
    },
    # MM
    MM_MAIN: {
        (5147, 788, 2874): [], # Tree 1
        (3459, 755, 2636): [], # Tree 2
        (5818, 2354, -3218): [], # Behind Skull
        (5274, 2756, -2905): [], # Other Mumbos Eye
        (5595, 3089, -2972): [], # Atop Mumbos Skull
    },
    MM_TICKERS_TOWER: {
        (-10, 0, -26): [], # Floor 1
        (-10, 817, -26): [], # Floor 2
        (-10, 1507, -26): [], # Floor 3
    },
    MM_MUMBOS_SKULL: {
        (0, 600, 0): [], # Ceiling
    },
    # TTC
    TTC_MAIN: {
        (4118, -14, -7566): [], # Underwater Gap
    },
    TTC_BLUBBERS: {},
    TTC_NIPPERS: {},
    TTC_SANDCATLE: {},
    TTC_SHARKFOOD_ISLAND: {},
    # CC
    CC_MAIN: {
        (-9586, 4045, 1480): [], # Underneath Entrance
        (6768, 2145, 3500): [], # Middle Of Long Pipe
        (14177, 3231, -21): [], # Mutie Snippets Under Pipe
    },
    CC_BELLY_MOUTH: {},
    CC_BLOWHOLE: {},
    CC_GOLD_FEATHER: {},
    # BGS
    BGS_MAIN: {
        (-6592, 1717, -5498): [], # Atop Mumbos Skull
        (-8885, 0, -6143): [], # Corner Under Maze Switch
        (-3360, 0, -2192): [], # Corner Near Path To Maze
        (-6569, 1360, -5214): [], # Mumbos Eye 1
        (-6301, 1360, -5462): [], # Mumbos Eye 1
        (4702, 601, -3587): [], # Hut 1
        (4895, 1101, -4381): [], # Hut 2
        (5202, 1901, -5092): [], # Hut 3
        (6084, 2401, -4983): [], # Hut 4
        (-7552, 1599, -3445): [], # Atop Maze
    },
    BGS_MR_VILE: {},
    BGS_TANKTUP: {},
    BGS_MUMBOS_SKULL: {},
    # FP
    FP_MUMBOS_SKULL: {
        (6853, 1050, -3316): [], # Mumbos Eye 1
        (7049, 1050, -2958): [], # Mumbos Eye 2
        (4834, 449, -929): [], # Behind House
    },
    FP_IGLOO: {},
    FP_MUMBOS_SKULL: {
        (0, 600, 0): [], # Ceiling
    },
    FP_TREE: {},
    FP_WOZZAS: {
        (-3194, -365, -215): [], # Middle Of Tunnel
        (-1617, -361, -340): [], # Behind Green Crystal
    },
    # GV
    GV_MAIN: {
        (-5965, 1980, 5941): [], # Jinxy Butt
    },
    GV_MATCHING_PUZZLE: {},
    GV_KING_SANDYBUTT: {},
    GV_WATER_PYRAMID: {
        (5, 2200, -7): [], # Top Entrance
    },
    GV_RUPEE: {},
    GV_JINXY: {},
    GV_SNS: {},
    # MMM
    MMM_MAIN: {
        (5699, 400, -3349): [], # Above Well
        (-650, 460, -4798): [], # Mumbos Eye 1
        (-454, 460, -4598): [], # Mumbos Eye 2
        (-437, 745, -4822): [], # Atop Mumbos
        (-1304, 0, -1042): [], # Atop Mumbos
        (685, 1099, 1259): [], # Mansion Floor 2 #1
        (1350, 1099, 1265): [], # Mansion Floor 2 #2
        (681, 1099, -751): [], # Mansion Floor 2 #3
        (-1203, 174, -1425): [], # Tall Grass Corner 1
        (3053, 174, -2991): [], # Tall Grass Corner 2
        (3060, 174, -1993): [], # Tall Grass Corner 3
        (3096, 174, -1704): [], # Tall Grass Corner 4
        (3529, 29, 2506): [], # Corner 1
        (3529, 29, 2506): [], # Corner 2
        (1681, 29, 3742): [], # Corner 3
        (323, 29, 3764): [], # Corner 4
        (-1236, 29, 2678): [], # Corner 5
        (-175, 174, 439): [], # Mansion Corner 1
        (-183, 174, 35): [], # Mansion Corner 2
        (-2911, 449, 1320): [], # Atop Maze
    },
    MMM_INSIDE_LOGGO: {
        (531, 136, -478): [], # Loggo Corner 1
    },
    MMM_CHURCH: {
        (2243, 0, 4462): [], # Corner 1
        (-2304, 0, 4493): [], # Corner 2
        (-1639, 288, 2080): [], # Chair 1
        (-1624, 288, 498): [], # Chair 2
        (1624, 288, 2067): [], # Chair 3
        (1619, 288, 507): [], # Chair 4
        (1876, 200, -3450): [], # Side Of Organ 1
        (-1874, 200, -3450): [], # Side Of Organ 2
    },
    MMM_BASEMENT: {
        (-466, 31, -195): [], # Barrel 1
        (474, 31, 480): [], # Barrel 2
        (-513, 0, -784): [], # Corner 1
        (520, 0, -771): [], # Corner 2
    },
    MMM_TUMBLAR: {},
    MMM_WELL: {
        (5, 2000, 10): [], # Rope
    },
    MMM_DINING_ROOM: {
        (1465, 0, 2282): [], # Corner 1
        (-1465, 0, 2282): [], # Corner 2
        (1468, 0, -2466): [], # Corner 3
        (-1468, 0, -2466): [], # Corner 4
        (0, 200, 0): [], # Under Dining Table
    },
    MMM_FLOOR_1_ROOM_2_BLUE_EGGS: {
        (424, 0, 339): [], # Corner
    },
    MMM_FLOOR_3_ROOM_1_NOTES: {
        (408, 0, 319): [], # Corner
    },
    MMM_FLOOR_1_ROOM_1_RED_FEATHERS: {
        (-426, 0, 380): [], # Corner 1
        (-426, 0, -375): [], # Corner 1
    },
    MMM_SECRET_ROOM: {
        (0, 0, -600): [], # Between Windows
    },
    MMM_FLOOR_2_ROOM_2_LOGGO: {},
    MMM_FLOOR_3_ROOM_2_BEDROOM: {},
    MMM_FLOOR_2_ROOM_1_HONEYCOMB: {},
    MMM_INSIDE_GUTTER: {},
    MMM_MUMBOS_SKULL: {
        (0, 600, 0): [], # Ceiling
    },
    # RBB
    # CCW
    # GL
}

#############################
### AUTOMATIC ACQUIREMENT ###
#############################

AUTOMATIC_ACQUIREMENT_DICT = {
}