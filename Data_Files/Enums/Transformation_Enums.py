from enum import IntEnum, auto

class TRANSFORMATION_ENUMS(IntEnum):
    
    @classmethod
    def get_debug_name(self, transformation):
        return transformation.name

    @classmethod
    def get_transformation_enum(self, transformation):
        return transformation.value

    NO_TRANSFORM = 1
    TERMITE_BK = auto()
    CROCODILE_BK = auto()
    WALRUS_BK = auto()
    PUMPKIN_BK = auto()
    BEE_BK = auto()
    WISHYWASHY = auto()

if __name__ == '__main__':
    for transformation in TRANSFORMATION_ENUMS:
        print(TRANSFORMATION_ENUMS.get_debug_name(transformation), TRANSFORMATION_ENUMS.get_transformation_enum(transformation))