from math import floor
import sys
import pandas as pd

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS
from Data_Files.Setups.Map_Setup_Dict import MAP_SETUP_DICT
from Data_Files.Setups.Object_Dict import PHYSICAL_OBJECT_DICT, TIMED_OBJECT_DICT, RADIUS_OBJECT_ID_DICT, RADIUS_ASSOCIATED_ID_DICT, MISC_OBJECT_DICT, FOUND_UNKNOWN_OBJECT_DICT
from Data_Files.Setups.Struct_Dict import SPRITE_STRUCT_DICT, OBJECT_STRUCT_DICT, FOUND_UNKNOWN_STRUCT_DICT

############################
### GATHER XYZ POSITIONS ###
############################

object_list = [
    "Mumbo Token", "Jiggy", "Empty Honeycomb", "Extra Life",
    "Honeycomb", "Blue Egg", "Red Feather", "Gold Feather",
    "Orange", "Blubber's Gold", "CCW Acorn", "CCW Caterpillar"]
struct_list = [
    "Red Feather", "Gold Feather", "Blue Egg", "Note",
    "MM Blue Flower", "MM Orange Yellow Flower", "MM Red Flower",
    "Orange (2D)", "Seashell", "SM Yellow Flower", "SM Purple Flower",
    "SM Yellow/Blue Flower", "SM Blue Flower",
]
area_name_list = []
rom_address_list = []
item_type_list = []
x_position_list = []
y_position_list = []
z_position_list = []

def convert_lists_to_excel(file_dir):
    df = pd.DataFrame({
        "Area_Name": area_name_list,
        "ROM_Address": rom_address,
        "Item_Type": item_type_list,
        "X_Position": x_position_list,
        "Y_Position": y_position_list,
        "Z_Position": z_position_list
        })
    writer = pd.ExcelWriter(f"{file_dir}XYZ_Positions.xlsx")
    df.to_excel(writer, index=False)
    writer.save()

def convert_lists_to_code(file_dir):
    with open(f"{file_dir}XYZ_Positions.txt", "w+") as xyz_file:
        xyz_file.write("FLOATING_ITEMS_DICT = {\n")
        for count, area_name in enumerate(area_name_list):
            xyz_file.write(f"\t(\"{area_name}\", {x_position_list[count]}, {y_position_list[count]}, {z_position_list[count]}): [ # {item_type_list[count]}\n")
            xyz_file.write(f"\t\t],\n")
        xyz_file.write("\t}")

class GENERIC_SETUP_FILE(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._file_name = file_name
        self._object_dict = {}
        self._additional_struct_dict = {}
        self._camera_dict = {}
        self._unknown_dict = {}
    
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
            # print(f"Current Voxel Count: {curr_voxel}/{voxel_count}")
            # print(f"Current Index: {hex(curr_index)}")
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
        while(self._read_byte_list_to_int(curr_index, 2) != 0x0004):
            curr_index = self._get_camera_info(curr_index)
        return curr_index + 2
    
    def _obtain_all_unknown(self, curr_index):
        unknown_count = 0
        while(self._read_byte(curr_index) == 0x01):
            self._get_unknown_section_info(unknown_count, curr_index)
            unknown_count += 1
            curr_index += 0x24
        return curr_index

    def _breakdown_setup_file(self):
        print("\tVoxels")
        voxel_count = self._get_voxel_count()
        print("\tObjects")
        curr_index = self._obtain_all_objects(voxel_count)
        print("\tCameras")
        curr_index = self._obtain_all_cameras(curr_index)
        print("\tUnknown")
        curr_index = self._obtain_all_unknown(curr_index)

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
                if(curr_x > 6000):
                    print(f"Curr Object: {curr_object}")
                    exit(0)
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
        print(f"neg_x_voxel_count: {hex(neg_x_voxel_count)}")
        print(f"pos_x_voxel_count: {hex(pos_x_voxel_count)}")
        print(f"neg_y_voxel_count: {hex(neg_y_voxel_count)}")
        print(f"pos_y_voxel_count: {hex(pos_y_voxel_count)}")
        print(f"neg_z_voxel_count: {hex(neg_z_voxel_count)}")
        print(f"pos_z_voxel_count: {hex(pos_z_voxel_count)}")

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
        self._voxel_dict = {}
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
                "Unk_Byte_32": self._read_byte_list_to_float(index_start + 0x32, 4),
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
                "Unk_Byte_32": self._read_byte_list_to_float(index_start + 0x32, 4),
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

    def _get_camera_info(self, curr_index):
        camera_type = self._read_byte(curr_index + 0x4)
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

#######################
### UNKNOWN SECTION ###
#######################

    def _get_unknown_section_info(self, unknown_num, index_start):
        self._unknown_dict[unknown_num] = {
            "Section1": self._read_byte(index_start),
            "Section2": self._read_byte(index_start + 0x01),
                "Section2_Unk1": self._read_byte_list_to_float(index_start + 0x02, 4),
                "Section2_Unk2": self._read_byte_list_to_float(index_start + 0x06, 4),
                "Section2_Unk2": self._read_byte_list_to_float(index_start + 0x0A, 4),
            "Section3": self._read_byte(index_start + 0x0E),
                "Section3_Unk1": self._read_byte_list_to_float(index_start + 0x0F, 4),
                "Section3_Unk2": self._read_byte_list_to_float(index_start + 0x13, 4),
            "Section4": self._read_byte(index_start + 0x17),
                "Section4_Unk1": self._possible_negative(self._read_byte_list_to_int(index_start + 0x18, 4), 4),
                "Section4_Unk2": self._possible_negative(self._read_byte_list_to_int(index_start + 0x1C, 4), 4),
                "Section4_Unk3": self._possible_negative(self._read_byte_list_to_int(index_start + 0x20, 4), 4),
        }
    
######################
### PRINT TO EXCEL ###
######################

    def _add_objects_to_lists(self, rom_address):
        for item_type in self._object_dict:
            if(item_type.startswith("Bottles Mound") or item_type.endswith("Jinjo") or item_type in object_list):
                for item in self._object_dict[item_type]:
                    area_name_list.append(MAP_SETUP_DICT[rom_address])
                    rom_address_list.append(rom_address)
                    item_type_list.append(item_type)
                    x_position_list.append(item['X_Position'])
                    y_position_list.append(item['Y_Position'])
                    z_position_list.append(item['Z_Position'])
        for item_type in self._additional_struct_dict:
            if(item_type in struct_list):
                for item in self._additional_struct_dict[item_type]:
                    area_name_list.append(MAP_SETUP_DICT[rom_address])
                    rom_address_list.append(rom_address)
                    item_type_list.append(item_type)
                    x_position_list.append(item['X_Position'])
                    y_position_list.append(item['Y_Position'])
                    z_position_list.append(item['Z_Position'])

##########################
### SPECIFIC FUNCTIONS ###
##########################

    def _convert_shock_jump_pads(self):
        pass

    def _convert_flight_pads(self):
        pass

    def _randomize_each_enemy(self):
        pass

###############
### TESTING ###
###############

if __name__ == '__main__':
    ORIGINAL_FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    COPY_FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test3/"
    from shutil import copy
    for rom_address in MAP_SETUP_DICT:
        print(f"Map: {rom_address} - {MAP_SETUP_DICT[rom_address]}")
        copy(ORIGINAL_FILE_DIR + rom_address + ".bin", COPY_FILE_DIR + rom_address + ".bin")
        setup_obj = GENERIC_SETUP_FILE(COPY_FILE_DIR, rom_address)
        setup_obj._breakdown_setup_file()
        setup_obj._add_objects_to_lists(rom_address)
        # for item in setup_obj._object_dict:
        #     print(item, setup_obj._object_dict[item], "\n")
        # for item in setup_obj._additional_struct_dict:
        #     print(item, setup_obj._additional_struct_dict[item], "\n")
        # for item in setup_obj._camera_dict:
        #     print(item, setup_obj._camera_dict[item], "\n")
        # for item in setup_obj._unknown_dict:
        #     print(item, setup_obj._unknown_dict[item], "\n")
        setup_obj._reconstruct_setup_file()
        exit(0)
    # convert_lists_to_excel("C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/XYZ_Positions/")
    # convert_lists_to_code("C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/XYZ_Positions/")
    print("Done")