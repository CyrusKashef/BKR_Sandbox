# CONTANTS FOR COLLISION INDICES
UNKNOWN = 0x2
CLAW_SWIPE = 0x4
ROLL_ATTACK = 0x6
JUMPING_ON_THEM = 0x8
RATATAP_RAP = 0xA
BEAK_BARGE = 0xC
BEAK_BUSTER = 0xE
BEAK_BOMB = 0x10
EGG_FIRING = 0x12
WONDERWING = 0x14
CROC_BITE = 0x16
OTHER_CONTACT = 0x18

# CONSTANTS FOR PARAMETERS
MARKER = "MARKER"
ENTITY_NAME = "ENTITY_NAME"
KNOCKBACK = "KNOCKBACK"
ONE_REQUIRED_WEAKNESS = "ONE_REQUIRED_WEAKNESS"
HONEYCOMB_LIMITS = "HONEYCOMB_LIMITS"

# ALLOWED KNOCKBACK PARAMETERS
DEFAULT = "DEFAULT"
NO_KNOCKBACK = [0]
DAMAGES_BK_KNOCKBACK = [x for x in range(0x1, 0x6)]
BOUNCE_OFF_KNOCKBACK = [x for x in range(0x7, 0xC)]
ALL_FORMS_OF_KNOCKBACK = DAMAGES_BK_KNOCKBACK + BOUNCE_OFF_KNOCKBACK

# MARKER DICTS
ENEMY_MARKER_DICT = {
    0: {
        MARKER: 0x012A,
        ENTITY_NAME: "Topper (Training)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE],
        HONEYCOMB_LIMITS: (0, 3),
    },
    1: {
        MARKER: 0x0129,
        ENTITY_NAME: "Bawl (Training)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK],
        HONEYCOMB_LIMITS: (0, 3),
    },
    2: {
        MARKER: 0x0128,
        ENTITY_NAME: "Cauliwobble (Training)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, RATATAP_RAP],
        HONEYCOMB_LIMITS: (0, 3),
    },
    3: {
        MARKER: 0x0135,
        ENTITY_NAME: "Quarrie",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    4: {
        MARKER: 0x01E6,
        ENTITY_NAME: "Topper (Non-Tutorial)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    5: {
        MARKER: 0x01E7,
        ENTITY_NAME: "Bawl (Non-Tutorial)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    6: {
        MARKER: 0x01E8,
        ENTITY_NAME: "Cauliwobble (Non-Tutorial)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    # 7: {
    #     MARKER: 0x01EA,
    #     ENTITY_NAME: "Gruntling (Red)",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 3),
    # },
    # 8: {
    #     MARKER: 0x0295,
    #     ENTITY_NAME: "Gruntling (Blue)",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 3),
    # },
    # 9: {
    #     MARKER: 0x01F1,
    #     ENTITY_NAME: "Gruntling (Black)",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 3),
    # },
    11: {
        MARKER: 0x0005,
        ENTITY_NAME: "Grublin",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    12: {
        MARKER: 0x0004,
        ENTITY_NAME: "Ticker",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    13: {
        MARKER: 0x0003,
        ENTITY_NAME: "Bigbutt (Active)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    16: {
        MARKER: 0x0013,
        ENTITY_NAME: "Snippet/Mutie Snippet",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    17: {
        MARKER: 0x016B,
        ENTITY_NAME: "Snippet/Mutie Snippet (Upside Down)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    18: {
        MARKER: 0x00DD,
        ENTITY_NAME: "Black Snippet",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    19: {
        MARKER: 0x00DE,
        ENTITY_NAME: "Black Snippet (Upside Down)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    20: {
        MARKER: 0x0015,
        ENTITY_NAME: "Yum-Yum",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    21: {
        MARKER: 0x0065,
        ENTITY_NAME: "Shrapnel",
        ONE_REQUIRED_WEAKNESS: [EGG_FIRING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    22: {
        MARKER: 0x0014,
        ENTITY_NAME: "Snacker",
        ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    28: {
        MARKER: 0x0029,
        ENTITY_NAME: "Grille Chompa A",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, RATATAP_RAP, BEAK_BARGE, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    29: {
        MARKER: 0x01CF,
        ENTITY_NAME: "Grille Chompa B",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, RATATAP_RAP, BEAK_BARGE, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    32: {
        MARKER: 0x0069,
        ENTITY_NAME: "Chump",
        ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    33: {
        MARKER: 0x0173,
        ENTITY_NAME: "Chump 2",
        ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    34: {
        MARKER: 0x00C1,
        ENTITY_NAME: "Red Flibbit",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    35: {
        MARKER: 0x00C5,
        ENTITY_NAME: "Yellow Flibbit",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    36: {
        MARKER: 0x00C2,
        ENTITY_NAME: "Buzzbomb",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    # 38: {
    #     MARKER: 0x0287,
    #     ENTITY_NAME: "Sir Slush (Hat?)",
    #     ONE_REQUIRED_WEAKNESS: [BEAK_BUSTER, BEAK_BOMB],
    #     HONEYCOMB_LIMITS: (0, 3),
    # },
    # 41: {
    #     MARKER: 0x0250,
    #     ENTITY_NAME: "Chinker (Large)",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    # },
    # 42: {
    #     MARKER: 0x025F,
    #     ENTITY_NAME: "Chinker (Small)",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 3),
    # },
    43: {
        MARKER: 0x00AD,
        ENTITY_NAME: "Slappa",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    44: {
        MARKER: 0x0253,
        ENTITY_NAME: "Scabby",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    # 45: {
    #     MARKER: 0x0219,
    #     ENTITY_NAME: "Mum-Mum",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 3),
    # },
    # 46: {
    #     MARKER: 0x0298,
    #     ENTITY_NAME: "Mum-Mum Ball",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 47: {
    #     MARKER: 0x0218,
    #     ENTITY_NAME: "Limbo",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 3),
    # },
    # 48: {
    #     MARKER: 0x0099,
    #     ENTITY_NAME: "Tee-Hee (Green)",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 3),
    # },
    # 49: {
    #     MARKER: 0x0296,
    #     ENTITY_NAME: "Purple Tee-Hee",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 3),
    # },
    50: {
        MARKER: 0x0096,
        ENTITY_NAME: "Ripper",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    51: {
        MARKER: 0x0297,
        ENTITY_NAME: "Giant Ripper",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, RATATAP_RAP, BEAK_BARGE, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    52: {
        MARKER: 0x0127,
        ENTITY_NAME: "Nibbly",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    53: {
        MARKER: 0x0254,
        ENTITY_NAME: "Portrait Chompa A",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, RATATAP_RAP, BEAK_BARGE, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    54: {
        MARKER: 0x01D1,
        ENTITY_NAME: "Portrait Chompa",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, RATATAP_RAP, BEAK_BARGE, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    55: {
        MARKER: 0x021A,
        ENTITY_NAME: "Seaman Grublin",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    56: {
        MARKER: 0x00C9,
        ENTITY_NAME: "Flotsam",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    # 57: {
    #     MARKER: 0x01B7,
    #     ENTITY_NAME: "Boom Box",
    #     ONE_REQUIRED_WEAKNESS: [EGG_FIRING],
    #     HONEYCOMB_LIMITS: (0, 3),
    # },
    # 58: {
    #     MARKER: 0x002E,
    #     ENTITY_NAME: "Grimlet",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 59: {
    #     MARKER: 0x01A1,
    #     ENTITY_NAME: "Boss Boom Box (Largest)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 60: {
    #     MARKER: 0x01A2,
    #     ENTITY_NAME: "Boss Boom Box (Large)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 61: {
    #     MARKER: 0x01A3,
    #     ENTITY_NAME: "Boss Boom Box (Medium)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 62: {
    #     MARKER: 0x01A4,
    #     ENTITY_NAME: "Boss Boom Box (Small)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    67: {
        MARKER: 0x01E2,
        ENTITY_NAME: "Grublin Hood",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    68: {
        MARKER: 0x01C5,
        ENTITY_NAME: "Whipcrack",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, RATATAP_RAP, BEAK_BARGE, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    70: {
        MARKER: 0x01B2,
        ENTITY_NAME: "Clucker (Single Attack)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, RATATAP_RAP, BEAK_BARGE, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    71: {
        MARKER: 0x01D0,
        ENTITY_NAME: "Clucker (Multi Attack)",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, RATATAP_RAP, BEAK_BARGE, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 3),
    },
    # 118: {
    #     MARKER: 0x01AE,
    #     ENTITY_NAME: "Zubba (Attacking)",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    119: {
        MARKER: 0x0050,
        ENTITY_NAME: "Beehive",
        ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
        HONEYCOMB_LIMITS: (0, 0),
    },
}

OTHER_MARKER_DICT = {
    # 10: {
    #     MARKER: 0x01E0,
    #     ENTITY_NAME: "Brentilda",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 14: {
    #     MARKER: 0x029E,
    #     ENTITY_NAME: "Bigbutt (Knocked Down)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 15: {
    #     MARKER: 0x0007,
    #     ENTITY_NAME: "Conga",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 23: {
    #     MARKER: 0x00A5,
    #     ENTITY_NAME: "Nipper (Invulnerable)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 24: {
    #     MARKER: 0x016C,
    #     ENTITY_NAME: "Nipper (Vulnerable)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 25: {
    #     MARKER: 0x00A4,
    #     ENTITY_NAME: "Lockup (Slow)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 26: {
    #     MARKER: 0x00F6,
    #     ENTITY_NAME: "Lock Up (Medium)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 27: {
    #     MARKER: 0x00F7,
    #     ENTITY_NAME: "Lock Up (Fast)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 30: {
    #     MARKER: 0x01A6,
    #     ENTITY_NAME: "Beta Vent",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 31: {
    #     MARKER: 0x01A7,
    #     ENTITY_NAME: "Whiplash",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 37: {
    #     MARKER: 0x00B1,
    #     ENTITY_NAME: "Sir Slush (Body)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 39: {
    #     MARKER: 0x0205,
    #     ENTITY_NAME: "Twinklie Muncher",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 40: {
    #     MARKER: 0x0245,
    #     ENTITY_NAME: "Christmas Tree Egg Toll",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 63: {
    #     MARKER: 0x0185,
    #     ENTITY_NAME: "RBB Rear Propeller",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 64: {
    #     MARKER: 0x0191,
    #     ENTITY_NAME: "Engine Room Propeller 1",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 65: {
    #     MARKER: 0x0192,
    #     ENTITY_NAME: "Engine Room Propeller 2",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 66: {
    #     MARKER: 0x0193,
    #     ENTITY_NAME: "Engine Room Propeller 3",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 69: {
    #     MARKER: 0x01F9,
    #     ENTITY_NAME: "Snarebear",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 72: {
    #     MARKER: 0x01B4,
    #     ENTITY_NAME: "Eyrie (Baby)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 73: {
    #     MARKER: 0x000E,
    #     ENTITY_NAME: "Unk",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 74: {
    #     MARKER: 0x01AC,
    #     ENTITY_NAME: "CCW Zubba Entrance Lid",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 75: {
    #     MARKER: 0x0256,
    #     ENTITY_NAME: "Fire FX",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 76: {
    #     MARKER: 0x000C,
    #     ENTITY_NAME: "Orange (Projectile)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 77: {
    #     MARKER: 0x00DB,
    #     ENTITY_NAME: "Little Lockup",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 78: {
    #     MARKER: 0x0028,
    #     ENTITY_NAME: "Clanker Sawblade",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 79: {
    #     MARKER: 0x004A,
    #     ENTITY_NAME: "Clanker's Key",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 80: {
    #     MARKER: 0x006E,
    #     ENTITY_NAME: "BGS Pink Egg (Largest)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 81: {
    #     MARKER: 0x00D7,
    #     ENTITY_NAME: "Pink Egg (Medium)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 82: {
    #     MARKER: 0x00D9,
    #     ENTITY_NAME: "Orange Egg (Smallest)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 83: {
    #     MARKER: 0x00D6,
    #     ENTITY_NAME: "Pink Egg (Large)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 84: {
    #     MARKER: 0x00D8,
    #     ENTITY_NAME: "Orange Egg (Small)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 85: {
    #     MARKER: 0x006D,
    #     ENTITY_NAME: "Tanktup (Legs)",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 86: {
    #     MARKER: 0x019B,
    #     ENTITY_NAME: "Choir Member (Yellow)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 87: {
    #     MARKER: 0x019C,
    #     ENTITY_NAME: "Choir Member (Cyan)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 88: {
    #     MARKER: 0x019D,
    #     ENTITY_NAME: "Choir Member (Blue)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 89: {
    #     MARKER: 0x019E,
    #     ENTITY_NAME: "Choir Member (Red)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 90: {
    #     MARKER: 0x019F,
    #     ENTITY_NAME: "Choir Member (Magenta)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 91: {
    #     MARKER: 0x01A0,
    #     ENTITY_NAME: "Choir Member (Violet)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 92: {
    #     MARKER: 0x00B9,
    #     ENTITY_NAME: "FP Snowman Button",
    #     ONE_REQUIRED_WEAKNESS: [BEAK_BUSTER, BEAK_BOMB, EGG_FIRING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 93: {
    #     MARKER: 0x0124,
    #     ENTITY_NAME: "Boggy (Dying)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 94: {
    #     MARKER: 0x0097,
    #     ENTITY_NAME: "Unknown (Something With Player?)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 95: {
    #     MARKER: 0x0125,
    #     ENTITY_NAME: "FP Boggy Race Red Flag 1",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 96: {
    #     MARKER: 0x0126,
    #     ENTITY_NAME: "FP Boggy Race Red Flag 2",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 97: {
    #     MARKER: 0x01FD,
    #     ENTITY_NAME: "Blue Present (Collectable)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 98: {
    #     MARKER: 0x01FE,
    #     ENTITY_NAME: "Green Present (Collectable)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 99: {
    #     MARKER: 0x01FF,
    #     ENTITY_NAME: "Red Present (Collectable)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 100: {
    #     MARKER: 0x020B,
    #     ENTITY_NAME: "Wozza",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 101: {
    #     MARKER: 0x020F,
    #     ENTITY_NAME: "Wozza In Cave",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 102: {
    #     MARKER: 0x0204,
    #     ENTITY_NAME: "FP Twinklies Box",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 103: {
    #     MARKER: 0x0207,
    #     ENTITY_NAME: "FP Christmas Tree Star",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 104: {
    #     MARKER: 0x0206,
    #     ENTITY_NAME: "FP Christmas Tree Switch",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 105: {
    #     MARKER: 0x00BC,
    #     ENTITY_NAME: "Gobi 1",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 106: {
    #     MARKER: 0x00BE,
    #     ENTITY_NAME: "Gobi Rock",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 107: {
    #     MARKER: 0x00BF,
    #     ENTITY_NAME: "Gobi 2",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 108: {
    #     MARKER: 0x00C3,
    #     ENTITY_NAME: "Gobi 3",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 109: {
    #     MARKER: 0x0252,
    #     ENTITY_NAME: "Loggo",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 110: {
    #     MARKER: 0x0048,
    #     ENTITY_NAME: "Napper",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 111: {
    #     MARKER: 0x0132,
    #     ENTITY_NAME: "CCW Spring Switch",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 112: {
    #     MARKER: 0x0130,
    #     ENTITY_NAME: "CCW Summer Switch",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 113: {
    #     MARKER: 0x012E,
    #     ENTITY_NAME: "CCW Autumn Switch",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 114: {
    #     MARKER: 0x012C,
    #     ENTITY_NAME: "CCW Winter Switch",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 115: {
    #     MARKER: 0x01BF,
    #     ENTITY_NAME: "Gnawty's Boulder",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 116: {
    #     MARKER: 0x01B3,
    #     ENTITY_NAME: "Eyrie's Egg",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 117: {
    #     MARKER: 0x01B0,
    #     ENTITY_NAME: "CCW Beanstalk",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 120: {
    #     MARKER: 0x009A,
    #     ENTITY_NAME: "MMM Barrel Lid",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 121: {
    #     MARKER: 0x009E,
    #     ENTITY_NAME: "MMM Cellar Hatch",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 122: {
    #     MARKER: 0x009D,
    #     ENTITY_NAME: "MMM Mansion Front Door",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 123: {
    #     MARKER: 0x00E7,
    #     ENTITY_NAME: "MMM Dining Room Exit Door",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 124: {
    #     MARKER: 0x009C,
    #     ENTITY_NAME: "MMM Tumblar Shed Door",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 125: {
    #     MARKER: 0x00EA,
    #     ENTITY_NAME: "Lighthouse Door",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 126: {
    #     MARKER: 0x022D,
    #     ENTITY_NAME: "RBB Window 1",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 127: {
    #     MARKER: 0x022E,
    #     ENTITY_NAME: "RBB Window 2",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 128: {
    #     MARKER: 0x0235,
    #     ENTITY_NAME: "RBB Skylights (Shattered Window)",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 129: {
    #     MARKER: 0x0163,
    #     ENTITY_NAME: "GL Wooden Coffin Lid",
    #     ONE_REQUIRED_WEAKNESS: [BEAK_BUSTER],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 130: {
    #     MARKER: 0x0239,
    #     ENTITY_NAME: "CCW Nabnut's Window (Season?)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 131: {
    #     MARKER: 0x0236,
    #     ENTITY_NAME: "CCW Nabnut's Window (Season?)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 132: {
    #     MARKER: 0x0237,
    #     ENTITY_NAME: "CCW Nabnut's Window (Season?)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 133: {
    #     MARKER: 0x0238,
    #     ENTITY_NAME: "CCW Nabnut's Window (Season?)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 134: {
    #     MARKER: 0x0263,
    #     ENTITY_NAME: "CCW Wooden Door (To Whipcrack Room)",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 135: {
    #     MARKER: 0x017D,
    #     ENTITY_NAME: "Iron Gate (No Lock)",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 136: {
    #     MARKER: 0x009F,
    #     ENTITY_NAME: "Locked Gate",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 137: {
    #     MARKER: 0x00A0,
    #     ENTITY_NAME: "MMM Locked Gate (Lock On Right) 1",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 138: {
    #     MARKER: 0x00FF,
    #     ENTITY_NAME: "MMM Locked Gate (Lock On Right) 2",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 139: {
    #     MARKER: 0x0107,
    #     ENTITY_NAME: "RBB Steel Door To Engine Room",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 140: {
    #     MARKER: 0x0108,
    #     ENTITY_NAME: "RBB Captain's Room Wooden Door",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 141: {
    #     MARKER: 0x0109,
    #     ENTITY_NAME: "GL Brick Wall",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 142: {
    #     MARKER: 0x0118,
    #     ENTITY_NAME: "Grate To Level 3 Water Switch",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 143: {
    #     MARKER: 0x0119,
    #     ENTITY_NAME: "Grate Between MMM and RBB Puzzles",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 144: {
    #     MARKER: 0x011A,
    #     ENTITY_NAME: "Grate To RBB Puzzle",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 145: {
    #     MARKER: 0x011E,
    #     ENTITY_NAME: "Unsure (Ice Ball?)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 146: {
    #     MARKER: 0x011F,
    #     ENTITY_NAME: "Rareware Box",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 147: {
    #     MARKER: 0x0121,
    #     ENTITY_NAME: "GL Gruntilda Head Eyeball",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, BEAK_BOMB, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 148: {
    #     MARKER: 0x0123,
    #     ENTITY_NAME: "MMM Window",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, BEAK_BOMB, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 149: {
    #     MARKER: 0x01F2,
    #     ENTITY_NAME: "MMM Short Window",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, BEAK_BOMB, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 150: {
    #     MARKER: 0x01F3,
    #     ENTITY_NAME: "MMM Tall Window",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, BEAK_BOMB, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 151: {
    #     MARKER: 0x0224,
    #     ENTITY_NAME: "GL Yellow Cobweb (Floor)",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, BEAK_BOMB, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 152: {
    #     MARKER: 0x0225,
    #     ENTITY_NAME: "GL Yellow Cobweb (Wall)",
    #     ONE_REQUIRED_WEAKNESS: [JUMPING_ON_THEM, RATATAP_RAP, BEAK_BOMB, EGG_FIRING, WONDERWING],
    #     HONEYCOMB_LIMITS: (0, 0),
    # },
    # 153: {
    #     MARKER: 0x00A2,
    #     ENTITY_NAME: "MMM Church Door",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 154: {
    #     MARKER: 0x01A9,
    #     ENTITY_NAME: "CC Breakable Grates",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 155: {
    #     MARKER: 0x0,
    #     ENTITY_NAME: "RBB 1 Button",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 156: {
    #     MARKER: 0x0195,
    #     ENTITY_NAME: "RBB 2 Button",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 157: {
    #     MARKER: 0x0197,
    #     ENTITY_NAME: "RBB 3 Button",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 158: {
    #     MARKER: 0x002F,
    #     ENTITY_NAME: "RBB Anchor Button",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 159: {
    #     MARKER: 0x0194,
    #     ENTITY_NAME: "RBB Grey Propeller Switch (Slow Fans)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 160: {
    #     MARKER: 0x0186,
    #     ENTITY_NAME: "RBB Green Propeller Switch (Stop Propellers)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 161: {
    #     MARKER: 0x0183,
    #     ENTITY_NAME: "RBB Crane Up Switch Trigger",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 162: {
    #     MARKER: 0x0184,
    #     ENTITY_NAME: "RBB TNT Down Switch Trigger",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 163: {
    #     MARKER: 0x0164,
    #     ENTITY_NAME: "Grunty Eye Switch 1",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 164: {
    #     MARKER: 0x0165,
    #     ENTITY_NAME: "Grunty Eye Switch 2",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 165: {
    #     MARKER: 0x00E4,
    #     ENTITY_NAME: "Banjo & Kazooie (Gameboy/Beer/Sunglasses/Chair)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 166: {
    #     MARKER: 0x00E5,
    #     ENTITY_NAME: "Banjo & Kazooie Gameboy",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 167: {
    #     MARKER: 0x00E6,
    #     ENTITY_NAME: "Banjo & Kazooie Cooking",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 168: {
    #     MARKER: 0x00B2,
    #     ENTITY_NAME: "Snowball",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    # },
    # 169: {
    #     MARKER: 0x01A5,
    #     ENTITY_NAME: "Something King Sandybutt Egg Toll Related?",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 170: {
    #     MARKER: 0x01A6,
    #     ENTITY_NAME: "Beta Vent",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 171: {
    #     MARKER: 0x016D,
    #     ENTITY_NAME: "Cheato 1",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 172: {
    #     MARKER: 0x016E,
    #     ENTITY_NAME: "Cheato 2",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 173: {
    #     MARKER: 0x016F,
    #     ENTITY_NAME: "Cheato 3",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 174: {
    #     MARKER: 0x0170,
    #     ENTITY_NAME: "Blue Egg Refill Pillow",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 175: {
    #     MARKER: 0x0171,
    #     ENTITY_NAME: "Red Feather Refill Pillow",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 176: {
    #     MARKER: 0x0172,
    #     ENTITY_NAME: "Gold Feather Refill Pillow",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 177: {
    #     MARKER: 0x025C,
    #     ENTITY_NAME: "FB Fireblast",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    # },
    # 178: {
    #     MARKER: 0x025D,
    #     ENTITY_NAME: "FB Green Blast (2D)",
    #     ONE_REQUIRED_WEAKNESS: [CLAW_SWIPE, ROLL_ATTACK, JUMPING_ON_THEM, RATATAP_RAP, BEAK_BARGE, BEAK_BUSTER, EGG_FIRING, WONDERWING],
    # },
    # 179: {
    #     MARKER: 0x027A,
    #     ENTITY_NAME: "FB Jinjo Stand",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 180: {
    #     MARKER: 0x027F,
    #     ENTITY_NAME: "FB Jinjonator Stand",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 181: {
    #     MARKER: 0x025E,
    #     ENTITY_NAME: "FB Gruntilda On Broomstick (Default/Phase 1 & 2 Vulnerable)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 182: {
    #     MARKER: 0x0260,
    #     ENTITY_NAME: "FB Gruntilda On Broomstick (Phase 1 Attacking)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 183: {
    #     MARKER: 0x0281,
    #     ENTITY_NAME: "FB Gruntilda On Broomstick (Phase 2 Moving)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 184: {
    #     MARKER: 0x0282,
    #     ENTITY_NAME: "FB Gruntilda On Broomstick (Phase 3 Flying)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 185: {
    #     MARKER: 0x0283,
    #     ENTITY_NAME: "FB Gruntilda On Broomstick (Phase 4/5)",
    #     ONE_REQUIRED_WEAKNESS: [],
    # },
    # 186: {
    #     MARKER: 0x0284,
    #     ENTITY_NAME: "FB Gruntilda's Barrier Spell",
    #     ONE_REQUIRED_WEAKNESS: [],
    # }
}