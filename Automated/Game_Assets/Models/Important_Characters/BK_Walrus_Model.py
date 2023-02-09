import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class BK_WALRUS_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Body",
            1: "Shorts",
            2: "Backpack",
            3: "Eyes",
            4: "Sled_Blades",
            5: "Sled_Blades",
            6: "Sled_Wood",
            7: "Body", # Blinking Eyelid?
            8: "Body", # Closed Eyelid?
            9: "Body", # Half Eyelid?
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
            (0x00, 0x1A, 0x4E, 0xFF): "Backpack",
            (0x00, 0x22, 0x68, 0xFF): "Backpack",
            (0x00, 0x4A, 0xE0, 0xFF): "Backpack",
            (0x1D, 0x0C, 0x00, 0x00): "Body",
            (0x1D, 0x0C, 0x00, 0xFF): "Body",
            (0x2B, 0x71, 0xFF, 0xFF): "Backpack",
            (0x38, 0x38, 0x38, 0xFF): "Sled_Wood",
            (0x3B, 0x17, 0x10, 0x00): "Body",
            (0x3B, 0x17, 0x10, 0xFF): "Body",
            (0x4F, 0x4F, 0x4F, 0xFF): "Skip", # Too Much
            (0x5A, 0x26, 0x11, 0x00): "Body",
            (0x5A, 0x26, 0x11, 0xFF): "Body",
            (0x64, 0x28, 0x00, 0x00): "Shorts",
            (0x64, 0x28, 0x00, 0xFF): "Shorts",
            (0x6F, 0x51, 0x3E, 0x00): "Skip",
            (0x6F, 0x51, 0x3E, 0xFF): "Body",
            (0x7A, 0x7A, 0x7A, 0xFF): "Skip", # Too Much
            (0x84, 0x01, 0x00, 0xFF): "Mouth",
            (0x9A, 0x78, 0x5B, 0x00): "Body",
            (0x9A, 0x78, 0x5B, 0xFF): "Body",
            (0xA7, 0xA7, 0xA7, 0xFF): "Skip", # Too Much
            (0xC0, 0x9A, 0x77, 0xFF): "Body",
            (0xCE, 0x87, 0x00, 0x00): "Shorts",
            (0xCE, 0x87, 0x00, 0xFF): "Shorts",
            (0xD3, 0x69, 0x02, 0xFF): "Shorts",
            (0xDB, 0xDB, 0xDB, 0xFF): "Skip", # Eye
            (0xDF, 0xB7, 0x93, 0x00): "Body",
            (0xDF, 0xB7, 0x93, 0xFF): "Body",
            (0xE0, 0x7E, 0x55, 0xFF): "Body",
            (0xEA, 0xEA, 0x00, 0x00): "Shorts",
            (0xEA, 0xEA, 0x00, 0xFF): "Shorts",
            (0xF6, 0xB4, 0x00, 0xFF): "Shorts",
            (0xFD, 0x3A, 0x3D, 0xFF): "Mouth",
            (0xFF, 0x00, 0x00, 0xFF): "Mouth",
            (0xFF, 0xFF, 0xFF, 0x00): "Skip", # Unsure
            (0xFF, 0xFF, 0xFF, 0xFF): "Skip", # Unsure
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
    FILE_NAME = "1B4C40"
    JSON_FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Important_Characters/BK_Walrus_Model_Presets/"
    from shutil import copy
    ### SINGLE TESTING ###
    # JSON_FILE_NAME = "Grayscale.json"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Walrus_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    # level_model_obj = BK_WALRUS_MODEL_CLASS(FILE_DIR + "BK_Walrus_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    # level_model_obj._get_all_vertex_colors()
    # level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    from os import listdir
    for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
        print(JSON_FILE_NAME)
        copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Walrus_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
        level_model_obj = BK_WALRUS_MODEL_CLASS(FILE_DIR + "BK_Walrus_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
        level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])