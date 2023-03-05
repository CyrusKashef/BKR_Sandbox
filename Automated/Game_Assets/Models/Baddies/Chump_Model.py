import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class CHUMP_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            # 0: "Test", # Unsure
            1: "Eyes",
            2: "Body",
            3: "Fins",
            4: "Tail",
            # 5: "Test", # Unsure
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
            (0x38, 0x38, 0x38, 0xFF): "Skip",
            (0x4F, 0x4F, 0x4F, 0xFF): "Skip",
            (0x50, 0x00, 0x00, 0xFF): "Mouth", # Mouth & Teeth
            (0x6E, 0x00, 0x00, 0xFF): "Body", # Body & Teeth
            (0x7A, 0x7A, 0x7A, 0xFF): "Skip",
            (0xA7, 0xA7, 0xA7, 0x00): "Skip",
            (0xA7, 0xA7, 0xA7, 0xFF): "Skip",
            (0xB8, 0x00, 0x00, 0xFF): "Mouth", # Mouth & Tail
            (0xCA, 0x54, 0x07, 0xFF): "Fins",
            (0xDB, 0xDB, 0xDB, 0xFF): "Skip",
            (0xE3, 0x4E, 0x48, 0xFF): "Body",
            (0xF4, 0x6C, 0x00, 0x00): "Body",
            (0xF4, 0x6C, 0x00, 0xFF): "Body",
            (0xFF, 0x2D, 0x2D, 0xFF): "Mouth",
            (0xFF, 0xA8, 0x27, 0xFF): "Skip", # Too Much
            (0xFF, 0xE1, 0x33, 0xFF): "Body", # Fins & Body
            (0xFF, 0xFF, 0xFF, 0x00): "Skip",
            (0xFF, 0xFF, 0xFF, 0xFF): "Skip",
        }
        self._vertex_count_dict = {}
        for vert_count in [0x65, 0x6E, 0x78, 0x79, 0x7C, 0x8E, 0x8F, 0x90, 0x91, 0x92, 0x93, 0xB1, 0xB2, 0xB4, 0xBE]:
            self._vertex_count_dict[vert_count] = "Mouth"
        for vert_count in [0x66, 0x67, 0x6C, 0x6F, 0x74, 0x75, 0x77, 0x7B, 0x7F, 0x8B, 0x95, 0x96, 0x9C, 0x9D]:
            self._vertex_count_dict[vert_count] = "Body"
        for vert_count in [0xA3, 0xA7, 0xAB, 0xAF]:
            self._vertex_count_dict[vert_count] = "Teeth"
        for vert_count in [0x1, 0x5, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19]:
            self._vertex_count_dict[vert_count] = "Tail"
        for vert_count in [0x40, 0x41, 0x43, 0x44, 0x47, 0x48, 0x49, 0x4A, 0x4C, 0x4D, 0x4e, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x55, 0x56, 0x57, 0x58]:
            self._vertex_count_dict[vert_count] = "Fins"
        # for vert_count in [0xB9, 0xBB, 0xBC, 0xBF]:
        #     self._vertex_count_dict[vert_count] = "Skip" # Unsure
        # for vert_count in []:
        #     self._vertex_count_dict[vert_count] = "Test"

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
    FILE_NAME = "1C6E50"
    MODEL_NAME = "Chump"
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
    # level_model_obj = CHUMP_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
    # level_model_obj._get_texture_count()
    # level_model_obj._get_all_vertex_colors()
    # level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    # my_list = []
    # for item in [0x19C, 0x19E, 0x19F, 0x1A0, 0x1A1, 0x1A2, 0x1A4, 0x1A5, 0x1A7, 0x1A8, 0x1A9, 0x1AA, 0x1AB, 0x1AD, 0x1DB, 0x1DE, 0x1E2, 0x1E3, 0x1E6, 0x1E7, 0x1EB, 0x1EC, 0x200, 0x229, 0x230]:
    #     my_list.append(item - 0x194)
    # print('[{}]'.format(', '.join(hex(x) for x in my_list)))

    ### BULK TESTING ###
    from os import listdir
    for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
        print(JSON_FILE_NAME)
        old_file_name = f"{MODEL_DIR}{FILE_NAME}-Default.bin"
        new_file_name = f"{MODEL_DIR}{MODEL_NAME}_Models/{FILE_NAME}-{JSON_FILE_NAME[:-5]}.bin"
        copy(old_file_name, new_file_name)
        level_model_obj = CHUMP_MODEL_CLASS(f"{MODEL_DIR}{MODEL_NAME}_Models/", f"{FILE_NAME}-{JSON_FILE_NAME[:-5]}")
        level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])