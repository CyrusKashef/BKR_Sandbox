import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class BK_PUMPKIN_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Body",
            1: "Eyes",
            2: "Shorts",
            3: "Belt",
            4: "Backpack",
            5: "Body", # Half Eyelid?
            6: "Body", # Blinking Eyelid?
            7: "Body", # Closed Eyelid?
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
            (0x00, 0x1A, 0x4E, 0xFF): "Backpack",
            (0x00, 0x22, 0x68, 0xFF): "Backpack",
            (0x00, 0x30, 0x92, 0xFF): "Backpack",
            (0x00, 0x4A, 0xE0, 0xFF): "Backpack",
            (0x2B, 0x71, 0xFF, 0xFF): "Backpack",
            (0x46, 0x23, 0x23, 0xFF): "Body",
            (0x4F, 0x4F, 0x4F, 0xFF): "Skip", # Eyes
            (0x54, 0x2E, 0x1F, 0xFF): "Stem",
            (0x64, 0x28, 0x00, 0xFF): "Shorts",
            (0x74, 0x3B, 0x33, 0xFF): "Body",
            (0x7A, 0x7A, 0x7A, 0xFF): "Skip", # Eyes
            (0x87, 0x46, 0x00, 0xFF): "Shorts",
            (0x8E, 0x51, 0x43, 0xFF): "Body",
            (0x9C, 0x57, 0x3B, 0xFF): "Stem",
            (0xA3, 0x64, 0x38, 0xFF): "Body",
            (0xA7, 0x81, 0x42, 0xFF): "Body",
            (0xA7, 0xA7, 0xA7, 0xFF): "Skip", # Eyes
            (0xB7, 0xB7, 0x6C, 0xFF): "Body",
            (0xCE, 0x87, 0x00, 0xFF): "Shorts",
            (0xD3, 0x69, 0x02, 0xFF): "Shorts",
            (0xDB, 0xDB, 0xDB, 0xFF): "Skip", # Eyes
            (0xE7, 0x94, 0x70, 0xFF): "Stem",
            (0xEA, 0xEA, 0x00, 0xFF): "Shorts",
            (0xEA, 0xEA, 0xA3, 0xFF): "Body",
            (0xF2, 0x9E, 0x8C, 0xFF): "Skip", # Unsure
            (0xF6, 0xB4, 0x00, 0xFF): "Shorts",
            (0xFF, 0xFF, 0xFF, 0xFF): "Skip", # Too Much
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
            print(f'(0x{red}, 0x{green}, 0x{blue}, 0x{alpha}): "Test",')

if __name__ == '__main__':
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    FILE_NAME = "1CBCC0"
    JSON_FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Important_Characters/BK_Pumpkin_Model_Presets/"
    from shutil import copy
    ### SINGLE TESTING ###
    # JSON_FILE_NAME = "Grayscale.json"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Pumpkin_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    # level_model_obj = BK_PUMPKIN_MODEL_CLASS(FILE_DIR + "BK_Pumpkin_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    # level_model_obj._get_all_vertex_colors()
    # level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    from os import listdir
    for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
        print(JSON_FILE_NAME)
        copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Pumpkin_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
        level_model_obj = BK_PUMPKIN_MODEL_CLASS(FILE_DIR + "BK_Pumpkin_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
        level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])