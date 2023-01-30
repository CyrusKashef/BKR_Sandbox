import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

from Data_Files.Mumbo_Sign_Numbers import DIGIT_IMAGES

class MUMBO_SIGN_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
    
    def _conditional_convert_ci4_pixel(self, curr_index, condition):
        curr_value = self._read_byte(curr_index)
        first_8_bits = curr_value // 0x10
        second_8_bits = curr_value % 0x10
        if(first_8_bits not in condition):
            first_8_bits = 0
        if(second_8_bits not in condition):
            second_8_bits = 0
        new_value = first_8_bits * 0x10 + second_8_bits
        self._write_byte(curr_index, new_value)

    def _clear_cost_image(self):
        texture_offset, texture_type, self._x_dimension, self._y_dimension = self._get_object_texture_info(count=0)
        self._image_offset = texture_offset + 0x20 + 0x60
        for y_byte in range(0x2, 0x1D):
            for x_byte in range(0x3, 0xD):
                x_position = x_byte
                y_position = y_byte * self._x_dimension // 2
                self._conditional_convert_ci4_pixel(self._image_offset + x_position + y_position, [0x0, 0x3])

    def _set_ci4_pixel(self, image_list, starting_x_position, starting_y_position):
        for row_count, image_row in enumerate(image_list):
            for byte_count in range(len(image_row) // 2):
                first_8_bits_str = image_row[byte_count*2]
                second_8_bits_str = image_row[byte_count*2+1]
                curr_index = self._image_offset + starting_x_position + byte_count + (starting_y_position + row_count) * self._x_dimension // 2
                curr_byte = self._read_byte(curr_index)
                first_8_bits = curr_byte // 0x10
                second_8_bits = curr_byte % 0x10
                if(first_8_bits_str != "_"):
                    first_8_bits = int(first_8_bits_str, 16)
                if(second_8_bits_str != "_"):
                    second_8_bits = int(second_8_bits_str, 16)
                new_value = first_8_bits * 0x10 + second_8_bits
                self._write_byte(curr_index, new_value)

    def _modify_cost_image(self, new_cost):
        tens = new_cost // 10
        ones = new_cost % 10
        tens_image_list = DIGIT_IMAGES[tens]
        ones_image_list = DIGIT_IMAGES[ones]
        starting_x_position = 0x1
        starting_y_position = 0x2
        ones_starting_x_position = starting_x_position + len(tens_image_list[0]) // 2 + 1
        self._set_ci4_pixel(tens_image_list, starting_x_position, starting_y_position)
        self._set_ci4_pixel(ones_image_list, ones_starting_x_position, starting_y_position)