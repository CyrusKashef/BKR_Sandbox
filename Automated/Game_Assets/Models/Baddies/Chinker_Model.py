import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class CHINKER_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Body",
            1: "Eyes_Pupils",
            2: "Eyes_Sclera", # Unsure
            # 3: "Test", # Unsure
            # 4: "Test", # Unsure
        }
        self._texture_specific_dict = {
            1: {
                "Eyes_Sclera": [0, 3, 7, 10],
            }
        }
        self._vertex_dict = {
            # (0x01, 0x7E, 0x02, 0xFF): "Skip",
            # (0x02, 0x57, 0x5B, 0xFF): "Skip",
            # (0x02, 0x7E, 0x01, 0xFF): "Skip",
            # (0x02, 0x82, 0xF3, 0xFF): "Skip",
            # (0x03, 0x07, 0x7E, 0xFF): "Skip",
            # (0x03, 0x07, 0x82, 0xFF): "Skip",
            # (0x03, 0x54, 0x5E, 0xFF): "Skip",
            # (0x03, 0x58, 0xA5, 0xFF): "Skip",
            # (0x03, 0x7E, 0x06, 0xFF): "Skip",
            # (0x05, 0x82, 0x09, 0xFF): "Skip",
            # (0x06, 0x7E, 0x03, 0xFF): "Skip",
            # (0x07, 0x57, 0x5B, 0xFF): "Skip",
            # (0x08, 0xBA, 0x69, 0xFF): "Skip",
            # (0x09, 0x82, 0x05, 0xFF): "Skip",
            # (0x0A, 0x06, 0x7E, 0xFF): "Skip",
            # (0x0B, 0x07, 0x82, 0xFF): "Skip",
            # (0x0B, 0x7D, 0x0C, 0xFF): "Skip",
            # (0x0B, 0x82, 0xFE, 0xFF): "Skip",
            # (0x0B, 0xA9, 0xA5, 0xFF): "Skip",
            # (0x0B, 0xB5, 0x9B, 0xFF): "Skip",
            # (0x0B, 0xB8, 0x67, 0xFF): "Skip",
            # (0x0C, 0x5A, 0xA8, 0xFF): "Skip",
            # (0x0C, 0x7D, 0x0B, 0xFF): "Skip",
            (0x29, 0x3E, 0x42, 0xFF): "Eyes_Sclera",
            # (0x3B, 0x5C, 0x3E, 0xFF): "Skip",
            # (0x3D, 0x5F, 0xC8, 0xFF): "Skip",
            # (0x3E, 0x5B, 0x3E, 0xFF): "Skip",
            # (0x3E, 0x5C, 0x3B, 0xFF): "Skip",
            # (0x40, 0x5D, 0xC7, 0xFF): "Skip",
            # (0x41, 0xB3, 0xB5, 0xFF): "Skip",
            # (0x42, 0xA5, 0xC6, 0xFF): "Skip",
            # (0x45, 0xB3, 0x49, 0xFF): "Skip",
            # (0x46, 0xB2, 0x46, 0xFF): "Skip",
            # (0x48, 0xB0, 0xBF, 0xFF): "Skip",
            # (0x49, 0x5A, 0xCF, 0xFF): "Skip",
            # (0x49, 0xB3, 0x45, 0xFF): "Skip",
            # (0x59, 0x06, 0x59, 0xFF): "Skip",
            # (0x59, 0x07, 0x59, 0xFF): "Skip",
            # (0x5B, 0x57, 0x02, 0xFF): "Skip",
            # (0x5B, 0x57, 0x07, 0xFF): "Skip",
            # (0x5D, 0x06, 0xAA, 0xFF): "Skip",
            # (0x5D, 0x07, 0xAB, 0xFF): "Skip",
            # (0x5E, 0x54, 0x03, 0xFF): "Skip",
            (0x60, 0x92, 0x99, 0xFF): "Eyes_Sclera",
            # (0x66, 0xB7, 0xF3, 0xFF): "Skip",
            # (0x67, 0xB8, 0x0B, 0xFF): "Skip",
            # (0x68, 0xB8, 0xFD, 0xFF): "Skip",
            # (0x69, 0xBA, 0x08, 0xFF): "Skip",
            # (0x7E, 0x06, 0x0A, 0xFF): "Skip",
            # (0x7E, 0x06, 0xFD, 0xFF): "Skip",
            # (0x7E, 0x07, 0x03, 0xFF): "Skip",
            # (0x82, 0x06, 0xF5, 0xFF): "Skip",
            # (0x82, 0x07, 0x03, 0xFF): "Skip",
            # (0x82, 0x07, 0x0B, 0xFF): "Skip",
            # (0x82, 0xF9, 0xFD, 0xFF): "Skip",
            (0x95, 0xB5, 0xBA, 0xFF): "Eyes_Sclera",
            # (0x9B, 0xB5, 0x0B, 0xFF): "Skip",
            # (0x9F, 0x50, 0xF6, 0xFF): "Skip",
            # (0xA2, 0xAB, 0xFD, 0xFF): "Skip",
            # (0xA5, 0x58, 0x03, 0xFF): "Skip",
            # (0xA5, 0x58, 0xF9, 0xFF): "Skip",
            # (0xA5, 0xA8, 0xF9, 0xFF): "Skip",
            # (0xA5, 0xA9, 0x0B, 0xFF): "Skip",
            # (0xA7, 0x06, 0xA7, 0xFF): "Skip",
            # (0xA7, 0xF9, 0xA7, 0xFF): "Skip",
            # (0xA8, 0x5A, 0x0C, 0xFF): "Skip",
            # (0xAA, 0x06, 0x5D, 0xFF): "Skip",
            # (0xAB, 0x07, 0x5D, 0xFF): "Skip",
            # (0xB5, 0xB3, 0x41, 0xFF): "Skip",
            # (0xBE, 0x55, 0xBE, 0xFF): "Skip",
            # (0xBF, 0xB0, 0x48, 0xFF): "Skip",
            # (0xC2, 0x5C, 0xC5, 0xFF): "Skip",
            # (0xC2, 0xA4, 0xC5, 0xFF): "Skip",
            # (0xC2, 0xA5, 0xC2, 0xFF): "Skip",
            # (0xC5, 0x5C, 0xC2, 0xFF): "Skip",
            # (0xC5, 0xA4, 0xC2, 0xFF): "Skip",
            # (0xC6, 0xA5, 0x42, 0xFF): "Skip",
            # (0xC7, 0x5D, 0x40, 0xFF): "Skip",
            # (0xC8, 0x5F, 0x3D, 0xFF): "Skip",
            # (0xCF, 0x5A, 0x49, 0xFF): "Skip",
            # (0xF3, 0x82, 0x02, 0xFF): "Skip",
            # (0xF3, 0xB7, 0x66, 0xFF): "Skip",
            # (0xF5, 0x06, 0x82, 0xFF): "Skip",
            # (0xF6, 0x50, 0x9F, 0xFF): "Skip",
            # (0xF9, 0x58, 0xA5, 0xFF): "Skip",
            # (0xF9, 0x7E, 0xFC, 0xFF): "Skip",
            # (0xF9, 0x82, 0xFC, 0xFF): "Skip",
            # (0xF9, 0xA8, 0xA5, 0xFF): "Skip",
            # (0xFC, 0x7E, 0xF9, 0xFF): "Skip",
            # (0xFC, 0x82, 0xF9, 0xFF): "Skip",
            # (0xFD, 0x06, 0x7E, 0xFF): "Skip",
            # (0xFD, 0xAB, 0xA2, 0xFF): "Skip",
            # (0xFD, 0xB8, 0x68, 0xFF): "Skip",
            # (0xFD, 0xF9, 0x82, 0xFF): "Skip",
            # (0xFE, 0x82, 0x0B, 0xFF): "Skip",
            # (0xFF, 0xFF, 0xFF, 0xFF): "Skip",
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
    FILE_NAME = "39C330"
    MODEL_NAME = "Chinker"
    COLOR_RATIO = "01FF01"
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
    # JSON_FILE_NAME = "Grayscale.json"
    # old_file_name = f"{MODEL_DIR}{FILE_NAME}-Default.bin"
    # new_file_name = f"{MODEL_DIR}{MODEL_NAME}_Models/{FILE_NAME}-{JSON_FILE_NAME[:-5]}.bin"
    # copy(old_file_name, new_file_name)
    # level_model_obj = CHINKER_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
    # level_model_obj._get_texture_count()
    # level_model_obj._get_all_vertex_colors()
    # level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    from os import listdir
    for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
        print(JSON_FILE_NAME)
        old_file_name = f"{MODEL_DIR}{FILE_NAME}-Default.bin"
        new_file_name = f"{MODEL_DIR}{MODEL_NAME}_Models/{FILE_NAME}-{JSON_FILE_NAME[:-5]}.bin"
        copy(old_file_name, new_file_name)
        level_model_obj = CHINKER_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
        level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])