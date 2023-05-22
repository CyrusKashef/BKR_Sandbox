from enum import IntEnum, auto

class NOTE_DOOR_ENUMS(IntEnum):
    
    @classmethod
    def get_debug_name(self, note_door):
        return note_door.name

    @classmethod
    def get_note_door_enum(self, note_door):
        return note_door.value

    NOTE_DOOR_ONE = 0 # 50
    NOTE_DOOR_TWO = auto() # 180
    NOTE_DOOR_THREE = auto() # 260
    NOTE_DOOR_FOUR = auto() # 350
    NOTE_DOOR_FIVE = auto() # 450
    NOTE_DOOR_SIX = auto() # 640
    NOTE_DOOR_SEVEN = auto() # 765
    NOTE_DOOR_EIGHT = auto() # 810
    NOTE_DOOR_NINE = auto() # 828
    NOTE_DOOR_TEN = auto() # 846
    NOTE_DOOR_ELEVEN = auto() # 864
    NOTE_DOOR_TWELVE = auto() # 882

if __name__ == '__main__':
    for note_door in NOTE_DOOR_ENUMS:
        print(NOTE_DOOR_ENUMS.get_debug_name(note_door), NOTE_DOOR_ENUMS.get_note_door_enum(note_door))