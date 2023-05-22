import sys
sys.path.append(".")

from Data_Files.Enums.Logic_Enums import LOGIC_ENUMS
from Data_Files.Enums.Transformation_Enums import TRANSFORMATION_ENUMS

ORANGE_OBJ_ID =          0x0029
MUMBO_TOKEN_OBJ_ID =     0x002D
JIGGY_OBJ_ID =           0x0046
EMPTY_HONEYCOMB_OBJ_ID = 0x0047
EXTRA_LIFE_OBJ_ID =      0x0049
YELLOW_JINJO_OBJ_ID =    0x005E
ORANGE_JINJO_OBJ_ID =    0x005F
BLUE_JINJO_OBJ_ID =      0x0060
MAGENTA_JINJO_OBJ_ID =   0x0061
GREEN_JINJO_OBJ_ID =     0x0062
BLUBBERS_GOLD_OBJ_ID =   0x002A
BLUE_PRESENT_OBJ_ID =    0x01ED
GREEN_PRESENT_OBJ_ID =   0x01EE
RED_PRESENT_OBJ_ID =     0x01EF
CATERPILLAR_OBJ_ID =     0x02A2
ACORN_OBJ_ID =           0x02A9
HONEYCOMB_OBJ_ID =       0x0050

DEFAULT_SCRIPT_ID = 0x190C

LOGIC_COMPLEX_OBJECTS = {
    # WORLD KEY STRING : {
    #   ITEM KEY STRING: (
    #       (DEBUG_NAME, ASSOCIATED_FLAG, OBJECT_ID, SCRIPT_ID, REQUIREMENTS),
    #   )
    # }

    ### SPIRAL MOUNTAIN ###
    LOGIC_ENUMS.SPIRAL_MOUNTAIN: {
        LOGIC_ENUMS.EMPTY_HONEYCOMB: (
            ("EH SM Stump", 0x0076, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EH SM Waterfall", 0x0077, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EH SM Underwater", 0x0078, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EH SM Tree", 0x0079, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL SM House", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EL SM Waterfall", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
    },

    ### MUMBOS MOUNTAIN ###
    LOGIC_ENUMS.MUMBOS_MOUNTAIN: {
        LOGIC_ENUMS.JIGGY: (
            ("J MM Tickers Tower", 0x0001, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J MM Mumbos Eye", 0x0002, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J MM Stonehenge", 0x0005, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J MM Green Hill", 0x0006, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EMPTY_HONEYCOMB: (
            ("EH MM Alcove", 0x0064, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EH MM Juju", 0x0065, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT MM Conga", 0x00C8, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MM Stonehenge", 0x00C9, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MM Mumbos Bridge", 0x00CA, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MM Pink Jinjo", 0x00CB, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MM Tickers Tower", 0x00CC, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("YJ MM", None, YELLOW_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("OJ MM", None, ORANGE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("BJ MM", None, BLUE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MJ MM", None, MAGENTA_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("GJ MM", None, GREEN_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL MM", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.ORANGE: (
            ("Orange", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
    },

    ### TREASURE TROVE COVE ###
    LOGIC_ENUMS.TREASURE_TROVE_COVE: {
        LOGIC_ENUMS.JIGGY: (
            ("J TTC Lighthouse", 0x000B, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J TTC Shock Jump Alcove", 0x000C, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J TTC Backside Alcove", 0x000D, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J TTC Underwater Crater", 0x000E, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J TTC Sandcastle", 0x000F, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J TTC Alcove Lockup", 0x0012, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EMPTY_HONEYCOMB: (
            ("EH TTC Underwater", 0x0066, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EH TTC Crate", 0x0067, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT TTC Inside Blubbers Ship", 0x00CD, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT TTC Lockup 1", 0x00CE, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT TTC Lockup 2", 0x00CF, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT TTC Blubbers Crow", 0x00D0, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT TTC Lighthouse", 0x00D1, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT TTC Crate", 0x00D2, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT TTC Treasure Hunt End", 0x00D3, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT TTC Underwater Crater", 0x00D4, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT TTC Shock Jump", 0x00D5, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT TTC Nipper", 0x00D6, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("YJ TTC", None, YELLOW_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("OJ TTC", None, ORANGE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("BJ TTC", None, BLUE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MJ TTC", None, MAGENTA_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("GJ TTC", None, GREEN_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL TTC", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # TTC Main Ledge
            ("EL TTC", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # TTC Main Underwater
            ("EL TTC", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # TTC Main Crate
        ),
        LOGIC_ENUMS.BLUBBERS_GOLD: (
            ("BG TTC SHIP 1", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("BG TTC SHIP 2", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
    },

    ### CLANKERS CAVERN ###
    LOGIC_ENUMS.CLANKERS_CAVERN: {
        LOGIC_ENUMS.JIGGY: (
            ("J CC Behind Tail", 0x0017, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CC Above Blowhole", 0x0018, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CC Long Tunnel", 0x0019, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CC Blowhole", 0x001C, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CC Wonderwing", 0x001D, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EMPTY_HONEYCOMB: (
            ("EH CC Underwater", 0x0068, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EH CC Above Water", 0x0069, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT CC Behind Tail", 0x00D7, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CC Entrance", 0x00D8, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CC Short Tunnel", 0x00D9, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CC Alcove", 0x00DA, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CC Tooth", 0x00DB, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("YJ CC", None, YELLOW_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("OJ CC", None, ORANGE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("BJ CC", None, BLUE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MJ CC", None, MAGENTA_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("GJ CC", None, GREEN_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL CC", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CC Main Pipe
            ("EL CC", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CC Main Jump Shock
            ("EL CC", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CC Main Alcove
        ),
    },

    ### BUBBLEGLOOP SWAMP ###
    LOGIC_ENUMS.BUBBLEGLOOP_SWAMP: {
        LOGIC_ENUMS.JIGGY: (
        ),
        LOGIC_ENUMS.EMPTY_HONEYCOMB: (
            ("EH BGS Above Mumbo", 0x006A, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EH BGS Above Tiptup", 0x006B, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT BGS Under Huts 1", 0x00DC, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT BGS Under Huts 2", 0x00DD, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT BGS Cattail", 0x00DE, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT BGS Yellow Jinjo", 0x00DF, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT BGS Above Huts", 0x00E0, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT BGS Behind Skull", 0x00E1, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT BGS Central", 0x00E2, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT BGS Tiptup", 0x00E3, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT BGS Vile", 0x00E4, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT BGS Behind Mumbo", 0x00E5, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("YJ BGS", None, YELLOW_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("OJ BGS", None, ORANGE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("BJ BGS", None, BLUE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MJ BGS", None, MAGENTA_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("GJ BGS", None, GREEN_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL BGS", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # BGS Main Pink Egg
            ("EL BGS", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # BGS Main Under Huts
        ),
    },

    ### FREEZEEZY PEAK ###
    LOGIC_ENUMS.FREEZEEZY_PEAK: {
        LOGIC_ENUMS.JIGGY: (
            ("J FP Smoke Pipe", 0x002A, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EMPTY_HONEYCOMB: (
            ("EH FP Wozza", 0x006C, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EH FP Sir Slush", 0x006D, EMPTY_HONEYCOMB_OBJ_ID, 0x140C, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT FP Snowman Leg 1", 0x00E6, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT FP Snowman Leg 2", 0x00E7, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT FP Presents", 0x00E8, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT FP Chimney", 0x00E9, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT FP Sir Slush Start", 0x00EA, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT FP Sir Slush End", 0x00EB, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT FP Under Christmas Tree", 0x00EC, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT FP Scarf", 0x00ED, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT FP Underwater", 0x00EE, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT FP Igloo", 0x00EF, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("YJ FP", None, YELLOW_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("OJ FP", None, ORANGE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("BJ FP", None, BLUE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MJ FP", None, MAGENTA_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("GJ FP", None, GREEN_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL FP", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # FP Main Mumbos Skull
            ("EL FP", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # FP Main Finish Line
            ("EL FP", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # Wozza's Cave
        ),
        LOGIC_ENUMS.PRESENTS: (
            ("Blue Present", None, BLUE_PRESENT_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("Green Present", None, GREEN_PRESENT_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("Red Present", None, RED_PRESENT_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
    },

    ### GOBIS VALLEY ###
    LOGIC_ENUMS.GOBIS_VALLEY: {
        LOGIC_ENUMS.JIGGY: (
            ("J GV Jinxy", 0x003E, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J GV Sandybutt", 0x0040, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J GV Water Pyramid", 0x0041, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J GV Rubee", 0x0042, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT GV Jinxys Nose", 0x00F0, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GV Corner Near Jinxy", 0x00F1, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GV Moat", 0x00F2, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GV Atop Sandybutts Maze", 0x00F3, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GV Water Pyramid Bottom", 0x00F4, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GV Matching Puzzle", 0x00F5, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GV Inside Sandybutts Maze", 0x00F6, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GV Water Pyramid", 0x00F7, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GV Rubee", 0x00F8, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GV Jinxy", 0x00F9, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("YJ GV", None, YELLOW_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("OJ GV", None, ORANGE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("BJ GV", None, BLUE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MJ GV", None, MAGENTA_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("GJ GV", None, GREEN_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL GV", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # GV Main Behind Jinxy
            ("EL GV", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # GV Main Atop Water Pyramid
            ("EL GV", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # King Sandybutt's Maze
        ),
    },

    ### MAD MONSTER MANSION ###
    LOGIC_ENUMS.MAD_MONSTER_MANSION: {
        LOGIC_ENUMS.JIGGY: (
            ("J MMM Well", 0x005B, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J MMM Napper", 0x005C, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J MMM Cellar", 0x005D, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J MMM Atop Church", 0x005E, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J MMM Drainpipe", 0x0060, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J MMM Tumblar", 0x0061, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J MMM Loggo", 0x0063, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EMPTY_HONEYCOMB: (
            ("EH MMM Church Rafter", 0x0074, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EH MMM Pumpkin Only", 0x0075, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, [TRANSFORMATION_ENUMS.PUMPKIN_BK]),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT MMM Near Green Pool", 0x00FA, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Near Tumblars", 0x00FB, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Church Tower", 0x00FC, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Maze Pumpkin", 0x00FD, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Maze Top", 0x00FE, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Behind Tombstone", 0x00FF, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Inside Green Pool", 0x0100, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Church Rafter", 0x0101, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Church Chair", 0x0102, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Atop Tumblars", 0x0103, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Loggo/Cellar", 0x0104, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Dining Room", 0x0105, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Well", 0x0106, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Bedroom", 0x0107, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT MMM Bathroom", 0x0108, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("YJ MMM", None, YELLOW_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("OJ MMM", None, ORANGE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("BJ MMM", None, BLUE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MJ MMM", None, MAGENTA_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("GJ MMM", None, GREEN_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL MMM", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # MMM Church
            ("EL MMM", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # MMM Dining Room
            ("EL MMM", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # MMM Secret Church Room
        ),
    },

    ### RUSTY BUCKET BAY ###
    LOGIC_ENUMS.RUSTY_BUCKET_BAY: {
        LOGIC_ENUMS.JIGGY: (
            ("J RBB Chump Warehouse", 0x0051, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J RBB Smoke Pipe", 0x0054, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J RBB Boss Kaboom Boss", 0x0055, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J RBB Propellers", 0x0056, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J RBB Captains", 0x0057, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J RBB Caged", 0x0058, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J RBB Engine Room", 0x0059, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EMPTY_HONEYCOMB: (
            ("EH RBB Engine Room", 0x0073, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT RBB Smoke Pipe", 0x0109, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Ship Bow", 0x010A, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Lifeboat", 0x010B, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB 2 Toll", 0x010C, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Toxic Pool", 0x010D, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Near Witch Switch", 0x010E, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Chompa Container", 0x010F, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Seaman Container", 0x0110, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Cabins", 0x0111, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Navigation", 0x0112, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Kitchen", 0x0113, 0x0C8C, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Engine Room Pipe 1", 0x0114, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Engine Room Pipe 1", 0x0115, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Engine Room Bridge", 0x0116, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT RBB Middle Pipe", 0x0117, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("YJ RBB", None, YELLOW_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("OJ RBB", None, ORANGE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("BJ RBB", None, BLUE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MJ RBB", None, MAGENTA_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("GJ RBB", None, GREEN_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL RBB", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # RBB Engine Room
            ("EL RBB", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # RBB Chump Warehouse
        ),
    },

    ### CLICK CLOCK WOOD ###
    LOGIC_ENUMS.CLICK_CLOCK_WOOD_HUB: {
    },
    LOGIC_ENUMS.CLICK_CLOCK_WOOD_SPRING: {
        LOGIC_ENUMS.JIGGY: (
            ("J CCW Top Of Tree", 0x004E, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CCW Whipcracks", 0x004F, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT CCW Spring Treehouse", 0x0122, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Spring Low Branch", 0x0123, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Spring Near Eyrie", 0x0124, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Spring Bramble", 0x0125, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Spring Snarebear Plant", 0x0126, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Spring Snarebear Entrance", 0x0127, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Spring Zubba", 0x0128, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Spring Nabnuts", 0x0129, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("MJ CCW", None, MAGENTA_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("GJ CCW", None, GREEN_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Spring Branches
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Spring Snarebear
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Spring Whipcracks 1
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Spring Whipcracks 2
        ),
    },
    LOGIC_ENUMS.CLICK_CLOCK_WOOD_SUMMER: {
        LOGIC_ENUMS.JIGGY: (
            ("J CCW Treehouse", 0x0047, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CCW Zubba", 0x004B, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CCW Side Of Tree", 0x004D, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CCW Whipcracks", 0x004F, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT CCW Summer Near Eyrie", 0x012A, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Summer Garden Corner", 0x012B, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Summer Snarebear Near Mumbos", 0x012C, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Summer Low Branch", 0x012D, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Summer Path To Gnawtys", 0x012E, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Summer Side Leaf", 0x012F, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Summer Mumbos", 0x0130, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("YJ CCW", None, YELLOW_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Summer Grass
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Summer Treehouse
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Summer Whipcracks
        ),
        # CATERPILLAR_KEY: (),
    },
    LOGIC_ENUMS.CLICK_CLOCK_WOOD_AUTUMN: {
        LOGIC_ENUMS.JIGGY: (
            ("J CCW Treehouse", 0x0047, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CCW Gnawty", 0x004A, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CCW Side Of Tree", 0x004D, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CCW Whipcracks", 0x004F, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT CCW Autumn Side Leaf", 0x0131, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Autumn Snarebear Entrance", 0x0132, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Autumn Snarebear Top", 0x0133, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Autumn Snarebear Treehouse", 0x0134, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Autumn Low Branch", 0x0135, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("OJ CCW", None, ORANGE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Autumn Snarebear
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Autumn Gnawty
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Autumn Whipcracks
        ),
        # CATERPILLAR_KEY: (),
        LOGIC_ENUMS.ACORN: (
            ("Acorn", None, ACORN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("Acorn", None, ACORN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("Acorn", None, ACORN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("Acorn", None, ACORN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("Acorn", None, ACORN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("Acorn", None, ACORN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
    },
    LOGIC_ENUMS.CLICK_CLOCK_WOOD_WINTER: {
        LOGIC_ENUMS.JIGGY: (
            ("J CCW Gnawty", 0x004A, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CCW Top Of Tree", 0x004E, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J CCW Whipcracks", 0x004F, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT CCW Winter Dead Flower", 0x0136, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Winter Ice Fly Pad", 0x0137, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Winter Dead Hive", 0x0138, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Winter Platform Near Nabnut", 0x0139, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT CCW Winter Sir Slush", 0x013A, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EMPTY_HONEYCOMB: (
            ("EH CCW Gnawty", 0x0070, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("EH CCW Acorn Storage", 0x0071, EMPTY_HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.JINJOS: (
            ("BJ CCW", None, BLUE_JINJO_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Winter Sir Slush
            ("EL CCW", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Winter Ice Water
        ),
    },

    ### GRUNTILDAS LAIR ###
    LOGIC_ENUMS.GRUNTILDAS_LAIR: {
        LOGIC_ENUMS.JIGGY: (
            ("J GL First Jiggy", 0x0032, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J GL Grunty Statue", 0x0036, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J GL Sarcophagus", 0x0039, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("J GL FP Entrance", 0x0037, JIGGY_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.MUMBO_TOKEN: (
            ("MT GL Pink Cauldron", 0x0118, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GL CCW Puzzle", 0x0119, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GL Amber Cauldron", 0x011A, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GL CC Entrance", 0x011B, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GL Sarcophagus", 0x011C, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GL FP Entrance", 0x011D, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GL Coffin Room", 0x011E, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GL Water 3 Switch", 0x011F, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GL RBB Entrance", 0x0120, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("MT GL MMM Puzzle", 0x0121, MUMBO_TOKEN_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
        LOGIC_ENUMS.EXTRA_LIVES: (
            ("EL GL", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Puzzle
            ("EL GL", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # FP Entrance
            ("EL GL", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # CCW Entrance
            ("EL GL", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # DoG
            ("EL GL", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # BGS Entrance
            ("EL GL", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # MMM Entrance
            ("EL GL", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # MMM Puzzle
            ("EL GL", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # Furnace Fun
            ("EL GL", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # Furnace Fun
            ("EL GL", None, EXTRA_LIFE_OBJ_ID, DEFAULT_SCRIPT_ID, None), # Furnace Fun
        ),
        LOGIC_ENUMS.HONEYCOMB: (
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
            ("H GL", None, HONEYCOMB_OBJ_ID, DEFAULT_SCRIPT_ID, None),
        ),
    },
}