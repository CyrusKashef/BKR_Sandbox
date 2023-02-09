import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class BK_BEE_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Body",
            1: "Shorts",
            2: "Shorts", # Belt
            3: "Backpack",
            4: "Eyes",
            5: "Body",
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
            (0x00, 0x1A, 0x4E, 0xFF): "Backpack",
            (0x00, 0x22, 0x68, 0xFF): "Backpack",
            (0x00, 0x30, 0x92, 0xFF): "Backpack",
            (0x00, 0x4A, 0xE0, 0xFF): "Backpack",
            (0x10, 0x01, 0x02, 0xFF): "Skip", # Unsure
            (0x1D, 0x0E, 0x00, 0xFF): "Skip", # Unsure
            (0x20, 0x20, 0x20, 0xFF): "Skip", # Eyes
            (0x2B, 0x71, 0xFF, 0xFF): "Backpack",
            (0x2E, 0x08, 0x07, 0xFF): "Body",
            (0x4F, 0x4F, 0x4F, 0xFF): "Skip", # Eyes
            (0x60, 0x0A, 0x00, 0x00): "Body",
            (0x60, 0x0A, 0x00, 0xFF): "Body",
            (0x61, 0x08, 0x1F, 0xFF): "Mouth",
            (0x63, 0x31, 0x00, 0xFF): "Shorts",
            (0x7A, 0x7A, 0x7A, 0xFF): "Skip", # Unsure
            (0x80, 0xC9, 0xC7, 0x2D): "Wings",
            (0x80, 0xC9, 0xC7, 0x54): "Wings",
            (0x80, 0xC9, 0xC7, 0x99): "Wings",
            (0x91, 0x23, 0x22, 0x00): "Body",
            (0x91, 0x23, 0x22, 0xFF): "Body",
            (0xA3, 0x10, 0x36, 0xFF): "Mouth",
            (0xA7, 0xA7, 0xA7, 0xFF): "Skip", # Too Much
            (0xD1, 0x64, 0x60, 0xFF): "Body",
            (0xDB, 0xDB, 0xDB, 0xFF): "Skip", # Eyes
            (0xF6, 0xB4, 0x00, 0xFF): "Shorts",
            (0xFB, 0x8D, 0x8A, 0xFF): "Mouth",
            (0xFF, 0x34, 0x52, 0xFF): "Mouth",
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
    FILE_NAME = "1C23F8"
    JSON_FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Important_Characters/BK_Bee_Model_Presets/"
    from shutil import copy
    ### SINGLE TESTING ###
    JSON_FILE_NAME = "Grayscale.json"
    copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Bee_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    level_model_obj = BK_BEE_MODEL_CLASS(FILE_DIR + "BK_Bee_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    level_model_obj._get_all_vertex_colors()
    level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    # from os import listdir
    # for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
    #     print(JSON_FILE_NAME)
    #     copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Bee_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    #     level_model_obj = BK_BEE_MODEL_CLASS(FILE_DIR + "BK_Bee_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    #     level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])