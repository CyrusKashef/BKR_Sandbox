import struct
import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS
from Data_Files.Setups.Map_Setup_Dict import MAP_SETUP_DICT
from Data_Files.Setups.Object_Dicts import (
    ACTOR_OBJECT_DICT, TIMED_OBJECT_DICT, MISC_OBJECT_DICT,
    RADIUS_OBJECT_ID_DICT, RADIUS_ASSOCIATED_ID_DICT,
    SPRITE_OBJECT_DICT, STATIC_OBJECT_DICT)

EMPTY_VOXEL = "EMPTY_VOXEL"
OBJECT_0x14_LIST = "OBJECT_0x14_LIST"
OBJECT_0x0C_LIST = "OBJECT_0x0C_LIST"

class GENERIC_SETUP_FILE(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._file_name = file_name
        self._voxel_dict = {}
        self._camera_dict = {}
        self._lighting_dict = {}
        self._neg_x_voxel_count = None
        self._neg_y_voxel_count = None
        self._neg_z_voxel_count = None
        self._pos_x_voxel_count = None
        self._pos_y_voxel_count = None
        self._pos_z_voxel_count = None
    
    def _possible_negative_to_bytes(self, value, byte_count=1):
        if(value < 0):
            value += 1 << (byte_count * 8)
        return value.to_bytes(byte_count, 'big')
    
    def _float_to_byte_hex(self, float_val):
        hex_float = int(hex(struct.unpack('<I', struct.pack('<f', float_val))[0]), 16)
        return hex_float.to_bytes(4, 'big')

    ###########################
    ### GET SETUP FILE INFO ###
    ###########################

    def _get_header_info(self):
        '''
        Every voxel (also known as cubes) is 1000 units.
        There is a voxel in the center that goes from 0 to 999 in the x, y, and z directions.
        Every 1000 units/1 voxel in the positive direction after that voxel adds to the positive voxel count.
        Every 1000 units/1 voxel in the negative direction of that voxel adds to the negative voxel count.
        
        Example:
        neg_x_voxel_count = -1 (FFFFFFFF)
        neg_y_voxel_count = -2 (FFFFFFFE)
        neg_z_voxel_count = -3 (FFFFFFFD)
        pos_x_voxel_count = 1 (00000001)
        pos_x_voxel_count = 2 (00000002)
        pos_x_voxel_count = 3 (00000003)
        This would make a 3x5x7 box of voxels.
        '''
        # Negative Voxel Count
        self._neg_x_voxel_count = self._possible_negative(self._read_byte_list_to_int(0x02, 4), 4)
        self._neg_y_voxel_count = self._possible_negative(self._read_byte_list_to_int(0x06, 4), 4)
        self._neg_z_voxel_count = self._possible_negative(self._read_byte_list_to_int(0x0A, 4), 4)
        # Positive Voxel Count
        self._pos_x_voxel_count = self._read_byte_list_to_int(0x0E, 4)
        self._pos_y_voxel_count = self._read_byte_list_to_int(0x12, 4)
        self._pos_z_voxel_count = self._read_byte_list_to_int(0x16, 4)
        # Calculations
        x_voxel_count = self._pos_x_voxel_count - self._neg_x_voxel_count + 1
        y_voxel_count = self._pos_y_voxel_count - self._neg_y_voxel_count + 1
        z_voxel_count = self._pos_z_voxel_count - self._neg_z_voxel_count + 1
        return x_voxel_count * y_voxel_count * z_voxel_count

    def _debug_print(self, message, curr_index, byte_count=1):
        '''
        Prints out a statement in the console for an error and raises the error
        '''
        print(f"{message}: {hex(curr_index)} -> {hex(self._read_byte_list_to_int(curr_index, byte_count))}")
        raise SystemError(f"{message}: {hex(curr_index)} -> {hex(self._read_byte_list_to_int(curr_index, byte_count))}")

    ### VOXEL SECTION

    def _obtain_objects_0x14_in_voxel(self, curr_index, voxel_count):
        '''
        For objects with 20 bytes (will refer to as objects 0x14, or complex objects),
        the list starts with 0x0B, and ends with 0x08, with all objects in between.
        '''
        num_of_objects = self._read_byte(curr_index + 0x3)
        if(num_of_objects > 0):
            if(self._read_byte(curr_index + 0x4) != 0x0B):
                self._debug_print("Miscalculated Voxel Object 0x14 List Start", curr_index, byte_count=1, add_index_count=4)
            # Objects End Index = Voxel Start Index + Voxel Header (0x4) + Object List End Indicator (0x1) + Num Of Objects * Length Of Objects (0x14)
            objects_end_index = curr_index + 0x5 + num_of_objects * 0x14
            if(self._read_byte(objects_end_index) != 0x08):
                self._debug_print("Miscalculated Voxel Object 0x14 List End", curr_index, byte_count=1, add_index_count=0)
            for object_start_index in range(curr_index + 0x5, objects_end_index, 20):
                object_info_dict = self._get_object_0x14_info(object_start_index)
                self._voxel_dict[voxel_count][OBJECT_0x14_LIST].append(object_info_dict)
        else:
            objects_end_index = curr_index + 0x4
        return objects_end_index

    def _obtain_objects_0x0C_in_voxel(self, curr_index, voxel_count):
        '''
        For objects with 12 bytes (will refer to as objects 0x0C, or simple objects),
        the list starts with 0x09, followed by all objects, and no distinct ending.
        '''
        num_of_objects = self._read_byte(curr_index + 0x1)
        # If there are additional objects, the next value should be 0x09, followed by additional object list
        # If not, move on
        if(num_of_objects > 0):
            if(self._read_byte(curr_index + 0x2) != 0x09):
                self._debug_print("Miscalculated Voxel Object 0x0C List Start", curr_index, byte_count=1, add_index_count=2)
            objects_end_index = curr_index + 0x3 + num_of_objects * 0xC
            for object_start_index in range(curr_index + 0x3, objects_end_index, 0xC):
                object_info_dict = self._get_object_0x0C_info(object_start_index)
                self._voxel_dict[voxel_count][OBJECT_0x0C_LIST].append(object_info_dict)
        else:
            objects_end_index = curr_index + 0x2
        return objects_end_index

    def _check_voxel_condition(self, curr_index, byte_count, desired_value):
        '''
        Given a condition, we check whether the next byte(s) match a desired target.
        This is used for checking if a voxel is empty or has contents.
        '''
        return self._read_byte_list_to_int(curr_index, byte_count) == desired_value
    
    def _empty_voxel(self, curr_index, increase_index=0):
        '''
        When a voxel is empty, we typically pass over it or increase the current index
        '''
        return curr_index + increase_index

    def _voxel_with_content(self, curr_index, voxel_count, increase_index=0):
        '''
        When a voxel has content,
        we grab the list of objects with 20 byte attributes (0x14, or complex objects)
        and the list of objects with 12 byte attributes (0x0C, or simple objects)
        '''
        curr_index  = self._obtain_objects_0x14_in_voxel(curr_index, voxel_count)
        curr_index = self._obtain_objects_0x0C_in_voxel(curr_index, voxel_count)
        return curr_index + increase_index

    def _get_first_voxel_info(self, curr_index):
        '''
        Checks the first voxel for content, and grabs the object list(s), if any
        '''
        self._voxel_dict[0] = {OBJECT_0x14_LIST: [], OBJECT_0x0C_LIST: []}
        if(self._check_voxel_condition(curr_index, byte_count=1, desired_value=0x01)):
            self._voxel_dict[0][EMPTY_VOXEL] = True
            curr_index = self._empty_voxel(curr_index)
        elif(self._check_voxel_condition(curr_index, byte_count=2, desired_value=0x030A)):
            self._voxel_dict[0][EMPTY_VOXEL] = False
            curr_index = self._voxel_with_content(curr_index-1, voxel_count=0)
        else:
            self._debug_print("Unknown Voxel Header Start", curr_index, byte_count=3)
        return curr_index
    
    def _get_last_voxel_info(self, curr_index, voxel_count):
        '''
        Checks the last voxel for content, and grabs the object list(s), if any
        '''
        self._voxel_dict[voxel_count] = {OBJECT_0x14_LIST: [], OBJECT_0x0C_LIST: []}
        if(self._check_voxel_condition(curr_index, byte_count=3, desired_value=0x010003)):
            self._voxel_dict[voxel_count][EMPTY_VOXEL] = True
            curr_index = self._empty_voxel(curr_index, increase_index=3)
        elif(self._check_voxel_condition(curr_index, byte_count=2, desired_value=0x01030A)):
            self._voxel_dict[voxel_count][EMPTY_VOXEL] = False
            curr_index = self._voxel_with_content(curr_index, voxel_count, increase_index=2)
        else:
            self._debug_print("Unknown Voxel Header Start", curr_index, byte_count=2)
        return curr_index

    def _get_other_voxel_info(self, curr_index, voxel_count):
        '''
        Checks the voxel for content, and grabs the object list(s), if any
        '''
        self._voxel_dict[voxel_count] = {OBJECT_0x14_LIST: [], OBJECT_0x0C_LIST: []}
        if(self._check_voxel_condition(curr_index, byte_count=2, desired_value=0x0101)):
            self._voxel_dict[voxel_count][EMPTY_VOXEL] = True
            curr_index = self._empty_voxel(curr_index, increase_index=1)
        elif(self._check_voxel_condition(curr_index, byte_count=3, desired_value=0x01030A)):
            self._voxel_dict[voxel_count][EMPTY_VOXEL] = False
            curr_index = self._voxel_with_content(curr_index, voxel_count)
        else:
            self._debug_print("Unknown Voxel Header Start", curr_index, byte_count=2, add_index_count=1)
        return curr_index
    
    def _verifying_start_of_cameras(self, curr_index):
        if(not self._check_voxel_condition(curr_index-2, byte_count=2, desired_value=0x0003)):
            self._debug_print("Incorrect Camera Start", curr_index-2, byte_count=2)

    def _get_all_voxel_info(self, last_voxel_count):
        '''
        Runs through every voxel in the setup file to check for content.
        The first and last voxels have different conditions, so they get seperate functions.
        If the pattern doesn't match, an error is raised.
        '''
        curr_index = 0x1A
        curr_index = self._get_first_voxel_info(curr_index)
        for curr_voxel_count in range(1, last_voxel_count + 1):
            if(curr_voxel_count == last_voxel_count):
                curr_index = self._get_last_voxel_info(curr_index, curr_voxel_count)
                continue
            else:
                curr_index = self._get_other_voxel_info(curr_index, curr_voxel_count)
                continue
        self._verifying_start_of_cameras(curr_index)
        return curr_index

    ### CAMERA SECTION

    def _get_camera_info(self, curr_index):
        camera_type = self._read_byte(curr_index + 0x4)
        if(camera_type == 0):
            self._get_camera_type0_info(curr_index)
            curr_index += 0x5
        elif(camera_type == 1):
            self._get_camera_type1_info(curr_index)
            curr_index += 0x37
        elif(camera_type == 2):
            self._get_camera_type2_info(curr_index)
            curr_index += 0x20
        elif(camera_type == 3):
            self._get_camera_type3_info(curr_index)
            curr_index += 0x40
        elif(camera_type == 4):
            self._get_camera_type4_info(curr_index)
            curr_index += 0xB
        return curr_index

    def _end_of_camera_section(self, curr_index):
        return self._read_byte_list_to_int(curr_index, 2) != 0x0004

    def _get_all_camera_info(self, curr_index):
        '''
        PyDoc
        '''
        while(self._end_of_camera_section(curr_index)):
            curr_index = self._get_camera_info(curr_index)
        return curr_index + 2

    ### LIGHTING SECTION

    def _still_in_lighting_section(self, curr_index):
        return self._read_byte(curr_index) == 0x01

    def _get_all_lighting_section_info(self, curr_index):
        '''
        PyDoc
        '''
        lighting_count = 0
        while(self._still_in_lighting_section(curr_index)):
            self._get_lighting_section_info(lighting_count, curr_index)
            lighting_count += 1
            curr_index += 0x24
        return curr_index

    def _get_setup_file_info(self):
        '''
        PyDoc
        '''
        voxel_count = self._get_header_info()
        curr_index = self._get_all_voxel_info(voxel_count)
        curr_index = self._get_all_camera_info(curr_index)
        curr_index = self._get_all_lighting_section_info(curr_index)
        self._mmap.close()
    
    ############################
    ### GET OBJECT 0x14 INFO ###
    ############################

    def _get_actor_object_0x14_info(self, start_index):
        '''
        PyDoc
        '''
        node = self._read_byte_list_to_hex_str(start_index + 0x10, 3)
        object_info_dict = {
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x02, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x04, 2), 2),
            "Script_ID": self._read_byte_list_to_int(start_index + 0x06, 2),
            "Object_ID": self._read_byte_list_to_int(start_index + 0x08, 2),
            "Unk_Byte_A": self._read_byte(start_index + 0x0A),
            "Unk_Byte_B": self._read_byte(start_index + 0x0B),
            "Rotation": self._read_byte(start_index + 0x0C),
            "Unk_Byte_D": self._read_byte(start_index + 0x0D),
            "Size": self._read_byte_list_to_int(start_index + 0x0E, 2),
            "Current_Node": int(node[:3], 16),
            "Next_Node": int(node[3:], 16),
            "End_Object_Indicator": self._read_byte(start_index + 0x13),
        }
        return object_info_dict

    def _get_timed_object_0x14_info(self, start_index):
        '''
        PyDoc
        '''
        node = self._read_byte_list_to_hex_str(start_index + 0x10, 3)
        object_info_dict = {
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x02, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x04, 2), 2),
            "Script_ID": self._read_byte_list_to_int(start_index + 0x06, 2),
            "Object_ID": self._read_byte_list_to_int(start_index + 0x08, 2),
            "Unk_Byte_A": self._read_byte(start_index + 0x0A),
            "Unk_Byte_B": self._read_byte(start_index + 0x0B),
            "Timer": self._read_byte(start_index + 0x0C),
            "Unk_Byte_D": self._read_byte(start_index + 0x0D),
            "Size": self._read_byte_list_to_int(start_index + 0x0E, 2),
            "Current_Node": int(node[:3], 16),
            "Next_Node": int(node[3:], 16),
            "End_Object_Indicator": self._read_byte(start_index + 0x13),
        }
        return object_info_dict

    def _get_script_object_0x14_info(self, start_index):
        '''
        PyDoc
        '''
        node = self._read_byte_list_to_hex_str(start_index + 0x10, 3)
        object_info_dict = {
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x02, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x04, 2), 2),
            "Script_ID": self._read_byte_list_to_int(start_index + 0x06, 2),
            "Object_ID": self._read_byte_list_to_int(start_index + 0x08, 2),
            "Unk_Byte_A": self._read_byte(start_index + 0x0A),
            "Unk_Byte_B": self._read_byte(start_index + 0x0B),
            "Unk_Byte_C": self._read_byte(start_index + 0x0C),
            "Unk_Byte_D": self._read_byte(start_index + 0x0D),
            "Unk_Byte_E": self._read_byte(start_index + 0x0E),
            "Unk_Byte_F": self._read_byte(start_index + 0x0F),
            "Current_Node": int(node[:3], 16),
            "Next_Node": int(node[3:], 16),
            "End_Object_Indicator": self._read_byte(start_index + 0x13),
        }
        return object_info_dict

    def _get_radius_object_0x14_info(self, start_index):
        '''
        PyDoc
        '''
        node = self._read_byte_list_to_hex_str(start_index + 0x10, 3)
        object_info_dict = {
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x02, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x04, 2), 2),
            "Radius": self._read_byte(start_index + 0x06) << 1,
            "Object_ID": self._read_byte(start_index + 0x07),
            "Associated_ID": self._read_byte_list_to_int(start_index + 0x08, 2),
            "Unk_Byte_A": self._read_byte(start_index + 0x0A),
            "Unk_Byte_B": self._read_byte(start_index + 0x0B),
            "Unk_Byte_C": self._read_byte(start_index + 0x0C),
            "Unk_Byte_D": self._read_byte(start_index + 0x0D),
            "Unk_Byte_E": self._read_byte(start_index + 0x0E),
            "Unk_Byte_F": self._read_byte(start_index + 0x0F),
            "Current_Node": int(node[:3], 16),
            "Next_Node": int(node[3:], 16),
            "End_Object_Indicator": self._read_byte(start_index + 0x13),
        }
        return object_info_dict
    
    def _get_unknown_object_0x14_info(self, start_index):
        '''
        PyDoc
        '''
        node = self._read_byte_list_to_hex_str(start_index + 0x10, 3)
        object_info_dict = {
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x02, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x04, 2), 2),
            "Unk_Byte_6": self._read_byte(start_index + 0x06),
            "Unk_Byte_7": self._read_byte(start_index + 0x07),
            "Unk_Byte_8": self._read_byte(start_index + 0x08),
            "Unk_Byte_9": self._read_byte(start_index + 0x09),
            "Unk_Byte_A": self._read_byte(start_index + 0x0A),
            "Unk_Byte_B": self._read_byte(start_index + 0x0B),
            "Unk_Byte_C": self._read_byte(start_index + 0x0C),
            "Unk_Byte_D": self._read_byte(start_index + 0x0D),
            "Unk_Byte_E": self._read_byte(start_index + 0x0E),
            "Unk_Byte_F": self._read_byte(start_index + 0x0F),
            "Current_Node": int(node[:3], 16),
            "Next_Node": int(node[3:], 16),
            "End_Object_Indicator": self._read_byte(start_index + 0x13),
        }
        return object_info_dict

    def _get_object_0x14_info(self, start_index):
        '''
        PyDoc
        '''
        word4 = self._read_byte_list_to_int(start_index + 0x06, 2)
        word5 = self._read_byte_list_to_int(start_index + 0x08, 2)
        byte7 = self._read_byte(start_index + 0x07)
        if((word5, word4) in ACTOR_OBJECT_DICT):
            object_info_dict = self._get_actor_object_0x14_info(start_index)
        elif((word5, word4) in TIMED_OBJECT_DICT):
            object_info_dict = self._get_timed_object_0x14_info(start_index)
        elif((word5, word4) in MISC_OBJECT_DICT):
            object_info_dict = self._get_script_object_0x14_info(start_index)
        elif(byte7 in RADIUS_OBJECT_ID_DICT):
            object_info_dict = self._get_radius_object_0x14_info(start_index)
        else:
            object_info_dict = self._get_unknown_object_0x14_info(start_index)
        return object_info_dict
    
    ############################
    ### GET OBJECT 0x0C INFO ###
    ############################

    def _get_sprite_object_info(self, start_index):
        '''
        PyDoc
        '''
        object_info_dict = {
            "Object_ID": self._read_byte_list_to_int(start_index, 2),
            "Size": self._read_byte_list_to_int(start_index + 0x2, 2),
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x4, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x6, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x8, 2), 2),
            "Unk_Byte_A": self._read_byte(start_index + 0xA),
            "Unk_Byte_B": self._read_byte(start_index + 0xB),
        }
        return object_info_dict

    def _get_static_object_info(self, start_index):
        '''
        PyDoc
        '''
        object_info_dict = {
            "Object_ID": self._read_byte_list_to_int(start_index, 2),
            "Rotation_Y": self._read_byte(start_index + 0x2),
            "Rotation_XZ": self._read_byte(start_index + 0x3),
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x4, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x6, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x8, 2), 2),
            "Size": self._read_byte(start_index + 0xA),
            "Unk_Byte_B": self._read_byte(start_index + 0xB),
        }
        return object_info_dict

    def _get_unknown_object_0x0C_info(self, start_index):
        '''
        PyDoc
        '''
        object_info_dict = {
            "Object_ID": self._read_byte_list_to_int(start_index, 2),
            "Unk_Byte_2": self._read_byte(start_index + 0x2),
            "Unk_Byte_3": self._read_byte(start_index + 0x3),
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x4, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x6, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x8, 2), 2),
            "Unk_Byte_A": self._read_byte(start_index + 0xA),
            "Unk_Byte_B": self._read_byte(start_index + 0xB),
        }
        return object_info_dict

    def _get_object_0x0C_info(self, start_index):
        '''
        PyDoc
        '''
        object_id = self._read_byte_list_to_int(start_index, 2)
        if(object_id in SPRITE_OBJECT_DICT):
            object_info_dict = self._get_sprite_object_info(start_index)
        elif(object_id in STATIC_OBJECT_DICT):
            object_info_dict = self._get_static_object_info(start_index)
        else:
            object_info_dict = self._get_unknown_object_0x0C_info(start_index)
        return object_info_dict
    
    #############################
    ### GET CAMERA TYPES INFO ###
    #############################

    def _get_camera_type0_info(self, index_start):
        camera_id = self._read_byte(index_start + 0x2)
        self._camera_dict[camera_id] = {
            "Camera_Start": self._read_byte(index_start),
            "Unk_Byte_1": self._read_byte(index_start + 0x1),
            "Camera_Id": camera_id,
            "Unk_Byte_3": self._read_byte(index_start + 0x3), # It's always 02
            "Camera_End": self._read_byte(index_start + 0x4),
        }

    def _get_camera_type1_info(self, index_start):
        camera_id = self._read_byte(index_start + 0x2)
        self._camera_dict[camera_id] = {
            "Camera_Start": self._read_byte(index_start),
            "Unk_Byte_1": self._read_byte(index_start + 0x1),
            "Camera_Id": camera_id,
            "Unk_Byte_3": self._read_byte(index_start + 0x3), # It's always 02
            "Camera_Type": self._read_byte(index_start + 0x4),
            # "Section1": self._read_byte(index_start + 0x5), # It's always 01
                "X_Position": self._read_byte_list_to_float(index_start + 0x6, 4),
                "Y_Position": self._read_byte_list_to_float(index_start + 0xA, 4),
                "Z_Position": self._read_byte_list_to_float(index_start + 0xE, 4),
            # "Section2": self._read_byte(index_start + 0x12), # It's always 02
                "Horizontal_Speed": self._read_byte_list_to_float(index_start + 0x13, 4),
                "Vertical_Speed": self._read_byte_list_to_float(index_start + 0x17, 4),
            # "Section3": self._read_byte(index_start + 0x1B), # It's always 03
                "Rotation": self._read_byte_list_to_float(index_start + 0x1C, 4),
                "Acceleration": self._read_byte_list_to_float(index_start + 0x20, 4),
            # "Section4": self._read_byte(index_start + 0x24), # It's always 04
                "Pitch": self._read_byte_list_to_float(index_start + 0x25, 4),
                "Yaw": self._read_byte_list_to_float(index_start + 0x29, 4),
                "Roll": self._read_byte_list_to_float(index_start + 0x2D, 4),
            # "Section5": self._read_byte(index_start + 0x31), # It's always 05
                # "Unk_Byte_32": self._read_byte_list_to_float(index_start + 0x32, 4), # This causes errors
                "Unk_Byte_32": self._read_byte_list_to_int(index_start + 0x32, 4), # Just gonna use an int
            "Camera_End": self._read_byte(index_start + 0x36),
        }

    def _get_camera_type2_info(self, index_start):
        camera_id = self._read_byte(index_start + 0x2)
        self._camera_dict[camera_id] = {
            "Camera_Start": self._read_byte(index_start),
            "Unk_Byte_1": self._read_byte(index_start + 0x1),
            "Camera_Id": camera_id,
            "Unk_Byte_3": self._read_byte(index_start + 0x3), # It's always a 2
            "Camera_Type": self._read_byte(index_start + 0x4),
            "Section1": self._read_byte(index_start + 0x5),
                "X_Position": self._read_byte_list_to_float(index_start + 0x6, 4),
                "Y_Position": self._read_byte_list_to_float(index_start + 0xA, 4),
                "Z_Position": self._read_byte_list_to_float(index_start + 0xE, 4),
            "Section2": self._read_byte(index_start + 0x12),
                "Pitch": self._read_byte_list_to_float(index_start + 0x13, 4),
                "Yaw": self._read_byte_list_to_float(index_start + 0x17, 4),
                "Roll": self._read_byte_list_to_float(index_start + 0x1B, 4),
            "Camera_End": self._read_byte(index_start + 0x1F),
        }

    def _get_camera_type3_info(self, index_start):
        camera_id = self._read_byte(index_start + 0x2)
        self._camera_dict[camera_id] = {
            "Camera_Start": self._read_byte(index_start),
            "Unk_Byte_1": self._read_byte(index_start + 0x1),
            "Camera_Id": camera_id,
            "Unk_Byte_3": self._read_byte(index_start + 0x3), # It's always a 2
            "Camera_Type": self._read_byte(index_start + 0x4),
            "Section1": self._read_byte(index_start + 0x5),
                "X_Position": self._read_byte_list_to_float(index_start + 0x6, 4),
                "Y_Position": self._read_byte_list_to_float(index_start + 0xA, 4),
                "Z_Position": self._read_byte_list_to_float(index_start + 0xE, 4),
            "Section2": self._read_byte(index_start + 0x12),
                "Horizontal_Speed": self._read_byte_list_to_float(index_start + 0x13, 4),
                "Vertical_Speed": self._read_byte_list_to_float(index_start + 0x17, 4),
            "Section3": self._read_byte(index_start + 0x1B),
                "Rotation": self._read_byte_list_to_float(index_start + 0x1C, 4),
                "Acceleration": self._read_byte_list_to_float(index_start + 0x20, 4),
            "Section4": self._read_byte(index_start + 0x24),
                "Pitch": self._read_byte_list_to_float(index_start + 0x25, 4),
                "Yaw": self._read_byte_list_to_float(index_start + 0x29, 4),
                "Roll": self._read_byte_list_to_float(index_start + 0x2D, 4),
            "Section5": self._read_byte(index_start + 0x31),
                # "Unk_Byte_32": self._read_byte_list_to_float(index_start + 0x32, 4), # This causes errors
                "Unk_Byte_32": self._read_byte_list_to_int(index_start + 0x32, 4), # Just gonna use an int
            "Section6": self._read_byte(index_start + 0x36),
                "Close_Distance": self._read_byte_list_to_float(index_start + 0x37, 4),
                "Far_Distance": self._read_byte_list_to_float(index_start + 0x3B, 4),
            "Camera_End": self._read_byte(index_start + 0x3F),
        }

    def _get_camera_type4_info(self, index_start):
        camera_id = self._read_byte(index_start + 0x2)
        self._camera_dict[camera_id] = {
            "Camera_Start": self._read_byte(index_start),
            "Unk_Byte_1": self._read_byte(index_start + 0x1),
            "Camera_Id": camera_id,
            "Unk_Byte_3": self._read_byte(index_start + 0x3), # It's always a 2
            "Camera_Type": self._read_byte(index_start + 0x4),
            "Section1": self._read_byte(index_start + 0x5),
                "Unk_Byte_6": self._read_byte_list_to_float(index_start + 0x6, 4),
            "Camera_End": self._read_byte(index_start + 0xA),
        }

    #########################
    ### GET LIGHTING INFO ###
    #########################

    def _get_lighting_section_info(self, lighting_num, index_start):
        self._lighting_dict[lighting_num] = {
            "Section1": self._read_byte(index_start),
            "Section2": self._read_byte(index_start + 0x01),
                "X_Position": self._read_byte_list_to_float(index_start + 0x02, 4),
                "Y_Position": self._read_byte_list_to_float(index_start + 0x06, 4),
                "Z_Position": self._read_byte_list_to_float(index_start + 0x0A, 4),
            "Section3": self._read_byte(index_start + 0x0E),
                "Section3_Unk1": self._read_byte_list_to_float(index_start + 0x0F, 4),
                "Section3_Unk2": self._read_byte_list_to_float(index_start + 0x13, 4),
            "Section4": self._read_byte(index_start + 0x17),
                "Red": self._possible_negative(self._read_byte_list_to_int(index_start + 0x18, 4), 4),
                "Green": self._possible_negative(self._read_byte_list_to_int(index_start + 0x1C, 4), 4),
                "Blue": self._possible_negative(self._read_byte_list_to_int(index_start + 0x20, 4), 4),
        }
    
    #######################
    ### MAKE SETUP FILE ###
    #######################

    def _set_header(self):
        '''
        I won't be making changes to the header.
        There are some weird exceptions to the general rule that would
        make the setup files HUGE, and all of my editing won't need to
        remove the base voxels anyway.
        '''
        self._new_file.write(b"\x01\x01")
        if(self._neg_x_voxel_count):
            self._new_file.write((self._neg_x_voxel_count + 0x100000000).to_bytes(4, 'big'))
        else:
            self._new_file.write((0x00000000).to_bytes(4, 'big'))
        if(self._neg_y_voxel_count):
            self._new_file.write((self._neg_y_voxel_count + 0x100000000).to_bytes(4, 'big'))
        else:
            self._new_file.write((0x00000000).to_bytes(4, 'big'))
        if(self._neg_z_voxel_count):
            self._new_file.write((self._neg_z_voxel_count + 0x100000000).to_bytes(4, 'big'))
        else:
            self._new_file.write((0x00000000).to_bytes(4, 'big'))
        self._new_file.write(self._pos_x_voxel_count.to_bytes(4, 'big'))
        self._new_file.write(self._pos_y_voxel_count.to_bytes(4, 'big'))
        self._new_file.write(self._pos_z_voxel_count.to_bytes(4, 'big'))
        # Calculations
        x_voxel_count = self._pos_x_voxel_count - self._neg_x_voxel_count + 1
        y_voxel_count = self._pos_y_voxel_count - self._neg_y_voxel_count + 1
        z_voxel_count = self._pos_z_voxel_count - self._neg_z_voxel_count + 1
        return x_voxel_count * y_voxel_count * z_voxel_count

    def _set_voxel_section(self, voxel_count):
        '''
        PyDoc
        '''
        if(voxel_count + 1 != len(self._voxel_dict)):
            print(f"Voxel Count Changed: {voxel_count}, {len(self._voxel_dict)}")
            raise SystemError("Voxel Count Changed")
        for curr_voxel_count in sorted(self._voxel_dict):
            if(curr_voxel_count > 0):
                self._new_file.write(b"\x01")
            object_0x14_list_is_empty = len(self._voxel_dict[curr_voxel_count][OBJECT_0x14_LIST]) == 0
            object_0x0C_list_is_empty = len(self._voxel_dict[curr_voxel_count][OBJECT_0x0C_LIST]) == 0
            if(self._voxel_dict[curr_voxel_count][EMPTY_VOXEL]):
                continue
            self._new_file.write(b"\x03\x0A")
            self._new_file.write(len(self._voxel_dict[curr_voxel_count][OBJECT_0x14_LIST]).to_bytes(1, 'big'))
            if(not object_0x14_list_is_empty):
                self._new_file.write(b"\x0B")
                for object_0x14 in self._voxel_dict[curr_voxel_count][OBJECT_0x14_LIST]:
                    self._set_object_0x14_info(object_0x14)
            self._new_file.write(b"\x08")
            self._new_file.write(len(self._voxel_dict[curr_voxel_count][OBJECT_0x0C_LIST]).to_bytes(1, 'big'))
            if(not object_0x0C_list_is_empty):
                self._new_file.write(b"\x09")
                for object_0x0C in self._voxel_dict[curr_voxel_count][OBJECT_0x0C_LIST]:
                    self._set_object_0x0C_info(object_0x0C)

    def _set_camera_section(self):
        '''
        PyDoc
        '''
        self._new_file.write(b"\x00\x03")
        for camera_id in sorted(self._camera_dict):
            self._set_camera_info(self._camera_dict[camera_id])

    def _set_lighting_section(self):
        '''
        PyDoc
        '''
        self._new_file.write(b"\x00\x04")
        for lighting_num in sorted(self._lighting_dict):
            self._set_lighting_section_info(self._lighting_dict[lighting_num])
        self._new_file.write(b"\x00\x00")

    def _create_setup_file(self, file_dir, file_name):
        '''
        PyDoc
        '''
        with open(f"{file_dir}{file_name}.bin", "wb+") as self._new_file:
            voxel_count = self._set_header()
            self._set_voxel_section(voxel_count)
            self._set_camera_section()
            self._set_lighting_section()
    
    ############################
    ### SET OBJECT 0x14 INFO ###
    ############################

    def _set_actor_object_0x14_info(self, object_0x14):
        '''
        PyDoc
        '''
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["X_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Y_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Z_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Script_ID"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Object_ID"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_A"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_B"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Rotation"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_D"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Size"], 2))
        node = int(self._int_to_hex_str(object_0x14["Current_Node"], 3) + self._int_to_hex_str(object_0x14["Next_Node"], 3), 16)
        self._new_file.write(self._possible_negative_to_bytes(node, 3))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["End_Object_Indicator"], 1))

    def _set_timed_object_0x14_info(self, object_0x14):
        '''
        PyDoc
        '''
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["X_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Y_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Z_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Script_ID"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Object_ID"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_A"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_B"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Timer"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_D"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Size"], 2))
        node = int(self._int_to_hex_str(object_0x14["Current_Node"], 3) + self._int_to_hex_str(object_0x14["Next_Node"], 3), 16)
        self._new_file.write(self._possible_negative_to_bytes(node, 3))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["End_Object_Indicator"], 1))

    def _set_script_object_0x14_info(self, object_0x14):
        '''
        PyDoc
        '''
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["X_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Y_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Z_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Script_ID"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Object_ID"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_A"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_B"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_C"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_D"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_E"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_F"], 1))
        node = int(self._int_to_hex_str(object_0x14["Current_Node"], 3) + self._int_to_hex_str(object_0x14["Next_Node"], 3), 16)
        self._new_file.write(self._possible_negative_to_bytes(node, 3))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["End_Object_Indicator"], 1))

    def _set_radius_object_0x14_info(self, object_0x14):
        '''
        PyDoc
        '''
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["X_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Y_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Z_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Radius"] >> 1, 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Object_ID"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Associated_ID"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_A"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_B"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_C"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_D"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_E"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_F"], 1))
        node = int(self._int_to_hex_str(object_0x14["Current_Node"], 3) + self._int_to_hex_str(object_0x14["Next_Node"], 3), 16)
        self._new_file.write(self._possible_negative_to_bytes(node, 3))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["End_Object_Indicator"], 1))
    
    def _set_unknown_object_0x14_info(self, object_0x14):
        '''
        PyDoc
        '''
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["X_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Y_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Z_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_6"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_7"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_8"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_9"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_A"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_B"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_C"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_D"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_E"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["Unk_Byte_F"], 1))
        node = int(self._int_to_hex_str(object_0x14["Current_Node"], 3) + self._int_to_hex_str(object_0x14["Next_Node"], 3), 16)
        self._new_file.write(self._possible_negative_to_bytes(node, 3))
        self._new_file.write(self._possible_negative_to_bytes(object_0x14["End_Object_Indicator"], 1))

    def _set_object_0x14_info(self, object_0x14):
        '''
        PyDoc
        '''
        object_id = None
        script_id = None
        if("Object_ID" in object_0x14):
            object_id = object_0x14["Object_ID"]
        if("Script_ID" in object_0x14):
            script_id = object_0x14["Script_ID"]
        if(object_id == None and script_id == None):
            self._set_unknown_object_0x14_info(object_0x14)
        elif((object_id, script_id) in ACTOR_OBJECT_DICT):
            self._set_actor_object_0x14_info(object_0x14)
        elif((object_id, script_id) in TIMED_OBJECT_DICT):
            self._set_timed_object_0x14_info(object_0x14)
        elif((object_id, script_id) in MISC_OBJECT_DICT):
            self._set_script_object_0x14_info(object_0x14)
        elif(object_id in RADIUS_OBJECT_ID_DICT):
            self._set_radius_object_0x14_info(object_0x14)
        else:
            print("Unknown Object 0x14 Set")
            raise SystemError("Unknown Object 0x14 Set")
    
    ############################
    ### SET OBJECT 0x0C INFO ###
    ############################

    def _set_sprite_object_info(self, object_0x0C):
        '''
        PyDoc
        '''
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Object_ID"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Size"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["X_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Y_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Z_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Unk_Byte_A"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Unk_Byte_B"], 1))

    def _set_static_object_info(self, object_0x0C):
        '''
        PyDoc
        '''
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Object_ID"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Rotation_Y"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Rotation_XZ"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["X_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Y_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Z_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Size"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Unk_Byte_B"], 1))

    def _set_unknown_object_0x0C_info(self, object_0x0C):
        '''
        PyDoc
        '''
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Object_ID"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Unk_Byte_2"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Unk_Byte_3"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["X_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Y_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Z_Position"], 2))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Unk_Byte_A"], 1))
        self._new_file.write(self._possible_negative_to_bytes(object_0x0C["Unk_Byte_B"], 1))

    def _set_object_0x0C_info(self, object_0x0C):
        '''
        PyDoc
        '''
        object_id = object_0x0C["Object_ID"]
        if(object_id in SPRITE_OBJECT_DICT):
            self._set_sprite_object_info(object_0x0C)
        elif(object_id in STATIC_OBJECT_DICT):
            self._set_static_object_info(object_0x0C)
        else:
            self._set_unknown_object_0x0C_info(object_0x0C)
    
    #############################
    ### SET CAMERA TYPES INFO ###
    #############################

    def _set_camera_type0_info(self, camera_object):
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Start"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Unk_Byte_1"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Id"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Unk_Byte_3"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_End"], 1))

    def _set_camera_type1_info(self, camera_object):
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Start"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Unk_Byte_1"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Id"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Unk_Byte_3"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Type"], 1))
        self._new_file.write(b"\x01")
        self._new_file.write(self._float_to_byte_hex(camera_object["X_Position"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Y_Position"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Z_Position"]))
        self._new_file.write(b"\x02")
        self._new_file.write(self._float_to_byte_hex(camera_object["Horizontal_Speed"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Vertical_Speed"]))
        self._new_file.write(b"\x03")
        self._new_file.write(self._float_to_byte_hex(camera_object["Rotation"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Acceleration"]))
        self._new_file.write(b"\x04")
        self._new_file.write(self._float_to_byte_hex(camera_object["Pitch"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Yaw"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Roll"]))
        self._new_file.write(b"\x05")
        self._new_file.write(camera_object["Unk_Byte_32"].to_bytes(4, 'big')) # Fix This Later
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_End"], 1))

    def _set_camera_type2_info(self, camera_object):
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Start"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Unk_Byte_1"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Id"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Unk_Byte_3"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Type"], 1))
        self._new_file.write(b"\x01")
        self._new_file.write(self._float_to_byte_hex(camera_object["X_Position"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Y_Position"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Z_Position"]))
        self._new_file.write(b"\x02")
        self._new_file.write(self._float_to_byte_hex(camera_object["Pitch"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Yaw"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Roll"]))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_End"], 1))

    def _set_camera_type3_info(self, camera_object):
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Start"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Unk_Byte_1"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Id"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Unk_Byte_3"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Type"], 1))
        self._new_file.write(b"\x01")
        self._new_file.write(self._float_to_byte_hex(camera_object["X_Position"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Y_Position"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Z_Position"]))
        self._new_file.write(b"\x02")
        self._new_file.write(self._float_to_byte_hex(camera_object["Horizontal_Speed"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Vertical_Speed"]))
        self._new_file.write(b"\x03")
        self._new_file.write(self._float_to_byte_hex(camera_object["Rotation"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Acceleration"]))
        self._new_file.write(b"\x04")
        self._new_file.write(self._float_to_byte_hex(camera_object["Pitch"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Yaw"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Roll"]))
        self._new_file.write(b"\x05")
        self._new_file.write(camera_object["Unk_Byte_32"].to_bytes(4, 'big')) # Fix This Later
        self._new_file.write(b"\x06")
        self._new_file.write(self._float_to_byte_hex(camera_object["Close_Distance"]))
        self._new_file.write(self._float_to_byte_hex(camera_object["Far_Distance"]))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_End"], 1))

    def _set_camera_type4_info(self, camera_object):
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Start"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Unk_Byte_1"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Id"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Unk_Byte_3"], 1))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_Type"], 1))
        self._new_file.write(b"\x01")
        self._new_file.write(self._float_to_byte_hex(camera_object["Unk_Byte_6"]))
        self._new_file.write(self._possible_negative_to_bytes(camera_object["Camera_End"], 1))

    def _set_camera_info(self, camera_object):
        if("Camera_Type" not in camera_object):
            self._set_camera_type0_info(camera_object)
            return
        camera_type = camera_object["Camera_Type"]
        if(camera_type == 1):
            self._set_camera_type1_info(camera_object)
        elif(camera_type == 2):
            self._set_camera_type2_info(camera_object)
        elif(camera_type == 3):
            self._set_camera_type3_info(camera_object)
        elif(camera_type == 4):
            self._set_camera_type4_info(camera_object)
        else:
            print("Unknown Camera Type?")
            raise SystemError("Unknown Camera Type?")

    #########################
    ### SET LIGHTING INFO ###
    #########################

    def _set_lighting_section_info(self, lighting_object):
        self._new_file.write(self._possible_negative_to_bytes(lighting_object["Section1"], 1))
        self._new_file.write(self._possible_negative_to_bytes(lighting_object["Section2"], 1))
        self._new_file.write(self._float_to_byte_hex(lighting_object["X_Position"]))
        self._new_file.write(self._float_to_byte_hex(lighting_object["Y_Position"]))
        self._new_file.write(self._float_to_byte_hex(lighting_object["Z_Position"]))
        self._new_file.write(self._possible_negative_to_bytes(lighting_object["Section3"], 1))
        self._new_file.write(self._float_to_byte_hex(lighting_object["Section3_Unk1"]))
        self._new_file.write(self._float_to_byte_hex(lighting_object["Section3_Unk2"]))
        self._new_file.write(self._possible_negative_to_bytes(lighting_object["Section4"], 1))
        self._new_file.write(self._possible_negative_to_bytes(lighting_object["Red"], 4))
        self._new_file.write(self._possible_negative_to_bytes(lighting_object["Green"], 4))
        self._new_file.write(self._possible_negative_to_bytes(lighting_object["Blue"], 4))
    
    #############################
    ### MANIULATION FUNCTIONS ###
    #############################
    
    def _calculate_voxel_num(self, x_position, y_position, z_position):
        x_count = (self._possible_negative(x_position, 2) - (self._neg_x_voxel_count * 1000)) // 1000
        y_count = (self._possible_negative(y_position, 2) - (self._neg_y_voxel_count * 1000)) // 1000
        z_count = (self._possible_negative(z_position, 2) - (self._neg_z_voxel_count * 1000)) // 1000
        y_dimension = self._pos_y_voxel_count - self._neg_y_voxel_count + 1
        z_dimension = self._pos_z_voxel_count - self._neg_z_voxel_count + 1
        voxel_num = x_count * (y_dimension * z_dimension) + y_count * (z_dimension) + z_count
        return voxel_num

    ### REMOVE

    def _remove_complex_object_by_attributes(self, original_objects_dict):
        for voxel_num in self._voxel_dict:
            curr_item_num = 0
            while(curr_item_num < len(self._voxel_dict[voxel_num][OBJECT_0x14_LIST])):
                curr_item = self._voxel_dict[voxel_num][OBJECT_0x14_LIST][curr_item_num]
                remove_this = True
                for attribute in original_objects_dict:
                    if((attribute not in curr_item) or (curr_item[attribute] != original_objects_dict[attribute])):
                        remove_this = False
                        break
                if(remove_this):
                    self._voxel_dict[voxel_num][OBJECT_0x14_LIST].pop(curr_item_num)
                else:
                    curr_item_num += 1

    def _remove_simple_object_by_attributes(self, original_objects_dict):
        for voxel_num in self._voxel_dict:
            curr_item_num = 0
            while(curr_item_num < len(self._voxel_dict[voxel_num][OBJECT_0x0C_LIST])):
                curr_item = self._voxel_dict[voxel_num][OBJECT_0x0C_LIST][curr_item_num]
                remove_this = True
                for attribute in original_objects_dict:
                    if((attribute not in curr_item) or (curr_item[attribute] != original_objects_dict[attribute])):
                        remove_this = False
                        break
                if(remove_this):
                    self._voxel_dict[voxel_num][OBJECT_0x0C_LIST].pop(curr_item_num)
                else:
                    curr_item_num += 1

    def _remove_complex_object_instances(self, voxel_num, complex_object_list):
        curr_item_num = 0
        while(curr_item_num < len(self._voxel_dict[voxel_num][OBJECT_0x14_LIST])):
            item_popped = False
            curr_item = self._voxel_dict[voxel_num][OBJECT_0x14_LIST][curr_item_num]
            if("Script_ID" in curr_item):
                if((curr_item["Object_ID"], curr_item["Script_ID"]) in ACTOR_OBJECT_DICT):
                    if(ACTOR_OBJECT_DICT[(curr_item["Object_ID"], curr_item["Script_ID"])] in complex_object_list):
                        self._voxel_dict[voxel_num][OBJECT_0x14_LIST].pop(curr_item_num)
                        item_popped = True
                elif((curr_item["Object_ID"], curr_item["Script_ID"]) in TIMED_OBJECT_DICT):
                    if(TIMED_OBJECT_DICT[(curr_item["Object_ID"], curr_item["Script_ID"])] in complex_object_list):
                        self._voxel_dict[voxel_num][OBJECT_0x14_LIST].pop(curr_item_num)
                        item_popped = True
                elif((curr_item["Object_ID"], curr_item["Script_ID"]) in MISC_OBJECT_DICT):
                    if(MISC_OBJECT_DICT[(curr_item["Object_ID"], curr_item["Script_ID"])] in complex_object_list):
                        self._voxel_dict[voxel_num][OBJECT_0x14_LIST].pop(curr_item_num)
                        item_popped = True
            elif("Object_ID" in curr_item):
                if(curr_item["Object_ID"] in RADIUS_OBJECT_ID_DICT):
                    if(RADIUS_OBJECT_ID_DICT[curr_item["Object_ID"]] in complex_object_list):
                        self._voxel_dict[voxel_num][OBJECT_0x14_LIST].pop(curr_item_num)
                        item_popped = True
            if(not item_popped):
                curr_item_num += 1

    def _remove_simple_object_instances(self, voxel_num, simple_object_list):
        curr_item_num = 0
        while(curr_item_num < len(self._voxel_dict[voxel_num][OBJECT_0x0C_LIST])):
            item_popped = False
            curr_item = self._voxel_dict[voxel_num][OBJECT_0x0C_LIST][curr_item_num]
            if(curr_item["Object_ID"] in SPRITE_OBJECT_DICT):
                if(SPRITE_OBJECT_DICT[curr_item["Object_ID"]] in simple_object_list):
                    self._voxel_dict[voxel_num][OBJECT_0x0C_LIST].pop(curr_item_num)
                    item_popped = True
            elif(curr_item["Object_ID"] in STATIC_OBJECT_DICT):
                if(STATIC_OBJECT_DICT[curr_item["Object_ID"]] in simple_object_list):
                    self._voxel_dict[voxel_num][OBJECT_0x0C_LIST].pop(curr_item_num)
                    item_popped = True
            if(not item_popped):
                curr_item_num += 1

    def _remove_all_object_instances(self, complex_object_list=None, simple_object_list=None):
        for voxel_num in self._voxel_dict:
            if(complex_object_list is not None):
                self._remove_complex_object_instances(voxel_num, complex_object_list)
            if(simple_object_list is not None):
                self._remove_simple_object_instances(voxel_num, simple_object_list)
    
    def _remove_camera(self, camera_id):
        if(camera_id not in self._camera_dict):
            raise SystemError(f"Camera Doesn't Exists: {camera_id}")
        del self._camera_dict[camera_id]
    
    def _remove_lighting_dict(self):
        self._lighting_dict = {}

    ### MODIFY
    
    def _replace_complex_objects_by_id(self, original_objects_dict, new_object_dict):
        for voxel_num in self._voxel_dict:
            curr_item_num = 0
            while(curr_item_num < len(self._voxel_dict[voxel_num][OBJECT_0x14_LIST])):
                curr_item = self._voxel_dict[voxel_num][OBJECT_0x14_LIST][curr_item_num]
                if("Object_ID" in curr_item and
                   "Script_ID" in curr_item and 
                   (curr_item["Object_ID"], curr_item["Script_ID"]) in original_objects_dict):
                    self._voxel_dict[voxel_num][OBJECT_0x14_LIST][curr_item_num]["Object_ID"] = new_object_dict["Object_ID"]
                    self._voxel_dict[voxel_num][OBJECT_0x14_LIST][curr_item_num]["Script_ID"] = new_object_dict["Script_ID"]
                curr_item_num += 1
    
    def _modify_complex_objects(self, original_objects_dict, modification_dict):
        for voxel_num in self._voxel_dict:
            curr_item_num = 0
            while(curr_item_num < len(self._voxel_dict[voxel_num][OBJECT_0x14_LIST])):
                curr_item = self._voxel_dict[voxel_num][OBJECT_0x14_LIST][curr_item_num]
                modify_this = True
                same_voxel = True
                for attribute in original_objects_dict:
                    if((attribute not in curr_item) or (curr_item[attribute] != original_objects_dict[attribute])):
                        modify_this = False
                        break
                if(modify_this):
                    x_position = curr_item["X_Position"]
                    y_position = curr_item["Y_Position"]
                    z_position = curr_item["Z_Position"]
                    if("X_Position" in modification_dict):
                        x_position = modification_dict["X_Position"]
                    if("Y_Position" in modification_dict):
                        x_position = modification_dict["Y_Position"]
                    if("Z_Position" in modification_dict):
                        x_position = modification_dict["Z_Position"]
                    new_voxel_num = self._calculate_voxel_num(x_position, y_position, z_position)
                    same_voxel = voxel_num == new_voxel_num
                    if(same_voxel):
                        for attribute in modification_dict:
                            self._voxel_dict[voxel_num][OBJECT_0x14_LIST][curr_item_num][attribute] = modification_dict[attribute]
                    else:
                        for attribute in modification_dict:
                            curr_item[attribute] = modification_dict[attribute]
                        self._voxel_dict[voxel_num][OBJECT_0x14_LIST].pop(curr_item_num)
                        self._voxel_dict[new_voxel_num][OBJECT_0x14_LIST].append(curr_item)
                        self._voxel_dict[new_voxel_num][EMPTY_VOXEL] = False
                if(same_voxel):
                    curr_item_num += 1
    
    def _replace_static_with_actor_object(self, replacement_dict):
        for voxel_num in self._voxel_dict:
            curr_item_num = 0
            while(curr_item_num < len(self._voxel_dict[voxel_num][OBJECT_0x0C_LIST])):
                item_replaced = False
                curr_item = self._voxel_dict[voxel_num][OBJECT_0x0C_LIST][curr_item_num]
                curr_obj_id = curr_item["Object_ID"]
                if(curr_item["Object_ID"] in replacement_dict):
                    self._voxel_dict[voxel_num][OBJECT_0x0C_LIST].pop(curr_item_num)
                    replacement_object = replacement_dict[curr_obj_id]
                    object_dict = {
                        "X_Position": curr_item["X_Position"],
                        "Y_Position": curr_item["Y_Position"],
                        "Z_Position": curr_item["Z_Position"],
                        "Script_ID": replacement_object["Script_ID"],
                        "Object_ID": replacement_object["Object_ID"],
                        "Unk_Byte_A": replacement_object["Unk_Byte_A"],
                        "Unk_Byte_B": replacement_object["Unk_Byte_B"],
                        "Rotation": curr_item["Rotation_Y"],
                        "Unk_Byte_D": replacement_object["Unk_Byte_D"],
                        "Size": curr_item["Size"],
                        "Current_Node": replacement_object["Current_Node"],
                        "Next_Node": replacement_object["Next_Node"],
                        "End_Object_Indicator": 0x40,
                    }
                    self._voxel_dict[voxel_num][OBJECT_0x14_LIST].append(object_dict)
                    item_replaced = True
                if(not item_replaced):
                    curr_item_num += 1
    
    def _change_camera_id(self, old_camera_id, new_camera_id):
        self._camera_dict[new_camera_id] = self._camera_dict[old_camera_id]
        self._camera_dict[new_camera_id]["Camera_Id"] = new_camera_id
        del self._camera_dict[old_camera_id]

    def _adjust_all_lighting_colors(self, lighting_num, red=None, green=None, blue=None):
        if(red is not None):
            self._lighting_dict[lighting_num]["Red"] = red
        if(green is not None):
            self._lighting_dict[lighting_num]["Green"] = green
        if(blue is not None):
            self._lighting_dict[lighting_num]["Blue"] = blue

    def _adjust_lighting_position(self, lighting_num, x_pos=None, y_pos=None, z_pos=None):
        if(x_pos is not None):
            self._lighting_dict[lighting_num]["X_Position"] = x_pos
        if(y_pos is not None):
            self._lighting_dict[lighting_num]["Y_Position"] = y_pos
        if(z_pos is not None):
            self._lighting_dict[lighting_num]["Z_Position"] = z_pos
    
    def _adjust_lighting_unknown(self, lighting_num, unk1=None, unk2=None):
        if(unk1 is not None):
            self._lighting_dict[lighting_num]["Section3_Unk1"] = unk1
        if(unk2 is not None):
            self._lighting_dict[lighting_num]["Section3_Unk2"] = unk2

    ### ADD

    def _add_complex_object(self, object_dict):
        # Calculate Voxel Number
        x_position = object_dict["X_Position"]
        y_position = object_dict["Y_Position"]
        z_position = object_dict["Z_Position"]
        voxel_num = self._calculate_voxel_num(x_position, y_position, z_position)
        print(f"Voxel Num: {voxel_num}")
        # Add Object
        self._voxel_dict[voxel_num][OBJECT_0x14_LIST].append(object_dict)
        self._voxel_dict[voxel_num][EMPTY_VOXEL] = False

    def _add_simple_object(self, object_dict):
        # Calculate Voxel Number
        x_position = object_dict["X_Position"]
        y_position = object_dict["Y_Position"]
        z_position = object_dict["Z_Position"]
        voxel_num = self._calculate_voxel_num(x_position, y_position, z_position)
        print(f"Voxel Num: {voxel_num}")
        # Add Object
        self._voxel_dict[voxel_num][OBJECT_0x0C_LIST].append(object_dict)
        self._voxel_dict[voxel_num][EMPTY_VOXEL] = False
    
    def _add_camera(self, camera_dict):
        curr_camera_id = camera_dict["Camera_Id"]
        if(curr_camera_id in self._camera_dict):
            raise SystemError(f"Camera Already Exists: {curr_camera_id}")
        self._camera_dict[curr_camera_id] = camera_dict
    
    ### MISC

    def _object_count(self, object_name_list, object_count_dict=None):
        if(not object_count_dict):
            object_count_dict = {}
            for object_name in object_name_list:
                object_count_dict[object_name] = 0
        for voxel_num in self._voxel_dict:
            for curr_item in self._voxel_dict[voxel_num][OBJECT_0x14_LIST]:
                object_name = None
                if("Object_ID" in curr_item and "Script_ID" in curr_item):
                    object_tuple = (curr_item["Object_ID"], curr_item["Script_ID"])
                    if(object_tuple in ACTOR_OBJECT_DICT):
                        if(ACTOR_OBJECT_DICT[object_tuple] in object_count_dict):
                            object_name = ACTOR_OBJECT_DICT[object_tuple]
                    elif(object_tuple in TIMED_OBJECT_DICT):
                        if(TIMED_OBJECT_DICT[object_tuple] in object_count_dict):
                            object_name = TIMED_OBJECT_DICT[object_tuple]
                    elif(object_tuple in MISC_OBJECT_DICT):
                        if(MISC_OBJECT_DICT[object_tuple] in object_count_dict):
                            object_name = MISC_OBJECT_DICT[object_tuple]
                    if(object_name):
                        object_count_dict[object_name] += 1
            for curr_item in self._voxel_dict[voxel_num][OBJECT_0x0C_LIST]:
                object_name = None
                object_id = curr_item["Object_ID"]
                if("Object_ID" in curr_item):
                    if(object_id in SPRITE_OBJECT_DICT):
                        if(SPRITE_OBJECT_DICT[object_id] in object_count_dict):
                            object_name = SPRITE_OBJECT_DICT[object_id]
                    elif(object_id in STATIC_OBJECT_DICT):
                        if(STATIC_OBJECT_DICT[object_id] in object_count_dict):
                            object_name = STATIC_OBJECT_DICT[object_id]
                    if(object_name):
                        object_count_dict[object_name] += 1
        return object_count_dict

    def _object_xyz_positions(self, setup_pointer, setup_name, object_name_list):
        file_dir = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/Object_XYZ_Positions/"
        with open(f"{file_dir}{setup_pointer}-{setup_name}.txt", "w+") as f:
            for voxel_num in self._voxel_dict:
                for curr_item in self._voxel_dict[voxel_num][OBJECT_0x14_LIST]:
                    object_name = None
                    if("Object_ID" in curr_item and "Script_ID" in curr_item):
                        object_tuple = (curr_item["Object_ID"], curr_item["Script_ID"])
                        if(object_tuple in ACTOR_OBJECT_DICT):
                            if(ACTOR_OBJECT_DICT[object_tuple] in object_name_list):
                                object_name = ACTOR_OBJECT_DICT[object_tuple]
                        elif(object_tuple in TIMED_OBJECT_DICT):
                            if(TIMED_OBJECT_DICT[object_tuple] in object_name_list):
                                object_name = TIMED_OBJECT_DICT[object_tuple]
                        elif(object_tuple in MISC_OBJECT_DICT):
                            if(MISC_OBJECT_DICT[object_tuple] in object_name_list):
                                object_name = MISC_OBJECT_DICT[object_tuple]
                        if(object_name):
                            f.write(f"    ({curr_item['X_Position']}, {curr_item['Y_Position']}, {curr_item['Z_Position']}): [ # {object_name}\n    ],\n")
                for curr_item in self._voxel_dict[voxel_num][OBJECT_0x0C_LIST]:
                    object_name = None
                    object_id = curr_item["Object_ID"]
                    if("Object_ID" in curr_item):
                        if(object_id in SPRITE_OBJECT_DICT):
                            if(SPRITE_OBJECT_DICT[object_id] in object_name_list):
                                object_name = SPRITE_OBJECT_DICT[object_id]
                        elif(object_id in STATIC_OBJECT_DICT):
                            if(STATIC_OBJECT_DICT[object_id] in object_name_list):
                                object_name = STATIC_OBJECT_DICT[object_id]
                        if(object_name):
                            f.write(f"    ({curr_item['X_Position']}, {curr_item['Y_Position']}, {curr_item['Z_Position']}): [ # {object_name}\n    ],\n")

#############################################
################## TESTING ##################
#############################################

if __name__ == '__main__':
    import filecmp
    ORIGINAL_FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    COPY_FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test3/"

    ### SINGLE SETUP FILE TESTING ###
    rom_address = "4F0EC8"
    setup_obj = GENERIC_SETUP_FILE(ORIGINAL_FILE_DIR, rom_address)
    setup_obj._get_setup_file_info()
    setup_obj._create_setup_file(COPY_FILE_DIR, rom_address)

    ### ALL SETUP FILE TESTING ###
    # for rom_address in MAP_SETUP_DICT:
    #     print(f"Map: {rom_address} - {MAP_SETUP_DICT[rom_address]}")
    #     setup_obj = GENERIC_SETUP_FILE(ORIGINAL_FILE_DIR, rom_address)
    #     setup_obj._get_setup_file_info()
    #     setup_obj._create_setup_file(COPY_FILE_DIR, rom_address)
    #     if(not filecmp.cmp(f"{ORIGINAL_FILE_DIR}{rom_address}.bin", f"{COPY_FILE_DIR}{rom_address}.bin")):
    #         print("Does Not Match")
    #         exit(0)
    # print("Done")