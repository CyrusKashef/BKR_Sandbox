import sys

sys.path.append(".")

from Automated.Game_Assets.Setups.Generic_Setup_File import GENERIC_SETUP_FILE
from Data_Files.Setups.Map_Setup_Pointer_Dict import MAP_SETUP_POINTER_DICT, LAIR_SETUP_POINTER_DICT
from Data_Files.Setups.Lair_Enemy_Id_Dict import LAIR_ENEMY_ID_DICT
from Data_Files.Setups.Clear_Setup_File_Lists import CLEAR_SETUP_FILE_COMPLEX_LIST, CLEAR_SETUP_FILE_SIMPLE_LIST

class SETUP_CLASS():
    def __init__(self, file_dir):
        # CONSTANTS
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        # VARIABLES
        self._file_dir = file_dir

    def _banjo_soulie_enemies(self):
        for pointer in MAP_SETUP_POINTER_DICT:
            print(f"Map: {pointer} - {MAP_SETUP_POINTER_DICT[pointer]}")
            setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{pointer}-Decompressed")
            setup_obj._get_setup_file_info()
            setup_obj._remove_all_object_instances(complex_object_list=["Extra Life"], simple_object_list=["Note"])
            if(pointer in LAIR_SETUP_POINTER_DICT):
                # (0x0367, 0x190C): "Red Gruntling"
                # (0x03BF, 0x190C): "Blue Gruntling"
                # (0x03C0, 0x190C): "Black Gruntling"
                red_gruntling_dict = {"Object_ID": 0x0367, "Script_ID": 0x190C}
                setup_obj._replace_complex_objects_by_id(original_objects_dict=LAIR_ENEMY_ID_DICT, new_object_dict=red_gruntling_dict)
            setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{pointer}-Decompressed")
        
    def _clear_setup_files(self):
        print("Clear Setup Files")
        for pointer in MAP_SETUP_POINTER_DICT:
            print(f"Map: {pointer} - {MAP_SETUP_POINTER_DICT[pointer]}")
            setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{pointer}-Decompressed")
            setup_obj._get_setup_file_info()
            setup_obj._remove_all_object_instances(complex_object_list=CLEAR_SETUP_FILE_COMPLEX_LIST, simple_object_list=CLEAR_SETUP_FILE_SIMPLE_LIST)
            setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{pointer}-Decompressed")
    
    def _furnace_fun_finale(self):
        # Final Battle
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9BF8-Decompressed")
        setup_obj._get_setup_file_info()
        entry_1 = {"Object_ID": 0x01, "Script_ID": 0x190C}
        move_it = {"X_Position": -5, "Y_Position": 50, "Z_Position": 1020}
        setup_obj._modify_complex_objects(original_objects_dict=entry_1, modification_dict=move_it)
        shock_jump_pad_dict = {
            "X_Position": 0x0000,
            "Y_Position": 0x0000,
            "Z_Position": 0x0514,
            "Script_ID": 0x190C,
            "Object_ID": 0x000B,
            "Unk_Byte_A": 0x00,
            "Unk_Byte_B": 0x00,
            "Rotation": 0x00,
            "Unk_Byte_D": 0x00,
            "Size": 0x0064,
            "Current_Node": 0x0,
            "Next_Node": 0x0,
            "End_Object_Indicator": 0x40,
        }
        setup_obj._add_complex_object(object_dict=shock_jump_pad_dict)
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9BF8-Decompressed")
    
    def _remove_unknown_object(self):
        for pointer in MAP_SETUP_POINTER_DICT:
            print(f"Map: {pointer} - {MAP_SETUP_POINTER_DICT[pointer]}")
            setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{pointer}-Decompressed")
            setup_obj._get_setup_file_info()
            setup_obj._remove_all_object_instances(complex_object_list=["Unknown (Jombo's Favorite)"])
            setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{pointer}-Decompressed")
    
    def _engine_room_remove_death_plane(self):
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9918-Decompressed")
        setup_obj._get_setup_file_info()
        setup_obj._remove_all_object_instances(complex_object_list=["Death Plane"])
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9918-Decompressed")
    
    def _remove_always_active_pads(self):
        for pointer in MAP_SETUP_POINTER_DICT:
            print(f"Map: {pointer} - {MAP_SETUP_POINTER_DICT[pointer]}")
            setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{pointer}-Decompressed")
            setup_obj._get_setup_file_info()
            shock_jump_pad_dict = {
                "Object_ID": 0x000B, "Script_ID": 0x190C,
                "Unk_Byte_A": 0x00, "Unk_Byte_B": 0x00,
                "Unk_Byte_D": 0x00, "Current_Node": 0x00,
                "Next_Node": 0x00,
                }
            flight_pad_dict = {
                "Object_ID": 0x00E4, "Script_ID": 0x190C,
                "Unk_Byte_A": 0x00, "Unk_Byte_B": 0x00,
                "Unk_Byte_D": 0x00, "Current_Node": 0x00,
                "Next_Node": 0x00,
                }
            replacement_dict = {
                # Shock Jump Pads
                0x00C0: shock_jump_pad_dict, 0x00C1: shock_jump_pad_dict,
                0x00C2: shock_jump_pad_dict, 0x00C4: shock_jump_pad_dict,
                0x00C5: shock_jump_pad_dict, 0x00C7: shock_jump_pad_dict,
                # Flight Pads
                0x0170: flight_pad_dict, 0x0172: flight_pad_dict,
                0x0175: flight_pad_dict,
            }
            setup_obj._replace_static_with_actor_object(replacement_dict)
            setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{pointer}-Decompressed")