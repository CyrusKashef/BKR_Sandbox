from Data_Files.Enums.Jigsaw_Puzzle_Enums import *
from Data_Files.Enums.Map_Enums import ROOM_ENUMS
from Data_Files.Enums.IntEnums.Warp_Enums import WARP_ENUMS
from Data_Files.Enums.IntEnums.Area_Enums import AREA_ENUMS

WARP_MAP_DICT = {
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/code_956B0.c
    # https://hack64.net/wiki/doku.php?id=banjo_kazooie:enums#map_exit_indices
    # WORLD_ENUM: {
    #     ROOM_ENUM: {
    #         WARP_ENUM: AREA_ENUM,
    #     }
    # }
    SPIRAL_MOUNTAIN: {
        ROOM_ENUMS.SM_MAIN: {
            WARP_ENUMS.SM_MAIN_TO_GL_MM_ENTRANCE: None,
            WARP_ENUMS.SM_MAIN_TO_SM_BANJOS_HOUSE: None,
        },
        ROOM_ENUMS.SM_BANJOS_HOUSE: {
            WARP_ENUMS.SM_BANJOS_HOUSE_TO_SM_MAIN: None,
        },
    },
    MUMBOS_MOUNTAIN: {
        ROOM_ENUMS.MM_MAIN: {
            WARP_ENUMS.MM_MAIN_TO_MM_LOWER_TICKERS: None,
            WARP_ENUMS.MM_MAIN_TO_MM_UPPER_TICKERS: None,
            WARP_ENUMS.MM_MAIN_TO_MM_MUMBOS_SKULL: None,
        },
        ROOM_ENUMS.MM_INSIDE_TICKERS_TOWER: {
            WARP_ENUMS.MM_LOWER_TICKERS_TO_MM_MAIN: None,
            WARP_ENUMS.MM_UPPER_TICKERS_TO_MM_MAIN: None,
        },
        ROOM_ENUMS.MM_MUMBOS_SKULL: {
            WARP_ENUMS.MM_MUMBOS_SKULL_TO_MM_MAIN: None,
        },
    },
    TREASURE_TROVE_COVE: {
        ROOM_ENUMS.TTC_MAIN: {
            WARP_ENUMS.TTC_MAIN_TO_GL_TTC_ENTRANCE: None,
            WARP_ENUMS.TTC_MAIN_TO_TTC_SANDCASTLE: None,
            WARP_ENUMS.TTC_MAIN_TO_TTC_NIPPER: None,
            WARP_ENUMS.TTC_MAIN_TO_TTC_SALTY_HIPPO_SIDE: None,
            WARP_ENUMS.TTC_MAIN_TO_TTC_SALTY_HIPPO_TOP: None,
            WARP_ENUMS.TTC_MAIN_TO_TTC_SHARKFOOD_ISLAND: None,
            WARP_ENUMS.TTC_ALCOVE_LOWER_TO_TTC_ALCOVE_UPPER: None,
            WARP_ENUMS.TTC_ALCOVE_UPPER_TO_TTC_ALCOVE_LOWER: None,
            WARP_ENUMS.TTC_LIGHTHOUSE_LOWER_TO_TTC_LIGHTHOUSE_UPPER: None,
            WARP_ENUMS.TTC_LIGHTHOUSE_UPPER_TO_TTC_LIGHTHOUSE_LOWER: None,
        },
        ROOM_ENUMS.TTC_BLUBBERS: {
            WARP_ENUMS.TTC_SALTY_HIPPO_SIDE_TO_TTC_MAIN: None,
            WARP_ENUMS.TTC_SALTY_HIPPO_TOP_TO_TTC_MAIN: None,
        },
        ROOM_ENUMS.TTC_NIPPERS: {
            WARP_ENUMS.TTC_NIPPER_TO_TTC_MAIN: None,
        },
        ROOM_ENUMS.TTC_SANDCATLE: {
            WARP_ENUMS.TTC_SANDCASTLE_TO_TTC_MAIN: None,
        },
        ROOM_ENUMS.TTC_SHARKFOOD_ISLAND: {
            WARP_ENUMS.TTC_SHARKFOOD_ISLAND_TO_TTC_MAIN: None,
        },
    },
    CLANKERS_CAVERN: {
        ROOM_ENUMS.CC_MAIN: {
            WARP_ENUMS.CC_MAIN_TO_GL_CC_ENTRANCE: None,
            WARP_ENUMS.CC_MAIN_TO_CC_CLANKER_BLOWHOLE: None,
            WARP_ENUMS.CC_MAIN_TO_CC_CLANKER_LEFT_TOOTH: None,
            WARP_ENUMS.CC_MAIN_TO_CC_CLANKER_RIGHT_TOOTH: None,
            WARP_ENUMS.CC_MAIN_TO_CC_CLANKER_LEFT_GILL: None,
            WARP_ENUMS.CC_MAIN_TO_CC_CLANKER_RIGHT_GILL: None,
        },
        ROOM_ENUMS.CC_BLOWHOLE: {
            WARP_ENUMS.CC_CLANKER_BLOWHOLE_TO_CC_CLANKER_MOUTH: None,
            WARP_ENUMS.CC_CLANKER_BLOWHOLE_TO_CC_CLANKER_BELLY: None,
        },
        ROOM_ENUMS.CC_BELLY_MOUTH: {
            WARP_ENUMS.CC_CLANKER_BELLY_TO_CC_CLANKER_WONDERWING: None,
            WARP_ENUMS.CC_CLANKER_LEFT_TOOTH_TO_CC_MAIN: None,
            WARP_ENUMS.CC_CLANKER_RIGHT_TOOTH_TO_CC_MAIN: None,
            WARP_ENUMS.CC_CLANKER_LEFT_GILL_TO_CC_MAIN: None,
            WARP_ENUMS.CC_CLANKER_RIGHT_GILL_TO_CC_MAIN: None,
        },
        ROOM_ENUMS.CC_GOLD_FEATHER: {
            WARP_ENUMS.CC_CLANKER_WONDERWING_TO_CC_CLANKER_BELLY: None,
        },
    },
    BUBBLEGLOOP_SWAMP: {
        ROOM_ENUMS.BGS_MAIN: {
            WARP_ENUMS.BGS_MAIN_TO_GL_BGS_ENTRANCE: None,
            WARP_ENUMS.BGS_MAIN_TO_BGS_MUMBOS_SKULL: None,
            WARP_ENUMS.BGS_MAIN_TO_BGS_TANKTUP: None,
            WARP_ENUMS.BGS_MAIN_TO_BGS_VILE_LEFT: None,
            WARP_ENUMS.BGS_MAIN_TO_BGS_VILE_RIGHT: None,
        },
        ROOM_ENUMS.BGS_MR_VILE: {
            WARP_ENUMS.BGS_VILE_LEFT_TO_BGS_MAIN: None,
            WARP_ENUMS.BGS_VILE_RIGHT_TO_BGS_MAIN: None,
        },
        ROOM_ENUMS.BGS_TANKTUP: {
            WARP_ENUMS.BGS_TANKTUP_TO_BGS_MAIN: None,
        },
        ROOM_ENUMS.BGS_MUMBOS_SKULL: {
            WARP_ENUMS.BGS_MUMBOS_SKULL_TO_BGS_MAIN: None,
        },
    },
    FREEZEEZY_PEAK: {
        ROOM_ENUMS.FP_MAIN: {
            WARP_ENUMS.FP_MAIN_TO_GL_FP_ENTRANCE: None,
            WARP_ENUMS.FP_MAIN_TO_FP_IGLOO: None,
            WARP_ENUMS.FP_MAIN_TO_FP_TREE: None,
            WARP_ENUMS.FP_MAIN_TO_FP_MUMBOS_SKULL: None,
            WARP_ENUMS.FP_MAIN_TO_FP_WOZZAS_CAVE: None,
        },
        ROOM_ENUMS.FP_IGLOO: {
            WARP_ENUMS.FP_IGLOO_TO_FP_MAIN: None,
        },
        ROOM_ENUMS.FP_MUMBOS_SKULL: {
            WARP_ENUMS.FP_MUMBOS_SKULL_TO_FP_MAIN: None,
        },
        ROOM_ENUMS.FP_TREE: {
            WARP_ENUMS.FP_TREE_TO_FP_MAIN: None,
        },
        ROOM_ENUMS.FP_WOZZAS: {
            WARP_ENUMS.FP_WOZZAS_CAVE_TO_FP_MAIN: None,
        },
    },
    GOBIS_VALLEY: {
        ROOM_ENUMS.GV_MAIN: {
            WARP_ENUMS.GV_MAIN_TO_GL_GV_ENTRANCE: None,
            WARP_ENUMS.GV_MAIN_TO_GV_JINXY: None,
            WARP_ENUMS.GV_MAIN_TO_GV_RUBEE: None,
            WARP_ENUMS.GV_MAIN_TO_GV_WATER_PYRAMID_UPPER: None,
            WARP_ENUMS.GV_MAIN_TO_GV_WATER_PYRAMID_LOWER: None,
            WARP_ENUMS.GV_MAIN_TO_GV_MATCHING_PYRAMID: None,
            WARP_ENUMS.GV_MAIN_TO_GV_SNS_ROOM: None,
            WARP_ENUMS.GV_MAIN_TO_KING_SANDYBUTT: None,
        },
        ROOM_ENUMS.GV_MATCHING_PUZZLE: {
            WARP_ENUMS.GV_MATCHING_PYRAMID_TO_GV_MAIN: None,
        },
        ROOM_ENUMS.GV_KING_SANDYBUTT: {
            WARP_ENUMS.GV_KING_SANDYBUTT_FRONT_TO_GV_MAIN: None,
            WARP_ENUMS.GV_KING_SANDYBUTT_BACK_TO_GV_MAIN: None,
        },
        ROOM_ENUMS.GV_WATER_PYRAMID: {
            WARP_ENUMS.GV_WATER_PYRAMID_LOWER_TO_GV_MAIN: None,
        },
        ROOM_ENUMS.GV_RUBEE: {
            WARP_ENUMS.GV_RUBEE_TO_GV_MAIN: None,
        },
        ROOM_ENUMS.GV_JINXY: {
            WARP_ENUMS.GV_JINXY_TO_GV_MAIN: None,
        },
        ROOM_ENUMS.GV_SNS: {
            WARP_ENUMS.GV_SNS_ROOM_TO_GV_MAIN: None,
        },
    },
    MAD_MONSTER_MANSION: {
        ROOM_ENUMS.MMM_MAIN: {
            WARP_ENUMS.MMM_MAIN_TO_GL_MMM_ENTRANCE: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_NAPPER_FRONT: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_NAPPER_CHIMNEY: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_EGG_ROOM: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_RED_FEATHER_ROOM: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_HONEYCOMB_ROOM: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_LOGGO_ROOM: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_BEDROOM: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_NOTE_ROOM: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_CHURCH: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_SECRET_ROOM: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_CELLAR: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_WELL_TOP: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_MUMBOS_SKULL: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_TUMBLAR: None,
            WARP_ENUMS.MMM_CHURCH_LOWER_TO_MMM_CHURCH_UPPER: None,
            WARP_ENUMS.MMM_CHURCH_UPPER_TO_MMM_CHURCH_LOWER: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_GUTTER_TOP: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_GUTTER_BOTTOM: None,
            WARP_ENUMS.MMM_MAIN_TO_MMM_WELL_BOTTOM: None,
        },
        ROOM_ENUMS.MMM_CHURCH: {
            WARP_ENUMS.MMM_CHURCH_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_BASEMENT: {
            WARP_ENUMS.MMM_CELLAR_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_TUMBLAR: {
            WARP_ENUMS.MMM_TUMBLAR_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_WELL: {
            WARP_ENUMS.MMM_WELL_TOP_TO_MMM_MAIN: None,
            WARP_ENUMS.MMM_WELL_BOTTOM_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_DINING_ROOM: {
            WARP_ENUMS.MMM_NAPPER_FRONT_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_FLOOR_1_ROOM_1_RED_FEATHERS: {
            WARP_ENUMS.MMM_RED_FEATHER_ROOM_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_FLOOR_1_ROOM_2_BLUE_EGGS: {
            WARP_ENUMS.MMM_EGG_ROOM_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_FLOOR_2_ROOM_1_HONEYCOMB: {
            WARP_ENUMS.MMM_HONEYCOMB_ROOM_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_FLOOR_2_ROOM_2_LOGGO: {
            WARP_ENUMS.MMM_LOGGO_ROOM_TO_MMM_MAIN: None,
            WARP_ENUMS.MMM_LOGGO_ROOM_TO_MMM_INSIDE_LOGGO: None,
        },
        ROOM_ENUMS.MMM_FLOOR_3_ROOM_1_NOTES: {
            WARP_ENUMS.MMM_NOTE_ROOM_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_FLOOR_3_ROOM_2_BEDROOM: {
            WARP_ENUMS.MMM_BEDROOM_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_SECRET_ROOM: {
            WARP_ENUMS.MMM_SECRET_ROOM_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_INSIDE_GUTTER: {
            WARP_ENUMS.MMM_GUTTER_BOTTOM_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_MUMBOS_SKULL: {
            WARP_ENUMS.MMM_MUMBOS_SKULL_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.MMM_INSIDE_LOGGO: {
            WARP_ENUMS.MMM_INSIDE_LOGGO_TO_MMM_LOGGO_ROOM: None,
        },
    },
    RUSTY_BUCKET_BAY: {
        ROOM_ENUMS.RBB_MAIN: {
            WARP_ENUMS.RBB_MAIN_TO_GL_RBB_ENTRANCE: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_BIG_FISH_WAREHOUSE_TOP: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_BIG_FISH_WAREHOUSE_BOTTOM: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_BOAT_ROOM: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_MINI_KABOOM_CONTAINER: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_SEAMAN_GRUBLIN_CONTAINER: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_CHOMPA_CONTAINER: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_KITCHEN_PIPE: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_MINI_KABOOM_PIPE: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_ENGINE_ROOM_PIPE: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_ENGINE_ROOM_MAIN: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_CONTROL_ROOM_WINDOW: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_CAPTAINS_ROOM_WINDOW: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_CABIN_WINDOW: None,
            WARP_ENUMS.RBB_MAIN_TO_RBB_BOSS_KABOOM_BOSS: None,
        },
        ROOM_ENUMS.RBB_ENGINE_ROOM: {
            WARP_ENUMS.RBB_ENGINE_ROOM_PIPE_TO_RBB_MAIN: None,
            WARP_ENUMS.RBB_ENGINE_ROOM_MAIN_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.RBB_BLUE_CONTAINER_1_CHOMPA: {
            WARP_ENUMS.RBB_CHOMPA_CONTAINER_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN: {
            WARP_ENUMS.RBB_SEAMAN_GRUBLIN_CONTAINER_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.RBB_BLUE_CONTAINER_3_KABOOM_BOX: {
            WARP_ENUMS.RBB_MINI_KABOOM_CONTAINER_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.RBB_CABINS: {
            WARP_ENUMS.RBB_CABIN_WINDOW_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.RBB_BOSS_KABOOM_BOSS: {
            WARP_ENUMS.RBB_BOSS_KABOOM_BOSS_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.RBB_CAPTAIN_ROOM: {
            WARP_ENUMS.RBB_CAPTAINS_ROOM_WINDOW_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.RBB_ANCHOR: {
            WARP_ENUMS.RBB_ANCHOR_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.RBB_BIG_FISH_WAREHOUSE: {
            WARP_ENUMS.RBB_BIG_FISH_WAREHOUSE_BOTTOM_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.RBB_BOAT_ROOM: {
            WARP_ENUMS.RBB_BOAT_ROOM_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.RBB_NAVIGATION: {
            WARP_ENUMS.RBB_CONTROL_ROOM_WINDOW_TO_RBB_MAIN: None,
        }
    },
    CLICK_CLOCK_WOOD: {
        ROOM_ENUMS.CCW_LOBBY: {
            WARP_ENUMS.CCW_MAIN_TO_GL_CCW_ENTRANCE: None,
            WARP_ENUMS.CCW_MAIN_TO_CCW_SPRING_MAIN: None,
            WARP_ENUMS.CCW_MAIN_TO_CCW_SUMMER_MAIN: None,
            WARP_ENUMS.CCW_MAIN_TO_CCW_AUTUMN_MAIN: None,
            WARP_ENUMS.CCW_MAIN_TO_CCW_WINTER_MAIN: None,
        },
    },
    CLICK_CLOCK_WOOD_SPRING: {
        ROOM_ENUMS.CCW_SPRING_MAIN: {
            WARP_ENUMS.CCW_SPRING_MAIN_TO_CCW_MAIN: None,
            WARP_ENUMS.CCW_SPRING_MAIN_TO_CCW_SPRING_MUMBOS_SKULL: None,
            WARP_ENUMS.CCW_SPRING_MAIN_TO_CCW_SPRING_ZUBBA: None,
            WARP_ENUMS.CCW_SPRING_MAIN_TO_CCW_SPRING_NABNUT: None,
            WARP_ENUMS.CCW_SPRING_MAIN_TO_CCW_SPRING_WHIPCRACKS: None,
        },
        ROOM_ENUMS.CCW_SPRING_MUMBOS_SKULL: {
            WARP_ENUMS.CCW_SPRING_MUMBOS_SKULL_TO_CCW_SPRING_MAIN: None,
        },
        ROOM_ENUMS.CCW_SPRING_ZUBBA: {
            WARP_ENUMS.CCW_SPRING_ZUBBA_TO_CCW_SPRING_MAIN: None,
        },
        ROOM_ENUMS.CCW_SPRING_NABNUT: {
            WARP_ENUMS.CCW_SPRING_NABNUT_TO_CCW_SPRING_MAIN: None,
        },
        ROOM_ENUMS.CCW_SPRING_WHIPCRACKS: {
            WARP_ENUMS.CCW_SPRING_WHIPCRACKS_TO_CCW_SPRING_MAIN: None,
        },
    },
    CLICK_CLOCK_WOOD_SUMMER: {
        ROOM_ENUMS.CCW_SUMMER_MAIN: {
            WARP_ENUMS.CCW_SUMMER_MAIN_TO_CCW_MAIN: None,
            WARP_ENUMS.CCW_SUMMER_MAIN_TO_CCW_SUMMER_MUMBOS_SKULL: None,
            WARP_ENUMS.CCW_SUMMER_MAIN_TO_CCW_SUMMER_ZUBBA: None,
            WARP_ENUMS.CCW_SUMMER_MAIN_TO_CCW_SUMMER_NABNUT: None,
            WARP_ENUMS.CCW_SUMMER_MAIN_TO_CCW_SUMMER_WHIPCRACKS: None,
        },
        ROOM_ENUMS.CCW_SUMMER_MUMBOS_SKULL: {
            WARP_ENUMS.CCW_SUMMER_MUMBOS_SKULL_TO_CCW_SUMMER_MAIN: None,
        },
        ROOM_ENUMS.CCW_SUMMER_ZUBBA: {
            WARP_ENUMS.CCW_SUMMER_ZUBBA_TO_CCW_SUMMER_MAIN: None,
        },
        ROOM_ENUMS.CCW_SUMMER_NABNUT: {
            WARP_ENUMS.CCW_SUMMER_NABNUT_TO_CCW_SUMMER_MAIN: None,
        },
        ROOM_ENUMS.CCW_SUMMER_WHIPCRACKS: {
            WARP_ENUMS.CCW_SUMMER_WHIPCRACKS_TO_CCW_SUMMER_MAIN: None,
        },
    },
    CLICK_CLOCK_WOOD_AUTUMN: {
        ROOM_ENUMS.CCW_AUTUMN_MAIN: {
            WARP_ENUMS.CCW_AUTUMN_MAIN_TO_CCW_MAIN: None,
            WARP_ENUMS.CCW_AUTUMN_MAIN_TO_CCW_AUTUMN_MUMBOS_SKULL: None,
            WARP_ENUMS.CCW_AUTUMN_MAIN_TO_CCW_AUTUMN_ZUBBA: None,
            WARP_ENUMS.CCW_AUTUMN_MAIN_TO_CCW_AUTUMN_NABNUT: None,
            WARP_ENUMS.CCW_AUTUMN_MAIN_TO_CCW_AUTUMN_FLOODED_ATTIC: None,
            WARP_ENUMS.CCW_AUTUMN_MAIN_TO_CCW_AUTUMN_WHIPCRACKS: None,
        },
        ROOM_ENUMS.CCW_AUTUMN_MUMBOS_SKULL: {
            WARP_ENUMS.CCW_AUTUMN_MUMBOS_SKULL_TO_CCW_AUTUMN_MAIN: None,
        },
        ROOM_ENUMS.CCW_AUTUMN_ZUBBA: {
            WARP_ENUMS.CCW_AUTUMN_ZUBBA_TO_CCW_AUTUMN_MAIN: None,
        },
        ROOM_ENUMS.CCW_AUTUMN_NABNUT: {
            WARP_ENUMS.CCW_AUTUMN_NABNUT_TO_CCW_AUTUMN_MAIN: None,
        },
        ROOM_ENUMS.CCW_AUTUMN_FLOODED_ATTIC: {
            WARP_ENUMS.CCW_AUTUMN_FLOODED_ATTIC_TO_CCW_AUTUMN_MAIN: None,
        },
        ROOM_ENUMS.CCW_AUTUMN_WHIPCRACKS: {
            WARP_ENUMS.CCW_AUTUMN_WHIPCRACKS_TO_CCW_AUTUMN_MAIN: None,
        },
    },
    CLICK_CLOCK_WOOD_WINTER: {
        ROOM_ENUMS.CCW_WINTER_MAIN: {
            WARP_ENUMS.CCW_WINTER_MAIN_TO_CCW_MAIN: None,
            WARP_ENUMS.CCW_WINTER_MAIN_TO_CCW_WINTER_MUMBOS_SKULL: None,
            WARP_ENUMS.CCW_WINTER_MAIN_TO_CCW_WINTER_NABNUT: None,
            WARP_ENUMS.CCW_WINTER_MAIN_TO_CCW_WINTER_ACORN_STORAGE: None,
            WARP_ENUMS.CCW_WINTER_MAIN_TO_CCW_WINTER_FLOODED_ATTIC: None,
            WARP_ENUMS.CCW_WINTER_MAIN_TO_CCW_WINTER_WHIPCRACKS: None,
        },
        ROOM_ENUMS.CCW_WINTER_MUMBOS_SKULL: {
            WARP_ENUMS.CCW_WINTER_MUMBOS_SKULL_TO_CCW_WINTER_MAIN: None,
        },
        ROOM_ENUMS.CCW_WINTER_NABNUT: {
            WARP_ENUMS.CCW_WINTER_NABNUT_TO_CCW_WINTER_MAIN: None,
        },
        ROOM_ENUMS.CCW_WINTER_ACORN_STORAGE: {
            WARP_ENUMS.CCW_WINTER_ACORN_STORAGE_TO_CCW_WINTER_MAIN: None,
        },
        ROOM_ENUMS.CCW_WINTER_FLOODED_ATTIC: {
            WARP_ENUMS.CCW_WINTER_FLOODED_ATTIC_TO_CCW_WINTER_MAIN: None,
        },
        ROOM_ENUMS.CCW_WINTER_WHIPCRACKS: {
            WARP_ENUMS.CCW_WINTER_WHIPCRACKS_TO_CCW_WINTER_MAIN: None,
        },
    },
    GRUNTILDAS_LAIR: {
        ROOM_ENUMS.GL_MM_ENTRANCE: {
            WARP_ENUMS.GL_MM_ENTRANCE_TO_SM_MAIN: None,
            WARP_ENUMS.GL_MM_ENTRANCE_TO_MM_MAIN: None,
            WARP_ENUMS.GL_MM_ENTRANCE_TO_GL_TTC_CC_PUZZLES: None,
        },
        ROOM_ENUMS.GL_TTC_CC_PUZZLES: {
            WARP_ENUMS.GL_TTC_CC_PUZZLES_TO_GL_MM_ENTRANCE: None,
            WARP_ENUMS.GL_TTC_CC_PUZZLES_TO_GL_CCW_PUZZLE: None,
        },
        ROOM_ENUMS.GL_CCW_PUZZLE: {
            WARP_ENUMS.GL_CCW_PUZZLE_TO_GL_TTC_CC_PUZZLES: None,
            WARP_ENUMS.GL_CCW_PUZZLE_TO_GL_TTC_ENTRANCE: None,
            WARP_ENUMS.GL_CCW_PUZZLE_TO_GL_PIPE_ROOM: None,
            WARP_ENUMS.GL_CCW_PUZZLE_TO_GL_CC_ENTRANCE: None,
            WARP_ENUMS.GL_CCW_PUZZLE_TO_GL_GRUNTY_STATUE: None,
        },
        ROOM_ENUMS.GL_CAULDRON_PIPE: {
            WARP_ENUMS.GL_PIPE_ROOM_TO_GL_CCW_PUZZLE: None,
        },
        ROOM_ENUMS.GL_TTC_ENTRANCE: {
            WARP_ENUMS.GL_PIPE_ROOM_TO_GL_CCW_PUZZLE: None,
        },
        ROOM_ENUMS.GL_GV_ENTRANCE: {
            WARP_ENUMS.GL_GV_ENTRANCE_TO_GV_MAIN: None,
            WARP_ENUMS.GL_GV_ENTRANCE_TO_GL_FP_ENTRANCE: None,
            WARP_ENUMS.GL_GV_ENTRANCE_TO_GL_GRUNTY_STATUE_WITCH_SWITCH: None,
            WARP_ENUMS.GL_GV_ENTRANCE_TO_GL_GRUNTY_STATUE_NOTE_DOOR: None,
        },
        ROOM_ENUMS.GL_FP_ENTRANCE: {
            WARP_ENUMS.GL_FP_ENTRANCE_TO_FP_MAIN: None,
            WARP_ENUMS.GL_FP_ENTRANCE_TO_GL_GV_ENTRANCE: None,
            WARP_ENUMS.GL_FP_ENTRANCE_TO_GL_GV_PUZZLE: None,
            WARP_ENUMS.GL_FP_ENTRANCE_TO_GL_WATER_THREE_SWITCH: None,
        },
        ROOM_ENUMS.GL_CC_ENTRANCE: {
            WARP_ENUMS.GL_CC_ENTRANCE_TO_CC_MAIN: None,
            WARP_ENUMS.GL_CC_ENTRANCE_TO_GL_CCW_PUZZLE: None,
        },
        ROOM_ENUMS.GL_FULL_GRUNTY_STATUE: {
            WARP_ENUMS.GL_GRUNTY_STATUE_TO_GL_CCW_PUZZLE: None,
            WARP_ENUMS.GL_GRUNTY_STATUE_TO_GL_BGS_ENTRANCE: None,
            WARP_ENUMS.GL_GRUNTY_STATUE_TO_GL_GV_ENTRANCE: None,
        },
        ROOM_ENUMS.GL_BGS_ENTRANCE: {
            WARP_ENUMS.GL_BGS_ENTRANCE_TO_BGS_MAIN: None,
        },
        ROOM_ENUMS.GL_GV_PUZZLE: {
            WARP_ENUMS.GL_GV_PUZZLE_TO_GL_FP_ENTRANCE: None,
            WARP_ENUMS.GL_GV_PUZZLE_TO_GL_MMM_ENTRANCE: None,
        },
        ROOM_ENUMS.GL_MMM_ENTRANCE: {
            WARP_ENUMS.GL_MMM_ENTRANCE_TO_GL_GV_PUZZLE: None,
            WARP_ENUMS.GL_MMM_ENTRANCE_TO_GL_SHED: None,
            WARP_ENUMS.GL_MMM_ENTRANCE_TO_MMM_MAIN: None,
        },
        ROOM_ENUMS.GL_640_NOTE_DOOR: {
            WARP_ENUMS.GL_WATER_THREE_SWITCH_TO_GL_FP_ENTRANCE: None,
            WARP_ENUMS.GL_WATER_THREE_SWITCH_TO_GL_RBB_ENTRANCE: None,
            WARP_ENUMS.GL_WATER_THREE_SWITCH_TO_GL_CCW_ENTRANCE_NOTE_DOOR: None,
            WARP_ENUMS.GL_WATER_THREE_SWITCH_TO_GL_CCW_ENTRANCE_TOKEN: None,
        },
        ROOM_ENUMS.GL_RBB_ENTRANCE: {
            WARP_ENUMS.GL_RBB_ENTRANCE_TO_GL_WATER_THREE_SWITCH: None,
            WARP_ENUMS.GL_RBB_ENTRANCE_TO_GL_MMM_PUZZLE: None,
            WARP_ENUMS.GL_RBB_ENTRANCE_TO_GL_RBB_PUZZLE: None,
            WARP_ENUMS.GL_RBB_ENTRANCE_TO_RBB_MAIN: None,
        },
        ROOM_ENUMS.GL_MMM_PUZZLE: {
            WARP_ENUMS.GL_MMM_PUZZLE_TO_GL_RBB_ENTRANCE: None,
        },
        ROOM_ENUMS.GL_CCW_ENTRANCE: {
            WARP_ENUMS.GL_CCW_ENTRANCE_TO_CCW_MAIN: None,
            WARP_ENUMS.GL_CCW_ENTRANCE_TO_GL_PATH_TO_FF: None,
            WARP_ENUMS.GL_CCW_ENTRANCE_TO_GL_WATER_THREE_SWITCH_TOKEN: None,
            WARP_ENUMS.GL_CCW_ENTRANCE_TO_GL_WATER_THREE_SWITCH_NOTE_DOOR: None,
        },
        ROOM_ENUMS.GL_MMM_SHED: {
            WARP_ENUMS.GL_SHED_TO_GL_MMM_ENTRANCE: None,
        },
        ROOM_ENUMS.GL_PATH_TO_FF: {
            WARP_ENUMS.GL_PATH_TO_FF_TO_GL_CCW_ENTRANCE: None,
        },
        ROOM_ENUMS.GL_FURNACE_FUN: {
            WARP_ENUMS.GL_FF_TO_GL_DOOR_OF_GRUNTY: None,
        },
        ROOM_ENUMS.GL_FINAL_ROOM: {
            WARP_ENUMS.GL_DOOR_OF_GRUNTY_TO_GL_FF: None,
            WARP_ENUMS.GL_DOOR_OF_GRUNTY_TO_FINAL_BATTLE: None,
        }
    },
}