import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class CS_GRUNTY_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._texture_dict = {
            0: "Grunty_Scarf_&_Socks",
            1: "Grunty_Eyes",
            2: "Grunty_Shoes",
            # 3: "Unk",
            # 4: "Unk",
            # 5: "Unk",
            # 6: "Unk",
            # Where Are These?
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
            (0x78, 0x6C, 0x1B, 0xFF): "Grunty_Teeth",
            (0xC2, 0xB1, 0x31, 0xFF): "Grunty_Teeth",
        }
        for vert_count in range(0xD4, 0xDF + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Hair"
        for vert_count in range(0x326, 0x35C + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Shoes"
        for vert_count in range(0xA, 0x1A + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Hat"
        for vert_count in range(0x39B, 0x3AE + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Hat"
        for vert_count in range(0x273, 0x288 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Main"
        for vert_count in range(0x2BB, 0x2C2 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Sleeve"
        for vert_count in range(0x2D0, 0x2DA + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Sleeve"
        for vert_count in range(0x309, 0x310 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Sleeve"
        for vert_count in range(0x31E, 0x325 + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Sleeve"
        for vert_count in range(0x3BF, 0x3DE + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Sleeve"
        for vert_count in range(0x35D, 0x36C + 0x1):
            self._vertex_count_dict[vert_count] = "Grunty_Dress_Pants"

if __name__ == '__main__':
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    FILE_NAME = "2C2608"
    JSON_FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Automated/Game_Assets/Models/Specific_Models/Important_Characters/Gruntilda_Model_Presets/"
    from shutil import copy
    ### FULL BODY TESTING ###
    # NEW_FILE_NAME = "Blue"
    # red_ratio, green_ratio, blue_ratio, brightness = 0x0, 0x0, 0x1, "Default"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "CS_Gruntilda_Models/" + FILE_NAME + "-" + NEW_FILE_NAME + ".bin")
    # fb_grunty_model_obj = CS_GRUNTY_MODEL_CLASS(FILE_DIR + "CS_Gruntilda_Models/", FILE_NAME + "-" + NEW_FILE_NAME)
    # fb_grunty_model_obj._full_model_color_shift(red_ratio, green_ratio, blue_ratio, brightness)

    ### SINGLE TESTING ###
    # JSON_FILE_NAME = "Gruntilda_&_Broomstick.json"
    # copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "CS_Gruntilda_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
    # fb_grunty_model_obj = CS_GRUNTY_MODEL_CLASS(FILE_DIR + "CS_Gruntilda_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
    # fb_grunty_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])

    ### BULK TESTING ###
    from os import listdir
    for JSON_FILE_NAME in listdir(JSON_FILE_DIR):
        print(JSON_FILE_NAME)
        copy(FILE_DIR + FILE_NAME + "-Default.bin", FILE_DIR + "CS_Gruntilda_Models/" + FILE_NAME + "-" + JSON_FILE_NAME[:-5] + ".bin")
        fb_grunty_model_obj = CS_GRUNTY_MODEL_CLASS(FILE_DIR + "CS_Gruntilda_Models/", FILE_NAME + "-" + JSON_FILE_NAME[:-5])
        fb_grunty_model_obj._color_shift_based_on_json(JSON_FILE_DIR, JSON_FILE_NAME[:-5])