import sys
from os import listdir
from shutil import copy
from random import seed, randint

sys.path.append(".")

from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS
from Automated.Game_Assets.Models.Objects.Note_Doors import NOTE_DOOR_CLASS
from Automated.Game_Assets.Models.Objects.Mumbo_Signs import MUMBO_SIGN_CLASS
from Automated.Game_Assets.Models.Important_Characters.BK_Model import BK_MODEL_CLASS
from Automated.Game_Assets.Models.Levels.Mumbos_Mountain.MM_A_Model import MM_A_MODEL_CLASS
from Automated.Game_Assets.Models.Levels.Treasure_Trove_Cove.TTC_A_Model import TTC_A_MODEL_CLASS
from Automated.Game_Assets.Models.Levels.Treasure_Trove_Cove.TTC_B_Model import TTC_B_MODEL_CLASS
from Automated.Game_Assets.Models.Levels.Gruntildas_Lair.Furance_Fun import FURNACE_FUN_MODEL_CLASS
from Automated.Game_Assets.Models.Levels.Gobis_Valley.Matching_Puzzle import MATCHING_PUZZLE_MODEL_CLASS

class MODEL_CLASS():
    def __init__(self, file_dir):
        # CONSTANTS
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        self._MODELS_DIR = "Automated/Game_Assets/Models/"
        self._BK_MODEL_PRESET_DIR = "Important_Characters/BK_Model_Presets/"
        self._MM_MODEL_PRESET_DIR = "Levels/Mumbos_Mountain/MM_Presets/"
        self._TTC_MODEL_PRESET_DIR = "Levels/Treasure_Trove_Cove/TTC_Presets/"
        # VARIABLES
        self._file_dir = file_dir
    
    def _rand_int(self, lower, upper, add_val=0, this_seed=None):
        if(this_seed):
            seed(a=(this_seed + add_val))
        return randint(lower, upper)
    
    def _grayscale_model(self, model_file_pointer):
        try:
            file_name = str(hex(model_file_pointer))[2:].upper() + "-Decompressed"
            model_obj = GENERIC_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, file_name)
            # model_obj._full_model_color_shift(0x01, 0x01, 0x01, brightness="Darker")
            model_obj._full_model_color_shift(0x01, 0x01, 0x01)
        except FileNotFoundError:
            print(f"File Not Found: {file_name}")
        except Exception as e:
            print(f"\tError: {file_name}")
            raise e
    
    def _random_color_model(self, model_file_pointer, additional_scaling, this_seed=None):
        try:
            file_name = str(hex(model_file_pointer))[2:].upper() + "-Decompressed"
            model_obj = GENERIC_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, file_name)
            red_ratio = self._rand_int(0x30, 0xCF, model_file_pointer, this_seed)
            green_ratio = self._rand_int(0x30, 0xCF, model_file_pointer + 1, this_seed)
            blue_ratio = self._rand_int(0x30, 0xCF, model_file_pointer + 2, this_seed)
            model_obj._full_model_color_shift(red_ratio, green_ratio, blue_ratio, brightness=additional_scaling)
        except FileNotFoundError:
            print(f"File Not Found: {file_name}")
        except Exception as e:
            print(f"\tError: {file_name}")
            raise e
    
    def _replace_mm_model(self, selection):
        if((selection + ".json") in listdir(self._file_dir + self._MODELS_DIR + self._MM_MODEL_PRESET_DIR)):
            mm_a_model_obj = MM_A_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "103E8-Decompressed")
            mm_a_model_obj._color_shift_based_on_json(self._file_dir + self._MODELS_DIR + self._MM_MODEL_PRESET_DIR, selection)
        else:
            print("SOMETHING IS HAPPENING")
            print(selection + ".json")
            print(listdir(self._file_dir + self._MODELS_DIR + self._MM_MODEL_PRESET_DIR))
            exit(0)
    
    def _replace_ttc_model(self, selection):
        if((selection + ".json") in listdir(self._file_dir + self._MODELS_DIR + self._TTC_MODEL_PRESET_DIR)):
            ttc_a_model_obj = TTC_A_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "101F0-Decompressed")
            ttc_a_model_obj._color_shift_based_on_json(self._file_dir + self._MODELS_DIR + self._TTC_MODEL_PRESET_DIR, selection)
            ttc_a_model_obj = TTC_B_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "101F8-Decompressed")
            ttc_a_model_obj._color_shift_based_on_json(self._file_dir + self._MODELS_DIR + self._TTC_MODEL_PRESET_DIR, selection)
        else:
            print("SOMETHING IS HAPPENING")
            print(selection + ".json")
            print(listdir(self._file_dir + self._MODELS_DIR + self._TTC_MODEL_PRESET_DIR))
            exit(0)
    
    def _set_note_door_values(self, note_door_value_list):
        note_door_obj = NOTE_DOOR_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "8320-Decompressed")
        for door_num, door_value in enumerate(note_door_value_list):
            note_door_obj._modify_door_count_requirement(door_num, door_value)
    
    def _set_transformation_sign_costs(self, transformation_cost_list):
        mumbo_sign_pointers = ["76A0", "76A8", "76B0", "76B8", "76C0"]
        five_cost_sign_file = f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{mumbo_sign_pointers[0]}-Decompressed.bin"
        for mumbo_sign_pointer in mumbo_sign_pointers[1:]:
            curr_mumbo_sign_file = f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{mumbo_sign_pointer}-Decompressed.bin"
            copy(five_cost_sign_file, curr_mumbo_sign_file)
        for transformation_count, transformation_cost in enumerate(transformation_cost_list):
            mumbo_sign_obj = MUMBO_SIGN_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, f"{mumbo_sign_pointers[transformation_count]}-Decompressed")
            mumbo_sign_obj._clear_cost_image()
            mumbo_sign_obj._modify_cost_image(transformation_cost)
    
    def _reassign_ff_tile_textures(self, ff_tile_dict):
        furnace_fun_model_obj = FURNACE_FUN_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "105D8-Decompressed")
        furnace_fun_model_obj._reassign_ff_tile_textures(ff_tile_dict)
    
    def _furnace_fun_finale(self):
        furnace_fun_model_obj = FURNACE_FUN_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "105D8-Decompressed")
        furnace_fun_model_obj._lower_invisible_barriers()
    
    def _bk_model(self, selection):
        bk_model_obj = BK_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "7908-Decompressed")
        bk_model_obj._color_shift_based_on_json(self._file_dir + self._MODELS_DIR + self._BK_MODEL_PRESET_DIR, selection)

    def _flood_engine_room(self):
        '''
        Currently copies the inside of clanker's belly for water.
        This doesn't work, as it's missing the walkable entrance
        '''
        cc_inside_clanker_b = f"{self._file_dir}{self._EXTRACTED_FILES_DIR}10620-Decompressed.bin"
        rbb_engine_room_b = f"{self._file_dir}{self._EXTRACTED_FILES_DIR}10430-Decompressed.bin"
        copy(cc_inside_clanker_b, rbb_engine_room_b)
        rbb_engine_room_b_model_obj = GENERIC_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "10430-Decompressed")
        rbb_engine_room_b_model_obj._get_object_vertex_header_info()
        for count in range(rbb_engine_room_b_model_obj._vertex_count):
            vertex_info_index_start, x_position, y_position, z_position, u_mapping, v_mapping, red_val, green_val, blue_val, alpha_val = rbb_engine_room_b_model_obj._get_vertex_info(count)
            new_x = rbb_engine_room_b_model_obj._possible_negative_to_positive(x_position+750, 2)
            new_y = rbb_engine_room_b_model_obj._possible_negative_to_positive(y_position-600, 2)
            new_z = rbb_engine_room_b_model_obj._possible_negative_to_positive(z_position-1500, 2)
            rbb_engine_room_b_model_obj._set_vertex_xyz_coords(count, new_x, new_y, new_z)
        rbb_engine_room_b_model_obj._full_model_color_shift(0x12, 0x26, 0x50)
    
    def _reassign_gv_matching_puzzle_tiles(self, gv_mp_tile_dict):
        matching_puzzle_model_obj = MATCHING_PUZZLE_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "10248-Decompressed")
        matching_puzzle_model_obj._reassign_gv_mp_tile_textures(gv_mp_tile_dict)
    
    ####################
    ### BANJO SOULIE ###
    ####################

    def _banjo_soulie_furnace_fun_map(self):
        furnace_fun_model_obj = FURNACE_FUN_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "105D8-Decompressed")
        furnace_fun_model_obj._lower_invisible_barriers()
        # furnace_fun_model_obj._remove_board_textures()
        # for texture_count in range(17, 25):
        #     furnace_fun_model_obj._invisible_side_textures(texture_count)
        # for texture_count in range(44, 51):
        #     furnace_fun_model_obj._invisible_side_textures(texture_count)
        # furnace_fun_model_obj._invisible_side_textures(64)