# CONTANTS FOR COLLISION INDICES
COMMON = 0x2
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

BANJO_SOULIE_MARKERS = {
	# 0x0000: { # MARKER NAME
	# 	  COMMON:          [],
    #     CLAW_SWIPE:      [],
    #     ROLL_ATTACK:     [],
    #     JUMPING_ON_THEM: [],
    #     RATATAP_RAP:     [],
    #     BEAK_BARGE:      [],
    #     BEAK_BUSTER:     [],
    #     BEAK_BOMB:       [],
    #     EGG_FIRING:      [],
    #     WONDERWING:      [],
    #     CROC_BITE:       [],
    #     OTHER_CONTACT:   [],
	# },
	0xD598: { # Topper (Non-Tutorial)
		COMMON:          [0, 0, 0, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        BEAK_BARGE:      [8, 0, 2, 0, 0, 0],
        BEAK_BUSTER:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 0, 0, 0, 1, 0],
	},
	0xD5B2: { # Bawl (Non-Tutorial)
		COMMON:          [0, 0, 0, 0, 0, 0],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        BEAK_BARGE:      [8, 0, 2, 0, 0, 0],
        BEAK_BUSTER:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 0, 0, 0, 1, 0],
	},
    0xD5CC: { # Cauliwobble (Non-Tutorial)
		COMMON:          [0, 0, 0, 0, 0, 0],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        BEAK_BARGE:      [8, 0, 2, 0, 0, 0],
        BEAK_BUSTER:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 0, 0, 0, 1, 0],
    },
    0xD5E6: { # Gruntling (Red)
		COMMON:          [0, 0, 0, 0, 0, 0],
    },
    0xD600: { # Gruntling (Blue)
		COMMON:          [0, 0, 0, 0, 0, 0],
    },
    0xD61A: { # Gruntling (Black)
		COMMON:          [0, 0, 0, 0, 0, 0],
    },
    0xD64E: { # Grublin
		COMMON:          [0, 0, 0, 0, 0, 2],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 2, 3, 0, 3, 0],
    },
    0xD668: { # Ticker
		COMMON:          [0, 0, 0, 0, 0, 3],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        JUMPING_ON_THEM: [0, 2, 3, 0, 1, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 2, 3, 0, 3, 0],
    },
    0xD6D0: { # Snippet/Mutie Snippet
		COMMON:          [0, 0, 0, 0, 0, 2],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        JUMPING_ON_THEM: [7, 1, 3, 0, 1, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 0, 0, 0, 1, 0],
    },
    0xD6EA: { # Snippet/Mutie Snippet (Upside Down)
		COMMON:          [0, 0, 0, 0, 0, 1],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        JUMPING_ON_THEM: [0, 2, 2, 0, 1, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        BEAK_BARGE:      [0, 2, 2, 0, 1, 0],
        EGG_FIRING:      [0, 0, 0, 0, 1, 0],
    },
    0xD704: { # Black Snippet
		COMMON:          [0, 0, 0, 0, 0, 2],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        JUMPING_ON_THEM: [7, 1, 3, 0, 3, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 0, 0, 0, 1, 0],
    },
    0xD71E: { # Black Snippet (Upside Down)
		COMMON:          [0, 0, 0, 0, 0, 1],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        JUMPING_ON_THEM: [0, 2, 2, 0, 3, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        BEAK_BARGE:      [0, 2, 2, 0, 3, 0],
        EGG_FIRING:      [0, 0, 0, 0, 1, 0],
    },
    0xD738: { # Yum-Yum
		COMMON:          [0, 0, 0, 0, 0, 2],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        BEAK_BARGE:      [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 0, 0, 0, 1, 0],
    },
    0xD752: { # Shrapnel
        EGG_FIRING:      [0, 2, 2, 0, 3, 3],
    },
    0xD76C: { # Snacker
		COMMON:          [0, 0, 0, 0, 0, 0],
    },
    0xD808:  { # Grille Chompa A
		COMMON:          [0, 0, 0, 0, 0, 1],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
    },
    0xD822:  { # Grille Chompa B
		COMMON:          [0, 0, 0, 0, 0, 1],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
    },
    0xD856: { # Whiplash
    },
    0xD870: { # Chump 1 (Lair vs RBB?)
		COMMON:          [0, 0, 0, 0, 0, 0],
    },
    0xD88A: { # Chump 2 (Lair vs RBB?)
		COMMON:          [0, 0, 0, 0, 0, 0],
    },
    0xD8A4: { # Red Flibbit
        CLAW_SWIPE:      [0, 2, 4, 0, 2, 2],
        ROLL_ATTACK:     [0, 2, 3, 0, 1, 2],
        RATATAP_RAP:     [0, 2, 3, 0, 1, 2],
        BEAK_BARGE:      [0, 2, 4, 0, 1, 2],
        BEAK_BUSTER:     [0, 2, 4, 0, 1, 2],
        EGG_FIRING:      [0, 2, 3, 0, 2, 2],
        WONDERWING:      [0, 2, 4, 0, 1, 2],
        CROC_BITE:       [0, 2, 3, 0, 1, 3],
    },
    0xD8BE: { # Yellow Flibbit
        CLAW_SWIPE:      [0, 2, 4, 0, 3, 0],
        ROLL_ATTACK:     [0, 2, 3, 0, 2, 0],
        RATATAP_RAP:     [0, 2, 3, 0, 2, 0],
        BEAK_BARGE:      [0, 2, 4, 0, 2, 0],
        BEAK_BUSTER:     [0, 2, 4, 0, 2, 0],
        EGG_FIRING:      [0, 2, 3, 0, 3, 0],
        WONDERWING:      [0, 2, 4, 0, 1, 0],
        CROC_BITE:       [0, 2, 3, 0, 1, 0],
    },
    0xD8D8: { # Buzzbomb
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        JUMPING_ON_THEM: [0, 2, 3, 0, 1, 0],
        RATATAP_RAP:     [0, 2, 0, 0, 1, 2],
        BEAK_BARGE:      [8, 0, 2, 0, 0, 0],
        BEAK_BUSTER:     [0, 2, 0, 0, 1, 2],
        EGG_FIRING:      [0, 2, 0, 0, 1, 2],
        WONDERWING:      [0, 2, 0, 0, 1, 2],
        CROC_BITE:       [0, 2, 0, 0, 1, 3],
    },
    0xD8F2: { # Sir Slush (Body)
    },
    0xD90C: { # Sir Slush (Hat)
		COMMON:          [0, 0, 0, 0, 0, 1],
    },
    0xD926: { # Twinklie Muncher
        RATATAP_RAP:     [0, 0, 0, 0, 0, 0],
        BEAK_BARGE:      [0, 0, 0, 0, 0, 0],
        EGG_FIRING:      [0, 1, 0, 0, 3, 0],
    },
    0xD95A: { # Chinker (Large)
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
    },
    0xD974: { # Chinker (Small)
		COMMON:          [0, 0, 0, 0, 0, 1],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
    },
    0xD98E: { # Slappa
		COMMON:          [0, 0, 0, 0, 0, 3],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        BEAK_BARGE:      [8, 0, 2, 0, 0, 0],
    },
    0xD9A8: { # Scabby
		COMMON:          [0, 0, 0, 0, 0, 2],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        JUMPING_ON_THEM: [0, 2, 3, 0, 1, 0],
        RATATAP_RAP:     [0, 2, 0, 0, 1, 0],
        BEAK_BARGE:      [8, 0, 2, 0, 0, 0],
        BEAK_BUSTER:     [0, 2, 0, 0, 1, 0],
        EGG_FIRING:      [0, 2, 0, 0, 1, 0],
        WONDERWING:      [0, 2, 0, 0, 1, 0],
    },
    0xD9C2: { # Mum-Mum
		COMMON:          [0, 0, 0, 0, 0, 2],
    },
    # 0xD9DC: { # Mum-Mum Ball
    # },
    0xD9F6: { # Limbo
		COMMON:          [0, 0, 0, 0, 0, 2],
    },
    0xDA10: { # Tee-Hee (Green)
		COMMON:          [0, 0, 0, 0, 0, 2],
    },
    0xDA2A: { # Tee-Hee (Purple)
    },
    0xDA44: { # Ripper
		COMMON:          [0, 0, 0, 0, 0, 2],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        BEAK_BUSTER:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 0, 0, 0, 1, 0],
    },
    0xDA5E: { # Giant Ripper
		COMMON:          [0, 0, 0, 0, 0, 2],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        BEAK_BUSTER:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 0, 0, 0, 1, 0],
    },
    0xDA78: { # Nibbly
		COMMON:          [0, 0, 0, 0, 0, 1],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        JUMPING_ON_THEM: [0, 2, 3, 0, 1, 0],
        RATATAP_RAP:     [0, 2, 0, 0, 1, 0],
        BEAK_BARGE:      [8, 0, 2, 0, 0, 0],
        BEAK_BUSTER:     [0, 2, 0, 0, 1, 0],
        EGG_FIRING:      [0, 2, 0, 0, 1, 0],
        WONDERWING:      [0, 2, 0, 0, 1, 0],
    },
    0xDA92: { # Portrait Chompa A
		COMMON:          [0, 0, 0, 0, 0, 1],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
    },
    0xDAAC: { # Portrait Chompa B
		COMMON:          [0, 0, 0, 0, 0, 1],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
    },
    0xDAC6: { # Seaman Grublin
		COMMON:          [0, 0, 0, 0, 0, 2],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 2, 3, 0, 4, 0],
    },
    0xDAE0: { # Flotsam
		COMMON:          [0, 0, 0, 0, 0, 1],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        JUMPING_ON_THEM: [8, 0, 2, 0, 0, 0],
    },
    # 0xDAFA: { # Boom Box
    # },
    # 0xDB14: { # Grimlet
    # },
    # 0xDB2E: { # Boss Boom Box (Largest)
    # },
    # 0xDB48: { # Boss Boom Box (Large)
    # },
    # 0xDB62: { # Boss Boom Box (Medium)
    # },
    # 0xDB7C: { # Boss Boom Box (Small)
    # },
    0xDBFE: { # Grublin Hood
		COMMON:          [0, 0, 0, 0, 0, 1],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
        RATATAP_RAP:     [8, 0, 2, 0, 0, 0],
        EGG_FIRING:      [0, 2, 3, 0, 3, 0],
    },
    0xDC18: { # Whipcrack
		COMMON:          [0, 0, 0, 0, 0, 0],
    },
    0xDC4C: { # Clucker (Single Attack)
		COMMON:          [0, 0, 0, 0, 0, 1],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
    },
    0xDC66: { # Clucker (Multi Attack)
		COMMON:          [0, 0, 0, 0, 0, 1],
        CLAW_SWIPE:      [8, 0, 2, 0, 0, 0],
        ROLL_ATTACK:     [8, 0, 2, 0, 0, 0],
    },
    # 0xE12C: { # Zubba (Attacking)
    # },
    0xE146: { # Beehive
		COMMON:          [0, 0, 0, 0, 0, 0],
    },
    0xE640: {
		COMMON:          [0, 0, 0, 0, 0, 0],
    },
    # 0xE792: { # FB Gruntilda On Broomstick (Default/Phase 1 & 2 Vulnerable)
    # },
    # 0xE7AC: { # FB Gruntilda On Broomstick (Phase 1 Attacking)
    # },
    # 0xE7C6: { # FB Gruntilda On Broomstick (Phase 2 Moving)
    # },
    # 0xE7E0: { # FB Gruntilda On Broomstick (Phase 3 Flying)
    # },
    # 0xE7FA: { # FB Gruntilda On Broomstick (Phase 4/5)
    # },
    # 0xE814: { # FB Gruntilda's Barrier Spell
    # },
}