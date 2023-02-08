import sys

sys.path.append(".")
from Automated.Game_Assets.Speeches.Generic_Speech_Class import GENERIC_SPEECH_CLASS

class FURNACE_FUN_SPEECH_CLASS(GENERIC_SPEECH_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        # CONSTANTS 
        self._SPRITE_DICT = {
            0x80: "Question",
            0x81: "Answer1",
            0x82: "Answer2",
            0x83: "Answer3",
        }
        # VARIABLES
        self._speech_dict = {}
        self._header = self._read_byte_list_to_int(0, 5)
        self._create_speech_dict()
        self._file_size = len(self._mmap)

    def _create_speech_dict(self):
        curr_index = 0x6
        for section_count in range(self._read_byte(5)):
            curr_index = self._get_speech_section(curr_index, section_count)
    
    def _remove_section(self, section):
        self._speech_dict.pop(section)
    
    def _recontruct_speech_file(self):
        self._mmap.resize(self._file_size)
        self._write_bytes(0, 5, self._header)
        section_count = 0
        for section in self._speech_dict:
            if(self._speech_dict[section]):
                section_count += 1
        self._write_byte(5, section_count)
        curr_index = 6
        for section in sorted(self._speech_dict):
            if(self._speech_dict[section]):
                self._write_byte(curr_index, self._speech_dict[section]["Sprite"])
                length_val = self._speech_dict[section]["Length"]
                self._write_byte(curr_index + 0x1, length_val)
                self._write_bytes(curr_index + 0x2, length_val, int(self._speech_dict[section]["Line"], 16))
                curr_index += 0x2 + length_val

if __name__ == '__main__':
    # FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/Speeches/"
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    FILE_NAME = "5CABD0"
    from shutil import copy
    copy(FILE_DIR + FILE_NAME + ".bin", FILE_DIR + FILE_NAME + "-Test.bin")
    speech_obj = FURNACE_FUN_SPEECH_CLASS(FILE_DIR, FILE_NAME + "-Test")
    speech_obj._replace_section_by_sprite(0x82, new_line=f"{speech_obj._FONT_DICT['<Squiggly_Font>']}THIS IS A TEST")
    speech_obj._print_speech_dict()
    speech_obj._recontruct_speech_file()