import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class SPIRAL_MOUNTAIN_DATA_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    ####################################
    ### SPIRAL MOUNTAIN MOVE CAMERAS ###
    ####################################
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/SM/code_2990.c#L40

    def _get_move_camera_dict(self):
        move_camera_dict = {}
        # starting_index = 0x4F4
        starting_index = 0x4FA
        ending_index = 0x51D
        # ending_index = 0x524
        for count, curr_index in enumerate(range(starting_index, ending_index, 0x6)):
            move_camera_dict[count] = {
                "Learn_Text": self._read_byte_list_to_int(curr_index, 2),
                "Refresher_Text": self._read_byte_list_to_int(curr_index + 0x2, 2),
                "Camera": self._read_byte(curr_index + 0x4),
                "Ability": self._read_byte(curr_index + 0x5),
            }
        return move_camera_dict

    def _set_move_camera_dict(self, move_camera_dict):
        # starting_index = 0x4F4
        starting_index = 0x4FA
        ending_index = 0x51D
        # ending_index = 0x524
        for count, curr_index in enumerate(range(starting_index, ending_index, 0x6)):
            self._write_bytes(curr_index, 2, move_camera_dict[count]["Learn_Text"])
            self._write_bytes(curr_index + 0x2, 2, move_camera_dict[count]["Refresher_Text"])
            self._write_byte(curr_index + 0x4, move_camera_dict[count]["Camera"])
            self._write_byte(curr_index + 0x5, move_camera_dict[count]["Ability"])