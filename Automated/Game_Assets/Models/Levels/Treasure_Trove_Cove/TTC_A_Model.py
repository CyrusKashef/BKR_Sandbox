import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class TTC_A_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Floor",
            1: "Road",
            2: "Mountain",
            3: "Walls",
            4: "Walls",
            5: "Walls",
            6: "Walls",
            7: "Platforms",
            8: "Pools",
            9: "Sandcastle",
            10: "Sandcastle",
            11: "Pools",
            12: "Mountain",
            13: "Mountain",
            14: "Mountain",
            15: "Mountain",
            16: "Mountain",
            17: "Mountain",
            18: "Mountain",
            19: "Mountain",
            20: "Brick_Walls",
            21: "Brick_Walls",
            22: "Brick_Floors",
            23: "Brick_Walls",
            24: "Brick_Walls",
            25: "Bramble",
            26: "Mountain",
            27: "Wood_Top",
            28: "Wood_Top",
            29: "Mountain",
            30: "Wood_Sides",
            31: "Wood_Sides",
            32: "Mountain",
            33: "Grass",
            34: "Boxes",
            35: "Boxes",
            36: "Grass",
            37: "Wood_Sides",
            38: "Boxes",
            39: "Boxes",
            40: "Wood_Sides",
            41: "Wood_Sides",
            42: "Wood_Sides",
            43: "Wood_Sides",
            44: "Wood_Sides",
            45: "Wood_Sides",
            46: "Wood_Sides",
            47: "Salty_Hippo",
            48: "Salty_Hippo",
            49: "Wood_Top",
            50: "Fence",
        }
        self._vertex_dict = {
            (0x00, 0x80, 0x00, 0xFF): "Brick_Walls",
            (0x48, 0x48, 0x55, 0xFF): "Skip",
            (0x4E, 0x4E, 0x5D, 0xFF): "Skip",
            (0x50, 0x50, 0x80, 0xFF): "Skip",
            (0x54, 0x4A, 0x1B, 0xFF): "Floor",
            (0x55, 0x55, 0x65, 0xFF): "Skip",
            (0x58, 0x58, 0x8C, 0xFF): "Skip",
            (0x5B, 0x51, 0x1E, 0xFF): "Floor",
            (0x60, 0x55, 0x1F, 0xFF): "Walls",
            (0x62, 0x62, 0x74, 0xFF): "Skip",
            (0x63, 0x58, 0x20, 0xFF): "Floor",
            (0x72, 0x65, 0x25, 0xFF): "Floor",
            (0x81, 0x73, 0x2A, 0x00): "Floor",
            (0x81, 0x73, 0x2A, 0xFF): "Floor",
            (0x90, 0x80, 0x2F, 0xFF): "Floor",
            (0x9F, 0x8D, 0x34, 0xFF): "Floor",
            (0xAE, 0x9B, 0x39, 0xFF): "Sandcastle",
            (0xBD, 0xA8, 0x3E, 0xFF): "Floor",
            (0x00, 0x00, 0x00, 0xFF): "Skip",
            (0x28, 0x28, 0x28, 0xFF): "Floor",
            (0x3C, 0x3C, 0x3C, 0xFF): "Floor",
            (0x44, 0x44, 0x44, 0xFF): "Mountain",
            (0x48, 0x48, 0x48, 0xFF): "Mountain",
            (0x50, 0x50, 0x50, 0xFF): "Floor",
            (0x5A, 0x5A, 0x5A, 0xFF): "Skip",
            (0x5C, 0x5C, 0x5C, 0xFF): "Skip",
            (0x60, 0x60, 0x60, 0xFF): "Walls",
            (0x62, 0x62, 0x62, 0xFF): "Skip",
            (0x64, 0x64, 0x64, 0xFF): "Floor",
            (0x66, 0x66, 0x66, 0xFF): "Walls",
            (0x6A, 0x6A, 0x6A, 0xFF): "Walls",
            (0x6F, 0x6F, 0x83, 0x00): "Skip",
            (0x6F, 0x6F, 0x83, 0xFF): "Skip",
            (0x70, 0x70, 0x70, 0xFF): "Skip",
            (0x72, 0x72, 0x72, 0xFF): "Boxes",
            (0x78, 0x78, 0x78, 0xFF): "Walls",
            (0x7C, 0x7C, 0x92, 0xFF): "Skip",
            (0x7E, 0x7E, 0x7E, 0xFF): "Floor",
            (0x84, 0x84, 0x84, 0xFF): "Skip",
            (0x89, 0x89, 0xA1, 0xFF): "Skip",
            (0x8A, 0x8A, 0x8A, 0xFF): "Walls",
            (0x8C, 0x8C, 0x8C, 0xFF): "Skip",
            (0x96, 0x96, 0x96, 0xFF): "Walls",
            (0x96, 0x96, 0xB1, 0xFF): "Skip",
            (0x98, 0x98, 0x98, 0xFF): "Skip",
            (0x9A, 0x9A, 0x9A, 0x00): "Skip",
            (0x9A, 0x9A, 0x9A, 0xFF): "Skip",
            (0x9C, 0x9C, 0x9C, 0xFF): "Boxes",
            (0x9D, 0x9D, 0x9D, 0xFF): "Skip",
            (0x9E, 0x9E, 0x9E, 0xFF): "Skip",
            (0xA0, 0xA0, 0xA0, 0xFF): "Skip",
            (0xA1, 0xA1, 0xA1, 0xFF): "Mountain",
            (0xA3, 0xA3, 0xC0, 0xFF): "Skip",
            (0xA4, 0xA4, 0xA4, 0xFF): "Skip",
            (0xA5, 0xA5, 0xA5, 0xFF): "Skip",
            (0xA8, 0xA8, 0xA8, 0xFF): "Skip",
            (0xAA, 0xAA, 0xAA, 0xFF): "Skip",
            (0xAC, 0xAC, 0xAC, 0xFF): "Skip",
            (0xAF, 0xAF, 0xAF, 0xFF): "Pools",
            (0xB0, 0xB0, 0xB0, 0xFF): "Floor",
            (0xB2, 0xB2, 0xB2, 0xFF): "Walls",
            (0xB4, 0xB4, 0xB4, 0xFF): "Walls",
            (0xB8, 0xB8, 0xB8, 0xFF): "Floor",
            (0xB9, 0x01, 0x01, 0xFF): "Skip",
            (0xBA, 0xBA, 0xBA, 0xFF): "Floor",
            (0xBB, 0xBB, 0xBB, 0x00): "Skip",
            (0xBB, 0xBB, 0xBB, 0xFF): "Skip",
            (0xBC, 0xBC, 0xBC, 0x00): "Skip",
            (0xBC, 0xBC, 0xBC, 0xFF): "Skip",
            (0xBD, 0xBD, 0xBD, 0xFF): "Skip",
            (0xBE, 0xBE, 0xBE, 0xFF): "Pools",
            (0xC0, 0xC0, 0xC0, 0xFF): "Mountain",
            (0xC2, 0xC2, 0xC2, 0xFF): "Mountain",
            (0xC4, 0xC4, 0xC4, 0xFF): "Floor",
            (0xC6, 0xC6, 0xC6, 0xFF): "Skip",
            (0xC7, 0xC7, 0xC7, 0x00): "Skip",
            (0xC7, 0xC7, 0xC7, 0xFF): "Fence",
            (0xC8, 0xC8, 0xC8, 0xFF): "Skip",
            (0xC9, 0xC9, 0xC9, 0x00): "Skip",
            (0xC9, 0xC9, 0xC9, 0xFF): "Fence",
            (0xCC, 0xCC, 0xCC, 0xFF): "Wood_Sides",
            (0xD0, 0xD0, 0xD0, 0xFF): "Skip",
            (0xD2, 0xD2, 0xD2, 0xFF): "Pools",
            (0xD4, 0xD4, 0xD4, 0xFF): "Skip",
            (0xD5, 0xD5, 0xD5, 0xFF): "Brick_Walls",
            (0xD6, 0xD6, 0xD6, 0xFF): "Floor",
            (0xDC, 0xDC, 0xDC, 0xFF): "Skip",
            (0xE4, 0xE4, 0xE4, 0xFF): "Skip",
            (0xE6, 0xE6, 0xE6, 0xFF): "Pools",
            (0xE8, 0xE8, 0xE8, 0xFF): "Skip",
            (0xEA, 0xEA, 0xEA, 0xFF): "Skip",
            (0xEC, 0xEC, 0xEC, 0xFF): "Skip",
            (0xEE, 0xEE, 0xEE, 0xFF): "Skip",
            (0xF0, 0xF0, 0xF0, 0xFF): "Skip",
            (0xF2, 0xF2, 0xF2, 0xFF): "Skip",
            (0xF4, 0xF4, 0xF4, 0xFF): "Skip",
            (0xF6, 0xF6, 0xF6, 0xFF): "Skip",
            (0xF8, 0xF8, 0xF8, 0xFF): "Skip",
            (0xFA, 0xFA, 0xFA, 0xFF): "Skip",
            (0xFC, 0xFC, 0xFC, 0xFF): "Skip",
            (0xFE, 0xFE, 0xFE, 0x00): "Skip",
            (0xFF, 0x01, 0x01, 0x00): "Skip",
            (0xFF, 0x01, 0x01, 0xFF): "Skip",
            (0xFF, 0xFF, 0xFF, 0x00): "Skip",
            (0xFF, 0xFF, 0xFF, 0xFF): "Skip",
        }

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
    FILE_NAME = "5D93D0"
    JSON_FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Specific_Models/Levels/Treasure_Trove_Cove/TTC_Presets/"
    from shutil import copy
    ### FULL BODY TESTING ###
    # NEW_FILE_NAME = "Grayscale"
    # red_ratio, green_ratio, blue_ratio, brightness = 0x1, 0x1, 0x1, "Default"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "TTC_A_Models/" + FILE_NAME + "-" + NEW_FILE_NAME + ".bin")
    # level_model_obj = LEVEL_MODEL_CLASS(FILE_DIR + "TTC_A_Models/", FILE_NAME + "-" + NEW_FILE_NAME)
    # level_model_obj._full_model_color_shift(red_ratio, green_ratio, blue_ratio, brightness)

    ### SINGLE TESTING ###
    JSON_FILE_NAME = "Rusty_Bucket_Bay.json"
    copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "TTC_A_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    level_model_obj = TTC_A_MODEL_CLASS(FILE_DIR + "TTC_A_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    level_model_obj._get_all_vertex_colors()
    level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    # from os import listdir
    # for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
    #     print(JSON_FILE_NAME)
    #     copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "TTC_A_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    #     level_model_obj = LEVEL_MODEL_CLASS(FILE_DIR + "TTC_A_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    #     level_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])