import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class FB_GRUNTY_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Grunty_Broomstick_Front",
            1: "Grunty_Broomstick_Back",
            2: "Grunty_Scarf_&_Socks",
            4: "Grunty_Eyes",
            5: "Grunty_Shoes",
            # Where Are These?
            # 3: "Unk",
            # 6: "Unk",
        }
        self._texture_specific_dict = {}
        self._vertex_dict = {
            (0x38, 0x00, 0x00, 0xFF): "Grunty_Dress_Inside",
            (0x78, 0x00, 0x00, 0xFF): "Grunty_Dress_Inside",
            (0xC8, 0x01, 0x00, 0xFF): "Grunty_Dress_Inside",
            (0x1D, 0x31, 0x02, 0xFF): "Grunty_Skin",
            (0x30, 0x58, 0x05, 0xFF): "Grunty_Skin",
            (0x64, 0x9F, 0x0C, 0xFF): "Grunty_Skin",
            (0xF9, 0xFF, 0x4B, 0xFF): "Grunty_Skin",
            (0xA1, 0xDF, 0x18, 0xFF): "Grunty_Skin",
            (0xD7, 0xF1, 0x32, 0xFF): "Grunty_Skin",
            (0x61, 0x08, 0x1F, 0xFF): "Grunty_Mouth",
            (0xA3, 0x10, 0x36, 0xFF): "Grunty_Mouth",
            (0xFF, 0x34, 0x52, 0xFF): "Grunty_Mouth",
        }
        for vert_count in range(0xA, 0x1A + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Hat"
        for vert_count in range(0x3C2, 0x3D5 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Hat"
        for vert_count in range(0xAB, 0xB6 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Hair"
        for vert_count in range(0x227, 0x258 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Shoes"
        for vert_count in range(0x227, 0x258 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Shoes"
        for vert_count in range(0x2D, 0x37 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Teeth"
        for vert_count in range(0xBF, 0xC8 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Teeth"
        for vert_count in range(0xBF, 0xC8 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Teeth"
        for vert_count in range(0x15E, 0x173 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Main"
        for vert_count in range(0x1B7, 0x1C6 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Sleeve"
        for vert_count in range(0x217, 0x226 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Sleeve"
        for vert_count in range(0x259, 0x268 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Pants"
        for vert_count in range(0x3EE, 0x40D + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Sleeve"

if __name__ == '__main__':
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    FILE_NAME = "3E7F10"
    JSON_FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Specific_Models/Important_Characters/Gruntilda_Model_Presets/"
    from shutil import copy
    ### FULL BODY TESTING ###
    # NEW_FILE_NAME = "Blue"
    # red_ratio, green_ratio, blue_ratio, brightness = 0x0, 0x0, 0x1, "Default"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "FB_Gruntilda_Models/" + FILE_NAME + "-" + NEW_FILE_NAME + ".bin")
    # fb_grunty_model_obj = FB_GRUNTY_MODEL_CLASS(FILE_DIR + "FB_Gruntilda_Models/", FILE_NAME + "-" + NEW_FILE_NAME)
    # fb_grunty_model_obj._full_model_color_shift(red_ratio, green_ratio, blue_ratio, brightness)

    ### SINGLE TESTING ###
    # JSON_FILE_NAME = "Gruntilda_&_Broomstick.json"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "FB_Gruntilda_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    # fb_grunty_model_obj = FB_GRUNTY_MODEL_CLASS(FILE_DIR + "FB_Gruntilda_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    # fb_grunty_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    from os import listdir
    for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
        print(JSON_FILE_NAME)
        copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "FB_Gruntilda_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
        fb_grunty_model_obj = FB_GRUNTY_MODEL_CLASS(FILE_DIR + "FB_Gruntilda_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
        fb_grunty_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])