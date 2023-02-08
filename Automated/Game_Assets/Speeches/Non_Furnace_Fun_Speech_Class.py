import sys

sys.path.append(".")
from Automated.Game_Assets.Speeches.Generic_Speech_Class import GENERIC_SPEECH_CLASS

class NON_FURNACE_FUN_SPEECH_CLASS(GENERIC_SPEECH_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        # CONSTANTS 
        self._SPRITE_DICT = {
            # Special?
            0x01: "Mr Vile Waiting For User Input A/B",
            0x02: "Check For Health Refill & Tutorial Waiting For User Input A/B",
            0x03: "Boggy & Third Cheat Waiting For User Input A/B",
            0x04: "Typically End Of Top/Bottom Section",
            0x06: "Typically Transition To Top/Bottom Screen",
            0x07: "Unknown (Pause Period?)",
            0x08: "Picks For Brentilda Hints/Picked Up Present Sprite/Cheato Cheat",
            0x09: "Grabs Note Count/Jiggy Count",
            # Sprites
            0x80: "Banjo",
            0x81: "Kazooie", # Verify?
            0x82: "Kazooie", # Verify?
            0x83: "Bottles",
            0x84: "Mumbo",
            0x85: "Chimpy",
            0x86: "Conga", # Verify?
            0x87: "Blubber",
            0x88: "Nipper",
            0x89: "Clanker",
            0x8A: "Mutie Snippet",
            0x8B: "Mr Vile",
            0x8C: "Choir Member",
            0x8D: "Tanktup",
            0x8E: "Yellow Flibbit",
            0x8F: "Trunker",
            0x90: "Rubee",
            0x91: "Gobi",
            0x92: "Grabba",
            0x93: "Napper",
            0x94: "Yellow Jinjo",
            0x95: "Green Jinjo",
            0x96: "Blue Jinjo",
            0x97: "Pink Jinjo",
            0x98: "Orange Jinjo",
            0x99: "Note",
            0x9A: "Mumbo Token",
            0x9A: "Orange",
            0x9B: "Blue Egg",
            0x9C: "Red Feather",
            0x9D: "Gold Feather",
            0x9E: "Conga",
            0x9F: "Blubber's Gold",
            0xA0: "Beehive", # Verify?
            0xA1: "Empty Honeycomb",
            0xA2: "Extra Life",
            0xA3: "Jiggy",
            0xA4: "Beehive",
            0xA5: "Wading Boots",
            0xA6: "Turbo Trainers",
            0xA7: "BGS Piranha",
            0xA8: "Ticker",
            0xA9: "Ju-Ju",
            0xAA: "Yum-Yum",
            0xAB: "Little Lockup",
            0xAC: "Leaky",
            0xAD: "Gloop",
            0xAE: "Tiptup",
            0xAF: "Snacker",
            0xB0: "Jinxy",
            0xB1: "GV Sand Eel",
            0xB2: "Snorkel",
            0xB3: "Ancient Ones",
            0xB4: "Croctus",
            0xB5: "Gruntilda", # Verify?
            0xB6: "Tooty", # FF Cutscene Before Staff Credits?
            0xB7: "Boggy",
            0xB8: "Wozza",
            0xB9: "Motzand",
            0xBA: "Tumblar",
            0xBB: "Mum-Mum",
            0xBC: "Present", # Dunno Which Color
            0xBD: "Caterpillar",
            0xBE: "FP Ice Water",
            0xBF: "Twinklie",
            0xC0: "Twinklie Muncher",
            0xC1: "Gnawty",
            0xC2: "Boss Boom Box",
            0xC3: "Zubba",
            0xC4: "Nabnut",
            0xC5: "Boggy's Kids",
            0xC6: "Baby Eyrie",
            0xC7: "Baby Eyrie",
            0xC8: "Baby Eyrie",
            0xC9: "Adult Eyrie",
            0xCA: "Cauldron",
            0xCB: "Brentilda",
            0xCC: "Tooty",
            0xCD: "Black Snippet",
            0xCE: "Loggo",
            0xCF: "Cheato",
            0xD0: "Present", # Dunno Which Color
            0xD1: "Present", # Dunno Which Color
            0xD2: "Klungo",
            0xD3: "Sexy Grunty",
            0xD4: "Ugly Tooty",
            0xD5: "Banjo", # FF Cutscene After Staff Credits?
            0xD6: "Kazooie", # FF Cutscene After Staff Credits?
            0xD7: "Tooty", # FF Staff Credits?
            0xD8: "Dingpot",
            0xD9: "Mr Vile", # Says You Cheated
            0xDA: "Gruntilda", # Finale Credits?
            0xDB: "Lockup",
        }
        # VARIABLES
        self._speech_dict = {}
        self._header = self._read_byte_list_to_int(0, 3)
        self._create_speech_dict()
        self._file_size = len(self._mmap)
    
    def _create_speech_dict(self):
        curr_index = 0x4
        self._num_of_bottom_speeches = self._read_byte(3)
        for section_count in range(self._num_of_bottom_speeches):
            curr_index = self._get_speech_section(curr_index, section_count)
        self._num_of_top_speeches = self._read_byte(curr_index)
        curr_index += 1
        for section_count in range(self._num_of_bottom_speeches, self._num_of_bottom_speeches + self._num_of_top_speeches):
            curr_index = self._get_speech_section(curr_index, section_count)
    
    def _remove_section(self, section):
        self._speech_dict.pop(section)
        if(section < self._num_of_bottom_speeches):
            self._num_of_bottom_speeches -= 1
        else:
            self._num_of_top_speeches -= 1

    def _recontruct_speech_file(self):
        self._mmap.resize(self._file_size)
        self._write_bytes(0, 3, self._header)
        self._write_byte(3, self._num_of_bottom_speeches)
        curr_index = 0x4
        for section in sorted(self._speech_dict)[:self._num_of_bottom_speeches]:
            self._write_byte(curr_index, self._speech_dict[section]["Sprite"])
            length_val = self._speech_dict[section]["Length"]
            self._write_byte(curr_index + 0x1, length_val)
            self._write_bytes(curr_index + 0x2, length_val, int(self._speech_dict[section]["Line"], 16))
            curr_index += 0x2 + length_val
        self._write_byte(curr_index, self._num_of_top_speeches)
        curr_index += 1
        for section in sorted(self._speech_dict)[self._num_of_bottom_speeches:]:
            self._write_byte(curr_index, self._speech_dict[section]["Sprite"])
            length_val = self._speech_dict[section]["Length"]
            self._write_byte(curr_index + 0x1, length_val)
            self._write_bytes(curr_index + 0x2, length_val, int(self._speech_dict[section]["Line"], 16))
            curr_index += 0x2 + length_val

if __name__ == '__main__':
    # FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/Speeches/"
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    FILE_NAME = "5CDB50"
    from shutil import copy
    copy(FILE_DIR + FILE_NAME + ".bin", FILE_DIR + FILE_NAME + "-Test.bin")
    speech_obj = NON_FURNACE_FUN_SPEECH_CLASS(FILE_DIR, FILE_NAME + "-Test")
    speech_obj._print_speech_dict()
    # speech_obj._recontruct_speech_file()