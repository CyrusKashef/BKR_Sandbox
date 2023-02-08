import sys
from textwrap import wrap

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class GENERIC_SPEECH_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._FONT_DICT = {
            "<Squiggly_Font>": "ýl",
            "<Shaky_Font>": "ýh",
        }
        self._file_type = self._determine_speech_type()
        # VARIABLES
        self._speech_dict = {}
        self._header = None
        self._create_speech_dict()
        self._file_size = len(self._mmap)

    def _determine_speech_type(self):
        # Start with 01 03 00 05 00 or 01 01 02 05 00
        if(self._read_byte_list_to_int(0, 5) in [0x0103000500, 0x0101020500]):
            self._file_type = "Furnace Fun"
        # Start with 01 03 00
        elif(self._read_byte_list_to_int(0, 3) == 0x010300):
            self._file_type = "Other"
        else:
            print(f"Unknown Speech File Type Error")
            exit(0)

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
    
    def _translate_section_to_str(self, section):
        translation = ""
        for byte_str in wrap(self._speech_dict[section]["Line"], 2):
            translation += chr(int(byte_str, 16))
        for special_font in self._FONT_DICT:
            translation = translation.replace(self._FONT_DICT[special_font], special_font)
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
    
    def _import_speech_dict(self, speech_dict):
        self._speech_dict = speech_dict