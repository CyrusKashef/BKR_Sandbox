import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class GRILLE_CHOMPA_MODEL_CLASS(GENERIC_MODEL_CLASS):
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
            5: "Grille",
            6: "Grille",
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
            # (0x20, 0x20, 0x20, 0xFF): "Skip",
            (0x38, 0x07, 0x07, 0x00): "Body",
            (0x38, 0x07, 0x07, 0xFF): "Body",
            # (0x38, 0x38, 0x38, 0xFF): "Skip",
            # (0x4F, 0x4F, 0x4F, 0xFF): "Skip",
            (0x54, 0x00, 0x01, 0xFF): "Mouth",
            # (0x7A, 0x7A, 0x7A, 0xFF): "Skip",
            (0x90, 0x2D, 0x32, 0x00): "Body",
            (0x90, 0x2D, 0x32, 0xFF): "Body",
            # (0xA7, 0xA7, 0xA7, 0xFF): "Skip",
            (0xD2, 0x5E, 0x59, 0xFF): "Body",
            (0xF0, 0x5E, 0x59, 0xFF): "Body",
            (0xFD, 0xFA, 0x79, 0xFF): "Body",
            (0xFF, 0x33, 0x45, 0xFF): "Mouth",
            # (0xFF, 0xFF, 0xFF, 0x00): "Skip",
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
    FILE_NAME = "299D70"
    MODEL_NAME = "Grille_Chompa"
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
    # JSON_FILE_NAME = "Grayscale.json"
    # old_file_name = f"{MODEL_DIR}{FILE_NAME}-Default.bin"
    # new_file_name = f"{MODEL_DIR}{MODEL_NAME}_Models/{FILE_NAME}-{JSON_FILE_NAME[:-5]}.bin"
    # copy(old_file_name, new_file_name)
    # level_model_obj = GRILLE_CHOMPA_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
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
        level_model_obj = GRILLE_CHOMPA_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
        level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])