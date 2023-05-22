import sys

sys.path.append(".")

from Automated.Game_Assets.Setups.Generic_Setup_File import GENERIC_SETUP_FILE
from Data_Files.Setups.Map_Setup_Pointer_Dict import MAP_SETUP_POINTER_DICT, LAIR_SETUP_POINTER_DICT
from Data_Files.Setups.Lair_Enemy_Id_Dict import LAIR_ENEMY_ID_DICT
from Data_Files.Setups.Clear_Setup_File_Lists import CLEAR_SETUP_FILE_COMPLEX_LIST, CLEAR_SETUP_FILE_SIMPLE_LIST
from Data_Files.Setups.Bottles_Dict import BOTTLES_DICT
from Data_Files.Enums.Ability_Enums import ABILITY_ENUMS

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
    
    def _remove_bottles_moves(self, map_pointer, ability_enum_list):
        # Open Map Setup File
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{map_pointer}-Decompressed")
        setup_obj._get_setup_file_info()
        # Remove All Bottles Moves
        for ability_enum in ability_enum_list:
            original_objects_dict = {"Object_ID": 0x12B, "Script_ID": BOTTLES_DICT[ability_enum]["Original_Script_Id"]}
            setup_obj._remove_complex_object_by_attributes(original_objects_dict)
            setup_obj._remove_camera(BOTTLES_DICT[ability_enum]["Old_Camera"])
        #### End ###
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{map_pointer}-Decompressed")
    
    def _remove_moveable_bottles_moves(self):
        sm_ability_enum_list = [ABILITY_ENUMS.BEAK_BARGE, ABILITY_ENUMS.CAMERA_CONTROL, ABILITY_ENUMS.CLIMB, ABILITY_ENUMS.DIVE]
        self._remove_bottles_moves("9780", sm_ability_enum_list)
        mm_ability_enum_list = [ABILITY_ENUMS.TALON_TROT, ABILITY_ENUMS.BEAK_BUSTER, ABILITY_ENUMS.EGG_FIRING]
        self._remove_bottles_moves("9788", mm_ability_enum_list)
        ttc_ability_enum_list = [ABILITY_ENUMS.SHOCK_SPRING_JUMP, ABILITY_ENUMS.FLIGHT]
        self._remove_bottles_moves("97B0", ttc_ability_enum_list)
        cc_ability_enum_list = [ABILITY_ENUMS.WONDERWING]
        self._remove_bottles_moves("97D0", cc_ability_enum_list)
        bgs_ability_enum_list = [ABILITY_ENUMS.STILT_STRIDE]
        self._remove_bottles_moves("97E0", bgs_ability_enum_list)
        fp_ability_enum_list = [ABILITY_ENUMS.BEAK_BOMB]
        self._remove_bottles_moves("98B0", fp_ability_enum_list)
        gv_ability_enum_list = [ABILITY_ENUMS.TURBO_TALON_TROT]
        self._remove_bottles_moves("9808", gv_ability_enum_list)
    
    def _remove_top_of_sm_bottles(self):
        # Open Map Setup File
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9780-Decompressed")
        setup_obj._get_setup_file_info()
        # Remove These
        complex_object_list = ["SM Bridge Bottles 03BD", "SM Bridge Bottles 03BE",
                               "Bottles Mound (Top Of SM)", "SM Bridge Bottles 0349"]
        setup_obj._remove_all_object_instances(complex_object_list)
        #### End ###
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9780-Decompressed")
    
    def _set_bottles_with_camera(self, map_pointer, bottles_info_dict, camera_id):
        # Open Map Setup File
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{map_pointer}-Decompressed")
        setup_obj._get_setup_file_info()
        # Bottles Molehill
        bottles_dict = {
            "X_Position": bottles_info_dict["X_Position"],
            "Y_Position": bottles_info_dict["Y_Position"],
            "Z_Position": bottles_info_dict["Z_Position"],
            "Script_ID": bottles_info_dict["Script_ID"], "Object_ID": 0x12B,
            "Unk_Byte_A": 0x00, "Unk_Byte_B": 0x00, "Unk_Byte_D": 0x00,
            "Rotation": 0x00, "Size": 0x0064,
            "Current_Node": 0x00, "Next_Node": 0x00,
            "End_Object_Indicator": 0x40,
        }
        setup_obj._add_complex_object(bottles_dict)
        # Associated Camera
        camera_dict = {
            "Camera_Start": 0x01, "Unk_Byte_1": 0x00,
            "Camera_Id": camera_id, "Unk_Byte_3": 0x02, "Camera_Type": 0x02,
            "X_Position": bottles_info_dict["X_Position"] - 550,
            "Y_Position": bottles_info_dict["Y_Position"] + 480,
            "Z_Position": bottles_info_dict["Z_Position"] + 285,
            "Pitch": 324, "Yaw": 297, "Roll": 0,
            "Camera_End": 0x00,
        }
        setup_obj._add_camera(camera_dict)
        #### End ###
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{map_pointer}-Decompressed")
    
    def _bottles_poc(self):
        # Re-Add Dive Bottles
        # bottles_info_dict = {
        #     "X_Position": -2336, "Y_Position": 302,
        #     "Z_Position": 973, "Script_ID": 0x018C,
        # }
        # self._set_bottles_with_camera("9780", bottles_info_dict, 0x74)
        # Add Roll Attack Bottles
        # Open Map Setup File
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9780-Decompressed")
        setup_obj._get_setup_file_info()
        # Remove These
        complex_object_list = ["SM Attack Tutorial Bottles 0379"]
        setup_obj._remove_all_object_instances(complex_object_list)
        #### End ###
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9780-Decompressed")
    
    def _change_camera_on_map(self, old_camera_id, new_camera_id, map_pointer):
        # Open Map Setup File
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{map_pointer}-Decompressed")
        setup_obj._get_setup_file_info()
        # Change Camera Id
        setup_obj._change_camera_id(old_camera_id, new_camera_id)
        #### End ###
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{map_pointer}-Decompressed")
    
    def _mushroom_poc(self):
        # Open Map Setup File
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9780-Decompressed")
        setup_obj._get_setup_file_info()
        # Add Mushroom
        for count, unkB in enumerate(range(51, 256, 51)):
            object_dict = {
                "Object_ID": 0x0940, "Size": 0x0080,
                "X_Position": -375 + count * 175, "Y_Position": -50, "Z_Position": 4000,
                "Unk_Byte_A": 0x00, "Unk_Byte_B": 0x00,
            }
            setup_obj._add_simple_object(object_dict)
        # object_dict = {
        #     "Object_ID": 0x0940, "Size": 0x07FF,
        #     "X_Position": -375, "Y_Position": -50, "Z_Position": 4000,
        #     "Unk_Byte_A": 0x03, "Unk_Byte_B": 0x10,
        # }
        # setup_obj._add_simple_object(object_dict)
        #### End ###
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9780-Decompressed")
    
    def _static_object_poc(self):
        # Open Map Setup File
        setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9780-Decompressed")
        setup_obj._get_setup_file_info()
        # Add Tree
        for count, rotation_xz in enumerate(range(51, 256, 51)):
            object_dict = {
                "Object_ID": 0x02E4, "Rotation_Y": 0x4A, "Rotation_XZ": rotation_xz,
                "X_Position": -375 + count * 175, "Y_Position": -50, "Z_Position": 4000,
                "Size": 0x41, "Unk_Byte_B": 0xD2,
            }
            setup_obj._add_simple_object(object_dict)
        # object_dict = {
        #     "Object_ID": 0x02E4, "Rotation_Y": 0x4A, "Rotation_XZ": 0x00,
        #     "X_Position": -375, "Y_Position": -50, "Z_Position": 4000,
        #     "Size": 0x41, "Unk_Byte_B": 0xD2,
        # }
        # setup_obj._add_simple_object(object_dict)
        #### End ###
        setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"9780-Decompressed")
    
    def _setup_item_counts(self, setup_pointers, object_name_list):
        object_count_dict = None
        for pointer in setup_pointers:
            setup_obj = GENERIC_SETUP_FILE(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{pointer}-Decompressed")
            setup_obj._get_setup_file_info()
            object_count_dict = setup_obj._object_count(object_name_list, object_count_dict)
            setup_obj._create_setup_file(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}", f"{pointer}-Decompressed")
        return object_count_dict