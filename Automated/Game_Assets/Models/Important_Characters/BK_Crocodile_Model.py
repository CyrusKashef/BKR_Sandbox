import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class BK_CROCODILE_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Scales",
            1: "Eyes",
            2: "Shorts",
            3: "Backpack",
            4: "Scales",
            5: "Scales", # Half Eyelid?
            6: "Scales", # Blinking Eyelid?
            7: "Scales", # Closed Eyelid?
            # 8: "Test", # Running Shoe Laces
            # 9: "Test", # Running Shoe Star
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
            (0x00, 0x1A, 0x4E, 0xFF): "Backpack",
            (0x00, 0x22, 0x68, 0xFF): "Backpack",
            (0x00, 0x30, 0x92, 0xFF): "Backpack",
            (0x00, 0x4A, 0xE0, 0xFF): "Backpack",
            (0x1F, 0x28, 0x09, 0xFF): "Scales",
            (0x2B, 0x71, 0xFF, 0xFF): "Backpack",
            (0x2D, 0x40, 0x09, 0xFF): "Underbelly",
            (0x36, 0x23, 0x15, 0xFF): "Skip", # Unsure
            (0x38, 0x38, 0x38, 0xFF): "Tooth",
            (0x39, 0x4A, 0x0F, 0xFF): "Scales",
            (0x4F, 0x4F, 0x4F, 0xFF): "Skip", # Eyes
            (0x52, 0x6D, 0x0E, 0x00): "Scales",
            (0x52, 0x6D, 0x0E, 0xFF): "Scales",
            (0x5B, 0x72, 0x00, 0xFF): "Scales",
            (0x61, 0x08, 0x1F, 0xFF): "Mouth",
            (0x7A, 0x7A, 0x7A, 0xFF): "Skip", # Eyes
            (0x7A, 0x9A, 0x00, 0xFF): "Scales",
            (0x87, 0x46, 0x00, 0xFF): "Shorts",
            (0x99, 0xBF, 0x12, 0xFF): "Scales",
            (0x9C, 0x57, 0x3B, 0xFF): "Skip", # Unsure
            (0xA3, 0x10, 0x36, 0xFF): "Mouth",
            (0xA7, 0xA7, 0xA7, 0xFF): "Skip", # Unsure
            (0xB9, 0x69, 0x48, 0xFF): "Skip", # Unsure
            (0xBA, 0xE7, 0x19, 0xFF): "Scales",
            (0xC1, 0xD4, 0x65, 0xFF): "Underbelly",
            (0xCE, 0x87, 0x00, 0xFF): "Shorts",
            (0xDB, 0xDB, 0xDB, 0xFF): "Skip", # Unsure
            (0xEA, 0xEA, 0x00, 0xFF): "Shorts",
            (0xF8, 0xBB, 0x37, 0xFF): "Underbelly",
            (0xF8, 0xFE, 0x81, 0xFF): "Underbelly",
            (0xFF, 0x34, 0x52, 0xFF): "Mouth",
            (0xFF, 0xFF, 0xFF, 0x00): "Skip", # Unsure
            (0xFF, 0xFF, 0xFF, 0xFF): "Skip", # Scales
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
    FILE_NAME = "1D4B58"
    JSON_FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Important_Characters/BK_Crocodile_Model_Presets/"
    from shutil import copy
    ### FULL BODY TESTING ###
    # NEW_FILE_NAME = "Grayscale"
    # red_ratio, green_ratio, blue_ratio, brightness = 0x1, 0x1, 0x1, "Default"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Crocodile_Models/" + FILE_NAME + "-" + NEW_FILE_NAME + ".bin")
    # level_model_obj = LEVEL_MODEL_CLASS(FILE_DIR + "BK_Crocodile_Models/", FILE_NAME + "-" + NEW_FILE_NAME)
    # level_model_obj._full_model_color_shift(red_ratio, green_ratio, blue_ratio, brightness)

    ### SINGLE TESTING ###
    # JSON_FILE_NAME = "Grayscale.json"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Crocodile_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    # level_model_obj = BK_CROCODILE_MODEL_CLASS(FILE_DIR + "BK_Crocodile_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    # level_model_obj._get_all_vertex_colors()
    # level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    from os import listdir
    for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
        print(JSON_FILE_NAME)
        copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "BK_Crocodile_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
        level_model_obj = BK_CROCODILE_MODEL_CLASS(FILE_DIR + "BK_Crocodile_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
        level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])