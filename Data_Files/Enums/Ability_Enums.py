from enum import IntEnum, auto

class ABILITY_ENUMS(IntEnum):
    
    @classmethod
    def get_debug_name(self, ability):
        return ability.name

    @classmethod
    def get_ability_enum(self, ability):
        return ability.value

    BEAK_BARGE = 0
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

    TOP_OF_SM_BOTTLES = 0xFF

if __name__ == '__main__':
    for ability in ABILITY_ENUMS:
        print(ABILITY_ENUMS.get_debug_name(ability), ABILITY_ENUMS.get_ability_enum(ability))