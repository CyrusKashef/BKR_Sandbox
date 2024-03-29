import sys
from shutil import copy
import os
from os import listdir
from random import seed, randint, choice, choices, shuffle, sample

if __name__ == '__main__':
    from Generic_File import GENERIC_FILE_CLASS
else:
    from .Generic_File import GENERIC_FILE_CLASS

sys.path.append(".")
from Automated.Extract_And_Insert.BK_ROM import BK_ROM_CLASS
from Automated.Extract_And_Insert.Decompress import DECOMPRESS_CLASS
from Automated.Extract_And_Insert.Compress import COMPRESS_CLASS
from Automated.Clean_Up.Clean_Up import CLEAN_UP_CLASS
if __name__ == '__main__':
    from Assembly.Assembly_Class import ASSEMBLY_CLASS
else:
    from .Assembly.Assembly_Class import ASSEMBLY_CLASS

from Automated.Game_Assets.Models.Model_Class import MODEL_CLASS
from Automated.Game_Assets.Sounds.Sound_Class import SOUND_CLASS
from Automated.Game_Assets.Speeches.Speech_Class import SPEECH_CLASS
from Automated.Game_Assets.Setups.Setup_Class import SETUP_CLASS

from Data_Files.Asset_Table_Pointer_Dict import ASSET_TABLE_POINTER_DICT
from Data_Files.Skybox_And_Cloud_Dict import SKYBOX_AND_CLOUD_DICT

from Data_Files.Speeches import (
    Cheato_Speech_Dicts,
    Game_Over_Cutscene_Speeches,
    General_Speech_Dict,
    Gruntilda_Lair_Quip_Lists,
    Intro_Bottles_Speech_Dicts,
    Move_Speech_Dict,
)

from Data_Files.Enums.Map_Enums import MAP_ENUMS
from Data_Files.Enums.Warp_Enums import WARP_ENUMS
from Data_Files.Enums.World_Enums import WORLD_ENUMS
from Data_Files.Enums.Ability_Enums import ABILITY_ENUMS

from Data_Files.Speeches.General_Speech_Dict import SHORTEN_BOTTLES_SECRET_GAME_SPEECH_DICT

from Data_Files.Setups.Map_Setup_Pointer_Dict import MAP_SETUP_POINTER_DICT

class AUTOMATED_CLASS():
    def __init__(self, file_dir, original_rom_path, new_rom_path):
        ### CONSTANTS ###
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        self._COMPRESSED_BIN_EXTENSION = "-Compressed.bin"
        self._DECOMPRESSED_BIN_EXTENSION = "-Decompressed.bin"
        self._MODELS_DIR = "Automated/Game_Assets/Models/"
        self._BK_MODEL_PRESET_DIR = "Important_Characters/BK_Model_Presets/"
        self._BK_TERMITE_MODEL_PRESET_DIR = "Important_Characters/BK_Termite_Model_Presets/"
        self._BK_CROCODILE_MODEL_PRESET_DIR = "Important_Characters/BK_Crocodile_Model_Presets/"
        self._BK_WALRUS_MODEL_PRESET_DIR = "Important_Characters/BK_Walrus_Model_Presets/"
        self._BK_PUMPKIN_MODEL_PRESET_DIR = "Important_Characters/BK_Pumpkin_Model_Presets/"
        self._BK_BEE_MODEL_PRESET_DIR = "Important_Characters/BK_Bee_Model_Presets/"
        ### VARIABLES ###
        self._file_dir = file_dir
        self._make_copy_of_ROM(original_rom_path, new_rom_path)
        self._bk_rom_obj = BK_ROM_CLASS(file_dir, new_rom_path)
        self._assembly_obj = None
        self._automated_speech_obj = None
        self._setup_obj = None
        self._sound_obj = None
        self._model_obj = None
        self._clean_up_obj = None
        self._seed = None
    
    def _make_copy_of_ROM(self, original_rom_path, new_rom_path):
        print("Make Copy Of ROM")
        copy(original_rom_path, new_rom_path)

    ########################
    ### RANDOM FUNCTIONS ###
    ########################
    # Functions for selecting random values

    def _set_seed(self, seed_val):
        self._seed = seed_val
    
    def _rand_int(self, lower, upper, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return randint(lower, upper)
    
    def _rand_choice(self, this_list, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return choice(this_list)
    
    def _rand_choice_weighted(self, this_dict, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return choices(list(this_dict.keys()), weights=this_dict.values(), k=1)[0]
    
    def _rand_shuffle(self, list, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        shuffle(list)
        return list
    
    def _rand_sample(self, list, sample_count, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        sample_list = sample(list, sample_count)
        return sample_list

    ############################
    ### EXTRACT & DECOMPRESS ###
    ############################
    # Pulls files out of the ROM and decompresses the files

    def _extract_and_decompress_asset_category(self, asset_category):
        print(f"Decompress Asset Category: {asset_category}")
        pointer_start = ASSET_TABLE_POINTER_DICT[asset_category]["Start"]
        pointer_end = ASSET_TABLE_POINTER_DICT[asset_category]["End"]
        self._bk_rom_obj._extract_pointer_table_assets(pointer_start, pointer_end)
        for pointer in range(pointer_start, pointer_end+1, 0x8):
            decompress_obj = DECOMPRESS_CLASS(self._file_dir, pointer)
            decompress_obj._decompress_main()

    # def _extract_and_decompress_all_assets(self):
    #     print("Decompress All Assets")
    #     for asset_category in ASSET_TABLE_POINTER_DICT:
    #         self._extract_and_decompress_asset_category(asset_category)
    
    def _extract_and_decompress_all_assets(self):
        print("Decompress All Assets")
        self._bk_rom_obj._extract_all_asset_table_pointers()
        for pointer in range(self._bk_rom_obj._ASSET_TABLE_START_INDEX, self._bk_rom_obj._ASSET_TABLE_END_INDEX+1, 0x8):
            decompress_obj = DECOMPRESS_CLASS(self._file_dir, pointer)
            decompress_obj._decompress_main()
    
    def _extract_and_decompress_all_asm(self):
        print("Decompress All ASM")
        self._asm_pointer_address_dict = self._bk_rom_obj._extract_all_asm()
        for asm_file in self._asm_pointer_address_dict:
            decompress_obj = DECOMPRESS_CLASS(self._file_dir, self._asm_pointer_address_dict[asm_file]["Code"])
            decompress_obj._decompress_main()
            decompress_obj = DECOMPRESS_CLASS(self._file_dir, self._asm_pointer_address_dict[asm_file]["Data"])
            decompress_obj._decompress_main()

    #########################
    ### COMPRESS & INSERT ###
    #########################
    # Compresses the files and inserts them back into the ROM
    # Most likely requires pointer adjustments

    def _compress_and_insert_asset_category(self, asset_category, skip_pointer_list=[]):
        print(f"Compress Asset Category: {asset_category}")
        pointer_start = ASSET_TABLE_POINTER_DICT[asset_category]["Start"]
        pointer_end = ASSET_TABLE_POINTER_DICT[asset_category]["End"]
        for pointer in range(pointer_start, pointer_end+1, 0x8):
            compress_obj = COMPRESS_CLASS(self._file_dir, pointer)
            file_exists = compress_obj._compress_main(b"\xAA", 0x8)
            if(not file_exists):
                skip_pointer_list.append(pointer)
        self._bk_rom_obj._insert_pointer_table_assets(pointer_start, pointer_end, skip_pointer_list)
    
    def _compress_and_insert_all_assets(self, skip_pointer_list=[]):
        print("Compress & Insert All Assets")
        for asset_category in ASSET_TABLE_POINTER_DICT:
            self._compress_and_insert_asset_category(asset_category, skip_pointer_list)
    
    def _compress_and_append_all_asset_table_pointers(self):
        print("Compress & Append All Assets")
        skip_pointer_list=[]
        for pointer in range(self._bk_rom_obj._ASSET_TABLE_START_INDEX, self._bk_rom_obj._ASSET_TABLE_END_INDEX+1, 0x8):
            compress_obj = COMPRESS_CLASS(self._file_dir, pointer)
            file_exists = compress_obj._compress_main(b"\xAA", 0x8)
            if(not file_exists):
                skip_pointer_list.append(pointer)
        self._bk_rom_obj._append_all_asset_table_pointers(skip_pointer_list)

    def _compress_and_insert_all_asm(self):
        print("Compress & Insert All ASM")
        curr_address = self._asm_pointer_address_dict["C_Library"]["Code"]
        for asm_section, asm_section_name in enumerate(self._asm_pointer_address_dict):
            print(f"ASM Section Name: {asm_section_name}")
            # self._bk_rom_obj._write_asm_address(asm_section, curr_address) # This should work, but it doesn't :(
            old_code_index_start = self._asm_pointer_address_dict[asm_section_name]["Code"]
            if(curr_address > old_code_index_start):
                print(f"Last File Was Too Big: {asm_section_name}")
                raise SystemError(f"Last File Was Too Big: {asm_section_name}")
            code_compress_obj = COMPRESS_CLASS(self._file_dir, old_code_index_start)
            code_compress_obj._compress_main(padding=None, padding_interval=1)
            old_data_index_start = self._asm_pointer_address_dict[asm_section_name]["Data"]
            data_compress_obj = COMPRESS_CLASS(self._file_dir, old_data_index_start)
            data_compress_obj._compress_main(padding=None, padding_interval=1)
            # curr_address = self._bk_rom_obj._insert_asm(curr_address, old_code_index_start, old_data_index_start) # This should work, but it doesn't :(
            curr_address = self._bk_rom_obj._insert_asm(old_code_index_start, old_code_index_start, old_data_index_start)
    
    def _remove_known_anti_tampering(self):
        print("Remove Known Anti-Tampering")
        self._assembly_class_creation()
        self._assembly_obj._remove_known_anti_tampering()
    
    def _core_checksums(self):
        print("Core Checksums")
        self._assembly_class_creation()
        core_checksum_dict = self._assembly_obj._adjust_core_checksums()
        self._bk_rom_obj._write_bytes(0x5E78, 4, core_checksum_dict["Code_CRC1"])
        self._bk_rom_obj._write_bytes(0x5E7C, 4, core_checksum_dict["Code_CRC2"])
        self._bk_rom_obj._write_bytes(0x5E80, 4, core_checksum_dict["Vars_CRC1"])
        self._bk_rom_obj._write_bytes(0x5E84, 4, core_checksum_dict["Vars_CRC2"])
    
    def _adjust_crc(self):
        print("Adjust CRC")
        self._bk_rom_obj._adjust_crc()

    #######################    
    ### CLASS CREATIONS ###
    #######################
    # These create classes that have functions for modifying files
    # It just makes this file look cleaner and makes functions
    # easier to find

    def _assembly_class_creation(self):
        if(not self._assembly_obj):
            self._assembly_obj = ASSEMBLY_CLASS(self._file_dir)
    
    def _automated_speech_class_creation(self):
        if(not self._automated_speech_obj):
            self._automated_speech_obj = SPEECH_CLASS(self._file_dir)
    
    def _setup_class_creation(self):
        if(not self._setup_obj):
            self._setup_obj = SETUP_CLASS(self._file_dir)
    
    def _sound_class_creation(self):
        if(not self._sound_obj):
            self._sound_obj = SOUND_CLASS(self._file_dir)
    
    def _model_class_creation(self):
        if(not self._model_obj):
            self._model_obj = MODEL_CLASS(self._file_dir)
    
    def _clean_up_class_creation(self):
        if(not self._clean_up_obj):
            self._clean_up_obj = CLEAN_UP_CLASS(self._file_dir)
    
    ##############
    ### MODELS ###
    ##############
    # These are functions for model stuff
    # can be selected on the GUI,
    # but might also trigger from other features

    def _replace_bk_model(self, preset_selection):
        print("Replace BK Model")
        self._assembly_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        if((adjusted_selection + ".json") in listdir(self._file_dir + self._MODELS_DIR + self._BK_MODEL_PRESET_DIR)):
            self._model_class_creation()
            self._model_obj._bk_model(adjusted_selection)
            self._assembly_obj._replace_bk_model_with_asset(0x34E)
        elif(preset_selection in GUI_MODELS_DICT):
            asset = GUI_MODELS_DICT[preset_selection]
            self._assembly_obj._replace_bk_model_with_asset(asset)
        else:
            print("Replace BK Model Error: {preset_selection}")
            exit(0)
    
    def _replace_bk_termite_model(self, preset_selection):
        print("Replace BK Termite Model")
        self._model_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        if((adjusted_selection + ".json") in listdir(self._file_dir + self._MODELS_DIR + self._BK_TERMITE_MODEL_PRESET_DIR)):
            self._model_class_creation()
            self._model_obj._bk_model(adjusted_selection)
        elif(preset_selection in GUI_MODELS_DICT):
            asset = GUI_MODELS_DICT[preset_selection]
            self._assembly_obj._replace_bk_termite_model_with_asset(asset)
        else:
            print("Replace BK Termite Model Error: {preset_selection}")
            exit(0)
    
    def _replace_bk_crocodile_model(self, preset_selection):
        print("Replace BK Crocodile Model")
        self._model_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        if((adjusted_selection + ".json") in listdir(self._file_dir + self._MODELS_DIR + self._BK_CROCODILE_MODEL_PRESET_DIR)):
            self._model_class_creation()
            self._model_obj._bk_model(adjusted_selection)
        elif(preset_selection in GUI_MODELS_DICT):
            asset = GUI_MODELS_DICT[preset_selection]
            self._assembly_obj._replace_bk_crocodile_model_with_asset(asset)
        else:
            print("Replace BK Termite Model Error: {preset_selection}")
            exit(0)
    
    def _replace_bk_walrus_model(self, preset_selection):
        print("Replace BK Walrus Model")
        self._model_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        if((adjusted_selection + ".json") in listdir(self._file_dir + self._MODELS_DIR + self._BK_WALRUS_MODEL_PRESET_DIR)):
            self._model_class_creation()
            self._model_obj._bk_model(adjusted_selection)
        elif(preset_selection in GUI_MODELS_DICT):
            asset = GUI_MODELS_DICT[preset_selection]
            self._assembly_obj._replace_bk_walrus_model_with_asset(asset)
        else:
            print("Replace BK Termite Model Error: {preset_selection}")
            exit(0)
    
    def _replace_bk_pumpkin_model(self, preset_selection):
        print("Replace BK Pumpkin Model")
        self._model_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        if((adjusted_selection + ".json") in listdir(self._file_dir + self._MODELS_DIR + self._BK_PUMPKIN_MODEL_PRESET_DIR)):
            self._model_class_creation()
            self._model_obj._bk_model(adjusted_selection)
        elif(preset_selection in GUI_MODELS_DICT):
            asset = GUI_MODELS_DICT[preset_selection]
            self._assembly_obj._replace_bk_pumpkin_model_with_asset(asset)
        else:
            print("Replace BK Termite Model Error: {preset_selection}")
            exit(0)
    
    def _replace_bk_bee_model(self, preset_selection):
        print("Replace BK Bee Model")
        self._model_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        if((adjusted_selection + ".json") in listdir(self._file_dir + self._MODELS_DIR + self._BK_BEE_MODEL_PRESET_DIR)):
            self._model_class_creation()
            self._model_obj._bk_model(adjusted_selection)
        elif(preset_selection in GUI_MODELS_DICT):
            asset = GUI_MODELS_DICT[preset_selection]
            self._assembly_obj._replace_bk_bee_model_with_asset(asset)
        else:
            print("Replace BK Termite Model Error: {preset_selection}")
            exit(0)
    
    def _replace_bk_wishywashy_model(self, preset_selection):
        print("Replace BK Wishywashy Model")
        self._model_class_creation()
        if(preset_selection in GUI_MODELS_DICT):
            asset = GUI_MODELS_DICT[preset_selection]
            self._assembly_obj._replace_bk_wishywashy_model_with_asset(asset)
        else:
            print("Replace BK Termite Model Error: {preset_selection}")
            exit(0)

    def _grayscale_category(self, category, skip_pointer=[]):
        print("Grayscale Category")
        self._model_class_creation()
        pointer_start = ASSET_TABLE_POINTER_DICT[category]["Start"]
        pointer_end = ASSET_TABLE_POINTER_DICT[category]["End"]
        for pointer in range(pointer_start, pointer_end+1, 0x8):
            if(pointer not in skip_pointer):
                self._model_obj._grayscale_model(pointer)

    def _random_color_category(self, category, additional_scaling=1, skip_pointer=[]):
        print("Randomize Color Category")
        self._model_class_creation()
        pointer_start = ASSET_TABLE_POINTER_DICT[category]["Start"]
        pointer_end = ASSET_TABLE_POINTER_DICT[category]["End"]
        for pointer in range(pointer_start, pointer_end+1, 0x8):
            if(pointer not in skip_pointer):
                self._model_obj._random_color_model(pointer, additional_scaling, self._seed)

    def _replace_skyboxes_and_cloud(self, adjusted_selection):
        print("Replace Skyboxes And Clouds")
        self._assembly_class_creation()
        if(adjusted_selection in SKYBOX_AND_CLOUD_DICT):
            for map_count in SKYBOX_AND_CLOUD_DICT["Treasure_Trove_Cove"]["Map_Count"]:
                self._assembly_obj._set_skybox_and_clouds(map_count,
                                SKYBOX_AND_CLOUD_DICT[adjusted_selection]["Skybox"],
                                SKYBOX_AND_CLOUD_DICT[adjusted_selection]["Cloud1"],
                                SKYBOX_AND_CLOUD_DICT[adjusted_selection]["Cloud2"])

    def _replace_mm_model(self, preset_selection):
        print("Replace MM Model")
        self._model_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        self._model_obj._replace_mm_model(adjusted_selection)
        self._replace_skyboxes_and_cloud(adjusted_selection)

    def _replace_ttc_model(self, preset_selection):
        print("Replace TTC Model")
        self._model_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        self._model_obj._replace_ttc_model(adjusted_selection)
        self._replace_skyboxes_and_cloud(adjusted_selection)

    ###########################
    ###### GUI FUNCTIONS ######
    ###########################
    # These are functions you'd probably hand select from the GUI
    # there's potential for these to be randomized

    def _starting_lives(self, starting_life_count):
        print("Starting Lives")
        self._assembly_class_creation()
        self._assembly_obj._starting_lives(starting_life_count)
    
    def _starting_health(self, start_health_val, default_cap=True):
        print("Starting Health")
        self._assembly_class_creation()
        self._assembly_obj._starting_max_health(start_health_val, default_cap)
    
    def _empty_honeycombs_for_extra_health(self, eh_val):
        print("Empty Honeycombs For Extra Health")
        self._assembly_class_creation()
        self._assembly_obj._empty_honeycombs_for_extra_health(eh_val)
    
    def _starting_inventory_counts(self, start_val):
        print("Starting Inventory Counts")
        self._assembly_class_creation()
        self._assembly_obj._starting_inventory_counts(start_val)
    
    def _transformation_costs(self, transformation_cost_dict):
        print("Transformation Costs")
        self._assembly_class_creation()
        self._assembly_obj._transformation_costs(transformation_cost_dict)
    
    def _carrying_capacity(self, capacity_dict):
        print("Carrying Capacity")
        self._assembly_class_creation()
        self._assembly_obj._carrying_capacity(capacity_dict)
    
    def _randomize_skybox_and_clouds(self):
        print("Randomize Skybox And Clouds")
        self._assembly_class_creation()
        self._assembly_obj._randomize_skybox_and_clouds(self._seed)
    
    def _randomize_collisions(self):
        print("Randomize Collisions")
        self._assembly_class_creation()
        self._assembly_obj._modify_collision_markers(self._seed, effect_to_bk_option="Randomize", sound_effect_option="Randomize",
                                                     bk_damage_option="Randomize", hit_count_option="Randomize", num_of_honeycombs_option="Randomize")

    def _remove_hut_notes(self):
        print("Remove Hut Notes")
        self._assembly_class_creation()
        self._assembly_obj._remove_hut_notes()
        
    def _clear_setup_files(self):
        print("Clear Setup Files")
        self._setup_class_creation()
        self._setup_obj._clear_setup_files()
    
    def _enemy_note_drop(self, note_count1, note_count2, note_count3):
        print("Enemy Note Drop")
        # automated_obj._enemy_note_drop(note_count1=3, note_count2=6, note_count3=9)
        self._assembly_class_creation()
        self._assembly_obj._enemy_note_drops(note_count1, note_count2, note_count3)
    
    def _exit_to_witchs_lair(self):
        print("Exit To Witchs Lair")
        self._assembly_class_creation()
        self._assembly_obj._exit_to_witchs_lair()
    
    def _fallproof(self):
        print("Fallproof")
        self._assembly_class_creation()
        self._assembly_obj._fallproof()
    
    def _jiggy_win_condition(self, jiggy_count):
        print("Jiggy Win Condition")
        self._assembly_class_creation()
        self._assembly_obj._jiggy_win_condition(jiggy_count)
    
    def _note_count_win_condition(self, note_count):
        print("Note Count Win Condition")
        self._assembly_class_creation()
        self._assembly_obj._note_count_win_condition(note_count)
    
    def _skippable_cutscenes(self):
        print("Skippable Cutscenes")
        self._assembly_class_creation()
        self._assembly_obj._skippable_cutscenes()
    
    def _boot_to_game_select(self):
        print("Boot To Game Select")
        self._assembly_class_creation()
        self._assembly_obj._boot_to_game_select()
    
    def _set_swim_a_speed(self, swim_a_speed):
        self._assembly_class_creation()
        self._assembly_obj._set_swim_a_speed(swim_a_speed)
    
    def _set_swim_b_speed(self, swim_b_speed):
        self._assembly_class_creation()
        self._assembly_obj._set_swim_b_speed(swim_b_speed)
    
    def _set_roll_speed(self, roll_speed):
        self._assembly_class_creation()
        self._assembly_obj._set_roll_speed(roll_speed)
    
    def _super_banjo(self):
        print("Super Banjo")
        self._assembly_class_creation()
        self._assembly_obj._scale_bk_talon_trot_speed(1.5)
        self._assembly_obj._scale_banjos_surface_swim_speed(1.5)
        self._assembly_obj._scale_banjos_walk_speed(1.5)
        self._assembly_obj._set_swim_a_speed(450)
        self._assembly_obj._set_swim_b_speed(900)
    
    def _faster_transformation_movement(self):
        print("Faster Transformation Movement")
        self._assembly_class_creation()
        self._assembly_obj._scale_termite_speed(2)
        self._assembly_obj._scale_crocodile_speed(2)
        self._assembly_obj._scale_walrus_speed(2)
        self._assembly_obj._scale_pumpkin_speed(2)
    
    def _default_totals_screen(self):
        print("Default Totals Screen")
        self._assembly_class_creation()
        self._assembly_obj._default_totals_screen()
    
    def _replace_note_doors(self, collectable_type, new_max):
        print("Replace Note Doors")
        self._assembly_class_creation()
        self._assembly_obj._replace_note_doors(collectable_type, new_max)
    
    def _set_note_door_values(self, note_door_value_list):
        print("Set Note Door Values")
        self._assembly_class_creation()
        self._assembly_obj._set_note_door_values(note_door_value_list)
        self._model_class_creation()
        self._model_obj._set_note_door_values(note_door_value_list)

    def _replace_jigsaw_puzzles(self, collectable_type, new_max):
        print("Replace Jigsaw Puzzles")
        self._assembly_class_creation()
        self._assembly_obj._replace_jigsaw_puzzles(collectable_type, new_max)
    
    def _set_jigsaw_puzzle_costs(self, jigsaw_puzzle_cost_list):
        print("Set Jigsaw Puzzle Costs")
        self._assembly_class_creation()
        self._assembly_obj._set_jigsaw_puzzle_costs(jigsaw_puzzle_cost_list)
    
    def _modify_transformation_costs(self, collectable_type, new_max):
        print("Mody Transformation Costs")
        self._assembly_class_creation()
        self._assembly_obj._replace_transformation_costs(collectable_type, new_max)
    
    def _set_transformation_costs(self, transformation_cost_list):
        print("Set Transformation Costs")
        self._assembly_class_creation()
        self._assembly_obj._set_transformation_costs(transformation_cost_list)
        self._model_class_creation()
        self._model_obj._set_transformation_sign_costs(transformation_cost_list)
    
    def _randomize_furnace_fun_tiles(self, allowed_tile_type_dict):
        # "Blank_Tile": 0
        # "BK_Tile": 1
        # "Eye_Tile": 2
        # "Sound_Tile": 3
        # "Timer_Tile": 4
        # "Gruntilda_Tile": 5
        # "Skull_Tile": 6
        # "Joker_Tile": 8
        # blank space is currently glitched
        blank_tile_list = [
            0x02, 0x05, 0x08, 0x0E, 0x13, 0x1B,
            0x1C, 0x23, 0x24, 0x27, 0x33, 0x3D,
            0x44, 0x4A, 0x54, 0x58, 0x5A, 0x5D
            ]
        joker_tile_list = [
            0x04, 0x0C, 0x10, 0x3B, 0x4E
            ]
        ff_tile_dict = {}
        for count in range(0, 0x5F):
            if(count in blank_tile_list):
                ff_tile_dict[count] = "Blank_Tile"
            elif(count in joker_tile_list):
                ff_tile_dict[count] = "Joker_Tile"
            else:
                ff_tile_dict[count] = self._rand_choice_weighted(allowed_tile_type_dict, count)
        self._assembly_class_creation()
        self._assembly_obj._reassign_ff_tile_types(ff_tile_dict)
        self._model_class_creation()
        self._model_obj._reassign_ff_tile_textures(ff_tile_dict)
    
    def _furnace_fun_finale(self):
        print("Furnace Fun Finale")
        self._assembly_class_creation()
        self._assembly_obj._replace_level_model(104, 127, ["Side_A", "Unk3", "Unk4", "Unk5", "Unk6", "Unk7", "Unk8"])
        self._model_class_creation()
        self._model_obj._furnace_fun_finale()
        self._setup_class_creation()
        self._setup_obj._furnace_fun_finale()
    
    def _adjust_final_battle_phases(self,
                                    phase1_hits=None,
                                    phase2_hits=None, phase2_spots=None,
                                    phase3_hits=None,
                                    phase4_num_of_jinjos=None, phase4_egg_per_jinjo=None,
                                    phase5_eggs_per_hole=None):
        print("Adjust Final Battle Phases")
        self._assembly_class_creation()
        self._assembly_obj._adjust_final_battle_phases(phase1_hits,
                                                       phase2_hits, phase2_spots,
                                                       phase3_hits,
                                                       phase4_num_of_jinjos, phase4_egg_per_jinjo,
                                                       phase5_eggs_per_hole)
    
    def _overwrite_asset_file(self, pointer, custom_file_name):
        print("Overwrite Asset File")
        # automated_obj._overwrite_asset_file(0x10758, "KQ_ZDD_Main_Cave-Riposte")
        self._ASSET_TABLE_OFFSET = 0x10CD0
        index_start = self._bk_rom_obj._read_byte_list_to_int(pointer, 4) + self._ASSET_TABLE_OFFSET
        index_end = self._bk_rom_obj._read_byte_list_to_int(pointer + 0x8, 4) + self._ASSET_TABLE_OFFSET
        custom_file = GENERIC_FILE_CLASS(f"{self._file_dir}Custom_Files/", custom_file_name)
        if(index_end - index_start < len(custom_file._mmap)):
            print("The file you're trying to insert is too big.")
            raise SystemError("The file you're trying to insert is too big.")
        for index_count in range(len(custom_file._mmap)):
            self._bk_rom_obj._mmap[index_start + index_count] = custom_file._mmap[index_count]
        for index_count in range(index_end - index_start - len(custom_file._mmap)):
            self._bk_rom_obj._mmap[index_start + len(custom_file._mmap) + index_count] = 0xAA
        
    def _insert_compressed_asset_file(self, pointer, custom_file_name):
        print("Insert Compressed Asset File")
        # automated_obj._insert_compressed_asset_file(0x10758, "KQ_ZDD_Main_Cave-Riposte")
        self._ASSET_TABLE_OFFSET = 0x10CD0
        index_start = self._bk_rom_obj._read_byte_list_to_int(pointer, 4) + self._ASSET_TABLE_OFFSET
        index_end = self._bk_rom_obj._read_byte_list_to_int(pointer + 0x8, 4) + self._ASSET_TABLE_OFFSET
        custom_file = GENERIC_FILE_CLASS(f"{self._file_dir}Custom_Files/", custom_file_name)
        if(index_end - index_start < len(custom_file._mmap)):
            print("The file you're trying to insert is too big.")
            raise SystemError("The file you're trying to insert is too big.")
        file_name = str(hex(pointer))[2:].upper()
        if(os.path.exists(self._file_dir + self._EXTRACTED_FILES_DIR + f"{file_name}{self._DECOMPRESSED_BIN_EXTENSION}")):
            os.remove(self._file_dir + self._EXTRACTED_FILES_DIR + f"{file_name}{self._DECOMPRESSED_BIN_EXTENSION}")
        copy(f"{self._file_dir}Custom_Files/{custom_file_name}.bin", f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{file_name}-Raw.bin")
    
    def _insert_decompressed_asset_file(self, pointer, custom_file_name):
        print("Insert Decompressed Asset File")
        # automated_obj._insert_decompressed_asset_file(0x8900, "BK_Rando_Logo-TSRStormed_&_Kurko")
        self._ASSET_TABLE_OFFSET = 0x10CD0
        file_name = str(hex(pointer))[2:].upper()
        if(os.path.exists(self._file_dir + self._EXTRACTED_FILES_DIR + f"{file_name}{self._DECOMPRESSED_BIN_EXTENSION}")):
            os.remove(self._file_dir + self._EXTRACTED_FILES_DIR + f"{file_name}{self._DECOMPRESSED_BIN_EXTENSION}")
        copy(f"{self._file_dir}Custom_Files/{custom_file_name}.bin", f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{file_name}{self._DECOMPRESSED_BIN_EXTENSION}")
    
    def _randomize_music_instruments(self):
        print("Random Music Instruments")
        self._sound_class_creation()
        self._sound_obj._randomize_music_instruments(sound_file_pointer=0x10758, this_seed=self._seed)
        
    def _ambience(self):
        print("Ambience")
        self._assembly_class_creation()
        self._assembly_obj._set_all_music(new_music1=0x19, new_music2=0x19, new_music3=0x19)
        self._sound_class_creation()
        self._sound_obj._remove_music_sound(sound_file_pointer=0x10810)
    
    def _snacker_everywhere(self):
        print("Snacker Everywhere")
        self._assembly_class_creation()
        self._assembly_obj._snacker_everywhere()
    
    def _mm_fix_honeycomb_flags(self):
        print("MM Fix Honeycomb Flags")
        self._assembly_class_creation()
        self._assembly_obj._mm_fix_honeycomb_flags()
    
    def _mmm_anyones_empty_honeycomb(self):
        print("MMM Anyones Empty Honeycomb")
        self._assembly_class_creation()
        self._assembly_obj._mmm_anyones_empty_honeycomb()
    
    def _remove_tutorial_option(self):
        print("Remove Tutorial Option")
        self._assembly_class_creation()
        self._assembly_obj._remove_tutorial_option()
        self._automated_speech_class_creation()
        self._automated_speech_obj._replace_non_furnace_fun_speech(General_Speech_Dict.GENERAL_REMOVE_BOTTLES_TUTORIAL_SPEECH_DICT)

    def _one_round_vile(self):
        '''DOESNT WORK, BUT BELIEVE IN THE DREAM'''
        print("One Round Vile")
        self._assembly_class_creation()
        self._assembly_obj._one_round_vile()

    def _starting_moves(self, starting_move_list):
        print("Starting Moves")
        self._assembly_class_creation()
        self._assembly_obj._sm_starting_moves(starting_move_list)
    
    def _forgiving_engine_room(self):#, level=1):
        print("Forgiving Engine Room")
        # if(level > 0):
        self._setup_class_creation()
        self._setup_obj._engine_room_remove_death_plane()
        # if(level > 1):
        #     self._model_class_creation()
        #     self._model_obj._flood_engine_room()
    
    def _randomize_matching_puzzle(self):
        print("Randomizing Matching Puzzle")
        gv_mp_tile_dict = {}
        tile_choices = [count for count in range(8)] * 2
        tile_choices = self._rand_shuffle(tile_choices)
        for count, tile_value in enumerate(tile_choices):
            gv_mp_tile_dict[count] = tile_value
        self._assembly_class_creation()
        self._assembly_obj._reassign_gv_matching_puzzle_tile_types(gv_mp_tile_dict)
        self._model_class_creation()
        self._model_obj._reassign_gv_matching_puzzle_tiles(gv_mp_tile_dict)

    def _randomize_motzands_songs(self):
        print("Randomizing Motzands Songs")
        self._assembly_class_creation()
        first_song_list = self._rand_sample(range(0, 23), 5, add_val=5)
        second_song_list = self._rand_sample(range(0, 23), 10, add_val=10)
        self._assembly_obj._reassign_motzands_songs(first_song_list, second_song_list)
    
    def _reassign_tumblars_tiles(self):
        print("Randomizing Tumblars Tiles")
        mm_t_tile_dict = {}
        tile_choices = [0x4A, 0x41, 0x4E, 0x4F, 0x4B, 0x42, 0x41,
                        0x5A, 0x45, 0x4F, 0x49, 0x4F, 0x58, 0x58,
                        0x58, 0x58, 0x58, 0x58, 0x58, 0x58, 0x58,
                        0x58, 0x58, 0x58, 0x58, 0x58]
        tile_choices = self._rand_shuffle(tile_choices)
        for count, tile_value in enumerate(tile_choices):
            mm_t_tile_dict[count] = tile_value
        self._assembly_class_creation()
        self._assembly_obj._reassign_tumblars_tiles(mm_t_tile_dict)
    
    def _remove_always_active_pads(self):
        self._setup_class_creation()
        self._setup_obj._remove_always_active_pads()
    
    def _reassign_sm_main_to_sm_banjos_house_warp(self, map_id, exit_id):
        self._assembly_class_creation()
        self._assembly_obj._reassign_sm_main_to_sm_banjos_house_warp(map_id, exit_id)
    
    def _new_game_start_area(self, map_id, entry_id):
        self._assembly_class_creation()
        self._assembly_obj._new_game_start_area(map_id, entry_id)
    
    def _shock_jump_to_gl_cc_entrance(self):
        self._setup_class_creation()
        self._setup_obj._shock_jump_to_gl_cc_entrance()
    
    def _remove_slope_slide_timer(self):
        self._assembly_class_creation()
        self._assembly_obj._remove_slope_slide_timer()
    
    def _unlimited_cheat_codes(self):
        self._assembly_class_creation()
        self._assembly_obj._unlimited_cheat_codes()
    
    def _modified_cheat_codes(self, jump_pad_cheat_move="Shock_Jump", fly_pad_cheat_move="Flight"):
        self._assembly_class_creation()
        self._assembly_obj._simplified_cheat_codes(jump_pad_cheat_move, fly_pad_cheat_move)
    
    def _water_level_automatically(self, level=0):
        self._assembly_class_creation()
        if(level == 1):
            self._assembly_obj._water_level_one_automatically()
        elif(level == 2):
            self._assembly_obj._water_level_two_automatically()
    
    def _raise_sharkfood_island(self):
        self._assembly_class_creation()
        self._assembly_obj._raise_sharkfood_island()
    
    ####################
    ### BANJO SOULIE ###
    ####################
        
    def _banjo_soulie(self):
        print("Banjo Soulie")
        self._assembly_class_creation()
        self._assembly_obj._soulie_collision_markers()
        self._setup_class_creation()
        self._setup_obj._banjo_soulie_enemies()
        self._automated_speech_class_creation()
        self._automated_speech_obj._replace_non_furnace_fun_speech(Intro_Bottles_Speech_Dicts.BANJO_SOULIE_INTRO_BOTTLES_SPEECH_DICT)
        self._automated_speech_obj._replace_non_furnace_fun_speech(General_Speech_Dict.BANJO_SOULIE_FIRST_DEATH_SPEECH_DICT)
    
    def _banjo_soulie_enemy_drops(self):
        self._assembly_class_creation()
        self._assembly_obj._banjo_soulie_enemy_drops()
        self._assembly_obj._increase_note_pickup_count(5)
    
    def _banjo_soulie_collisions(self):
        pass

    def _banjo_soulie_maps(self):
        self._model_class_creation()
        self._model_obj._banjo_soulie_furnace_fun_map()

    def _banjo_soulie_map_assignment(self):
        self._assembly_class_creation()
        # Map Models
        new_level_model_dict = {
            # Tutorial World
            MAP_ENUMS.SM_MAIN: {"Scale": 1.5},
            # Bonfire
            # Ice World
            # Dirty World
            # Laval World
            # Final Boss
        }
        self._assembly_obj._modify_level_model_by_dict(new_level_model_dict)
    
    def _banjo_soulie_asm_assignment(self):
        # Map Assembly
        new_gc_section_info_dict = {
            # Tutorial World
            MAP_ENUMS.GV_SNS_ROOM: WORLD_ENUMS.SPIRAL_MOUNTAIN,
            # Bonfire
            MAP_ENUMS.GL_CRYPT: WORLD_ENUMS.GRUNTILDAS_LAIR,
            # Ice World
            # Dirty World
            # Laval World
            # Final Boss
        }
        self._assembly_obj._adjust_gc_section_info_by_level(new_gc_section_info_dict)

    ############################
    ### BACKGROUND FUNCTIONS ###
    ############################
    # These don't affect gameplay,
    # but are typically ran anyway in order to make something easier
    
    def _remove_unknown_object(self):
        print("Remove Unknown Object")
        self._setup_class_creation()
        self._setup_obj._remove_unknown_object()
    
    def _shorten_text(self):
        print("Shorten Text")
        self._automated_speech_class_creation()
        self._automated_speech_obj._replace_non_furnace_fun_speech(SHORTEN_BOTTLES_SECRET_GAME_SPEECH_DICT)
    
    ########################
    ### CUSTOM FUNCTIONS ###
    ########################
    # These aren't really made for the randomizer,
    # just for me to play around with,
    # but it uses the randomizer to get around the anti-tampering stuff
    
    def _stonehenge_conga(self):
        self._assembly_class_creation()
        self._assembly_obj._stonehenge_conga()
        self._setup_class_creation()
        self._setup_obj._stonehenge_conga()
        
    def _banjo_bingo(self):
        print("Banjo Bingo")
        self._automated_speech_class_creation()
        BANJO_BINGO_INTRO_BOTTLES_SPEECH_DICT = {
            "CE30": { # 5C85D8
                0: "WELCOME TO BANJO-BINGO!",
                12: "WHAT'S BANJO-BINGO?",
                2: "BASE GAME, BUT NOTE DOORS ARE FREE AND THE WATER LEVEL STARTS AT TWO.",
                14: "IS THAT IT?",
                15: "SOUNDS LIKE FUN!",
                4: "I CAN'T BELIEVE YOU HAVEN'T SKIPPED MY TEXT YET.",
                17: "OH RIGHT! LET'S SKIP THIS, BANJO!",
                6: "I'M ALMOST DONE TALKING ALREADY.",
                8: "YOU MIGHT AS WELL LET ME FINISH.",
            }
        }
        self._automated_speech_obj._replace_non_furnace_fun_speech(BANJO_BINGO_INTRO_BOTTLES_SPEECH_DICT)
    
    def _bottles_poc(self, sm_moves, non_sm_moves):
        # self._assembly_class_creation()
        # script_id_dict = self._assembly_obj._adjusted_bottles_cameras(sm_moves, non_sm_moves)
        self._assembly_class_creation()
        script_id_dict = self._assembly_obj._adjusted_seperated_bottles_cameras(sm_moves, non_sm_moves)
        # self._setup_class_creation()
        # self._setup_obj._remove_top_of_sm_bottles()
        # self._setup_obj._remove_moveable_bottles_moves()
        # self._setup_obj._change_camera_on_map(6, 0x5F, "9780")

    def _mushroom_poc(self):
        self._setup_class_creation()
        self._setup_obj._mushroom_poc()
    
    def _static_object_poc(self):
        self._setup_class_creation()
        self._setup_obj._static_object_poc()
    
    def _remove_tutorial_vegetable_despawn(self):
        '''Does not work'''
        self._assembly_class_creation()
        self._assembly_obj._remove_tutorial_vegetable_despawn()
    
    def _forgiving_deaths(self):
        self._assembly_class_creation()
        self._assembly_obj._forgiving_deaths()
    
    def _get_level_item_counts(self):
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        spiral_mountain_setup_pointers = ["9780", "9BD8"]
        mumbos_mountain_setup_pointers = ["9788", "97D8", "97E8"]
        treasure_trove_cove_setup_pointers = ["97A0", "97A8", "97B0", "97C8", "9BF0"]
        clankers_cavern_setup_pointers = ["97D0", "9880", "9888", "9890"]
        bubblegloop_swamp_setup_pointers = ["97E0", "97F8", "9800", "99B0"]
        freezeezy_peak_setup_pointers = ["98B0", "9980", "99B8", "9A10", "9B70"]
        gobis_valley_setup_pointers = ["9808", "9810", "9818", "9820", "9828", "9848", "9C08"]
        mad_monster_mansion_setup_pointers = [
            "9850", "9858", "9860", "9898", "98A0", "98A8", "98B8",
            "98C0", "98C8", "98D0", "98D8", "98E0", "98E8", "98F0",
            "98F8", "9BE0"
        ]
        rusty_bucket_bay_setup_pointers = [
            "9900", "9918", "9920", "9928", "9930", "9938", "9940",
            "9948", "9950", "9958", "9960", "9968", "9970", "9BD0"
        ]
        click_clock_wood_hub_setup_pointers = ["9978"]
        click_clock_wood_spring_setup_pointers = ["9990", "99C8", "9A50", "9A68", "9AA0"]
        click_clock_wood_summer_setup_pointers = ["9998", "99D0", "9A48", "9A70", "9AA8"]
        click_clock_wood_autumn_setup_pointers = ["99A0", "99D8", "9A58", "9A78", "9A90", "9AB0"]
        click_clock_wood_winter_setup_pointers = ["99A8", "99E0", "9A80", "9A88", "9A98", "9AB8"]
        click_clock_wood_pointers = [
            "9978",
            "9990", "99C8", "9A50", "9A68", "9AA0",
            "9998", "99D0", "9A48", "9A70", "9AA8",
            "99A0", "99D8", "9A58", "9A78", "9A90", "9AB0",
            "99A8", "99E0", "9A80", "9A88", "9A98", "9AB8"
            ]
        gruntildas_lair_setup_pointers = [
            "9AC0", "9AC8", "9AD0", "9AD8", "9AE0", "9AE8", "9AF0",
            "9AF8", "9B00", "9B08", "9B18", "9B20", "9B28", "9B30",
            "9B38", "9B40", "9B48", "9B78", "9BE8", "9BF8", "9C10"
        ]
        self._setup_class_creation()
        object_name_list = [
            "Jiggy", "Empty Honeycomb", "Mumbo Token", "Extra Life", "Honeycomb",
            "Note", "Blue Egg", "Red Feather", "Gold Feather"]
        object_count_dict = self._setup_obj._setup_item_counts(spiral_mountain_setup_pointers, object_name_list)
        print("Spiral Mountain")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(mumbos_mountain_setup_pointers, object_name_list)
        print("Mumbos Mountain")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(treasure_trove_cove_setup_pointers, object_name_list)
        print("Treasure Trove Cove")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(clankers_cavern_setup_pointers, object_name_list)
        print("Clankers Cavern")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(bubblegloop_swamp_setup_pointers, object_name_list)
        print("Bubblegloop Swamp")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(freezeezy_peak_setup_pointers, object_name_list)
        print("Freezeezy Peak")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(gobis_valley_setup_pointers, object_name_list)
        print("Gobis Valley")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(mad_monster_mansion_setup_pointers, object_name_list)
        print("Mad Monster Mansion")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(rusty_bucket_bay_setup_pointers, object_name_list)
        print("Rusty Bucket Bay")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(click_clock_wood_hub_setup_pointers, object_name_list)
        print("Click Clock Wood Hub")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(click_clock_wood_spring_setup_pointers, object_name_list)
        print("Click Clock Wood Spring")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(click_clock_wood_summer_setup_pointers, object_name_list)
        print("Click Clock Wood Summer")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(click_clock_wood_autumn_setup_pointers, object_name_list)
        print("Click Clock Wood Autumn")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(click_clock_wood_winter_setup_pointers, object_name_list)
        print("Click Clock Wood Winter")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(click_clock_wood_pointers, object_name_list)
        print("Click Clock Wood Total")
        pp.pprint(object_count_dict)
        object_count_dict = self._setup_obj._setup_item_counts(gruntildas_lair_setup_pointers, object_name_list)
        print("Gruntildas Lair")
        pp.pprint(object_count_dict)

    def _print_map_object_positions(self):
        self._setup_class_creation()
        object_name_list = [
            "Jiggy", "Empty Honeycomb", "Mumbo Token", "Extra Life", "Honeycomb",
            "Note", "Blue Egg", "Red Feather", "Gold Feather",
            "Orange", "Blubber's Gold",
            "FP Blue Present (Collectable)", "FP Green Present (Collectable)", "FP Red Present (Collectable)",
            "Bottles Mound (Beak Bomb)", "Bottles Mound (Eggs)", "Bottles Mound (Beak Buster)", "Bottles Mound (Talon Trot)",
            "Bottles Mound (Shock Spring Jump)", "Bottles Mound (Flight)", "Bottles Mound (Wonderwing)", "Bottles Mound (Stilt Stride)",
            "Bottles Mound (Turbo Talon Trot)", "Bottles Mound (Note Door)", "Bottles Mound (Camera)", "Bottles Mound (Swim)",
            "Bottles Mound (Attack)", "Bottles Mound (Beak Barge)", "Bottles Mound (Jump)", "Bottles Mound (Climb)",
            "Yellow Jinjo", "Orange Jinjo", "Blue Jinjo", "Pink Jinjo", "Green Jinjo",
            "CCW Acorn", "CCW Caterpillar"]
        for setup_pointer in MAP_SETUP_POINTER_DICT:
            self._setup_obj._setup_item_xyz_positions(setup_pointer, MAP_SETUP_POINTER_DICT[setup_pointer], object_name_list)

    def _little_big_planet(self, scale=2):
        '''Won't work without editing EVERY assembly instance of a coordinate'''
        self._assembly_class_creation()
        # Level Models
        new_level_model_dict = {}
        for map_enum in MAP_ENUMS:
            new_level_model_dict[map_enum.value] = {"Scale": scale}
        self._assembly_obj._modify_level_model_by_dict(new_level_model_dict)
    
    def _replace_sir_slush_model(self, asset_id):
        self._assembly_class_creation()
        self._assembly_obj._replace_sir_slush_model(asset_id)
    
    def _remove_unknown_dict(self):
        self._setup_class_creation()
        self._setup_obj._remove_unknown_dict()
    
    def _adjust_lighting_colors(self, pointer, lighting_num, red=None, green=None, blue=None):
        self._setup_class_creation()
        self._setup_obj._adjust_lighting_colors(pointer, lighting_num, red, green, blue)
    
    def _adjust_lighting_position(self, pointer, lighting_num, x_pos=None, y_pos=None, z_pos=None):
        self._setup_class_creation()
        self._setup_obj._adjust_lighting_position(pointer, lighting_num, x_pos, y_pos, z_pos)
    
    def _adjust_lighting_unknown(self, pointer, lighting_num, unk1=None, unk2=None):
        self._setup_class_creation()
        self._setup_obj._adjust_lighting_unknown(pointer, lighting_num, unk1, unk2)

    ###################
    ### BANJO TOOIE ###
    ###################
    # If the user has a Banjo-Tooie ROM,
    # these functions can extract and use those files
    # for Banjo-Kazooie

    def _bt_to_bk_sound(self, tooie_pointer, kazooie_pointer):
        pass

    ######################
    ### DONKEY KONG 64 ###
    ######################
    # If the user has a Donkey Kong 64 ROM,
    # these functions can extract and use those files
    # for Banjo-Kazooie

    ################
    ### CLEAN UP ###
    ################
    # Once the randomized ROM is finished,
    # these functions remove extra files

    def _clean_up(self, clean_up_type="All"):
        print("Clean Up")
        self._clean_up_class_creation()
        if(clean_up_type == "Compressed"):
            self._clean_up_obj._clear_compressed_files()
        else:
            del self._assembly_obj
            self._clean_up_obj._clear_extracted_files_folder()

    ####################
    ### TESTING SHIT ###
    ####################

if __name__ == '__main__':
    print("START")
    OBJECT_SKIP_POINTERS = []
    LEVEL_SKIP_POINTERS = [
        0x10378, # Black everywhere! You dont fall and theres invisible walls and floors!
        0x10548, # Test Map
        0x10550, # Test Map
        ]

    print("Extraction & Decompression Start")
    FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/"
    automated_obj = AUTOMATED_CLASS(FILE_DIR, f"{FILE_DIR}Banjo-Kazooie.z64", f"{FILE_DIR}Banjo-Kazooie-NEW.z64")
    use_seed = randint(0, 1000000)
    print(f"Seed: {use_seed}")
    automated_obj._set_seed(897442)
    automated_obj._extract_and_decompress_all_assets()
    # automated_obj._extract_and_decompress_asset_category("Object Model Files")
    # automated_obj._extract_and_decompress_asset_category("Map Setup Files")
    # automated_obj._extract_and_decompress_asset_category("Text Files")
    # automated_obj._extract_and_decompress_asset_category("Level Model Files")
    # automated_obj._extract_and_decompress_asset_category("Sprite/Texture Files")
    # automated_obj._extract_and_decompress_asset_category("Music Files")
    automated_obj._extract_and_decompress_all_asm()
    automated_obj._clean_up("Compressed")
    print("Extraction & Decompression Complete")
    
    print("DEV Options Start")
    automated_obj._skippable_cutscenes()
    automated_obj._boot_to_game_select()
    # automated_obj._set_note_door_values([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # automated_obj._set_jigsaw_puzzle_costs([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # automated_obj._set_transformation_costs([0, 0, 0, 0, 0])
    # automated_obj._exit_to_witchs_lair()
    # automated_obj._super_banjo()
    # automated_obj._faster_transformation_movement()
    # automated_obj._default_totals_screen()

    print("Testing Options Start")
    # automated_obj._starting_lives("Infinite")
    # automated_obj._starting_lives(0)
    # automated_obj._mm_fix_honeycomb_flags()
    # automated_obj._mmm_anyones_empty_honeycomb()
    # automated_obj._snacker_everywhere()
    automated_obj._starting_health(8, default_cap=False)
    # automated_obj._empty_honeycombs_for_extra_health(3)
    # automated_obj._starting_inventory_counts(69)
    # automated_obj._randomize_collisions()
    # automated_obj._replace_bk_model("Wishywashy")
    # automated_obj._replace_bk_model("Conga")
    # automated_obj._replace_bk_model(MODEL_DEBUG_STRINGS.CONGA)
    # automated_obj._replace_bk_model("Pxl Weezy")
    # automated_obj._replace_bk_model("Mario & Luigi")
    # automated_obj._replace_bk_model("Mario & Purple Yoshi")
    # OBJECT_SKIP_POINTERS.append(0x7908)
    # automated_obj._replace_mm_model("Treasure Trove Cove")
    # automated_obj._replace_ttc_model("Freezeezy Peak")
    # LEVEL_SKIP_POINTERS.append(0x101F0)
    # LEVEL_SKIP_POINTERS.append(0x101F8)
    
    # automated_obj._grayscale_category("Object Model Files")
    # automated_obj._grayscale_category("Level Model Files")
    # automated_obj._grayscale_category("Sprite/Texture Files")
    
    # automated_obj._random_color_category("Object Model Files", skip_pointer=OBJECT_SKIP_POINTERS)
    # automated_obj._random_color_category("Level Model Files", skip_pointer=LEVEL_SKIP_POINTERS, additional_scaling=0.85)
    # automated_obj._random_color_category("Sprite/Texture Files")
    # automated_obj._randomize_skybox_and_clouds()
    # automated_obj._remove_hut_notes()
    # automated_obj._enemy_note_drop(note_count1=3, note_count2=6, note_count3=9)
    # automated_obj._fallproof()
    # automated_obj._jiggy_win_condition(1)
    # automated_obj._note_count_win_condition(3)
    # automated_obj._furnace_fun_finale()
    # automated_obj._randomize_music_instruments()
    # automated_obj._overwrite_asset_file(0x10758, "KQ_ZDD_Main_Cave-Riposte")
    # automated_obj._insert_compressed_asset_file(0x10758, "KQ_ZDD_Main_Cave-Riposte")
    # automated_obj._insert_decompressed_asset_file(0x8900, "BK_Rando_Logo-TSRStormed_&_Kurko")
    # automated_obj._insert_decompressed_asset_file(0x7900, "Green_Yoshi_Model-Decompressed")
    # automated_obj._insert_decompressed_asset_file(0x6538, "082620-Button_Down-Test")
    # automated_obj._insert_decompressed_asset_file(0x6538, "082620-Button_Down-Original")
    # automated_obj._remove_tutorial_option()
    # automated_obj._one_round_vile()
    # automated_obj._unlimited_cheat_codes()
    # automated_obj._modified_cheat_codes(jump_pad_cheat_move="Wonderwing", fly_pad_cheat_move="Beak_Bomb")
    # automated_obj._reassign_sm_main_to_sm_banjos_house_warp(0x77, 0x02)
    # automated_obj._water_level_automatically(level=2)
    # automated_obj._banjo_bingo()
    # Non-Separated
    # sm_moves = [ABILITY_ENUMS.CAMERA_CONTROL, ABILITY_ENUMS.DIVE, ABILITY_ENUMS.RAT_A_TAP_RAP,
    #             ABILITY_ENUMS.BEAK_BARGE, ABILITY_ENUMS.FLAP_FLIP, ABILITY_ENUMS.CLIMB]
    # non_sm_moves = [ABILITY_ENUMS.BEAK_BOMB, ABILITY_ENUMS.EGG_FIRING, ABILITY_ENUMS.BEAK_BUSTER,
    #                 ABILITY_ENUMS.TALON_TROT, ABILITY_ENUMS.SHOCK_SPRING_JUMP, ABILITY_ENUMS.FLIGHT,
    #                 ABILITY_ENUMS.WONDERWING, ABILITY_ENUMS.STILT_STRIDE, ABILITY_ENUMS.TURBO_TALON_TROT,
    #                 ABILITY_ENUMS.OPEN_NOTE_DOORS]
    # automated_obj._bottles_poc(sm_moves, non_sm_moves)
    # Separated
    # sm_moves = [ABILITY_ENUMS.CLAW_SWIPE, ABILITY_ENUMS.DIVE, ABILITY_ENUMS.RAT_A_TAP_RAP,
    #             ABILITY_ENUMS.BEAK_BARGE, ABILITY_ENUMS.FLAP_FLIP, ABILITY_ENUMS.CLIMB]
    # non_sm_moves = [ABILITY_ENUMS.BEAK_BOMB, ABILITY_ENUMS.EGG_FIRING, ABILITY_ENUMS.BEAK_BUSTER,
    #                 ABILITY_ENUMS.TALON_TROT, ABILITY_ENUMS.SHOCK_SPRING_JUMP, ABILITY_ENUMS.FLIGHT,
    #                 ABILITY_ENUMS.WONDERWING, ABILITY_ENUMS.STILT_STRIDE, ABILITY_ENUMS.TURBO_TALON_TROT,
    #                 ABILITY_ENUMS.OPEN_NOTE_DOORS]
    # automated_obj._bottles_poc(sm_moves, non_sm_moves)
    # automated_obj._mushroom_poc()
    # automated_obj._static_object_poc()
    # automated_obj._set_swim_a_speed(450)
    # automated_obj._set_swim_b_speed(900)
    # automated_obj._set_roll_speed(1200)
    # automated_obj._get_level_item_counts()
    # automated_obj._raise_sharkfood_island()
    # automated_obj._banjo_soulie_enemy_drops()
    # automated_obj._banjo_soulie_maps()
    # automated_obj._replace_sir_slush_model(0x0496) # Sir Slush -> Twinkly Muncher
    # automated_obj._new_game_start_area(0x01, 0x12) # Banjos House
    # automated_obj._new_game_start_area(0x47, 0x01) # BGS Mumbos Skull
    # curr_warp_enum = WARP_ENUMS.CC_CLANKER_BELLY_TO_CC_CLANKER_WONDERWING
    # curr_map = WARP_ENUMS.get_map_enum(curr_warp_enum)
    # curr_exit = WARP_ENUMS.get_exit_enum(curr_warp_enum)
    # automated_obj._reassign_sm_main_to_sm_banjos_house_warp(curr_map, curr_exit) # Warp Testing
    automated_obj._reassign_sm_main_to_sm_banjos_house_warp(0x07, 0x0C)
    # automated_obj._forgiving_deaths()
    # automated_obj._print_map_object_positions()
    # automated_obj._remove_unknown_dict()
    # automated_obj._adjust_lighting_colors("9890", 0, 0, 255, 0)
    # automated_obj._adjust_lighting_position("9890", 0, x_pos=None, y_pos=None, z_pos=-800)
    # automated_obj._adjust_lighting_unknown("9890", 0, unk1=0, unk2=1000) # 465.75 / 1048.25
    # automated_obj._adjust_lighting_unknown("9890", 1, unk1=0, unk2=1000) # 434.0 / 1179.875
    print("Options Complete")

    print("Adjusting Core Checksums Start")
    automated_obj._remove_known_anti_tampering()
    automated_obj._core_checksums()
    print("Adjusting Core Checksums Complete")

    print("Compression & Insertion Start")
    automated_obj._compress_and_append_all_asset_table_pointers()
    # automated_obj._compress_and_insert_asset_category("Object Model Files", skip_pointer_list=OBJECT_SKIP_POINTERS)
    # automated_obj._compress_and_insert_asset_category("Map Setup Files")
    # automated_obj._compress_and_insert_asset_category("Text Files")
    # automated_obj._compress_and_insert_asset_category("Level Model Files", skip_pointer_list=LEVEL_SKIP_POINTERS)
    # automated_obj._compress_and_insert_asset_category("Sprite/Texture Files")
    # automated_obj._compress_and_insert_asset_category("Music Files")
    automated_obj._compress_and_insert_all_asm()
    # automated_obj._clean_up("All")
    automated_obj._clean_up("Compressed")
    print("Compression & Insertion Complete")

    print("Adjusting CRC Start")
    automated_obj._adjust_crc()
    print("Adjusting CRC Complete")

    print("DONE")


    ####################
    ### BANJO SOULIE ###
    ####################

# if __name__ == '__main__':
#     print("BANJO SOULIE START")
#     OBJECT_SKIP_POINTERS = [
#         # 0x8460, # Jiggy Switch Beta?
#         ]
#     LEVEL_SKIP_POINTERS = [
#         0x10378, # Black everywhere! You dont fall and theres invisible walls and floors!
#         0x10548, # Test Map
#         0x10550, # Test Map
#         ]

#     print("Extraction & Decompression Start")
#     FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/"
#     # use_seed = randint(0, 1000000)
#     use_seed = 20000003
#     print(f"Seed: {use_seed}")
#     # automated_obj = AUTOMATED_CLASS(FILE_DIR, f"{FILE_DIR}Banjo-Kazooie.z64", f"{FILE_DIR}Banjo-Soulie_V0.z64")
#     automated_obj = AUTOMATED_CLASS(FILE_DIR, f"{FILE_DIR}Banjo-Kazooie.z64", f"{FILE_DIR}Seed_{use_seed}_Banjo-Soulie.z64")
#     automated_obj._set_seed(use_seed)
#     automated_obj._extract_and_decompress_asset_category("Object Model Files")
#     automated_obj._extract_and_decompress_asset_category("Map Setup Files")
#     automated_obj._extract_and_decompress_asset_category("Text Files")
#     automated_obj._extract_and_decompress_asset_category("Level Model Files")
#     automated_obj._extract_and_decompress_asset_category("Sprite/Texture Files")
#     automated_obj._extract_and_decompress_asset_category("Music Files")
#     automated_obj._extract_and_decompress_all_asm()
#     automated_obj._clean_up("Compressed")
#     print("Extraction & Decompression Complete")
    
#     print("DEV Options Start")
#     automated_obj._skippable_cutscenes()
#     automated_obj._boot_to_game_select()
#     # automated_obj._set_note_door_values([46, 92, 138, 184, 230, 276, 322, 368, 414, 460, 506, 552])
#     automated_obj._set_note_door_values([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     # automated_obj._set_jigsaw_puzzle_costs([1, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1])
#     automated_obj._set_jigsaw_puzzle_costs([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
#     # automated_obj._set_transformation_costs([0, 4, 9, 12, 17])
#     automated_obj._set_transformation_costs([0, 0, 0, 0, 0])
#     automated_obj._exit_to_witchs_lair()

#     print("Testing Options Start")
#     automated_obj._starting_lives("Infinite")
    # automated_obj._starting_health(2)
#     automated_obj._empty_honeycombs_for_extra_health(4)
#     automated_obj._replace_bk_model("Kazo & Banjooie")
#     # automated_obj._ambience()
#     automated_obj._remove_hut_notes()
#     automated_obj._banjo_soulie()
#     starting_moves = [
#         "Beak_Barge",
#         "Beak_Buster",
#         "Climb",
#         "Attacks",
#         "Dive",
#         "Talon_Trot",
#         "Egg_Firing",
#     ]
#     automated_obj._starting_moves(starting_moves)
#     automated_obj._remove_unknown_object()
#     automated_obj._enemy_note_drop(note_count1=1, note_count2=4, note_count3=7)
#     capacity_dict = {
#         "Blue_Eggs": {
#             "Before_Cheato": 50,
#             "After_Cheato": 250,
#         },
#         "Red_Feathers": {
#             "Before_Cheato": 20,
#             "After_Cheato": 100,
#         },
#         "Gold_Feathers": {
#             "Before_Cheato": 1,
#             "After_Cheato": 5,
#         }
#     }
#     automated_obj._carrying_capacity(capacity_dict)
#     automated_obj._remove_tutorial_option()
#     automated_obj._adjust_final_battle_phases(phase1_hits=1,
#                                               phase2_hits=1, phase2_spots=1,
#                                               phase3_hits=1,
#                                               phase4_num_of_jinjos=1, phase4_egg_per_jinjo=1,
#                                               phase5_eggs_per_hole=1)
#     automated_obj._faster_transformation_movement()
#     ff_weight_dict = {
#         "None": 0,
#         "Rare": 1,
#         "Low": 3,
#         "Medium": 5,
#         "High": 7,
#     }
#     weighted_ff_tile_dict = {
#         "BK_Tile": ff_weight_dict["High"],
#         "Eye_Tile": ff_weight_dict["Medium"],
#         "Sound_Tile": ff_weight_dict["High"],
#         "Timer_Tile": ff_weight_dict["Low"],
#         "Gruntilda_Tile": ff_weight_dict["None"],
#         "Skull_Tile": ff_weight_dict["Rare"],
#     }
#     automated_obj._randomize_furnace_fun_tiles(weighted_ff_tile_dict)
#     automated_obj._randomize_matching_puzzle()
#     automated_obj._randomize_motzands_songs()
#     automated_obj._new_game_start_area(0x01, 0x12)
#     automated_obj._shock_jump_to_gl_cc_entrance()
#     automated_obj._remove_slope_slide_timer()
#     # automated_obj._stonehenge_conga()
#     print("Options Complete")

#     print("Adjusting Core Checksums Start")
#     automated_obj._remove_known_anti_tampering()
#     automated_obj._core_checksums()
#     print("Adjusting Core Checksums Complete")

#     print("Compression & Insertion Start")
#     automated_obj._compress_and_insert_asset_category("Object Model Files", skip_pointer_list=OBJECT_SKIP_POINTERS)
#     automated_obj._compress_and_insert_asset_category("Map Setup Files")
#     automated_obj._compress_and_insert_asset_category("Text Files")
#     automated_obj._compress_and_insert_asset_category("Level Model Files", skip_pointer_list=LEVEL_SKIP_POINTERS)
#     automated_obj._compress_and_insert_asset_category("Sprite/Texture Files")
#     automated_obj._compress_and_insert_asset_category("Music Files")
#     automated_obj._compress_and_insert_all_asm()
#     automated_obj._clean_up("Compressed")
#     # automated_obj._clean_up("All")
#     print("Compression & Insertion Complete")

#     print("Adjusting CRC Start")
#     automated_obj._adjust_crc()
#     print("Adjusting CRC Complete")

#     print("DONE")

    ###########################
    ### GENERIC PLAYTHROUGH ###
    ###########################

# if __name__ == '__main__':
#     print("GENERIC PLAYTHROUGH START")
#     OBJECT_SKIP_POINTERS = [
#         # 0x8460, # Jiggy Switch Beta?
#         ]
#     LEVEL_SKIP_POINTERS = [
#         0x10378, # Black everywhere! You dont fall and theres invisible walls and floors!
#         0x10548, # Test Map
#         0x10550, # Test Map
#         ]

#     print("Extraction & Decompression Start")
#     FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/"
#     # use_seed = randint(10000000, 19940303)
#     use_seed = 10000002
#     print(f"Seed: {use_seed}")
#     automated_obj = AUTOMATED_CLASS(FILE_DIR, f"{FILE_DIR}Banjo-Kazooie.z64", f"{FILE_DIR}Seed_{use_seed}_Basic.z64")
#     automated_obj._set_seed(use_seed)
#     automated_obj._extract_and_decompress_asset_category("Object Model Files")
#     automated_obj._extract_and_decompress_asset_category("Map Setup Files")
#     automated_obj._extract_and_decompress_asset_category("Text Files")
#     automated_obj._extract_and_decompress_asset_category("Level Model Files")
#     automated_obj._extract_and_decompress_asset_category("Sprite/Texture Files")
#     automated_obj._extract_and_decompress_asset_category("Music Files")
#     automated_obj._extract_and_decompress_all_asm()
#     automated_obj._clean_up("Compressed")
#     print("Extraction & Decompression Complete")
    
#     print("DEV Options Start")
#     automated_obj._skippable_cutscenes()
#     automated_obj._boot_to_game_select()
#     automated_obj._exit_to_witchs_lair()
#     automated_obj._default_totals_screen()

#     print("Logic Start")
#     # Moves
#     # possible_starting_moves = [
#     #     "Beak_Barge",
#     #     "Beak_Bomb",
#     #     "Beak_Buster",
#     #     "Climb",
#     #     "Egg_Firing",
#     #     "Jumps",
#     #     "Flight",
#     #     "Attacks",
#     #     "Shock Jump",
#     #     "Stilt_Stride",
#     #     "Dive",
#     #     "Talon_Trot",
#     #     "Turbo_Talon_Trot",
#     #     "Wonderwing",
#     #     "Note_Door",
#     # ]
#     # move_count = 0
#     # starting_moves = []
#     # while(move_count < 9):
#     #     move_choice = automated_obj._rand_choice(possible_starting_moves)
#     #     possible_starting_moves.remove(move_choice)
#     #     starting_moves.append(move_choice)
#     #     move_count += 1
#     #     if(move_choice in ["Jumps", "Attacks"]):
#     #         move_count += 2
#     #     if(move_count > 6):
#     #         if("Jumps" in possible_starting_moves):
#     #             possible_starting_moves.remove("Jumps")
#     #         if("Attacks" in possible_starting_moves):
#     #             possible_starting_moves.remove("Attacks")
#     # automated_obj._starting_moves(starting_moves)
#     automated_obj._remove_always_active_pads()
#     automated_obj._remove_tutorial_option()
#     # Note Door Costs
#     note_door_50_cost = 0
#     note_door_180_cost = 0
#     note_door_270_cost = 0
#     note_door_350_cost = 0
#     note_door_450_cost = 0
#     note_door_640_cost = 0
#     note_door_765_cost = 0
#     note_door_810_cost = automated_obj._rand_int(300, 500, add_val=8)
#     note_door_828_cost = 0
#     note_door_846_cost = 0
#     note_door_864_cost = 0
#     note_door_882_cost = 0
#     automated_obj._set_note_door_values([note_door_50_cost, note_door_180_cost, note_door_270_cost,
#                                         note_door_350_cost, note_door_450_cost, note_door_640_cost,
#                                         note_door_765_cost, note_door_810_cost, note_door_828_cost,
#                                         note_door_846_cost, note_door_864_cost, note_door_882_cost])
#     # World Costs
#     # world_1_cost = automated_obj._rand_int(0, 1, add_val=1)
#     # world_2_cost = automated_obj._rand_int(0, 2, add_val=2)
#     # world_3_cost = automated_obj._rand_int(0, 5, add_val=3)
#     # world_4_cost = automated_obj._rand_int(0, 7, add_val=4)
#     # world_5_cost = automated_obj._rand_int(0, 8, add_val=5)
#     # world_6_cost = automated_obj._rand_int(0, 9, add_val=6)
#     # world_7_cost = automated_obj._rand_int(0, 10, add_val=7)
#     # world_8_cost = automated_obj._rand_int(0, 12, add_val=8)
#     # world_9_cost = automated_obj._rand_int(0, 15, add_val=9)
#     world_1_cost = 1
#     world_2_cost = 1
#     world_3_cost = 1
#     world_4_cost = 1
#     world_5_cost = 1
#     world_6_cost = 1
#     world_7_cost = 1
#     world_8_cost = 1
#     world_9_cost = 1
#     dog_cost = automated_obj._rand_int(10, 25, add_val=10)
#     double_health_cost = 1
#     automated_obj._set_jigsaw_puzzle_costs([world_1_cost, world_2_cost, world_3_cost,
#                                             world_4_cost, world_5_cost, world_6_cost,
#                                             world_7_cost, world_8_cost, world_9_cost,
#                                             dog_cost, double_health_cost])
#     # Transformation Costs
#     termite_cost = automated_obj._rand_int(0, 5, add_val=1)
#     crocodile_cost = automated_obj._rand_int(0, 10, add_val=2)
#     walrus_cost = automated_obj._rand_int(0, 15, add_val=3)
#     pumpkin_cost = automated_obj._rand_int(0, 20, add_val=4)
#     bee_cost = automated_obj._rand_int(0, 25, add_val=5)
#     automated_obj._set_transformation_costs([termite_cost, crocodile_cost, walrus_cost, pumpkin_cost, bee_cost])
#     # Final Battle
#     phase1_hits = automated_obj._rand_int(1, 4, add_val=1)
#     phase2_hits = automated_obj._rand_int(1, 3, add_val=2)
#     phase2_spots = automated_obj._rand_int(1, 4, add_val=3)
#     phase3_hits = automated_obj._rand_int(1, 4, add_val=4)
#     phase4_num_of_jinjos = automated_obj._rand_int(1, 4, add_val=5)
#     phase4_egg_per_jinjo = automated_obj._rand_int(1, 3, add_val=6)
#     phase5_eggs_per_hole = automated_obj._rand_int(1, 5, add_val=7)
#     automated_obj._adjust_final_battle_phases(phase1_hits=phase1_hits,
#                                             phase2_hits=phase2_hits, phase2_spots=phase2_spots,
#                                             phase3_hits=phase3_hits,
#                                             phase4_num_of_jinjos=phase4_num_of_jinjos, phase4_egg_per_jinjo=phase4_egg_per_jinjo,
#                                             phase5_eggs_per_hole=phase5_eggs_per_hole)
#     # Furnace Fun
#     ff_weight_dict = {
#         "None": 0,
#         "Rare": 1,
#         "Low": 3,
#         "Medium": 5,
#         "High": 7,
#     }
#     weighted_ff_tile_dict = {
#         "BK_Tile": ff_weight_dict["High"],
#         "Eye_Tile": ff_weight_dict["High"],
#         "Sound_Tile": ff_weight_dict["High"],
#         "Timer_Tile": ff_weight_dict["None"],
#         "Gruntilda_Tile": ff_weight_dict["Medium"],
#         "Skull_Tile": ff_weight_dict["Low"],
#     }
#     automated_obj._randomize_furnace_fun_tiles(weighted_ff_tile_dict)

#     print("Quality Of Life Settings")
#     automated_obj._starting_lives("Infinite")
#     automated_obj._new_game_start_area(0x01, 0x12)

#     print("Difficulty Settings")
#     # Capacities
#     blue_egg = automated_obj._rand_int(75, 125, add_val=0)
#     red_feather = automated_obj._rand_int(25, 75, add_val=1)
#     gold_feather = automated_obj._rand_int(5, 15, add_val=2)
#     capacity_dict = {
#         "Blue_Eggs":     {
#             "Before_Cheato": blue_egg,
#             "After_Cheato": blue_egg * 2,
#             },
#         "Red_Feathers":  {
#             "Before_Cheato": red_feather,
#             "After_Cheato": red_feather * 2,
#             },
#         "Gold_Feathers": {
#             "Before_Cheato": gold_feather,
#             "After_Cheato": gold_feather * 2,
#             }
#     }
#     automated_obj._carrying_capacity(capacity_dict)
#     # Health
#     # automated_obj._starting_health(2)
#     # automated_obj._empty_honeycombs_for_extra_health(4)
#     # Win Conditions
#     # automated_obj._jiggy_win_condition(100)
#     # automated_obj._note_count_win_condition(900)
#     # Misc
#     automated_obj._forgiving_engine_room()
#     automated_obj._randomize_matching_puzzle()
#     automated_obj._randomize_motzands_songs()
#     automated_obj._one_round_vile()
#     automated_obj._super_banjo()
#     automated_obj._faster_transformation_movement()
#     automated_obj._fallproof()

#     print("Aesthetic Settings")
#     automated_obj._replace_bk_model("Sonic & Tails")
#     automated_obj._randomize_skybox_and_clouds()
#     # automated_obj._ambience()

#     print("Miscellaneous Start")
#     automated_obj._remove_unknown_object()
#     automated_obj._mm_fix_honeycomb_flags()
#     print("Options Complete")

#     print("Adjusting Core Checksums Start")
#     automated_obj._remove_known_anti_tampering()
#     automated_obj._core_checksums()
#     print("Adjusting Core Checksums Complete")

#     print("Compression & Insertion Start")
#     automated_obj._compress_and_insert_asset_category("Object Model Files", skip_pointer_list=OBJECT_SKIP_POINTERS)
#     automated_obj._compress_and_insert_asset_category("Map Setup Files")
#     automated_obj._compress_and_insert_asset_category("Text Files")
#     automated_obj._compress_and_insert_asset_category("Level Model Files", skip_pointer_list=LEVEL_SKIP_POINTERS)
#     automated_obj._compress_and_insert_asset_category("Sprite/Texture Files")
#     automated_obj._compress_and_insert_asset_category("Music Files")
#     automated_obj._compress_and_insert_all_asm()
#     automated_obj._clean_up("Compressed")
#     print("Compression & Insertion Complete")

#     print("Adjusting CRC Start")
#     automated_obj._adjust_crc()
#     print("Adjusting CRC Complete")

#     print("DONE")