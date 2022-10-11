from math import floor
import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS
from Automated.Game_Assets.Setups.Object_Dict import PHYSICAL_OBJECT_DICT, TIMED_OBJECT_DICT, RADIUS_OBJECT_ID_DICT, RADIUS_ASSOCIATED_ID_DICT, MISC_OBJECT_DICT, FOUND_UNKNOWN_OBJECT_DICT
from Automated.Game_Assets.Setups.Struct_Dict import SPRITE_STRUCT_DICT, OBJECT_STRUCT_DICT, FOUND_UNKNOWN_STRUCT_DICT

class GENERIC_SETUP_FILE(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._file_name = file_name
        self._object_dict = {}
        self._additional_struct_dict = {}
        self._camera_dict = {}
    
    #################
    ### BREAKDOWN ###
    #################

    def _get_voxel_count(self):
        '''
        Every voxel (or cubes if you're Wedarobi) is 1000 units.
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
        neg_x_voxel_count = self._possible_negative(self._read_byte_list_to_int(0x02, 4), 4)
        neg_y_voxel_count = self._possible_negative(self._read_byte_list_to_int(0x06, 4), 4)
        neg_z_voxel_count = self._possible_negative(self._read_byte_list_to_int(0x0A, 4), 4)
        # Positive Voxel Count
        pos_x_voxel_count = self._read_byte_list_to_int(0x0E, 4)
        pos_y_voxel_count = self._read_byte_list_to_int(0x12, 4)
        pos_z_voxel_count = self._read_byte_list_to_int(0x16, 4)
        # Calculations
        x_voxel_count = pos_x_voxel_count - neg_x_voxel_count + 1
        y_voxel_count = pos_y_voxel_count - neg_y_voxel_count + 1
        z_voxel_count = pos_z_voxel_count - neg_z_voxel_count + 1
        return x_voxel_count * y_voxel_count * z_voxel_count

    def _obtain_objects_in_voxel(self, curr_index):
        num_of_objects = self._read_byte(curr_index + 0x3)
        if(num_of_objects > 0):
            if(self._read_byte(curr_index + 0x4) != 0x0B):
                print(f"Miscalculated Voxel Object List Start: {hex(curr_index + 0x4)} -> {hex(self._read_byte(curr_index + 0x4))}")
                raise SystemError(f"Miscalculated Voxel Object List Start: {hex(curr_index + 0x4)} -> {hex(self._read_byte(curr_index + 0x4))}")
            # Objects End Index = Voxel Start Index + Voxel Header (0x4) + Object List End Indicator (0x1) + Num Of Objects * Length Of Objects (0x14)
            objects_end_index = curr_index + 0x5 + num_of_objects * 0x14
            if(self._read_byte(objects_end_index) != 0x08):
                print(f"Miscalculated Voxel Object List End: {hex(objects_end_index)} -> {hex(self._read_byte(objects_end_index))}")
                raise SystemError(f"Miscalculated Voxel Object List End: {hex(objects_end_index)} -> {hex(self._read_byte(objects_end_index))}")
            for object_start_index in range(curr_index + 0x5, objects_end_index, 20):
                self._get_object_info(object_start_index)
        else:
            objects_end_index = curr_index + 0x4
        return objects_end_index

    def _obtain_additional_structs_in_voxel(self, curr_index):
        num_of_additional_structs = self._read_byte(curr_index + 0x1)
        # If there are additional structs, the next value should be 0x09, followed by struct list
        # If not, move on
        if(num_of_additional_structs > 0):
            if(self._read_byte(curr_index + 0x2) != 0x09):
                print(f"Miscalculated Voxel Struct List Start: {curr_index + 0x2} -> {self._read_byte(curr_index + 0x2)}")
                raise SystemError(f"Miscalculated Voxel Struct List Start: {curr_index + 0x2} -> {self._read_byte(curr_index + 0x2)}")
            struct_end_index = curr_index + 0x3 + num_of_additional_structs * 0xC
            for struct_start_index in range(curr_index + 0x3, struct_end_index, 0xC):
                self._get_additional_struct_info(struct_start_index)
        else:
            struct_end_index = curr_index + 0x2
        return struct_end_index

    def _obtain_all_objects(self, voxel_count):
        '''
        Each voxel (or cubes if you're Wedarobi) starts with 0x030A.
        0x01 means the start of the NEXT voxel.
        If you see a 0x01 where a 0x030A should be, that means the former voxel is empty.
        This also means if you see the first voxel is 0x01, it's an empty first voxel.
        '''
        curr_index = 0x1A
        for curr_voxel in range(voxel_count + 1):
            print(f"Current Voxel Count: {curr_voxel}/{voxel_count}")
            print(f"Current Index: {hex(curr_index)}")
            if(curr_voxel == 0):
                if(self._read_byte(curr_index) == 0x01):
                    # Empty Voxel
                    pass
                elif(self._read_byte_list_to_int(curr_index, 2) == 0x030A):
                    # Voxel With Content
                    objects_end_index = self._obtain_objects_in_voxel(curr_index - 1)
                    curr_index = self._obtain_additional_structs_in_voxel(objects_end_index)
                else:
                    print(f"Unknown Voxel Header Start: {hex(curr_index + 1)} -> {hex(self._read_byte_list_to_int(curr_index + 1, 2))}")
                    raise SystemError(f"Unknown Voxel Header Start: {hex(curr_index + 1)} -> {hex(self._read_byte_list_to_int(curr_index + 1, 2))}")
            elif(curr_voxel == voxel_count):
                if(self._read_byte_list_to_int(curr_index + 0x1, 2) == 0x0003):
                    # Empty Voxel/End Of Objects
                    curr_index += 3
                elif(self._read_byte_list_to_int(curr_index + 0x1, 2) == 0x030A):
                    # Voxel With Content
                    objects_end_index = self._obtain_objects_in_voxel(curr_index)
                    curr_index = self._obtain_additional_structs_in_voxel(objects_end_index) + 2
                else:
                    print(f"Unknown Voxel Header Start: {hex(curr_index + 1)} -> {hex(self._read_byte_list_to_int(curr_index + 1, 2))}")
                    raise SystemError(f"Unknown Voxel Header Start: {hex(curr_index + 1)} -> {hex(self._read_byte_list_to_int(curr_index + 1, 2))}")
            elif(self._read_byte(curr_index) == 0x1):
                if(self._read_byte(curr_index + 0x1) == 0x01):
                    # Empty Voxel
                    curr_index += 1
                elif(self._read_byte_list_to_int(curr_index + 0x1, 2) == 0x030A):
                    # Voxel With Content
                    objects_end_index = self._obtain_objects_in_voxel(curr_index)
                    curr_index = self._obtain_additional_structs_in_voxel(objects_end_index)
                else:
                    print(f"Unknown Voxel Header Start: {hex(curr_index + 1)} -> {hex(self._read_byte_list_to_int(curr_index + 1, 2))}")
                    raise SystemError(f"Unknown Voxel Header Start: {hex(curr_index + 1)} -> {hex(self._read_byte_list_to_int(curr_index + 1, 2))}")
            else:
                print(f"Unknown Voxel Start: {curr_index} -> {self._read_byte_list_to_int(curr_index, 2)}")
                raise SystemError(f"Unknown Voxel Start: {curr_index} -> {self._read_byte_list_to_int(curr_index, 2)}")
        return curr_index

    def _obtain_all_cameras(self, curr_index):
        while(curr_index < len(self._mmap)):
            curr_index = self._get_camera_info(curr_index)

    def _breakdown_setup_file(self):
        voxel_count = self._get_voxel_count()
        curr_index = self._obtain_all_objects(voxel_count)
        self._obtain_all_cameras(curr_index)
        print(self._camera_dict)

    ###################
    ### RECONSTRUCT ###
    ###################

    def _check_header_min_max(self, curr_x, curr_y, curr_z):
        converted_x = floor(curr_x / 1000) * 1000
        converted_y = floor(curr_y / 1000) * 1000
        converted_z = floor(curr_z / 1000) * 1000
        if(converted_x < self._min_x):
            self._min_x = converted_x
        if(converted_x > self._max_x):
            self._max_x = converted_x
        if(converted_y < self._min_y):
            self._min_y = converted_y
        if(converted_y > self._max_y):
            self._max_y = converted_y
        if(converted_z < self._min_z):
            self._min_z = converted_z
        if(converted_z > self._max_z):
            self._max_z = converted_z
        return converted_x, converted_y, converted_z
    
    def _add_object_to_object_voxel_dict(self, converted_x, converted_y, converted_z, curr_object):
        lower_corner = (converted_x, converted_y, converted_z)
        if(lower_corner not in self._voxel_dict):
            self._object_voxel_dict[lower_corner] = []
        self._object_voxel_dict[lower_corner].append(curr_object)
    
    def _add_struct_to_struct_voxel_dict(self, converted_x, converted_y, converted_z, curr_object):
        lower_corner = (converted_x, converted_y, converted_z)
        if(lower_corner not in self._voxel_dict):
            self._additional_struct_voxel_dict[lower_corner] = []
        self._additional_struct_voxel_dict[lower_corner].append(curr_object)

    def _obtain_header_and_voxel_info(self):
        for object_type in self._object_dict:
            for curr_object in self._object_dict[object_type]:
                curr_x = curr_object["X_Position"]
                curr_y = curr_object["Y_Position"]
                curr_z = curr_object["Z_Position"]
                converted_x, converted_y, converted_z = self._check_header_min_max(curr_x, curr_y, curr_z)
                self._add_object_to_object_voxel_dict(converted_x, converted_y, converted_z, curr_object)
        for additional_struct_type in self._additional_struct_dict:
            for curr_struct in self._additional_struct_dict[additional_struct_type]:
                curr_x = curr_struct["X_Position"]
                curr_y = curr_struct["Y_Position"]
                curr_z = curr_struct["Z_Position"]
                converted_x, converted_y, converted_z = self._check_header_min_max(curr_x, curr_y, curr_z)
                self._add_struct_to_struct_voxel_dict(converted_x, converted_y, converted_z, curr_struct)

    def _create_header(self):
        neg_x_voxel_count = self._possible_negative_to_positive(floor(self._min_x / 1000), 4)
        pos_x_voxel_count = floor(self._max_x / 1000)
        neg_y_voxel_count = self._possible_negative_to_positive(floor(self._min_y / 1000), 4)
        pos_y_voxel_count = floor(self._max_y / 1000)
        neg_z_voxel_count = self._possible_negative_to_positive(floor(self._min_z / 1000), 4)
        pos_z_voxel_count = floor(self._max_z / 1000)

    def _create_voxels(self):
        first_voxel = True
        for curr_x in range(self._min_x, self._max_x + 1, 1000):
            for curr_y in range(self._min_y, self._max_y + 1, 1000):
                for curr_z in range(self._min_z, self._max_z + 1, 1000):
                    lower_corner = (curr_x, curr_y, curr_z)
                    if(not first_voxel):
                        # 01
                        pass
                    else:
                        first_voxel = False
                    if(lower_corner in self._object_voxel_dict):
                        # 03 0A
                        # len(self._object_voxel_dict[lower_corner])
                        # List Of Objects
                        pass
                    if(lower_corner in self._additional_struct_voxel_dict):
                        # len(self._additional_struct_voxel_dict[lower_corner])
                        # 09
                        # List Of Structs
                        pass

    def _create_cameras(self):
        pass

    def _reconstruct_setup_file(self):
        self._min_x = self._min_y = self._min_z = 0xFFFF
        self._max_x = self._max_y = self._max_z = -0xFFFF
        self._object_voxel_dict = {}
        self._additional_struct_voxel_dict = {}
        self._obtain_header_and_voxel_info()
        self._create_header()
        self._create_voxels()
        self._create_cameras()

    ###########################
    ### OBJECT MANIPULATION ###
    ###########################

    def _get_physical_object_info(self, start_index):
        node = self._read_byte_list_to_hex_str(start_index + 0x10, 3)
        object_info_dict = {
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x02, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x04, 2), 2),
            "Script_ID": self._read_byte_list_to_int(start_index + 0x06, 2),
            "Object_ID": self._read_byte_list_to_int(start_index + 0x08, 2),
            "Unk_Byte_A": self._read_byte(start_index + 0x0A),
            "Unk_Byte_B": self._read_byte(start_index + 0x0B),
            "Rotation": self._read_byte_list_to_int(start_index + 0x0C, 2),
            "Size": self._read_byte_list_to_int(start_index + 0x0E, 2),
            "Current_Node": int(node[:3], 16),
            "Next_Node": int(node[3:], 16),
            "End_Object_Indicator": self._read_byte(start_index + 0x13),
        }
        return object_info_dict

    def _get_timed_object_info(self, start_index):
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

    def _get_script_object_info(self, start_index):
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

    def _get_radius_object_info(self, start_index):
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
    
    def _get_unknown_object_info(self, start_index):
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

    def _get_object_info(self, start_index):
        word4 = self._read_byte_list_to_int(start_index + 0x06, 2)
        word5 = self._read_byte_list_to_int(start_index + 0x08, 2)
        byte7 = self._read_byte(start_index + 0x07)
        if((word5, word4) in PHYSICAL_OBJECT_DICT):
            object_info_dict = self._get_physical_object_info(start_index)
            if(PHYSICAL_OBJECT_DICT[(word5, word4)] not in self._object_dict):
                self._object_dict[PHYSICAL_OBJECT_DICT[(word5, word4)]] = []
            self._object_dict[PHYSICAL_OBJECT_DICT[(word5, word4)]].append(object_info_dict)
        elif((word5, word4) in TIMED_OBJECT_DICT):
            object_info_dict = self._get_timed_object_info(start_index)
            if(TIMED_OBJECT_DICT[(word5, word4)] not in self._object_dict):
                self._object_dict[TIMED_OBJECT_DICT[(word5, word4)]] = []
            self._object_dict[TIMED_OBJECT_DICT[(word5, word4)]].append(object_info_dict)
        elif((word5, word4) in MISC_OBJECT_DICT):
            object_info_dict = self._get_script_object_info(start_index)
            if(MISC_OBJECT_DICT[(word5, word4)] not in self._object_dict):
                self._object_dict[MISC_OBJECT_DICT[(word5, word4)]] = []
            self._object_dict[MISC_OBJECT_DICT[(word5, word4)]].append(object_info_dict)
        elif(byte7 in RADIUS_OBJECT_ID_DICT):
            object_info_dict = self._get_radius_object_info(start_index)
            if((RADIUS_OBJECT_ID_DICT[byte7] in RADIUS_ASSOCIATED_ID_DICT) and
                (word5 in RADIUS_ASSOCIATED_ID_DICT[RADIUS_OBJECT_ID_DICT[byte7]])):
                if(RADIUS_ASSOCIATED_ID_DICT[RADIUS_OBJECT_ID_DICT[byte7]][word5] not in self._object_dict):
                    self._object_dict[RADIUS_ASSOCIATED_ID_DICT[RADIUS_OBJECT_ID_DICT[byte7]][word5]] = []
                self._object_dict[RADIUS_ASSOCIATED_ID_DICT[RADIUS_OBJECT_ID_DICT[byte7]][word5]].append(object_info_dict)
            else:
                if(RADIUS_OBJECT_ID_DICT[byte7] not in self._object_dict):
                    self._object_dict[RADIUS_OBJECT_ID_DICT[byte7]] = []
                self._object_dict[RADIUS_OBJECT_ID_DICT[byte7]].append(object_info_dict)
        elif(((word5, word4) in FOUND_UNKNOWN_OBJECT_DICT) and (self._file_name in FOUND_UNKNOWN_OBJECT_DICT[(word5, word4)])):
            object_info_dict = self._get_unknown_object_info(start_index)
            if("Unknown-Found" not in self._object_dict):
                self._object_dict["Unknown-Found"] = []
            self._object_dict["Unknown-Found"].append(object_info_dict)
        else:
            object_info_dict = self._get_unknown_object_info(start_index)
            if("Unknown-New" not in self._object_dict):
                self._object_dict["Unknown-New"] = []
            self._object_dict["Unknown-New"].append(object_info_dict)

    def _add_object(self, new_object):
        self._object_dict[new_object]

    def _remove_object(self, curr_object):
        del self._object_dict[curr_object]

    def _modify_object(self, curr_object, attribute, new_val):
        self._object_dict[curr_object][attribute] = new_val

    ######################################
    ### ADDITIONAL STRUCT MANIPULATION ###
    ######################################

    def _get_sprite_struct_info(self, start_index):
        struct_info_dict = {
            "Struct_Id": self._read_byte_list_to_int(start_index, 2),
            "Unk_Byte_2": self._read_byte(start_index + 0x2),
            "Size": self._read_byte(start_index + 0x3),
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x4, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x6, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x8, 2), 2),
            "Unk_Byte_A": self._read_byte(start_index + 0xA),
            "Unk_Byte_B": self._read_byte(start_index + 0xB),
        }
        return struct_info_dict

    def _get_object_struct_info(self, start_index):
        struct_info_dict = {
            "Struct_Id": self._read_byte_list_to_int(start_index, 2),
            "Rotation_Y": self._read_byte(start_index + 0x2),
            "Rotation_XZ": self._read_byte(start_index + 0x3),
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x4, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x6, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x8, 2), 2),
            "Size": self._read_byte(start_index + 0xA),
            "Unk_Byte_B": self._read_byte(start_index + 0xB),
        }
        return struct_info_dict

    def _get_unknown_struct_info(self, start_index):
        struct_info_dict = {
            "Struct_Id": self._read_byte_list_to_int(start_index, 2),
            "Unk_Byte_2": self._read_byte(start_index + 0x2),
            "Unk_Byte_3": self._read_byte(start_index + 0x3),
            "X_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x4, 2), 2),
            "Y_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x6, 2), 2),
            "Z_Position": self._possible_negative(self._read_byte_list_to_int(start_index + 0x8, 2), 2),
            "Unk_Byte_A": self._read_byte(start_index + 0xA),
            "Unk_Byte_B": self._read_byte(start_index + 0xB),
        }
        return struct_info_dict

    def _get_additional_struct_info(self, start_index):
        struct_id = self._read_byte_list_to_int(start_index, 2)
        if(struct_id in SPRITE_STRUCT_DICT):
            struct_info_dict = self._get_sprite_struct_info(start_index)
            if(SPRITE_STRUCT_DICT[struct_id] not in self._additional_struct_dict):
                self._additional_struct_dict[SPRITE_STRUCT_DICT[struct_id]] = []
            self._additional_struct_dict[SPRITE_STRUCT_DICT[struct_id]].append(struct_info_dict)
        elif(struct_id in OBJECT_STRUCT_DICT):
            struct_info_dict = self._get_object_struct_info(start_index)
            if(OBJECT_STRUCT_DICT[struct_id] not in self._additional_struct_dict):
                self._additional_struct_dict[OBJECT_STRUCT_DICT[struct_id]] = []
            self._additional_struct_dict[OBJECT_STRUCT_DICT[struct_id]].append(struct_info_dict)
        elif((struct_id in FOUND_UNKNOWN_STRUCT_DICT)  and (self._file_name in FOUND_UNKNOWN_STRUCT_DICT[struct_id])):
            struct_info_dict = self._get_unknown_struct_info(start_index)
            if("Unknown-Found" not in self._additional_struct_dict):
                self._additional_struct_dict["Unknown-Found"] = []
            self._additional_struct_dict["Unknown-Found"].append(struct_info_dict)
        else:
            struct_info_dict = self._get_unknown_struct_info(start_index)
            if("Unknown-New" not in self._additional_struct_dict):
                self._additional_struct_dict["Unknown-New"] = []
            self._additional_struct_dict["Unknown-New"].append(struct_info_dict)

    def _add_additional_struct(self):
        pass

    def _remove_additional_struct(self):
        pass

    def _modify_additional_struct(self):
        pass

    ###########################
    ### CAMERA MANIPULATION ###
    ###########################

    def _get_camera_type1_info(self, index_start):
        camera_id = self._read_byte(index_start + 0x2)
        self._camera_dict[camera_id] = {
            "Camera_Start": self._read_byte(index_start),
            "Unk_Byte_1": self._read_byte(index_start + 0x1),
            "Camera_Id": camera_id,
            "Unk_Byte_3": self._read_byte(index_start + 0x3), # It's always 02
            "Camera_Type": self._read_byte(index_start + 0x4),
            # "Section1": self._read_byte(index_start + 0x5), # It's always 01
                "X_Position": self._byte_list_to_float(index_start + 0x6, 4),
                "Y_Position": self._byte_list_to_float(index_start + 0xA, 4),
                "Z_Position": self._byte_list_to_float(index_start + 0xE, 4),
            # "Section2": self._read_byte(index_start + 0x12), # It's always 02
                "Horizontal_Speed": self._byte_list_to_float(index_start + 0x13, 4),
                "Vertical_Speed": self._byte_list_to_float(index_start + 0x17, 4),
            # "Section3": self._read_byte(index_start + 0x1B), # It's always 03
                "Rotation": self._byte_list_to_float(index_start + 0x1C, 4),
                "Acceleration": self._byte_list_to_float(index_start + 0x20, 4),
            # "Section4": self._read_byte(index_start + 0x24), # It's always 04
                "Pitch": self._byte_list_to_float(index_start + 0x25, 4),
                "Yaw": self._byte_list_to_float(index_start + 0x29, 4),
                "Roll": self._byte_list_to_float(index_start + 0x2D, 4),
            # "Section5": self._read_byte(index_start + 0x31), # It's always 05
                "Unk_Byte_32": self._byte_list_to_float(index_start + 0x32, 4),
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
                "X_Position": self._byte_list_to_float(index_start + 0x6, 4),
                "Y_Position": self._byte_list_to_float(index_start + 0xA, 4),
                "Z_Position": self._byte_list_to_float(index_start + 0xE, 4),
            "Section2": self._read_byte(index_start + 0x12),
                "Pitch": self._byte_list_to_float(index_start + 0x13, 4),
                "Yaw": self._byte_list_to_float(index_start + 0x17, 4),
                "Roll": self._byte_list_to_float(index_start + 0x1B, 4),
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
                "X_Position": self._byte_list_to_float(index_start + 0x6, 4),
                "Y_Position": self._byte_list_to_float(index_start + 0xA, 4),
                "Z_Position": self._byte_list_to_float(index_start + 0xE, 4),
            "Section2": self._read_byte(index_start + 0x12),
                "Horizontal_Speed": self._byte_list_to_float(index_start + 0x13, 4),
                "Vertical_Speed": self._byte_list_to_float(index_start + 0x17, 4),
            "Section3": self._read_byte(index_start + 0x1B),
                "Rotation": self._byte_list_to_float(index_start + 0x1C, 4),
                "Acceleration": self._byte_list_to_float(index_start + 0x20, 4),
            "Section4": self._read_byte(index_start + 0x24),
                "Pitch": self._byte_list_to_float(index_start + 0x25, 4),
                "Yaw": self._byte_list_to_float(index_start + 0x29, 4),
                "Roll": self._byte_list_to_float(index_start + 0x2D, 4),
            "Section5": self._read_byte(index_start + 0x31),
                "Unk_Byte_32": self._byte_list_to_float(index_start + 0x32, 4),
            "Section6": self._read_byte(index_start + 0x36),
                "Close_Distance": self._byte_list_to_float(index_start + 0x37, 4),
                "Far_Distance": self._byte_list_to_float(index_start + 0x3B, 4),
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
                "Unk_Byte_6": self._byte_list_to_float(index_start + 0x6, 4),
            "Camera_End": self._read_byte(index_start + 0xA),
        }

    def _get_camera_info(self, curr_index):
        camera_type = self._read_byte(0x4)
        if(camera_type == 1):
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

    def _add_camera(self):
        pass
    
    def _remove_camera(self):
        pass

    def _modify_camera(self):
        pass

if __name__ == '__main__':
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    from shutil import copy
    copy(FILE_DIR + "4C5A30-Default.bin", FILE_DIR + "4C5A30.bin")
    setup_obj = GENERIC_SETUP_FILE(FILE_DIR, "4C5A30")
    setup_obj._breakdown_setup_file()
    setup_obj._reconstruct_setup_file()

# if __name__ == '__main__':
#     from Automated.Game_Assets.Setups.Map_Setup_Dict import MAP_SETUP_DICT
#     FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
#     # FILE_NAME = "4C5A30" # Mumbo's Mountain Main
#     # FILE_NAME = "4C7918" # Blubber's Ship
#     for FILE_NAME in MAP_SETUP_DICT:
#         setup_obj = GENERIC_SETUP_FILE(FILE_DIR, FILE_NAME)
#         setup_obj._breakdown_setup_file()
#         print_dict = {}
#         if("Unknown-New" in setup_obj._object_dict):
#             for item in setup_obj._object_dict["Unknown-New"]:
#                 print_dict[f"(0x{setup_obj._int_to_hex_str(item['Unk_Byte_8'], 2)}{setup_obj._int_to_hex_str(item['Unk_Byte_9'], 2)}, " +
#                            f"0x{setup_obj._int_to_hex_str(item['Unk_Byte_6'], 2)}{setup_obj._int_to_hex_str(item['Unk_Byte_7'], 2)})"] = f"\t{item['X_Position']} {item['Y_Position']} {item['Z_Position']}"
#             for item in sorted(print_dict):
#                 print(f"{item}\t{print_dict[item]}")
#         print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#         if("Unknown-New" in setup_obj._additional_struct_dict):
#             for item in setup_obj._additional_struct_dict["Unknown-New"]:
#                 print(f"{setup_obj._int_to_hex_str(item['Struct_Id'], 4)}\t{item['X_Position']} {item['Y_Position']} {item['Z_Position']}")
#         if(("Unknown-New" in setup_obj._object_dict) or ("Unknown-New" in setup_obj._additional_struct_dict)):
#             print(f'File Name: "{FILE_NAME}", # {MAP_SETUP_DICT[FILE_NAME]}')
#             exit(0)