from enum import IntEnum, auto, unique

@unique
class WORLD_ENUMS(IntEnum):
    
    @classmethod
    def get_debug_name(self, curr_world):
        return curr_world.name

    @classmethod
    def get_world_enum(self, curr_world):
        return curr_world.value[0]
    
    MUMBOS_MOUNTAIN = 0x1
    TREASURE_TROVE_COVE = auto()
    CLANKERS_CAVERN = auto()
    BUBBLEGLOOP_SWAMP = auto()
    FREEZEEZY_PEAK = auto()
    GRUNTILDAS_LAIR = auto()
    GOBIS_VALLEY = auto()
    CLICK_CLOCK_WOOD = auto()
    RUSTY_BUCKET_BAY = auto()
    MAD_MONSTER_MANSION = auto()
    SPIRAL_MOUNTAIN = auto()
    FINAL_BATTLE = auto()
    CUTSCENE = auto()