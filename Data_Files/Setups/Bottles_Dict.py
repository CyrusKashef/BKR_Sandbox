from Data_Files.Enums.Ability_Enums import ABILITY_ENUMS
from copy import deepcopy

ORIGINAL_SCRIPT_ID = "Original_Script_Id"
OLD_CAMERA = "Old_Camera"
NEW_CAMERA = "New_Camera"
LEARN_TEXT = "Learn_Text"
REFRESHER_TEXT = "Refresher_Text"

BOTTLES_DICT = {
    # ABILITY_ENUMS.INTRO_BOTTLES: {
    #     ORIGINAL_SCRIPT_ID: 0x008C,
    #     OLD_CAMERA: 0x01,
    #     NEW_CAMERA: 0x01,
    #     LEARN_TEXT: 0xDF3,
    #     REFRESHER_TEXT: 0xE08,
    # },
    ABILITY_ENUMS.CAMERA_CONTROL: {
        ORIGINAL_SCRIPT_ID: 0x010C,
        OLD_CAMERA: 0x03,
        NEW_CAMERA: 0x6F,
        LEARN_TEXT: 0xDF4,
        REFRESHER_TEXT: 0xDF5,
    },
    ABILITY_ENUMS.DIVE: {
        ORIGINAL_SCRIPT_ID: 0x018C,
        OLD_CAMERA: 0x05,
        NEW_CAMERA: 0x6E,
        LEARN_TEXT: 0xDFB,
        REFRESHER_TEXT: 0xDFE,
    },
    ABILITY_ENUMS.RAT_A_TAP_RAP: {
        ORIGINAL_SCRIPT_ID: 0x020C,
        OLD_CAMERA: 0x06,
        NEW_CAMERA: 0x6D,
        LEARN_TEXT: 0xFFFF,
        REFRESHER_TEXT: 0xE00,
    },
    ABILITY_ENUMS.BEAK_BARGE: {
        ORIGINAL_SCRIPT_ID: 0x028C,
        OLD_CAMERA: 0x08,
        NEW_CAMERA: 0x6C,
        LEARN_TEXT: 0xE04,
        REFRESHER_TEXT: 0xE06,
    },
    ABILITY_ENUMS.FLAP_FLIP: {
        ORIGINAL_SCRIPT_ID: 0x030C,
        OLD_CAMERA: 0x04,
        NEW_CAMERA: 0x6B,
        LEARN_TEXT: 0xFFFF,
        REFRESHER_TEXT: 0xDFA,
    },
    ABILITY_ENUMS.CLIMB: {
        ORIGINAL_SCRIPT_ID: 0x038C,
        OLD_CAMERA: 0x07,
        NEW_CAMERA: 0x6A,
        LEARN_TEXT: 0xE01,
        REFRESHER_TEXT: 0xE03,
    },
    ABILITY_ENUMS.TOP_OF_SM_BOTTLES: {
        ORIGINAL_SCRIPT_ID: 0x040C,
        OLD_CAMERA: 0x11,
        NEW_CAMERA: 0x11,
        LEARN_TEXT: 0xE10,
        REFRESHER_TEXT: 0xE11,
    },
    ABILITY_ENUMS.BEAK_BOMB: {
        ORIGINAL_SCRIPT_ID: 0x048C,
        OLD_CAMERA: 0x0F,
        NEW_CAMERA: 0x69,
        LEARN_TEXT: 0xC23,
        REFRESHER_TEXT: 0xC24,
    },
    ABILITY_ENUMS.EGG_FIRING: {
        ORIGINAL_SCRIPT_ID: 0x050C,
        OLD_CAMERA: 0x16,
        NEW_CAMERA: 0x68,
        LEARN_TEXT: 0xB47,
        REFRESHER_TEXT: 0xB4B,
    },
    ABILITY_ENUMS.BEAK_BUSTER: {
        ORIGINAL_SCRIPT_ID: 0x058C,
        OLD_CAMERA: 0x17,
        NEW_CAMERA: 0x67,
        LEARN_TEXT: 0xB48,
        REFRESHER_TEXT: 0xB4C,
    },
    ABILITY_ENUMS.TALON_TROT: {
        ORIGINAL_SCRIPT_ID: 0x060C,
        OLD_CAMERA: 0x18,
        NEW_CAMERA: 0x66,
        LEARN_TEXT: 0xB49,
        REFRESHER_TEXT: 0xB4A,
    },
    ABILITY_ENUMS.SHOCK_SPRING_JUMP: {
        ORIGINAL_SCRIPT_ID: 0x068C,
        OLD_CAMERA: 0x0C,
        NEW_CAMERA: 0x65,
        LEARN_TEXT: 0xA1F,
        REFRESHER_TEXT: 0xA23,
    },
    ABILITY_ENUMS.FLIGHT: {
        ORIGINAL_SCRIPT_ID: 0x070C,
        OLD_CAMERA: 0x0D,
        NEW_CAMERA: 0x64,
        LEARN_TEXT: 0xA20,
        REFRESHER_TEXT: 0xA22,
    },
    ABILITY_ENUMS.WONDERWING: {
        ORIGINAL_SCRIPT_ID: 0x078C,
        OLD_CAMERA: 0x01,
        NEW_CAMERA: 0x63,
        LEARN_TEXT: 0xD35,
        REFRESHER_TEXT: 0xD36,
    },
    ABILITY_ENUMS.STILT_STRIDE: {
        ORIGINAL_SCRIPT_ID: 0x080C,
        OLD_CAMERA: 0x10,
        NEW_CAMERA: 0x62,
        LEARN_TEXT: 0xC88,
        REFRESHER_TEXT: 0xC89,
    },
    ABILITY_ENUMS.TURBO_TALON_TROT: {
        ORIGINAL_SCRIPT_ID: 0x088C,
        OLD_CAMERA: 0x19,
        NEW_CAMERA: 0x61,
        LEARN_TEXT: 0xA84,
        REFRESHER_TEXT: 0xA85,
    },
    ABILITY_ENUMS.OPEN_NOTE_DOORS: {
        ORIGINAL_SCRIPT_ID: 0x090C,
        OLD_CAMERA: 0x0E,
        NEW_CAMERA: 0x60,
        LEARN_TEXT: 0xF64,
        REFRESHER_TEXT: 0xF65,
    },
}

SEPARATED_BOTTLES_DICT = deepcopy(BOTTLES_DICT)

SEPARATED_BOTTLES_DICT[ABILITY_ENUMS.CLAW_SWIPE] = {
        ORIGINAL_SCRIPT_ID: 0x020C,
        OLD_CAMERA: 0x06,
        NEW_CAMERA: 0x5F,
        LEARN_TEXT: 0xDFF,
        REFRESHER_TEXT: 0xE00,
    }

SEPARATED_BOTTLES_DICT[ABILITY_ENUMS.ROLL_ATTACK] = {
        ORIGINAL_SCRIPT_ID: 0x020C,
        OLD_CAMERA: 0x06,
        NEW_CAMERA: 0x5E,
        LEARN_TEXT: 0xE15,
        REFRESHER_TEXT: 0xE00,
    }

SEPARATED_BOTTLES_DICT[ABILITY_ENUMS.RAT_A_TAP_RAP] = {
        ORIGINAL_SCRIPT_ID: 0x020C,
        OLD_CAMERA: 0x06,
        NEW_CAMERA: 0x5D,
        LEARN_TEXT: 0xE17,
        REFRESHER_TEXT: 0xE00,
    }

SEPARATED_BOTTLES_DICT[ABILITY_ENUMS.HIGH_JUMP] = {
        ORIGINAL_SCRIPT_ID: 0x030C,
        OLD_CAMERA: 0x04,
        NEW_CAMERA: 0x5B,
        LEARN_TEXT: 0xDF6,
        REFRESHER_TEXT: 0xDFA,
    }

SEPARATED_BOTTLES_DICT[ABILITY_ENUMS.FEATHERY_FLAP] = {
        ORIGINAL_SCRIPT_ID: 0x030C,
        OLD_CAMERA: 0x04,
        NEW_CAMERA: 0x5A,
        LEARN_TEXT: 0xDF7,
        REFRESHER_TEXT: 0xDFA,
    }

SEPARATED_BOTTLES_DICT[ABILITY_ENUMS.FLAP_FLIP] = {
        ORIGINAL_SCRIPT_ID: 0x030C,
        OLD_CAMERA: 0x04,
        NEW_CAMERA: 0x59,
        LEARN_TEXT: 0xDF8,
        REFRESHER_TEXT: 0xDFA,
    }