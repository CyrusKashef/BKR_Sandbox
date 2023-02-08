import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class BIG_CLUCKER_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Wings",
            1: "Beak_Legs",
            2: "Feathers",
            3: "Eyes",
            4: "Birdhole",
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
            (0x00, 0x00, 0x00, 0x00): "Skip", # Unsure
            (0x07, 0x22, 0x00, 0xFF): "Body",
            (0x13, 0x5C, 0x00, 0xFF): "Body",
            (0x29, 0xCE, 0x00, 0x00): "Skip", # Unsure
            (0x29, 0xCE, 0x00, 0xFF): "Body",
            (0x38, 0x38, 0x38, 0xFF): "Skip", # Birdhole
            (0x4F, 0x4F, 0x4F, 0xFF): "Skip", # Birdhole
            (0x54, 0x2E, 0x1F, 0xFF): "Beak_Legs",
            (0x61, 0x08, 0x1F, 0xFF): "Skip", # Unsure
            (0x73, 0x3E, 0x28, 0xFF): "Beak_Legs",
            (0x7A, 0x7A, 0x7A, 0xFF): "Skip", # Eye & Feathers
            (0x83, 0xFF, 0x3B, 0xFF): "Body",
            (0xA3, 0x10, 0x36, 0xFF): "Skip", # Unsure
            (0xA4, 0x5C, 0x00, 0xFF): "Skip", # Beak & Body
            (0xA7, 0xA7, 0xA7, 0xFF): "Skip", # Birdhole & Feathers
            (0xB9, 0x69, 0x48, 0xFF): "Beak_Legs",
            (0xF4, 0xA7, 0x00, 0xFF): "Skip", # Beak & Body
            (0xFF, 0x0B, 0x15, 0x00): "Skip", # Unsure
            (0xFF, 0x0B, 0x15, 0xFF): "Skip", # Unsure
            (0xFF, 0x34, 0x52, 0xFF): "Mouth",
            (0xFF, 0x4F, 0x55, 0x00): "Skip", # Unsure
            (0xFF, 0x4F, 0x55, 0xFF): "Skip", # Unsure
            (0xFF, 0xB3, 0xB5, 0x00): "Skip", # Unsure
            (0xFF, 0xB3, 0xB5, 0xFF): "Skip", # Unsure
            (0xFF, 0xC6, 0x8D, 0xFF): "Beak_Legs",
            (0xFF, 0xF0, 0x37, 0xFF): "Body",
            (0xFF, 0xFF, 0xFF, 0x00): "Skip", # Too Much
            (0xFF, 0xFF, 0xFF, 0xFF): "Skip", # Too Much
        }
        self._vertex_count_dict = {}
        for vert_count in [0x4F, 0x8D, 0x13D, 0x202, 0x204, 0x205, 0x20A]:
            self._vertex_count_dict[vert_count] = "Body"
        for vert_count in range(0x9E, 0x137 + 1):
            self._vertex_count_dict[vert_count] = "Beak_Legs" # Beak

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
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    FILE_NAME = "308548"
    MODEL_NAME = "Big_Clucker"
    JSON_FILE_DIR = f"C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Baddies/{MODEL_NAME}_Model_Presets/"
    from shutil import copy
    ### SINGLE TESTING ###
    # JSON_FILE_NAME = "Grayscale.json"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + f"{MODEL_NAME}_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    # level_model_obj = BIG_CLUCKER_MODEL_CLASS(FILE_DIR + f"{MODEL_NAME}_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    # level_model_obj._get_texture_count()
    # level_model_obj._get_all_vertex_colors()
    # level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    from os import listdir
    for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
        print(JSON_FILE_NAME)
        copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + f"{MODEL_NAME}_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
        level_model_obj = BIG_CLUCKER_MODEL_CLASS(FILE_DIR + f"{MODEL_NAME}_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
        level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])