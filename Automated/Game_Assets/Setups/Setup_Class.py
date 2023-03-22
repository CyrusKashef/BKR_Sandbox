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
    
    def _shock_jump_to_gl_cc_entrance(self):
        print("Shock Jump To GL CC Entrance")
        # CCW Puzzle Room
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9AD0-Decompressed")
        setup_obj._get_setup_file_info()
        shock_jump_pad_dict = {
            "X_Position": 0x0000, "Y_Position": 0x0190, "Z_Position": 0xFD66,
            "Object_ID": 0x000B, "Script_ID": 0x190C,
            "Unk_Byte_A": 0x00, "Unk_Byte_B": 0x00, "Unk_Byte_D": 0x00,
            "Rotation": 0x00, "Size": 0x0064,
            "Current_Node": 0x00, "Next_Node": 0x00,
            "End_Object_Indicator": 0x40,
            }
        setup_obj._add_complex_object(shock_jump_pad_dict)
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9AD0-Decompressed")
    
    def _stonehenge_conga(self):
        print("Stonehenge Conga")
        # MM Main
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9788-Decompressed")
        setup_obj._get_setup_file_info()
        ### Conga ###
        new_conga_x_position = -1214
        new_conga_y_position = 450
        new_conga_z_position = 3367
        original_conga_dict = {"Object_ID": 0x0008, "Script_ID": 0x190C}
        modified_conga_dict = {"X_Position": new_conga_x_position, "Y_Position": new_conga_y_position,
                               "Z_Position": new_conga_z_position}
        setup_obj._modify_complex_objects(original_conga_dict, modified_conga_dict)
        ### Conga Trigger ###
        original_conga_trigger_dict = {"Object_ID": 0x0150, "Script_ID": 0x640C,}
        modified_conga_trigger_dict = {"X_Position": -3150, "Y_Position": 2754, "Z_Position": -2730}
        setup_obj._modify_complex_objects(original_conga_trigger_dict, modified_conga_trigger_dict)
        ### Orange Pad 1 ###
        new_x_position = new_conga_x_position - 328
        new_y_position = new_conga_y_position - 436
        new_z_position = new_conga_z_position - 648
        # Pad
        original_orange_pad_1_dict = {"X_Position": -4428, "Y_Position": -200, "Z_Position": 4002}
        modified_orange_pad_1_dict = {"X_Position": new_x_position, "Y_Position": new_y_position,
                                      "Z_Position": new_z_position, "Size": 100}
        setup_obj._modify_complex_objects(original_orange_pad_1_dict, modified_orange_pad_1_dict)
        # Warp
        original_orange_pad_1_warp_dict = {"Object_ID": 0x86, "Associated_ID": 0x0002}
        modified_orange_pad_1_warp_dict = {"X_Position": new_x_position, "Y_Position": new_y_position + 30,
                                           "Z_Position": new_z_position}
        setup_obj._modify_complex_objects(original_orange_pad_1_warp_dict, modified_orange_pad_1_warp_dict)
        # Flag
        original_orange_pad_1_flag_dict = {"X_Position": -4609, "Y_Position": -200, "Z_Position": 4033}
        modified_orange_pad_1_flag_dict = {"X_Position": new_x_position, "Y_Position": new_y_position + 2,
                                           "Z_Position": new_z_position}
        setup_obj._modify_complex_objects(original_orange_pad_1_flag_dict, modified_orange_pad_1_flag_dict)
        ### Orange Pad 2 ###
        new_x_position = new_conga_x_position + 586
        new_y_position = new_conga_y_position - 446
        new_z_position = new_conga_z_position - 290
        # Pad
        original_orange_pad_2_dict = {"X_Position": -3514, "Y_Position": -210, "Z_Position": 4360}
        modified_orange_pad_2_dict = {"X_Position": new_x_position, "Y_Position": new_y_position,
                                      "Z_Position": new_z_position}
        setup_obj._modify_complex_objects(original_orange_pad_2_dict, modified_orange_pad_2_dict)
        # Warp
        original_orange_pad_2_warp_dict = {"Object_ID": 0x86, "Associated_ID": 0x0003}
        modified_orange_pad_2_warp_dict = {"X_Position": new_x_position, "Y_Position": new_y_position + 30,
                                           "Z_Position": new_z_position}
        setup_obj._modify_complex_objects(original_orange_pad_2_warp_dict, modified_orange_pad_2_warp_dict)
        # Flag
        original_orange_pad_2_flag_dict = {"X_Position": -3802, "Y_Position": -200, "Z_Position": 4099}
        modified_orange_pad_2_flag_dict = {"X_Position": new_x_position, "Y_Position": new_y_position + 2,
                                           "Z_Position": new_z_position}
        setup_obj._modify_complex_objects(original_orange_pad_2_flag_dict, modified_orange_pad_2_flag_dict)
        ### Orange Pad 3 ###
        new_x_position = new_conga_x_position + 321
        new_y_position = new_conga_y_position - 446
        new_z_position = new_conga_z_position + 645
        # Pad
        original_orange_pad_3_dict = {"X_Position": -3779, "Y_Position": -210, "Z_Position": 5295}
        modified_orange_pad_3_dict = {"X_Position": new_x_position, "Y_Position": new_y_position,
                                      "Z_Position": new_z_position}
        setup_obj._modify_complex_objects(original_orange_pad_3_dict, modified_orange_pad_3_dict)
        # Warp
        original_orange_pad_3_warp_dict = {"Object_ID": 0x06, "Associated_ID": 0x0004}
        modified_orange_pad_3_warp_dict = {"X_Position": new_x_position, "Y_Position": new_y_position + 30,
                                           "Z_Position": new_z_position}
        setup_obj._modify_complex_objects(original_orange_pad_3_warp_dict, modified_orange_pad_3_warp_dict)
        # Flag
        original_orange_pad_3_flag_dict = {"X_Position": -3904, "Y_Position": -200, "Z_Position": 5414}
        modified_orange_pad_3_flag_dict = {"X_Position": new_x_position, "Y_Position": new_y_position + 2,
                                           "Z_Position": new_z_position}
        setup_obj._modify_complex_objects(original_orange_pad_3_flag_dict, modified_orange_pad_3_flag_dict)
        #### End ###
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9788-Decompressed")