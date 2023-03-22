import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class TREASURE_TROVE_COVE_DATA_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._CHEAT_INDEX_START = 0xAA0
        self._CHEAT_INDEX_END = 0x12DC
        # Q is unused, X isn't there
        self._SANDCASTLE_TRANSLATION_DICT = {
            0x6E: "A", # n
            0x6B: "B", # k
            0x30: "C", # 0
            0x6C: "D", # l
            0x6A: "E", # j
            0x63: "F", # c
            0x35: "G", # 5
            0x6D: "H", # m
            0x34: "I", # 4
            0x70: "J", # p
            0x38: "K", # 8
            0x62: "L", # b
            0x31: "M", # 1
            0x69: "N", # i
            0x36: "O", # 6
            0x72: "P", # r
            0x39: "R", # 9
            0x32: "S", # 2
            0x64: "T", # d
            0x67: "U", # g
            0x61: "V", # a
            0x37: "W", # 7
            0x68: "X", # h
            0x65: "Y", # e
            0x33: "Z", # 3
        }
        self._SANDCASTLE_REVERSE_TRANSLATION_DICT = {}
        for key in self._SANDCASTLE_TRANSLATION_DICT:
            self._SANDCASTLE_REVERSE_TRANSLATION_DICT[self._SANDCASTLE_TRANSLATION_DICT[key]] = key
        self._cheat_dict = {}
    
    def _obtain_sandcastle_cheats(self):
        cheat_text = ""
        cheat_count = 0
        for curr_index in range(self._CHEAT_INDEX_START, self._CHEAT_INDEX_END):
            curr_index_val = self._mmap[curr_index]
            if((curr_index_val == 0x00) and (cheat_text)):
                self._cheat_dict[cheat_count] = cheat_text
                cheat_count += 1
                cheat_text = ""
            elif(curr_index_val != 0x00):
                cheat_text += self._SANDCASTLE_TRANSLATION_DICT[curr_index_val]
    
    def _edit_sandcastle_cheat(self, count, new_text):
        if(count not in self._cheat_dict):
            print(f"Illegal Cheat Count: {count}")
            raise SystemError(f"Illegal Cheat Count: {count}")
        for char in new_text:
            if((char < "A") or (char > "Z") or (char == "Q")):
                print(f"Illegal Character: {char}")
                raise SystemError(f"Illegal Character: {char}")
        old_cheat_len = len(self._cheat_dict[count])
        new_cheat_len = len(new_text)
        if(len(self._cheat_dict[count]) < len(new_text)):
            raise SystemError("New Cheat Too Long: {new_text}")
        self._cheat_dict[count] = new_text + " " * (old_cheat_len - new_cheat_len)
    
    def _set_sandcastle_cheats(self):
        curr_index = self._CHEAT_INDEX_START
        for cheat_num in self._cheat_dict:
            for curr_char in self._cheat_dict[cheat_num]:
                if(curr_char == " "):
                    self._write_byte(curr_index, 0x00)
                    curr_index += 1
                else:
                    translated_byte = self._SANDCASTLE_REVERSE_TRANSLATION_DICT[curr_char]
                    self._write_byte(curr_index, translated_byte)
                    curr_index += 1
            self._write_byte(curr_index, 0x00)
            curr_index += 1
            while(curr_index % 4 != 0):
                self._write_byte(curr_index, 0x00)
                curr_index += 1
        if(curr_index > self._CHEAT_INDEX_END):
            raise SystemError("Cheat Code Lengths Exceed Previous Length")

if __name__ == '__main__':
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    FILE_NAME = "FB1AEB"
    ttc_data_obj = TREASURE_TROVE_COVE_DATA_CLASS(FILE_DIR, FILE_NAME)
    ttc_data_obj._obtain_sandcastle_cheats()
    for key in ttc_data_obj._cheat_dict:
        print(f"{key}: {ttc_data_obj._cheat_dict[key]}")
    ttc_data_obj._edit_sandcastle_cheat(0, "KAZOOIEBANJO")