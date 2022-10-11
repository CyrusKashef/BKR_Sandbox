import sys
from textwrap import wrap

sys.path.append(".")
from Automated.Game_Assets.Speeches.Speech_Class import SPEECH_CLASS
from Automated.Game_Assets.Speeches.Speech_Dicts import FONT_DICT

class FURNACE_FUN_SPEECH_CLASS(SPEECH_CLASS):
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

    def _get_speech_section(self, curr_index, section_count):
        sprite_val = self._read_byte(curr_index)
        length_val = self._read_byte(curr_index + 0x1)
        line_val = self._read_byte_list_to_hex_str(curr_index + 0x2, length_val)
        self._speech_dict[section_count] = {
            "Sprite": sprite_val,
            "Length": length_val,
            "Line": line_val,
        }
        curr_index += 0x2 + length_val
        return curr_index

    def _create_speech_dict(self):
        curr_index = 0x6
        for section_count in range(self._read_byte(5)):
            curr_index = self._get_speech_section(curr_index, section_count)
    
    def _translate_section_to_str(self, section):
        translation = ""
        for byte_str in wrap(self._speech_dict[section]["Line"], 2):
            translation += chr(int(byte_str, 16))
        for special_font in FONT_DICT:
            translation = translation.replace(FONT_DICT[special_font], special_font)
        return translation
    
    def _translate_str_to_byte_str(self, new_string):
        byte_str = ""
        for char in new_string:
            byte_str += self._int_to_hex_str(ord(char), 2)
        return byte_str + "00"

    def _print_speech_dict(self):
        for section in self._speech_dict:
            print(f"Section: {section}")
            sprite_val = self._speech_dict[section]["Sprite"]
            translation = self._translate_section_to_str(section)
            print(f"{self._SPRITE_DICT[sprite_val]}: {translation}\n")

    def _replace_section(self, section, new_sprite=None, new_line=None):
        if(new_sprite):
            self._speech_dict[section]["Sprite"] = new_sprite
        if(new_line):
            byte_str = self._translate_str_to_byte_str(new_line)
            line_length = len(byte_str) // 2
            self._file_size += line_length - self._speech_dict[section]["Length"]
            self._speech_dict[section]["Length"] = line_length
            self._speech_dict[section]["Line"] = byte_str

    def _replace_section_by_sprite(self, old_sprite, new_sprite=None, new_line=None):
        for section in self._speech_dict:
            if(self._speech_dict[section]["Sprite"] == old_sprite):
                if(new_sprite):
                    self._speech_dict[section]["Sprite"] = new_sprite
                if(new_line):
                    byte_str = self._translate_str_to_byte_str(new_line)
                    line_length = len(byte_str) // 2
                    self._file_size += line_length - self._speech_dict[section]["Length"]
                    self._speech_dict[section]["Length"] = line_length
                    self._speech_dict[section]["Line"] = byte_str
    
    def _remove_section(self, section):
        self._speech_dict.pop(section)
    
    def _import_speech_dict(self, speech_dict):
        self._speech_dict = speech_dict
    
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
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/Speeches/"
    FILE_NAME = "5D7568"
    from shutil import copy
    copy(FILE_DIR + FILE_NAME + ".bin", FILE_DIR + FILE_NAME + "-Test.bin")
    speech_obj = FURNACE_FUN_SPEECH_CLASS(FILE_DIR, FILE_NAME + "-Test")
    speech_obj._replace_section_by_sprite(0x82, new_line=f"{FONT_DICT['<Squiggly_Font>']}THIS IS A TEST")
    speech_obj._print_speech_dict()
    speech_obj._recontruct_speech_file()