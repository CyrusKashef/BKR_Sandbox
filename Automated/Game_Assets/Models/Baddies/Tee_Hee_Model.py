import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class TEE_HEE_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Body_Glow", # Literall Everything
            1: "Eyes",
            # 2: "Test", # Unsure
            # 3: "Test", # Unsure
            # 4: "Test", # Unsure
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
            # (0x00, 0x00, 0x00, 0x96): "Skip", # Unsure
            # (0x00, 0x00, 0x00, 0xFF): "Skip", # Unsure
            (0x36, 0x51, 0x67, 0x96): "Body_Glow",
            (0x36, 0x51, 0x67, 0xFF): "Body_Glow",
            (0x78, 0x83, 0x86, 0x96): "Body_Glow",
            (0x7D, 0x9C, 0x96, 0x96): "Body_Glow",
            (0x7D, 0x9C, 0x96, 0xB4): "Body_Glow",
            (0x7D, 0x9C, 0x96, 0xFF): "Body_Glow",
            (0x8F, 0x9C, 0xA1, 0x96): "Body_Glow",
            (0x93, 0x7F, 0x72, 0x96): "Mouth",
            (0xBA, 0xCB, 0xD1, 0x96): "Body_Glow",
            (0xBA, 0xCB, 0xD1, 0xB4): "Body_Glow",
            (0xBA, 0xCB, 0xD1, 0xFF): "Body_Glow",
            (0xE9, 0xFF, 0xEB, 0x96): "Body_Glow",
            (0xE9, 0xFF, 0xEB, 0xBE): "Body_Glow",
            (0xE9, 0xFF, 0xEB, 0xD2): "Body_Glow",
            (0xFF, 0xFF, 0xFF, 0x00): "Body_Glow",
            (0xFF, 0xFF, 0xFF, 0x32): "Body_Glow",
            (0xFF, 0xFF, 0xFF, 0x64): "Body_Glow",
            (0xFF, 0xFF, 0xFF, 0x96): "Body_Glow",
            (0xFF, 0xFF, 0xFF, 0xB4): "Body_Glow",
            (0xFF, 0xFF, 0xFF, 0xBE): "Body_Glow",
            (0xFF, 0xFF, 0xFF, 0xFF): "Skip", # Too Much
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
    FILE_NAME = "21EED0"
    MODEL_NAME = "Tee_Hee"
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
    level_model_obj = TEE_HEE_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
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
    #     level_model_obj = TEE_HEE_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
    #     level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])