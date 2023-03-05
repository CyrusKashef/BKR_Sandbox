import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class BK_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Banjo_Belt",
            1: "Banjo_Skin",
            2: "Banjo_Fur",
            3: "Banjo_Skin",
            4: "Banjo_Nose",
            5: "Banjo_Shorts",
            6: "Banjo_Shorts",
            7: "Banjo_Shorts",
            8: "Banjo_Skin",
            9: "Banjo_Necklace_String",
            10: "Banjo_Shorts",
            11: "Backpack", # When Zoomed In
            12: "Backpack",
            13: "Banjo_Eyelids",
            14: "Banjo_Eyes", # Blinking
            15: "Kazooie_Feathers_Primary",
            16: "Banjo_Belt", # When Zoomed In
            17: "Kazooie_Eyes",
            18: "Banjo_Eyes",
            19: "Kazooie_Feathers_Secondary", # Idle
            20: "Turbo_Talon_Trainers",
            21: "Turbo_Talon_Trainers",
            22: "Turbo_Talon_Trainers",
            23: "Wading_Boots",
        }
        self._texture_specific_dict = {
            15: {
                "Kazooie_Feathers_Secondary": [3, 8, 9],
            },
            # 20: {
            #     "Kazooie_Feathers_Secondary": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            # },
            # 21: {
            #     "Kazooie_Feathers_Secondary": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            # },
            # 22: {
            #     "Kazooie_Feathers_Secondary": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            # }
        }
        self._vertex_dict = {
            (0x27, 0x0E, 0x00, 0xFF): "Banjo_Fur",
            (0x41, 0x17, 0x00, 0xFF): "Banjo_Fur",
            (0x63, 0x25, 0x01, 0xFF): "Banjo_Fur",
            (0x83, 0x32, 0x03, 0xFF): "Banjo_Fur",
            (0x87, 0x47, 0x08, 0xFF): "Banjo_Fur",
            (0xAE, 0x47, 0x07, 0xFF): "Banjo_Fur",
            (0xCC, 0x56, 0x0B, 0xFF): "Banjo_Fur",
            (0xFA, 0x6F, 0x12, 0xFF): "Banjo_Fur",
            (0x45, 0x25, 0x1F, 0xFF): "Banjo_Skin",
            (0x66, 0x37, 0x2F, 0xFF): "Banjo_Skin",
            (0x99, 0x54, 0x47, 0xFF): "Banjo_Skin",
            (0xC6, 0x6E, 0x5C, 0xFF): "Banjo_Skin",
            (0xEB, 0x83, 0x6D, 0xFF): "Banjo_Skin",
            (0xFF, 0xA3, 0x85, 0xFF): "Banjo_Skin",
            (0xFF, 0xBE, 0x97, 0xFF): "Banjo_Skin",
            (0xFF, 0xEA, 0xB4, 0xFF): "Banjo_Skin",
            (0xBA, 0x55, 0x00, 0xFF): "Banjo_Shorts",
            (0xCE, 0x87, 0x00, 0xFF): "Banjo_Shorts",
            (0xEA, 0xEA, 0x00, 0xFF): "Banjo_Shorts",
            (0xF6, 0xB4, 0x00, 0xFF): "Banjo_Shorts",
            (0xFF, 0xFF, 0x28, 0xFF): "Banjo_Shorts",
            (0x2D, 0x00, 0x32, 0xFF): "Kazooie_Feathers_Primary",
            (0x52, 0x00, 0x00, 0xFF): "Kazooie_Feathers_Primary",
            (0x88, 0x00, 0x00, 0xFF): "Kazooie_Feathers_Primary",
            (0xD0, 0x00, 0x00, 0xFF): "Kazooie_Feathers_Primary",
            (0xFF, 0x33, 0x00, 0xFF): "Kazooie_Feathers_Primary",
            (0xFF, 0x5F, 0x00, 0xFF): "Kazooie_Feathers_Primary",
            (0xFF, 0x89, 0x00, 0xFF): "Kazooie_Feathers_Primary",
            (0xFF, 0xC7, 0x00, 0xFF): "Kazooie_Feathers_Secondary",
            (0x66, 0x23, 0x00, 0xFF): "Kazooie_Beak/Legs",
            (0x92, 0x39, 0x00, 0xFF): "Kazooie_Beak/Legs",
            (0xC7, 0x47, 0x00, 0xFF): "Kazooie_Beak/Legs",
            (0xFF, 0x74, 0x25, 0xFF): "Kazooie_Beak/Legs",
            (0xFE, 0xA1, 0x31, 0xFF): "Kazooie_Beak/Legs",
            (0xFF, 0xCF, 0x3D, 0xFF): "Kazooie_Beak/Legs",
            (0xFF, 0xFF, 0x9F, 0xFF): "Kazooie_Beak/Legs",
            (0x80, 0x1F, 0x4B, 0xFF): "Mouths",
            (0xA3, 0x10, 0x36, 0xFF): "Mouths",
            (0xB3, 0x2C, 0x69, 0xFF): "Mouths",
            (0xBA, 0x7F, 0x4B, 0xFF): "Mouths",
            (0x3C, 0x0D, 0x22, 0xFF): "Mouths",
            (0xFF, 0x34, 0x52, 0xFF): "Mouths",
            (0x00, 0x1A, 0x4E, 0xFF): "Backpack",
            (0x00, 0x22, 0x68, 0xFF): "Backpack",
            (0x00, 0x30, 0x92, 0xFF): "Backpack",
            (0x00, 0x4A, 0xE0, 0xFF): "Backpack",
            (0x2B, 0x71, 0xFF, 0xFF): "Backpack",
            (0x55, 0x8D, 0xFF, 0xFF): "Backpack",
            (0x7F, 0xA9, 0xFF, 0xFF): "Backpack",
            (0x20, 0x20, 0x20, 0xFF): "Turbo_Talon_Trainers",
            (0x38, 0x38, 0x38, 0xFF): "Turbo_Talon_Trainers",
            (0xDB, 0xDB, 0xDB, 0xFF): "Turbo_Talon_Trainers",
            (0x13, 0x19, 0x12, 0xFF): "Wading_Boots",
            (0x21, 0x31, 0x1E, 0xFF): "Wading_Boots",
            (0x36, 0x4F, 0x32, 0xFF): "Wading_Boots",
            (0x5C, 0x87, 0x54, 0xFF): "Wading_Boots",
            (0x00, 0x00, 0x00, 0xFF): "Skip",
            (0x4F, 0x4F, 0x4F, 0xFF): "Skip",
            (0x4F, 0x4F, 0x4F, 0xFF): "Skip",
            (0x7A, 0x7A, 0x7A, 0xFF): "Skip",
            (0xA7, 0xA7, 0xA7, 0xFF): "Skip",
            (0xFF, 0xFF, 0xFF, 0xFF): "Skip",
        }
        self._vertex_count_dict = {}
        for vert_count in range(0x4EC, 0x4F5 + 0x1):
            self._vertex_count_dict[vert_count] = "Banjo_Necklace_Tooth"
        for vert_count in range(0x640, 0x64F + 0x1):
            self._vertex_count_dict[vert_count] = "Kazooie_Head_Feather"
        for vert_count in range(0x1225, 0x122F + 0x1):
            self._vertex_count_dict[vert_count] = "Kazooie_Head_Feather"

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
    FILE_NAME = "19D530"
    MODEL_NAME = "Banjo_Kazooie"
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
    level_model_obj = BK_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
    level_model_obj._get_texture_count()
    level_model_obj._get_all_vertex_colors()
    # level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    # from os import listdir
    # for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
    #     print(JSON_FILE_NAME)
    #     old_file_name = f"{MODEL_DIR}{FILE_NAME}-Default.bin"
    #     new_file_name = f"{MODEL_DIR}{MODEL_NAME}_Models/{FILE_NAME}-{JSON_FILE_NAME[:-5]}.bin"
    #     copy(old_file_name, new_file_name)
    #     level_model_obj = BK_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
    #     level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])