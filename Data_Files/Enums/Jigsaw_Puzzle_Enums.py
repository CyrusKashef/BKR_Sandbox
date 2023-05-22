from enum import IntEnum, auto

class JIGSAW_PUZZLE_ENUMS(IntEnum):
    
    @classmethod
    def get_debug_name(self, jigsaw_puzzle):
        return jigsaw_puzzle.name

    @classmethod
    def get_jigsaw_puzzle_enum(self, jigsaw_puzzle):
        return jigsaw_puzzle.value

    JIGSAW_PUZZLE_ONE = auto()
    JIGSAW_PUZZLE_TWO = auto()
    JIGSAW_PUZZLE_THREE = auto()
    JIGSAW_PUZZLE_FOUR = auto()
    JIGSAW_PUZZLE_FIVE = auto()
    JIGSAW_PUZZLE_SIX = auto()
    JIGSAW_PUZZLE_SEVEN = auto()
    JIGSAW_PUZZLE_EIGHT = auto()
    JIGSAW_PUZZLE_NINE = auto()
    JIGSAW_PUZZLE_TEN = auto()

if __name__ == '__main__':
    for jigsaw_puzzle in JIGSAW_PUZZLE_ENUMS:
        print(JIGSAW_PUZZLE_ENUMS.get_debug_name(jigsaw_puzzle), JIGSAW_PUZZLE_ENUMS.get_jigsaw_puzzle_enum(jigsaw_puzzle))