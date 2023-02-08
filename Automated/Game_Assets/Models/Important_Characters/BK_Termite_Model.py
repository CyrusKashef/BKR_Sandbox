import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class BK_TERMITE_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Body",
            1: "Body", # Half Eyelid?
            2: "Eyes",
            3: "Backpack",
            4: "Shorts",
            5: "Body", # Blinking Eyelid?
            6: "Body", # Closed Eyelid?
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
            (0x00, 0x1A, 0x4E, 0xFF): "Backpack",
            (0x00, 0x22, 0x68, 0xFF): "Backpack",
            (0x00, 0x30, 0x92, 0xFF): "Backpack",
            (0x00, 0x4A, 0xE0, 0xFF): "Backpack",
            (0x0F, 0x09, 0x09, 0xFF): "Body",
            (0x1F, 0x13, 0x13, 0xFF): "Body",
            (0x2B, 0x71, 0xFF, 0xFF): "Backpack",
            (0x33, 0x33, 0x08, 0xFF): "Shorts",
            (0x34, 0x34, 0x34, 0xFF): "Skip", # Eyes
            (0x4C, 0x11, 0x29, 0xFF): "Mouth",
            (0x4C, 0x4C, 0x4C, 0xFF): "Skip", # Eyes
            (0x55, 0x8D, 0xFF, 0xFF): "Backpack",
            (0x64, 0x33, 0x33, 0xFF): "Body",
            (0x65, 0x65, 0x65, 0xFF): "Skip", # Eyes
            (0x80, 0x80, 0x00, 0xFF): "Shorts",
            (0x80, 0x80, 0x80, 0xFF): "Skip", # Eyes
            (0x8C, 0x3D, 0x3D, 0xFF): "Body",
            (0xA0, 0xA0, 0xA0, 0xFF): "Skip", # Eyes
            (0xAB, 0x52, 0x52, 0xFF): "Body",
            (0xB9, 0x79, 0x79, 0xFF): "Body",
            (0xBA, 0x2B, 0x67, 0xFF): "Mouth",
            (0xC3, 0xA2, 0xA2, 0xFF): "Body",
            (0xC5, 0xC5, 0xC5, 0xFF): "Skip", # Eyes
            (0xCE, 0x9D, 0x90, 0xFF): "Legs",
            (0xE6, 0xE6, 0xE6, 0xFF): "Skip", # Eyes
            (0xFF, 0xFE, 0xD2, 0xFF): "Legs",
            (0xFF, 0xFF, 0x00, 0xFF): "Shorts",
            (0xFF, 0xFF, 0x79, 0xFF): "Shorts",
            (0xFF, 0xFF, 0xFF, 0xFF): "Skip",
        }
        self._vertex_count_dict = {}

    def _get_all_vertex_colors(self):
        vertex_dict = {}
        for count in range(self._vertex_count):
            vertex_info_index_start, x_position, y_position, z_position, u_mapping, v_mapping, old_red_val, old_green_val, old_blue_val, alpha_val = self._get_vertex_info(count)
            if((old_red_val, old_green_val, old_blue_val, alpha_val) not in vertex_dict):
                if((old_red_val, old_green_val, old_blue_val, alpha_val) not in self._vertex_dict):
                    vertex_dict[(old_red_val, old_green_val, old_blue_val, alpha_val)] = 1
            else:
                vertex_dict[(old_red_val, old_green_val, old_blue_val, alpha_val)] += 1
        for item in sorted(vertex_dict):
            red = self._int_to_hex_str(item[0])
            green = self._int_to_hex_str(item[1])
            blue = self._int_to_hex_str(item[2])
            alpha = self._int_to_hex_str(item[3])
            print(f"(0x{red}, 0x{green}, 0x{blue}, 0x{alpha})")

if __name__ == '__main__':
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    FILE_NAME = "1A5950"
    JSON_FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Important_Characters/BK_Termite_Model_Presets/"
    from shutil import copy
    ### FULL BODY TESTING ###
    # NEW_FILE_NAME = "Grayscale"
    # red_ratio, green_ratio, blue_ratio, brightness = 0x1, 0x1, 0x1, "Default"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Termite_Models/" + FILE_NAME + "-" + NEW_FILE_NAME + ".bin")
    # level_model_obj = LEVEL_MODEL_CLASS(FILE_DIR + "BK_Termite_Models/", FILE_NAME + "-" + NEW_FILE_NAME)
    # level_model_obj._full_model_color_shift(red_ratio, green_ratio, blue_ratio, brightness)

    ### SINGLE TESTING ###
    # JSON_FILE_NAME = "Spinarak.json"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Termite_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    # level_model_obj = BK_TERMITE_MODEL_CLASS(FILE_DIR + "BK_Termite_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    # level_model_obj._get_all_vertex_colors()
    # level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    from os import listdir
    for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
        print(JSON_FILE_NAME)
        copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Termite_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
        level_model_obj = BK_TERMITE_MODEL_CLASS(FILE_DIR + "BK_Termite_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
        level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])