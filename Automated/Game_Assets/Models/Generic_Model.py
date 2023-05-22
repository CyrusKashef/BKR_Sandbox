import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class GENERIC_MODEL_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._color_format_dict = {
            "RGBA5551": {
                "Max_Value": 31,
                "Shift_Values": (11, 6, 1),
                "Distribution": (31, 31, 31, 1),
            },
            "RGBA8888": {
                "Max_Value": 255,
                "Shift_Values": (24, 16, 8),
                "Distribution": (255, 255, 255, 255),
            },
            "IA8": {
                "Max_Value": 1,
                "Shift_Values": (0, 0, 0),
                "Distribution": (255, 255, 255, 31),
            }
        }
        self._current_section = None
        self._texture_dict = {}
        self._texture_specific_dict = {}
        self._vertex_dict = {}
        self._vertex_count_dict = {}
        # FC_DO_NOT_ADJUST_LIST are things that are shiny
        # that have FC commands that shouldn't adjusted
        # when adjusting their color
        self._FC_DO_NOT_ADJUST_LIST = [
            "7990-Decompressed", # Jiggy
            "79A0-Decompressed", # Empty Honeycomb
            "79B0-Decompressed", # Honeycomb (Health)
            "7CD0-Decompressed", # Blubber's Gold
            "81D0-Decompressed", # Jiggy Transition Picture
            ]
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        self._get_display_list_header_info()
        self._get_animation_header_info()
        self._get_collision_header_info()
        self._get_effect_header_info()
        self._get_geometry_layout_header_info()
        self._get_unknown1_header_info()
        self._get_unknown2_header_info()
    
    # Shift Sections

    def _adjust_offsets(self, starting_index, index_diff):
        if(self._texture_setup_offset >= starting_index):
            self._adjust_texture_setup_offset(index_diff)
        if(self._vertex_setup_offset >= starting_index):
            self._adjust_vertex_setup_offset(index_diff)
        if(self._display_list_setup_offset >= starting_index):
            self._adjust_display_list_setup_offset(index_diff)
        if(self._animation_setup_offset >= starting_index):
            self._adjust_animation_setup_offset(index_diff)
        if(self._collision_setup_offset >= starting_index):
            self._adjust_collision_setup_offset(index_diff)
        if(self._effect_setup_offset >= starting_index):
            self._adjust_effect_setup_offset(index_diff)
        if(self._geometry_layout_setup_offset >= starting_index):
            self._adjust_geometry_layout_setup_offset(index_diff)
        if(self._unknown1_setup_offset >= starting_index):
            self._adjust_unknown1_setup_offset(index_diff)
        if(self._unknown2_setup_offset >= starting_index):
            self._adjust_unknown2_setup_offset(index_diff)

    def _change_model_file_size(self, starting_index, index_diff):
        original_mmap_size = len(self._mmap)
        if(index_diff > 0):
            self._mmap.resize(original_mmap_size + index_diff)
            for curr_index in range(original_mmap_size - 1, starting_index - 1, -1):
                self._mmap[curr_index + index_diff] = self._mmap[curr_index]
            for curr_index in range(starting_index, starting_index + index_diff):
                self._mmap[curr_index] = 0
        if(index_diff < 0):
            for curr_index in range(starting_index, original_mmap_size):
                self._mmap[curr_index + index_diff] = self._mmap[curr_index]
            self._mmap.resize(original_mmap_size + index_diff)
        self._adjust_offsets(starting_index, index_diff)
    
    # COLORS

    def _calculate_luminosity(self, red, green, blue):
        luminosity = 0.2126 * red + 0.7152 * green + 0.0722 * blue
        return luminosity

    def _scale_colors_by_luminosity(self, red_ratio, green_ratio, blue_ratio, luminosity_scaling):
        new_red = round(red_ratio * luminosity_scaling)
        new_green = round(green_ratio * luminosity_scaling)
        new_blue = round(blue_ratio * luminosity_scaling)
        return new_red, new_green, new_blue

    def _calculate_colors_by_luminosity(self, old_red, old_green, old_blue, red_ratio, green_ratio, blue_ratio):
        old_luminosity = self._calculate_luminosity(old_red, old_green, old_blue)
        new_luminosity = self._calculate_luminosity(red_ratio, green_ratio, blue_ratio)
        luminosity_scaling = old_luminosity / new_luminosity
        new_red, new_green, new_blue = self._scale_colors_by_luminosity(red_ratio, green_ratio, blue_ratio, luminosity_scaling)
        return new_red, new_green, new_blue

    def _get_rgb_values(self, color_val, color_format):
        red_val = (color_val >> self._color_format_dict[color_format]["Shift_Values"][0]) & self._color_format_dict[color_format]["Distribution"][0]
        green_val = (color_val >> self._color_format_dict[color_format]["Shift_Values"][1]) & self._color_format_dict[color_format]["Distribution"][1]
        blue_val = (color_val >> self._color_format_dict[color_format]["Shift_Values"][2]) & self._color_format_dict[color_format]["Distribution"][2]
        alpha_val = color_val & self._color_format_dict[color_format]["Distribution"][3]
        return red_val, green_val, blue_val, alpha_val

    def _distribute_colors(self, color_format,
                            old_red_val, old_green_val, old_blue_val,
                            red_ratio, green_ratio, blue_ratio,
                            target_luminosity="Default"):
        if(target_luminosity == "Default"):
            new_red_val, new_green_val, new_blue_val = self._calculate_colors_by_luminosity(old_red_val, old_green_val, old_blue_val, red_ratio, green_ratio, blue_ratio)
        else:
            ten_percent = round(self._color_format_dict[color_format]["Max_Value"] * 0.05)
            old_red_val = max(old_red_val, ten_percent)
            old_green_val = max(old_green_val, ten_percent)
            old_blue_val = max(old_blue_val, ten_percent)
            old_luminosity = self._calculate_luminosity(old_red_val, old_green_val, old_blue_val)
            new_luminosity = self._calculate_luminosity(red_ratio, green_ratio, blue_ratio)
            luminosity_scaling = old_luminosity / new_luminosity * target_luminosity
            new_red_val, new_green_val, new_blue_val = self._scale_colors_by_luminosity(red_ratio, green_ratio, blue_ratio, luminosity_scaling)
        largest_val = max(new_red_val, new_green_val, new_blue_val, self._color_format_dict[color_format]["Max_Value"])
        if(largest_val > self._color_format_dict[color_format]["Max_Value"]):
            scale_down = largest_val / self._color_format_dict[color_format]["Max_Value"]
            new_red_val = round(new_red_val / scale_down)
            new_green_val = round(new_green_val / scale_down)
            new_blue_val = round(new_blue_val / scale_down)
        return new_red_val, new_green_val, new_blue_val
    
    def _construct_color(self, red_val, green_val, blue_val, alpha_val, color_format):
        return ((red_val << self._color_format_dict[color_format]["Shift_Values"][0]) +
                (green_val << self._color_format_dict[color_format]["Shift_Values"][1]) +
                (blue_val << self._color_format_dict[color_format]["Shift_Values"][2]) +
                alpha_val)

    def _color_shift(self, old_color, color_format, red_ratio, green_ratio, blue_ratio, brightness="Default"):
        old_red_val, old_green_val, old_blue_val, old_alpha_val = self._get_rgb_values(old_color, color_format)
        if((self._current_section == "Texture") and (self._ignore_gray) and (old_red_val == old_green_val == old_blue_val)):
            return old_color
        new_red_val, new_green_val, new_blue_val = self._distribute_colors(color_format, old_red_val, old_green_val, old_blue_val,
                                                                            red_ratio, green_ratio, blue_ratio, brightness)
        new_color = self._construct_color(new_red_val, new_green_val, new_blue_val, old_alpha_val, color_format)
        return new_color

    ################
    ### TEXTURES ###
    ################

    def _get_object_texture_header_info(self):
        self._texture_setup_offset = self._read_byte_list_to_int(0x8, 2)
        self._texture_count = self._read_byte_list_to_int(self._texture_setup_offset + 0x4, 2)
    
    def _adjust_texture_setup_offset(self, offset_diff):
        self._texture_setup_offset += offset_diff
        self._write_bytes(0x8, 4, self._texture_setup_offset)
    
    def _get_object_texture_info(self, count):
        texture_info_index_start = self._texture_setup_offset + 0x8 + count * 0x10
        # Segment Address From Texture Data Start
        texture_offset = self._read_byte_list_to_int(texture_info_index_start, 4)
        texture_type = self._read_byte_list_to_int(texture_info_index_start + 0x4, 2)
        x_dimension = self._read_byte(texture_info_index_start + 0x8)
        y_dimension = self._read_byte(texture_info_index_start + 0x9)
        return texture_offset, texture_type, x_dimension, y_dimension
    
    def _get_sprite_texture_header_info(self):
        self._texture_count = self._read_byte_list_to_int(0x0, 2)
        self._texture_type = self._read_byte_list_to_int(0x2, 2)
        self._texture_setup_offset = 0x10
    
    def _get_ci_sprite_texture_info(self, count, ci_type):
        if(ci_type == 4):
            color_index_byte_count = 0x20
        elif(ci_type == 8):
            color_index_byte_count = 0x200
        texture_info_offset = self._read_byte_list_to_int(self._texture_setup_offset + count * 4, 4) + 0x10 + self._texture_count * 4
        # print(f"Texture Info Offset: {self._int_to_hex_str(texture_info_offset)}")
        texture_color_index_bank_index_start = texture_info_offset + 0x18
        # print(f"Texture Color Index Bank Offset: {self._int_to_hex_str(texture_color_index_bank_index_start)}")
        texture_info_index_start = texture_color_index_bank_index_start + color_index_byte_count + 0x8
        # print(f"Texture Info Index Start: {self._int_to_hex_str(texture_info_index_start)}")
        x_dimension = self._read_byte_list_to_int(texture_color_index_bank_index_start + color_index_byte_count + 0x4, 2)
        # print(f"X Dimension: {self._read_byte_list_to_int(texture_color_index_bank_index_start + color_index_byte_count + 0x4, 2)} {self._int_to_hex_str(x_dimension)}")
        y_dimension = self._read_byte_list_to_int(texture_color_index_bank_index_start + color_index_byte_count + 0x6, 2)
        # print(f"Y Dimension: {self._read_byte_list_to_int(texture_color_index_bank_index_start + color_index_byte_count + 0x6, 2)} {self._int_to_hex_str(y_dimension)}")
        return texture_color_index_bank_index_start, texture_info_index_start, x_dimension, y_dimension
    
    def _get_rgba_sprite_texture_info(self, count):
        texture_info_index_start = self._read_byte_list_to_int(self._texture_setup_offset + count * 4, 4) + 0x10 + self._texture_count * 4
        # print(f"Texture Info Offset: {self._int_to_hex_str(texture_info_index_start)}")
        x_dimension = self._read_byte_list_to_int(texture_info_index_start + 0x18, 2)
        y_dimension = self._read_byte_list_to_int(texture_info_index_start + 0x1A, 2)
        texture_index_start = texture_info_index_start + 0x1E
        return texture_index_start, x_dimension, y_dimension
    
    def _unknown_sprite_texture_info(self):
        self._texture_type = self._read_byte(0)
        self._texture_count = self._read_byte_list_to_int(0x2, 2)
        x_dimension = self._read_byte_list_to_int(0xC, 2)
        y_dimension = self._read_byte_list_to_int(0xE, 2)
        texture_index_start = 0x10
        return texture_index_start, x_dimension, y_dimension

    ################
    ### VERTICES ###
    ################

    def _get_object_vertex_header_info(self):
        self._vertex_setup_offset = self._read_byte_list_to_int(0x10, 4)
        self._negative_coords_x = self._read_byte_list_to_int(self._vertex_setup_offset, 2)
        # print(f"Negative X: {self._int_to_hex_str(self._negative_coords_x, 4)}")
        self._negative_coords_y = self._read_byte_list_to_int(self._vertex_setup_offset + 0x2, 2)
        # print(f"Negative Y: {self._int_to_hex_str(self._negative_coords_y, 4)}")
        self._negative_coords_z = self._read_byte_list_to_int(self._vertex_setup_offset + 0x4, 2)
        # print(f"Negative Z: {self._int_to_hex_str(self._negative_coords_z, 4)}")
        self._positive_coords_x = self._read_byte_list_to_int(self._vertex_setup_offset + 0x6, 2)
        # print(f"Positive X: {self._int_to_hex_str(self._positive_coords_x, 4)}")
        self._positive_coords_y = self._read_byte_list_to_int(self._vertex_setup_offset + 0x8, 2)
        # print(f"Positive Y: {self._int_to_hex_str(self._positive_coords_y, 4)}")
        self._positive_coords_z = self._read_byte_list_to_int(self._vertex_setup_offset + 0xA, 2)
        # print(f"Positive Z: {self._int_to_hex_str(self._positive_coords_z, 4)}")
        self._min_obj_coord_range = self._read_byte_list_to_int(self._vertex_setup_offset + 0xC, 2)
        # print(f"Min Coord: {self._int_to_hex_str(self._min_obj_coord_range, 4)}")
        self._max_obj_coord_range = self._read_byte_list_to_int(self._vertex_setup_offset + 0xE, 2)
        # print(f"Max Coord: {self._int_to_hex_str(self._max_obj_coord_range, 4)}")
        self._vertex_count = self._read_byte_list_to_int(self._vertex_setup_offset + 0x14, 2)
    
    def _adjust_vertex_setup_offset(self, offset_diff):
        self._vertex_setup_offset += offset_diff
        self._write_bytes(0x10, 4, self._vertex_setup_offset)
    
    def _get_vertex_info(self, count):
        vertex_info_index_start = self._vertex_setup_offset + 0x18 + count * 0x10
        x_position = self._read_byte_list_to_int(vertex_info_index_start, 2)
        y_position = self._read_byte_list_to_int(vertex_info_index_start + 0x2, 2)
        z_position = self._read_byte_list_to_int(vertex_info_index_start + 0x4, 2)
        u_mapping = self._read_byte_list_to_int(vertex_info_index_start + 0x8, 2)
        v_mapping = self._read_byte_list_to_int(vertex_info_index_start + 0xA, 2)
        red_val = self._read_byte(vertex_info_index_start + 0xC)
        green_val = self._read_byte(vertex_info_index_start + 0xD)
        blue_val = self._read_byte(vertex_info_index_start + 0xE)
        alpha_val = self._read_byte(vertex_info_index_start + 0xF)
        return vertex_info_index_start, x_position, y_position, z_position, u_mapping, v_mapping, red_val, green_val, blue_val, alpha_val
    
    def _set_vertex_xyz_coords(self, count, new_x, new_y, new_z):
        vertex_info_index_start = self._vertex_setup_offset + 0x18 + count * 0x10
        self._write_bytes(vertex_info_index_start, 2, new_x)
        self._write_bytes(vertex_info_index_start + 0x2, 2, new_y)
        self._write_bytes(vertex_info_index_start + 0x4, 2, new_z)

    def _set_vertex_rgba(self, count, new_red, new_green, new_blue, new_alpha):
        vertex_info_index_start = self._vertex_setup_offset + 0x18 + count * 0x10
        self._write_byte(vertex_info_index_start + 0xC, new_red)
        self._write_byte(vertex_info_index_start + 0xD, new_green)
        self._write_byte(vertex_info_index_start + 0xE, new_blue)
        self._write_byte(vertex_info_index_start + 0xF, new_alpha)
    
    #############################
    ### DISPLAY LIST COMMANDS ###
    #############################

    def _get_display_list_header_info(self):
        self._display_list_setup_offset = self._read_byte_list_to_int(0xC, 4)
        self._display_list_command_count = self._read_byte_list_to_int(self._display_list_setup_offset, 4)
    
    def _adjust_display_list_setup_offset(self, offset_diff):
        self._display_list_setup_offset += offset_diff
        self._write_bytes(0xC, 4, self._display_list_setup_offset)

    def _adjust_display_list_command_count(self, count_diff):
        self._display_list_command_count += count_diff
        self._write_bytes(self._display_list_setup_offset, 4, self._display_list_command_count)
    
    def _get_display_list_command_info(self, count):
        display_list_command_index_start = self._display_list_setup_offset + 0x8 + count * 0x8
        display_list_command = self._read_byte(display_list_command_index_start)
        display_list_command_parameters = self._read_byte_list_to_int(display_list_command_index_start + 1, 7)
        # Something goes here to actually read what the command does
        # Maybe put it into a dictionary or something, idk
        return display_list_command, display_list_command_parameters
    
    def _find_display_list_command_count(self, dlist_command_line, start_count=0):
        if(start_count > self._display_list_command_count):
            return -1
        for count in range(start_count, self._display_list_command_count):
            display_list_command_index_start = self._display_list_setup_offset + 0x8 + count * 0x8
            curr_dlist_command_line = self._read_byte_list_to_int(display_list_command_index_start, 8)
            if(curr_dlist_command_line == dlist_command_line):
                return count
        # raise Exception(f"Could Not Find DList Command: {hex(dlist_command_line)}")
        return -1
    
    def _insert_display_list_command(self, count, dlist_command):
        display_list_command_index_start = self._display_list_setup_offset + 0x8 + count * 0x8
        self._change_model_file_size(display_list_command_index_start, 8)
        self._write_bytes(display_list_command_index_start, 8, dlist_command)
        self._adjust_display_list_command_count(1)
    
    def _modify_display_list_command(self, count, new_command):
        display_list_command_index_start = self._display_list_setup_offset + 0x8 + count * 0x8
        self._write_bytes(display_list_command_index_start, 8, new_command)
    
    def _pop_display_list_command(self, count):
        display_list_command_index_start = self._display_list_setup_offset + 0x8 + count * 0x8
        self._change_model_file_size(display_list_command_index_start, -8)
        self._adjust_display_list_command_count -= 1

    ##################
    ### ANIMATIONS ###
    ##################

    def _get_animation_header_info(self):
        self._animation_setup_offset = self._read_byte_list_to_int(0x18, 4)
    
    def _adjust_animation_setup_offset(self, offset_diff):
        self._animation_setup_offset += offset_diff
        self._write_bytes(0x18, 4, self._animation_setup_offset)

    ##################
    ### COLLISIONS ###
    ##################

    def _get_collision_header_info(self):
        self._collision_setup_offset = self._read_byte_list_to_int(0x1C, 4)
    
    def _adjust_collision_setup_offset(self, offset_diff):
        self._collision_setup_offset += offset_diff
        self._write_bytes(0x1C, 4, self._collision_setup_offset)

    ###############
    ### EFFECTS ###
    ###############

    def _get_effect_header_info(self):
        self._effect_setup_offset = self._read_byte_list_to_int(0x24, 4)
    
    def _adjust_effect_setup_offset(self, offset_diff):
        self._effect_setup_offset += offset_diff
        self._write_bytes(0x24, 4, self._effect_setup_offset)

    #######################
    ### GEOMETRY LAYOUT ###
    #######################

    def _get_geometry_layout_header_info(self):
        self._geometry_layout_setup_offset = self._read_byte_list_to_int(0x04, 4)
    
    def _adjust_geometry_layout_setup_offset(self, offset_diff):
        self._geometry_layout_setup_offset += offset_diff
        self._write_bytes(0x04, 4, self._geometry_layout_setup_offset)

    ########################
    ### UNKNOWN SECTIONS ###
    ########################

    def _get_unknown1_header_info(self):
        self._unknown1_setup_offset = self._read_byte_list_to_int(0x20, 4)
    
    def _adjust_unknown1_setup_offset(self, offset_diff):
        self._unknown1_setup_offset += offset_diff
        self._write_bytes(0x20, 4, self._unknown1_setup_offset)

    def _get_unknown2_header_info(self):
        self._unknown2_setup_offset = self._read_byte_list_to_int(0x2C, 4)
    
    def _adjust_unknown2_setup_offset(self, offset_diff):
        self._unknown2_setup_offset += offset_diff
        self._write_bytes(0x2C, 4, self._unknown2_setup_offset)

    #################################
    ### FULL MODEL COLOR SHIFTING ###
    #################################
    
    def _single_object_texture_color_shift(self, count, red_ratio, green_ratio, blue_ratio, brightness="Default"):
        texture_offset, texture_type, x_dimension, y_dimension = self._get_object_texture_info(count)
        texture_index_start = self._texture_setup_offset + texture_offset + 0x8 + self._texture_count * 0x10
        if(texture_type == 0x1):
            # print("Color Index 4")
            for color_offset in range(0x10):
                color_start_index = texture_index_start + color_offset * 0x2
                old_color_val = self._read_byte_list_to_int(color_start_index, 2)
                new_color_val = self._color_shift(old_color_val, "RGBA5551", red_ratio, green_ratio, blue_ratio, brightness)
                self._write_bytes(color_start_index, 2, new_color_val)
        elif(texture_type == 0x2):
            # print("Color Index 8")
            for color_offset in range(0x100):
                color_start_index = texture_index_start + color_offset * 0x2
                old_color_val = self._read_byte_list_to_int(color_start_index, 2)
                new_color_val = self._color_shift(old_color_val, "RGBA5551", red_ratio, green_ratio, blue_ratio, brightness)
                self._write_bytes(color_start_index, 2, new_color_val)
        elif(texture_type == 0x4):
            # print("RGB 5551")
            for color_offset in range(0, x_dimension * y_dimension):
                color_start_index = texture_index_start + color_offset * 0x2
                old_color_val = self._read_byte_list_to_int(color_start_index, 2)
                new_color_val = self._color_shift(old_color_val, "RGBA5551", red_ratio, green_ratio, blue_ratio, brightness)
                self._write_bytes(color_start_index, 2, new_color_val)
        elif(texture_type == 0x8):
            # print("RGBA 8888")
            for color_offset in range(0, x_dimension * y_dimension):
                color_start_index = texture_index_start + color_offset * 0x4
                old_color_val = self._read_byte_list_to_int(color_start_index, 4)
                new_color_val = self._color_shift(old_color_val, "RGBA8888", red_ratio, green_ratio, blue_ratio, brightness)
                self._write_bytes(color_start_index, 4, new_color_val)
        elif(texture_type == 0x10):
            # print("IA8 Are Not Colors, Therefore No Shift")
            pass
        else:
            print(f"Not Currently Covered: {texture_type}")
            raise KeyError(f"Not Currently Covered: {texture_type}")
    
    def _single_sprite_texture_color_shift(self, count, red_ratio, green_ratio, blue_ratio, brightness="Default"):
        if(self._texture_type == 0x1):
            # print("Color Index 4")
            texture_color_index_bank_index_start, texture_offset, x_dimension, y_dimension = self._get_ci_sprite_texture_info(count, 4)
            for color_offset in range(0x10):
                color_start_index = texture_color_index_bank_index_start + color_offset * 0x2
                old_color_val = self._read_byte_list_to_int(color_start_index, 2)
                new_color_val = self._color_shift(old_color_val, "RGBA5551", red_ratio, green_ratio, blue_ratio, brightness)
                self._write_bytes(color_start_index, 2, new_color_val)
        elif(self._texture_type == 0x4):
            # print("Color Index 8")
            texture_color_index_bank_index_start, texture_offset, x_dimension, y_dimension = self._get_ci_sprite_texture_info(count, 8)
            for color_offset in range(0x100):
                color_start_index = texture_color_index_bank_index_start + color_offset * 0x2
                old_color_val = self._read_byte_list_to_int(color_start_index, 2)
                new_color_val = self._color_shift(old_color_val, "RGBA5551", red_ratio, green_ratio, blue_ratio, brightness)
                self._write_bytes(color_start_index, 2, new_color_val)
        elif(self._texture_type == 0x20):
            # print("I think this is IA8 (ex 0xA3B0)")
            # print("IA8 Are Not Colors, Therefore No Shift")
            pass
        elif(self._texture_type == 0x40):
            # print("RGBA 5551")
            texture_index_start, x_dimension, y_dimension = self._get_rgba_sprite_texture_info(count)
            for color_offset in range(0, x_dimension * y_dimension // 2):
                color_start_index = texture_index_start + color_offset * 0x2
                old_color_val = self._read_byte_list_to_int(color_start_index, 2)
                new_color_val = self._color_shift(old_color_val, "RGBA5551", red_ratio, green_ratio, blue_ratio, brightness)
                self._write_bytes(color_start_index, 2, new_color_val)
        elif(self._texture_type == 0x100):
            # print("Alpha Masking, Skip For Now (ex 0x95F0)")
            pass
        elif(self._texture_type == 0x400):
            # print("RGBA 5551")
            texture_index_start, x_dimension, y_dimension = self._get_rgba_sprite_texture_info(count)
            for color_offset in range(0, x_dimension * y_dimension):
                color_start_index = texture_index_start + color_offset * 0x2
                old_color_val = self._read_byte_list_to_int(color_start_index, 2)
                new_color_val = self._color_shift(old_color_val, "RGBA5551", red_ratio, green_ratio, blue_ratio, brightness)
                self._write_bytes(color_start_index, 2, new_color_val)
        elif(self._texture_type == 0x800):
            # print("I think this is IA8")
            # print("IA8 Are Not Colors, Therefore No Shift")
            pass
        else:
            print(f"Not Currently Covered: {self._texture_type}")
            raise KeyError(f"Not Currently Covered: {self._texture_type}")
    
    def _single_unknown_texture_color_shift(self, red_ratio, green_ratio, blue_ratio, brightness="Default"):
        texture_index_start, x_dimension, y_dimension = self._unknown_sprite_texture_info()
        if(self._texture_type == 0x4):
            # print("RGBA 5551")
            for color_offset in range(0, x_dimension * y_dimension):
                color_start_index = texture_index_start + color_offset * 0x2
                old_color_val = self._read_byte_list_to_int(color_start_index, 2)
                new_color_val = self._color_shift(old_color_val, "RGBA5551", red_ratio, green_ratio, blue_ratio, brightness)
                self._write_bytes(color_start_index, 2, new_color_val)
        else:
            print(f"Not Currently Covered: {self._texture_type}")
            raise KeyError(f"Not Currently Covered: {self._texture_type}")

    def _single_vertex_color_shift(self, count, red_ratio, green_ratio, blue_ratio, brightness="Default"):
        vertex_info_index_start, x_position, y_position, z_position, u_mapping, v_mapping, old_red_val, old_green_val, old_blue_val, alpha_val = self._get_vertex_info(count)
        new_red_val, new_green_val, new_blue_val = self._distribute_colors("RGBA8888", old_red_val, old_green_val, old_blue_val, red_ratio, green_ratio, blue_ratio, brightness)
        self._set_vertex_rgba(count, new_red_val, new_green_val, new_blue_val, alpha_val)

    def _full_model_color_shift(self, red_ratio, green_ratio, blue_ratio, brightness="Default"):
        if(self._read_byte_list_to_int(0, 4) == 0x0000000B):
            self._get_object_texture_header_info()
            # print(f"Texture Count: {self._texture_count}")
            for count in range(self._texture_count):
                self._single_object_texture_color_shift(count, red_ratio, green_ratio, blue_ratio, brightness)
            self._get_object_vertex_header_info()
            # print(f"Vertex Count: {self._vertex_count}")
            # print(f"Vertex_Info_Start: {self._vertex_setup_offset}")
            for count in range(self._vertex_count):
                self._single_vertex_color_shift(count, red_ratio, green_ratio, blue_ratio, brightness)
            self._get_display_list_header_info()
            for count in range(self._display_list_command_count):
                display_list_command, display_list_command_parameters = self._get_display_list_command_info(count)
                if((display_list_command == 0xFC) and (self._file_name not in self._FC_DO_NOT_ADJUST_LIST)):
                    self._modify_display_list_command(count, 0xFC1298043F15FFFF)
        elif(self._read_byte_list_to_int(0, 2) == 0x0400):
            # print(f"Unknown Formatted Sprite")
            self._single_unknown_texture_color_shift(red_ratio, green_ratio, blue_ratio, brightness)
        else:
            self._get_sprite_texture_header_info()
            # print(f"Texture Count: {self._texture_count}")
            for count in range(self._texture_count):
                self._single_sprite_texture_color_shift(count, red_ratio, green_ratio, blue_ratio, brightness)
    
    #################################
    ### JSON BASED COLOR SHIFTING ###
    #################################

    def _read_ratios(self, color_ratio, body_part=None):
        red_ratio = int(color_ratio[:2], 16)
        green_ratio = int(color_ratio[2:4], 16)
        blue_ratio = int(color_ratio[4:], 16)
        ratio_total = red_ratio + green_ratio + blue_ratio
        brightness = "Default"
        if(body_part and ("Brightness" in self._json_data[body_part])):
            brightness = self._json_data[body_part]["Brightness"]
            # print(f"Brightness: {brightness}")
        return red_ratio, green_ratio, blue_ratio, brightness
    
    def _color_index_texture_color_shift(self, count, red_ratio, green_ratio, blue_ratio, color_index, brightness="Default"):
        texture_offset, texture_type, x_dimension, y_dimension = self._get_object_texture_info(count)
        texture_index_start = self._texture_setup_offset + texture_offset + 0x8 + self._texture_count * 0x10
        for color_offset in color_index:
            color_start_index = texture_index_start + color_offset * 0x2
            print(f"\tColor Index Start: {hex(color_start_index)}")
            old_color_val = self._read_byte_list_to_int(color_start_index, 2)
            print(f"\t\tOld Color Val: {hex(old_color_val)}")
            print(f"\t\tBrightness: {brightness}")
            new_color_val = self._color_shift(old_color_val, "RGBA5551", red_ratio, green_ratio, blue_ratio, brightness)
            print(f"\t\tNew Color Val: {hex(new_color_val)}")
            self._write_bytes(color_start_index, 2, new_color_val)

    def _conditional_vertex_color_shift(self, count):
        vertex_info_index_start, x_position, y_position, z_position, u_mapping, v_mapping, old_red_val, old_green_val, old_blue_val, alpha_val = self._get_vertex_info(count)
        body_part = "Skip"
        if(count in self._vertex_count_dict):
            body_part = self._vertex_count_dict[count]
        elif((old_red_val, old_green_val, old_blue_val, alpha_val) in self._vertex_dict):
            body_part = self._vertex_dict[(old_red_val, old_green_val, old_blue_val, alpha_val)]
        if(body_part != "Skip"):
            color_ratio = self._json_data[body_part]["Color_Ratio"]
            if(color_ratio != "Skip"):
                red_ratio, green_ratio, blue_ratio, brightness = self._read_ratios(color_ratio, body_part=body_part)
                new_red_val, new_green_val, new_blue_val = self._distribute_colors("RGBA8888", old_red_val, old_green_val, old_blue_val, red_ratio, green_ratio, blue_ratio, brightness)
                self._set_vertex_rgba(count, new_red_val, new_green_val, new_blue_val, alpha_val)

    def _color_shift_based_on_json(self, json_file_dir, json_file_name):
        self._read_json(json_file_dir, json_file_name)
        self._current_section = "Texture"
        for texture_count in self._texture_dict:
            body_part = self._texture_dict[texture_count]
            color_ratio = self._json_data[body_part]["Color_Ratio"]
            if(color_ratio != "Skip"):
                red_ratio, green_ratio, blue_ratio, brightness = self._read_ratios(color_ratio, body_part=body_part)
                self._ignore_gray = self._json_data[body_part]["Ignore_Gray"]
                self._single_object_texture_color_shift(texture_count, red_ratio, green_ratio, blue_ratio, brightness)
        for texture_count in self._texture_specific_dict:
            print(f"Texture Count: {texture_count}")
            for body_part in self._texture_specific_dict[texture_count]:
                print(f"\tBody Part: {body_part}")
                color_ratio = self._json_data[body_part]["Color_Ratio"]
                if(color_ratio != "Skip"):
                    print(f"\tColor Ratio: {color_ratio}")
                    red_ratio, green_ratio, blue_ratio, brightness = self._read_ratios(color_ratio, body_part=body_part)
                    self._ignore_gray = self._json_data[body_part]["Ignore_Gray"]
                    color_index = self._texture_specific_dict[texture_count][body_part]
                    self._color_index_texture_color_shift(texture_count, red_ratio, green_ratio, blue_ratio, color_index, brightness)
        self._current_section = "Vertex"
        for count in range(self._vertex_count):
            self._conditional_vertex_color_shift(count)

if __name__ == '__main__':
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    FILE_NAME = "19D530"
    model_obj = GENERIC_MODEL_CLASS(FILE_DIR, FILE_NAME)
    # model_obj._full_model_color_shift(0xA0, 0xA0, 0xA0, brightness="Default")
    model_obj._get_object_vertex_header_info()