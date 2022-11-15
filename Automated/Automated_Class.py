import sys
from shutil import copy
import os
from os import listdir
from random import seed, randint, choice, shuffle

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

from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS
from Automated.Game_Assets.Models.Specific_Models.Important_Characters.BK_Model import BK_MODEL_CLASS
from Automated.Game_Assets.Models.Specific_Models.Levels.Mumbos_Mountain.MM_A_Model import MM_A_MODEL_CLASS
from Automated.Game_Assets.Models.Specific_Models.Levels.Treasure_Trove_Cove.TTC_A_Model import TTC_A_MODEL_CLASS
from Automated.Game_Assets.Models.Specific_Models.Levels.Treasure_Trove_Cove.TTC_B_Model import TTC_B_MODEL_CLASS
from Automated.Game_Assets.Models.Specific_Models.Levels.Gruntildas_Lair.Furance_Fun import FURNACE_FUN_MODEL_CLASS

from Automated.Game_Assets.Sounds.BK_Sound import BK_SOUND_CLASS

from Data_Files.Asset_Table_Pointer_Dict import ASSET_TABLE_POINTER_DICT
from Data_Files.Asset_Id_Dict import ASSET_ID_DICT
from Data_Files.Skybox_And_Cloud_Dict import SKYBOX_AND_CLOUD_DICT

class AUTOMATED_CLASS():
    def __init__(self, file_dir, original_rom_path, new_rom_path):
        ### CONSTANTS ###
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        self._COMPRESSED_BIN_EXTENSION = "-Compressed.bin"
        self._SPECIFIC_MODEL_DIR = "Automated/Game_Assets/Models/Specific_Models/"
        self._BK_MODEL_PRESET_DIR = "Important_Characters/BK_Model_Presets/"
        self._MM_MODEL_PRESET_DIR = "Levels/Mumbos_Mountain/MM_Presets/"
        self._TTC_MODEL_PRESET_DIR = "Levels/Treasure_Trove_Cove/TTC_Presets/"

        ### VARIABLES ###
        self._file_dir = file_dir
        self._make_copy_of_ROM(original_rom_path, new_rom_path)
        self._bk_rom_obj = BK_ROM_CLASS(file_dir, new_rom_path)
        self._assembly_obj = None
        self._clean_up_obj = None
        self._seed = None
    
    def _make_copy_of_ROM(self, original_rom_path, new_rom_path):
        print("Make Copy Of ROM")
        copy(original_rom_path, new_rom_path)

    ########################
    ### RANDOM FUNCTIONS ###
    ########################

    def _set_seed(self, seed_val):
        self._seed = seed_val
    
    def _rand_int(self, lower, upper, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return randint(lower, upper)
    
    def _rand_choice(self, list, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return choice(list)
    
    def _rand_shuffle(self, list, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return shuffle(list)

    ### EXTRACT & DECOMPRESS ###

    def _extract_and_decompress_asset_category(self, asset_category):
        print(f"Decompress Asset Category: {asset_category}")
        pointer_start = ASSET_TABLE_POINTER_DICT[asset_category]["Start"]
        pointer_end = ASSET_TABLE_POINTER_DICT[asset_category]["End"]
        self._bk_rom_obj._extract_pointer_table_assets(pointer_start, pointer_end)
        for pointer in range(pointer_start, pointer_end+1, 0x8):
            decompress_obj = DECOMPRESS_CLASS(self._file_dir, pointer)
            decompress_obj._decompress_main()

    def _extract_and_decompress_all_assets(self):
        print("Decompress All Assets")
        for asset_category in ASSET_TABLE_POINTER_DICT:
            self._extract_and_decompress_asset_category(asset_category)
    
    def _extract_and_decompress_all_asm(self):
        print("Decompress All ASM")
        self._asm_pointer_address_dict = self._bk_rom_obj._extract_all_asm()
        for asm_file in self._asm_pointer_address_dict:
            decompress_obj = DECOMPRESS_CLASS(self._file_dir, self._asm_pointer_address_dict[asm_file]["Code"])
            decompress_obj._decompress_main()
            decompress_obj = DECOMPRESS_CLASS(self._file_dir, self._asm_pointer_address_dict[asm_file]["Data"])
            decompress_obj._decompress_main()

    ### COMPRESS & INSERT ###

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
        print("Compress All Assets")
        for asset_category in ASSET_TABLE_POINTER_DICT:
            self._compress_and_insert_asset_category(asset_category, skip_pointer_list)

    def _compress_and_insert_all_asm(self):
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
        self._assembly_class_creation()
        self._assembly_obj._remove_known_anti_tampering()
    
    def _core_checksums(self):
        self._assembly_class_creation()
        core_checksum_dict = self._assembly_obj._adjust_core_checksums()
        self._bk_rom_obj._write_bytes(0x5E78, 4, core_checksum_dict["Code_CRC1"])
        self._bk_rom_obj._write_bytes(0x5E7C, 4, core_checksum_dict["Code_CRC2"])
        self._bk_rom_obj._write_bytes(0x5E80, 4, core_checksum_dict["Vars_CRC1"])
        self._bk_rom_obj._write_bytes(0x5E84, 4, core_checksum_dict["Vars_CRC2"])
    
    def _adjust_crc(self):
        self._bk_rom_obj._adjust_crc()

    #######################    
    ### CLASS CREATIONS ###
    #######################

    def _assembly_class_creation(self):
        if(not self._assembly_obj):
            self._assembly_obj = ASSEMBLY_CLASS(self._file_dir)
    
    def _clean_up_class_creation(self):
        if(not self._clean_up_obj):
            self._clean_up_obj = CLEAN_UP_CLASS(self._file_dir)
    
    ##############
    ### MODELS ###
    ##############

    def _replace_bk_model(self, preset_selection):
        self._assembly_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        if((adjusted_selection + ".json") in listdir(self._file_dir + self._SPECIFIC_MODEL_DIR + self._BK_MODEL_PRESET_DIR)):
            bk_model_obj = BK_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "7908-Decompressed")
            bk_model_obj._color_shift_based_on_json(self._file_dir + self._SPECIFIC_MODEL_DIR + self._BK_MODEL_PRESET_DIR, adjusted_selection)
            self._assembly_obj._replace_bk_model_with_asset(0x34E)
        elif(preset_selection in ASSET_ID_DICT):
            asset = ASSET_ID_DICT[preset_selection]
            self._assembly_obj._replace_bk_model_with_asset(asset)
        else:
            print("SOMETHING IS HAPPENING")
            exit(0)

    def _replace_skyboxes_and_cloud(self, adjusted_selection):
        if(adjusted_selection in SKYBOX_AND_CLOUD_DICT):
            for map_count in SKYBOX_AND_CLOUD_DICT["Treasure_Trove_Cove"]["Map_Count"]:
                self._assembly_obj._set_skybox_and_clouds(map_count,
                                SKYBOX_AND_CLOUD_DICT[adjusted_selection]["Skybox"],
                                SKYBOX_AND_CLOUD_DICT[adjusted_selection]["Cloud1"],
                                SKYBOX_AND_CLOUD_DICT[adjusted_selection]["Cloud2"])

    def _replace_mm_model(self, preset_selection):
        self._assembly_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        if((adjusted_selection + ".json") in listdir(self._file_dir + self._SPECIFIC_MODEL_DIR + self._MM_MODEL_PRESET_DIR)):
            ttc_a_model_obj = MM_A_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "103E8-Decompressed")
            ttc_a_model_obj._color_shift_based_on_json(self._file_dir + self._SPECIFIC_MODEL_DIR + self._MM_MODEL_PRESET_DIR, adjusted_selection)
            self._replace_skyboxes_and_cloud(adjusted_selection)
        else:
            print("SOMETHING IS HAPPENING")
            print(adjusted_selection + ".json")
            print(listdir(self._file_dir + self._SPECIFIC_MODEL_DIR + self._MM_MODEL_PRESET_DIR))
            exit(0)

    def _replace_ttc_model(self, preset_selection):
        self._assembly_class_creation()
        adjusted_selection = preset_selection.replace(" ", "_")
        if((adjusted_selection + ".json") in listdir(self._file_dir + self._SPECIFIC_MODEL_DIR + self._TTC_MODEL_PRESET_DIR)):
            ttc_a_model_obj = TTC_A_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "101F0-Decompressed")
            ttc_a_model_obj._color_shift_based_on_json(self._file_dir + self._SPECIFIC_MODEL_DIR + self._TTC_MODEL_PRESET_DIR, adjusted_selection)
            ttc_a_model_obj = TTC_B_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "101F8-Decompressed")
            ttc_a_model_obj._color_shift_based_on_json(self._file_dir + self._SPECIFIC_MODEL_DIR + self._TTC_MODEL_PRESET_DIR, adjusted_selection)
            self._replace_skyboxes_and_cloud(adjusted_selection)
        else:
            print("SOMETHING IS HAPPENING")
            print(adjusted_selection + ".json")
            print(listdir(self._file_dir + self._SPECIFIC_MODEL_DIR + self._TTC_MODEL_PRESET_DIR))
            exit(0)
    
    def _increased_draw_distance(self, file_name):
        '''This Doesn't Do Anything :('''
        model_obj = GENERIC_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, f"{file_name}-Decompressed")
        model_obj._get_object_vertex_header_info()
        model_obj._set_draw_distance_coords(neg_x=0x8001, neg_y=0x8001, neg_z=0x8001, pos_x=0x7999, pos_y=0x7999, pos_z=0x7999, min_coord=0x8001, max_coord=0x7999)
        print()
        model_obj._get_object_vertex_header_info()

    ###########################
    ###### GUI FUNCTIONS ######
    ###########################

    def _starting_lives(self, starting_life_count):
        self._assembly_class_creation()
        self._assembly_obj._starting_lives(starting_life_count)
    
    def _starting_health(self, start_val):
        self._assembly_class_creation()
        self._assembly_obj._starting_max_health(start_val)
    
    def _empty_honeycombs_for_extra_health(self, eh_val):
        self._assembly_class_creation()
        self._assembly_obj._empty_honeycombs_for_extra_health(eh_val)
    
    def _starting_inventory_counts(self, start_val):
        self._assembly_class_creation()
        self._assembly_obj._starting_inventory_counts(start_val)
    
    def _transformation_costs(self, transformation_cost_dict):
        self._assembly_class_creation()
        self._assembly_obj._transformation_costs(transformation_cost_dict)
    
    def _carrying_capacity(self, capacity_dict):
        self._assembly_class_creation()
        self._assembly_obj._carrying_capacity(capacity_dict)

    def _grayscale_category(self, category, skip_pointer=[]):
        pointer_start = ASSET_TABLE_POINTER_DICT[category]["Start"]
        pointer_end = ASSET_TABLE_POINTER_DICT[category]["End"]
        for pointer in range(pointer_start, pointer_end+1, 0x8):
            if(pointer not in skip_pointer):
                try:
                    file_name = str(hex(pointer))[2:].upper() + "-Decompressed"
                    print(f"File Name: {file_name}")
                    model_obj = GENERIC_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, file_name)
                    model_obj._full_model_color_shift(0x01, 0x01, 0x01, brightness="Darker")
                except FileNotFoundError:
                    print(f"File Not Found: {file_name}")
                except Exception as e:
                    print(f"\tError: {file_name}")
                    raise e

    def _random_color_category(self, category, additional_scaling=1, skip_pointer=[]):
        pointer_start = ASSET_TABLE_POINTER_DICT[category]["Start"]
        pointer_end = ASSET_TABLE_POINTER_DICT[category]["End"]
        for pointer in range(pointer_start, pointer_end+1, 0x8):
            if(pointer not in skip_pointer):
                try:
                    file_name = str(hex(pointer))[2:].upper() + "-Decompressed"
                    print(f"File Name: {file_name}")
                    model_obj = GENERIC_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, file_name)
                    red_ratio = self._rand_int(0x30, 0xCF, pointer)
                    green_ratio = self._rand_int(0x30, 0xCF, pointer + 1)
                    blue_ratio = self._rand_int(0x30, 0xCF, pointer + 2)
                    model_obj._full_model_color_shift(red_ratio, green_ratio, blue_ratio, brightness=additional_scaling)
                except FileNotFoundError:
                    print(f"File Not Found: {file_name}")
                except Exception as e:
                    print(f"\tError: {file_name}")
                    raise e
    
    def _randomize_skybox_and_clouds(self):
        self._assembly_class_creation()
        self._assembly_obj._randomize_skybox_and_clouds(self._seed)
    
    def _randomize_collisions(self):
        self._assembly_class_creation()
        self._assembly_obj._modify_collision_markers(self._seed, effect_to_bk_option="Randomize", sound_effect_option="Randomize",
                                                     bk_damage_option="Randomize", hit_count_option="Randomize", num_of_honeycombs_option="Randomize")

    def _remove_hut_notes(self):
        self._assembly_class_creation()
        self._assembly_obj._remove_hut_notes()
    
    def _enemy_note_drop(self):
        self._assembly_class_creation()
        self._assembly_obj._enemy_note_drops()
    
    def _grublin_honeycomb(self):
        self._assembly_class_creation()
        self._assembly_obj._grublin_honeycomb()
    
    def _exit_to_witchs_lair(self):
        self._assembly_class_creation()
        self._assembly_obj._exit_to_witchs_lair()
    
    def _fallproof(self):
        self._assembly_class_creation()
        self._assembly_obj._fallproof()
    
    def _jiggy_win_condition(self, jiggy_count):
        self._assembly_class_creation()
        self._assembly_obj._jiggy_win_condition(jiggy_count)
    
    def _note_count_win_condition(self, note_count):
        self._assembly_class_creation()
        self._assembly_obj._note_count_win_condition(note_count)
    
    def _skippable_cutscenes(self):
        self._assembly_class_creation()
        self._assembly_obj._skippable_cutscenes()
    
    def _boot_to_game_select(self):
        self._assembly_class_creation()
        self._assembly_obj._boot_to_game_select()
    
    def _super_banjo(self):
        self._assembly_class_creation()
        self._assembly_obj._scale_bk_talon_trot_speed(1.5)
        self._assembly_obj._scale_banjos_swim_speed(1.5)
        self._assembly_obj._scale_banjos_walk_speed(1.5)
    
    def _faster_transformations(self):
        self._assembly_class_creation()
        self._assembly_obj._scale_termite_speed(2)
        self._assembly_obj._scale_crocodile_speed(2)
        self._assembly_obj._scale_walrus_speed(2)
        self._assembly_obj._scale_pumpkin_speed(2)
    
    def _default_totals_screen(self):
        self._assembly_class_creation()
        self._assembly_obj._default_totals_screen()
    
    def _replace_note_doors(self, collectable_type, new_max):
        self._assembly_class_creation()
        self._assembly_obj._replace_note_doors(collectable_type, new_max)

    def _replace_jigsaw_puzzles(self, collectable_type, new_max):
        self._assembly_class_creation()
        self._assembly_obj._replace_jigsaw_puzzles(collectable_type, new_max)
    
    def _modify_transformation_costs(self, collectable_type, new_max):
        self._assembly_class_creation()
        self._assembly_obj._replace_transformation_costs(collectable_type, new_max)
    
    def _furnace_fun_finale(self):
        self._assembly_class_creation()
        self._assembly_obj._replace_level_model(104, 127, ["Side_A", "Unk3", "Unk4", "Unk5", "Unk6", "Unk7", "Unk8"])
        furnace_fun_model_obj = FURNACE_FUN_MODEL_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, "105D8-Decompressed")
        furnace_fun_model_obj._lower_invisible_barriers()
    
    def _overwrite_asset_file(self, pointer, custom_file_name):
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
        self._ASSET_TABLE_OFFSET = 0x10CD0
        index_start = self._bk_rom_obj._read_byte_list_to_int(pointer, 4) + self._ASSET_TABLE_OFFSET
        index_end = self._bk_rom_obj._read_byte_list_to_int(pointer + 0x8, 4) + self._ASSET_TABLE_OFFSET
        custom_file = GENERIC_FILE_CLASS(f"{self._file_dir}Custom_Files/", custom_file_name)
        if(index_end - index_start < len(custom_file._mmap)):
            print("The file you're trying to insert is too big.")
            raise SystemError("The file you're trying to insert is too big.")
        file_name = str(hex(pointer))[2:].upper()
        if(os.path.exists(self._file_dir + self._EXTRACTED_FILES_DIR + f"{file_name}-Decompressed.bin")):
            os.remove(self._file_dir + self._EXTRACTED_FILES_DIR + f"{file_name}-Decompressed.bin")
        copy(f"{self._file_dir}Custom_Files/{custom_file_name}.bin", f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{file_name}-Raw.bin")
    
    def _insert_decompressed_asset_file(self, pointer, custom_file_name):
        self._ASSET_TABLE_OFFSET = 0x10CD0
        file_name = str(hex(pointer))[2:].upper()
        if(os.path.exists(self._file_dir + self._EXTRACTED_FILES_DIR + f"{file_name}-Decompressed.bin")):
            os.remove(self._file_dir + self._EXTRACTED_FILES_DIR + f"{file_name}-Decompressed.bin")
        copy(f"{self._file_dir}Custom_Files/{custom_file_name}.bin", f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{file_name}-Decompressed.bin")
    
    def _randomize_music_instruments(self):
        file_name = str(hex(0x10758))[2:].upper() + "-Decompressed"
        print(f"File Name: {file_name}")
        music_obj = BK_SOUND_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, file_name)
        music_obj._get_tracks_offsets()
        instrument_list = []
        for track_num in range(0x1, 0x10):
            # new_instrument = self._rand_choice(list(ALLOWED_INSTRUMENTS), 0x10758 + track_num)
            instrument_val = music_obj._get_instrument(track_num)
            instrument_list.append(instrument_val)
        self._rand_shuffle(instrument_list, 0x10758)
        for track_num in range(0x1, 0x10):
            music_obj._replace_instrument(track_num, instrument_list[track_num - 1])
    
    def _snacker_everywhere(self):
        self._assembly_class_creation()
        self._assembly_obj._snacker_everywhere()
    
    def _mm_fix_honeycomb_flags(self):
        self._assembly_class_creation()
        self._assembly_obj._mm_fix_honeycomb_flags()
    
    def _mmm_anyones_empty_honeycomb(self):
        self._assembly_class_creation()
        self._assembly_obj._mmm_anyones_empty_honeycomb()

    ###################
    ### BANJO TOOIE ###
    ###################

    def _bt_to_bk_sound(self, tooie_pointer, kazooie_pointer):
        pass

    ################
    ### CLEAN UP ###
    ################

    def _clean_up(self, clean_up_type="All"):
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
    OBJECT_SKIP_POINTERS = [0x8460, 0x8858]
    LEVEL_SKIP_POINTERS = [0x10378, 0x10548, 0x10550]

    print("Extraction & Decompression Start")
    FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/"
    automated_obj = AUTOMATED_CLASS(FILE_DIR, f"{FILE_DIR}Banjo-Kazooie.z64", f"{FILE_DIR}Banjo-Kazooie-NEW.z64")
    use_seed = randint(0, 1000000)
    print(f"Seed: {use_seed}")
    automated_obj._set_seed(897442)
    automated_obj._extract_and_decompress_asset_category("Object Model Files")
    # automated_obj._extract_and_decompress_asset_category("Level Model Files")
    # automated_obj._extract_and_decompress_asset_category("Sprite/Texture Files")
    # automated_obj._extract_and_decompress_asset_category("Music Files")
    automated_obj._extract_and_decompress_all_asm()
    automated_obj._clean_up("Compressed")
    print("Extraction & Decompression Complete")
    
    print("DEV Options Start")
    automated_obj._skippable_cutscenes()
    # automated_obj._boot_to_game_select()
    automated_obj._replace_note_doors("Note", 0)
    automated_obj._replace_jigsaw_puzzles("Jiggy", 0)
    automated_obj._modify_transformation_costs("Token", 0)
    automated_obj._exit_to_witchs_lair()
    automated_obj._super_banjo()
    automated_obj._faster_transformations()
    automated_obj._default_totals_screen()

    print("Testing Options Start")
    # automated_obj._starting_lives("Infinite")
    automated_obj._starting_lives(6)
    # automated_obj._mm_fix_honeycomb_flags()
    # automated_obj._mmm_anyones_empty_honeycomb()
    automated_obj._snacker_everywhere()
    automated_obj._starting_health(2)
    # automated_obj._empty_honeycombs_for_extra_health(3)
    # automated_obj._starting_inventory_counts(69)
    # automated_obj._randomize_collisions()
    # automated_obj._replace_bk_model("Wishywashy")
    # automated_obj._replace_bk_model("Conga")
    # automated_obj._replace_bk_model("Mario & Luigi")
    # OBJECT_SKIP_POINTERS.append(0x7908)
    # automated_obj._replace_ttc_model("Rusty Bucket Bay")
    # automated_obj._replace_mm_model("Treasure Trove Cove")
    # automated_obj._increased_draw_distance("7990")
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
    # automated_obj._enemy_note_drop()
    automated_obj._fallproof()
    # automated_obj._jiggy_win_condition(1)
    # automated_obj._note_count_win_condition(3)
    # automated_obj._furnace_fun_finale()
    # automated_obj._randomize_music_instruments()
    # automated_obj._overwrite_asset_file(0x10758, "KQ_ZDD_Main_Cave-Riposte")
    # automated_obj._insert_compressed_asset_file(0x10758, "KQ_ZDD_Main_Cave-Riposte")
    automated_obj._insert_decompressed_asset_file(0x8900, "BK_Rando_Logo-TSRStormed_&_Kurko")
    print("Options Complete")

    print("Adjusting Core Checksums Start")
    automated_obj._remove_known_anti_tampering()
    automated_obj._core_checksums()
    print("Adjusting Core Checksums Complete")

    print("Compression & Insertion Start")
    automated_obj._compress_and_insert_asset_category("Object Model Files", skip_pointer_list=OBJECT_SKIP_POINTERS)
    # automated_obj._compress_and_insert_asset_category("Level Model Files", skip_pointer_list=LEVEL_SKIP_POINTERS)
    # automated_obj._compress_and_insert_asset_category("Sprite/Texture Files")
    # automated_obj._compress_and_insert_asset_category("Music Files")
    automated_obj._compress_and_insert_all_asm()
    automated_obj._clean_up("All")
    print("Compression & Insertion Complete")

    print("Adjusting CRC Start")
    automated_obj._adjust_crc()
    print("Adjusting CRC Complete")

    print("DONE")