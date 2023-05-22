from enum import IntEnum, auto

class HEALTH_ENUMS(IntEnum):
    
    @classmethod
    def get_debug_name(self, health):
        return health.name

    @classmethod
    def get_health_enum(self, health):
        return health.value

    ONE_HEALTH = 1
    TWO_HEALTH = auto()
    THREE_HEALTH = auto()
    FOUR_HEALTH = auto()
    FIVE_HEALTH = auto()
    SIX_HEALTH = auto()
    SEVEN_HEALTH = auto()
    EIGHT_HEALTH = auto()
    DOUBLE_HEALTH = 16

if __name__ == '__main__':
    for health in HEALTH_ENUMS:
        print(HEALTH_ENUMS.get_debug_name(health), HEALTH_ENUMS.get_health_enum(health))