import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class GRIMLET_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
        }
        self._texture_specific_dict = {
        }
        self._vertex_dict = {
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
    MODEL_NAME = "Bawl"
    JSON_FILE_DIR = f"C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Baddies/{MODEL_NAME}_Model_Presets/"
    from shutil import copy
    ### SINGLE TESTING ###
    JSON_FILE_NAME = "Grayscale.json"
    copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + f"{MODEL_NAME}_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    level_model_obj = GRIMLET_MODEL_CLASS(FILE_DIR + f"{MODEL_NAME}_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    level_model_obj._get_all_vertex_colors()
    level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    from os import listdir
    for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
        print(JSON_FILE_NAME)
        copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + f"{MODEL_NAME}_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
        level_model_obj = GRIMLET_MODEL_CLASS(FILE_DIR + f"{MODEL_NAME}_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
        level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])