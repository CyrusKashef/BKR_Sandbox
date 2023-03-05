import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class TICKER_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Body",
            1: "Eyes",
            # 2: "Test", # Unsure
            # 3: "Test", # Unsure
            # 4: "Test", # Unsure
            # 5: "Test", # Unsure
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
            (0x0F, 0x09, 0x09, 0xFF): "Body",
            (0x1F, 0x13, 0x13, 0xFF): "Body",
            # (0x4C, 0x4C, 0x4C, 0xFF): "Skip", # Eyes
            (0x64, 0x33, 0x33, 0xFF): "Body",
            (0x80, 0x80, 0x80, 0xFF): "Skip", # Eyes
            (0x8C, 0x3D, 0x3D, 0xFF): "Body",
            (0x9B, 0x75, 0x6D, 0xFF): "Body",
            # (0xA0, 0xA0, 0xA0, 0xFF): "Skip", # Eyes
            (0xAB, 0x52, 0x52, 0xFF): "Body",
            (0xB9, 0x79, 0x79, 0xFF): "Body",
            (0xBA, 0x2B, 0x67, 0xFF): "Mouth",
            (0xC3, 0xA2, 0xA2, 0xFF): "Body",
            (0xC5, 0xC5, 0xC5, 0xFF): "Skip", # Eyes
            (0xCE, 0x9D, 0x90, 0xFF): "Body",
            (0xDE, 0x73, 0xA0, 0xFF): "Mouth",
            (0xF3, 0xBC, 0xA8, 0xFF): "Body",
            (0xFF, 0xFE, 0xD2, 0xFF): "Body",
            # (0xFF, 0xFF, 0xFF, 0xFF): "Skip", # Too Much
        }
        self._vertex_count_dict = {}

    def _get_texture_count(self):
        self._get_object_texture_header_info()
        print(f"Texture Count: {self._texture_count}")
        for texture_count in range(self._texture_count):
            print(f'{texture_count}: "Test",')

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
    # VARIABLES
    FILE_NAME = "1A7448"
    MODEL_NAME = "Ticker"
    COLOR_RATIO = "0101FF"
    # DO NOT CHANGE
    ORIGINAL_FILE_DIR = f"C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    JSON_FILE_DIR = f"C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Baddies/{MODEL_NAME}_Model_Presets/"
    MODEL_DIR = f"C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    MODEL_DIR_EXT = f"{MODEL_NAME}_Models/"
    # FUNCTIONS
    from shutil import copy
    from os.path import exists
    from os import mkdir
    import json
    if(not exists(f"{MODEL_DIR}{FILE_NAME}-Default.bin")):
        copy(f"{ORIGINAL_FILE_DIR}{FILE_NAME}.bin", f"{MODEL_DIR}{FILE_NAME}-Default.bin")
    if(not exists(f"{MODEL_DIR}{MODEL_DIR_EXT}")):
        mkdir(f"{MODEL_DIR}{MODEL_DIR_EXT}")
    if(not exists(JSON_FILE_DIR)):
        mkdir(JSON_FILE_DIR)
    if(not exists(f"{JSON_FILE_DIR}Grayscale.json")):
        json_dict = {"Test": {"Color_Ratio": COLOR_RATIO, "Ignore_Gray": False}}
        json_object = json.dumps(json_dict, indent=4)
        with open(f"{JSON_FILE_DIR}Grayscale.json", "w+") as json_file:
            json_file.write(json_object)
    ### SINGLE TESTING ###
    JSON_FILE_NAME = "Grayscale.json"
    old_file_name = f"{MODEL_DIR}{FILE_NAME}-Default.bin"
    new_file_name = f"{MODEL_DIR}{MODEL_NAME}_Models/{FILE_NAME}-{JSON_FILE_NAME[:-5]}.bin"
    copy(old_file_name, new_file_name)
    level_model_obj = TICKER_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
    level_model_obj._get_texture_count()
    level_model_obj._get_all_vertex_colors()
    level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    # from os import listdir
    # for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
    #     print(JSON_FILE_NAME)
    #     old_file_name = f"{MODEL_DIR}{FILE_NAME}-Default.bin"
    #     new_file_name = f"{MODEL_DIR}{MODEL_NAME}_Models/{FILE_NAME}-{JSON_FILE_NAME[:-5]}.bin"
    #     copy(old_file_name, new_file_name)
    #     level_model_obj = TICKER_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
    #     level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])