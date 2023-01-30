import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class MM_A_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Grass",
            1: "Grass_Platform_Side",
            2: "Grass_Platform_Top",
            3: "Road",
            4: "Stone_Walls",
            5: "Stone_Walls",
            6: "Stone_Walls",
            7: "Stone_Walls",
            8: "Grass",
            9: "Mudslide",
            10: "Grass",
            11: "Stone_Walls",
            12: "Grass_Platform_Side",
            13: "Grass_Platform_Side",
            14: "Stone_Walls",
            15: "Road",
            16: "Stone_Walls",
            17: "Stone_Walls",
            18: "Stone_Walls",
            19: "Stone_Walls",
            20: "Stone_Walls",
            21: "Stone_Walls",
            22: "Stone_Walls",
            23: "Stone_Walls",
            24: "Stone_Walls",
            25: "Stone_Walls",
            26: "Stone_Walls",
            27: "Stone_Walls",
            28: "Stone_Walls",
            29: "Stone_Walls",
            30: "Grass_Platform_Side",
            31: "Grass_Platform_Side",
            32: "Grass_Platform_Side",
            33: "Grass_Platform_Side",
            34: "Tickers_Tower_Top",
            35: "Tickers_Tower_Side",
            36: "Tickers_Tower_Side",
            37: "Staircase",
            38: "Staircase",
            39: "Staircase",
            40: "Stonehenge",
            41: "Stonehenge",
            42: "Stonehenge",
            43: "Stonehenge",
            44: "Stonehenge",
            45: "Stonehenge",
            46: "Staircase",
            47: "Wood_Platform_Top",
            48: "Wood_Platform_Side",
            49: "Wood_Walls",
            50: "Wood_Walls",
        }
        self._vertex_dict = {
            # (0x00, 0x00, 0x00, 0xFF): "Test",
            # (0x00, 0x80, 0x00, 0xFF): "Test",
            # (0x28, 0x28, 0x28, 0xFF): "Test",
            # (0x3C, 0x3C, 0x3C, 0xFF): "Test",
            # (0x44, 0x44, 0x44, 0xFF): "Test",
            # (0x48, 0x48, 0x48, 0xFF): "Test",
            # (0x50, 0x50, 0x50, 0xFF): "Test",
            # (0x54, 0x4A, 0x1B, 0xFF): "Test",
            # (0x5A, 0x5A, 0x5A, 0xFF): "Test",
            # (0x5B, 0x51, 0x1E, 0xFF): "Test",
            # (0x5C, 0x5C, 0x5C, 0xFF): "Test",
            # (0x60, 0x55, 0x1F, 0xFF): "Test",
            # (0x60, 0x60, 0x60, 0xFF): "Test",
            # (0x62, 0x62, 0x62, 0xFF): "Test",
            # (0x63, 0x58, 0x20, 0xFF): "Test",
            # (0x64, 0x64, 0x64, 0xFF): "Test",
            # (0x66, 0x66, 0x66, 0xFF): "Test",
            # (0x6A, 0x6A, 0x6A, 0xFF): "Test",
            # (0x70, 0x70, 0x70, 0xFF): "Test",
            # (0x72, 0x65, 0x25, 0xFF): "Test",
            # (0x72, 0x72, 0x72, 0xFF): "Test",
            # (0x78, 0x78, 0x78, 0xFF): "Test",
            # (0x7E, 0x7E, 0x7E, 0xFF): "Test",
            # (0x81, 0x73, 0x2A, 0x00): "Test",
            # (0x81, 0x73, 0x2A, 0xFF): "Test",
            # (0x84, 0x84, 0x84, 0xFF): "Test",
            # (0x8A, 0x8A, 0x8A, 0xFF): "Test",
            # (0x8C, 0x8C, 0x8C, 0xFF): "Test",
            # (0x90, 0x80, 0x2F, 0xFF): "Test",
            # (0x96, 0x96, 0x96, 0xFF): "Test",
            # (0x98, 0x98, 0x98, 0xFF): "Test",
            # (0x9A, 0x9A, 0x9A, 0x00): "Test",
            # (0x9A, 0x9A, 0x9A, 0xFF): "Test",
            # (0x9C, 0x9C, 0x9C, 0xFF): "Test",
            # (0x9D, 0x9D, 0x9D, 0xFF): "Test",
            # (0x9E, 0x9E, 0x9E, 0xFF): "Test",
            # (0x9F, 0x8D, 0x34, 0xFF): "Test",
            # (0xA0, 0xA0, 0xA0, 0xFF): "Test",
            # (0xA1, 0xA1, 0xA1, 0xFF): "Test",
            # (0xA4, 0xA4, 0xA4, 0xFF): "Test",
            # (0xA5, 0xA5, 0xA5, 0xFF): "Test",
            # (0xA8, 0xA8, 0xA8, 0xFF): "Test",
            # (0xAA, 0xAA, 0xAA, 0xFF): "Test",
            # (0xAC, 0xAC, 0xAC, 0xFF): "Test",
            # (0xAE, 0x9B, 0x39, 0xFF): "Test",
            # (0xAF, 0xAF, 0xAF, 0xFF): "Test",
            # (0xB0, 0xB0, 0xB0, 0xFF): "Test",
            # (0xB2, 0xB2, 0xB2, 0xFF): "Test",
            # (0xB4, 0xB4, 0xB4, 0xFF): "Test",
            # (0xB8, 0xB8, 0xB8, 0xFF): "Test",
            # (0xBA, 0xBA, 0xBA, 0xFF): "Test",
            # (0xBB, 0xBB, 0xBB, 0x00): "Test",
            # (0xBB, 0xBB, 0xBB, 0xFF): "Test",
            # (0xBC, 0xBC, 0xBC, 0x00): "Test",
            # (0xBC, 0xBC, 0xBC, 0xFF): "Test",
            # (0xBD, 0xA8, 0x3E, 0xFF): "Test",
            # (0xBD, 0xBD, 0xBD, 0xFF): "Test",
            # (0xBE, 0xBE, 0xBE, 0xFF): "Test",
            # (0xC0, 0xC0, 0xC0, 0xFF): "Test",
            # (0xC2, 0xC2, 0xC2, 0xFF): "Test",
            # (0xC4, 0xC4, 0xC4, 0xFF): "Test",
            # (0xC6, 0xC6, 0xC6, 0xFF): "Test",
            # (0xC7, 0xC7, 0xC7, 0x00): "Test",
            # (0xC7, 0xC7, 0xC7, 0xFF): "Test",
            # (0xC8, 0xC8, 0xC8, 0xFF): "Test",
            # (0xC9, 0xC9, 0xC9, 0x00): "Test",
            # (0xC9, 0xC9, 0xC9, 0xFF): "Test",
            # (0xCC, 0xCC, 0xCC, 0xFF): "Test",
            # (0xD0, 0xD0, 0xD0, 0xFF): "Test",
            # (0xD2, 0xD2, 0xD2, 0xFF): "Test",
            # (0xD4, 0xD4, 0xD4, 0xFF): "Test",
            # (0xD5, 0xD5, 0xD5, 0xFF): "Test",
            # (0xD6, 0xD6, 0xD6, 0xFF): "Test",
            # (0xDC, 0xDC, 0xDC, 0xFF): "Test",
            # (0xE4, 0xE4, 0xE4, 0xFF): "Test",
            # (0xE6, 0xE6, 0xE6, 0xFF): "Test",
            # (0xE8, 0xE8, 0xE8, 0xFF): "Test",
            # (0xEA, 0xEA, 0xEA, 0xFF): "Test",
            # (0xEC, 0xEC, 0xEC, 0xFF): "Test",
            # (0xEE, 0xEE, 0xEE, 0xFF): "Test",
            # (0xF0, 0xF0, 0xF0, 0xFF): "Test",
            # (0xF2, 0xF2, 0xF2, 0xFF): "Test",
            # (0xF4, 0xF4, 0xF4, 0xFF): "Test",
            # (0xF6, 0xF6, 0xF6, 0xFF): "Test",
            # (0xF8, 0xF8, 0xF8, 0xFF): "Test",
            # (0xFA, 0xFA, 0xFA, 0xFF): "Test",
            # (0xFC, 0xFC, 0xFC, 0xFF): "Test",
            # (0xFE, 0xFE, 0xFE, 0x00): "Test",
            # (0xFF, 0xFF, 0xFF, 0x00): "Test",
            # (0xFF, 0xFF, 0xFF, 0xFF): "Test",
        }

    def _get_all_vertex_colors(self):
        print(f"Texture Count: {self._texture_count}")
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
    COPY_FILE_DIR = FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    FILE_NAME = "77CF08"
    JSON_FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Specific_Models/Levels/Mumbos_Mountain/MM_Presets/"
    from shutil import copy
    ### FULL BODY TESTING ###
    # NEW_FILE_NAME = "Grayscale"
    # red_ratio, green_ratio, blue_ratio, brightness = 0x1, 0x1, 0x1, "Default"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "TTC_A_Models/" + FILE_NAME + "-" + NEW_FILE_NAME + ".bin")
    # level_model_obj = LEVEL_MODEL_CLASS(FILE_DIR + "TTC_A_Models/", FILE_NAME + "-" + NEW_FILE_NAME)
    # level_model_obj._full_model_color_shift(red_ratio, green_ratio, blue_ratio, brightness)

    ### SINGLE TESTING ###
    JSON_FILE_NAME = "Treasure_Trove_Cove.json"
    copy(COPY_FILE_DIR + FILE_NAME + ".bin", FILE_DIR + "MM_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    level_model_obj = MM_A_MODEL_CLASS(FILE_DIR + "MM_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    # level_model_obj._get_all_vertex_colors()
    level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    # from os import listdir
    # for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
    #     print(JSON_FILE_NAME)
    #     copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "TTC_A_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    #     level_model_obj = LEVEL_MODEL_CLASS(FILE_DIR + "TTC_A_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    #     level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])