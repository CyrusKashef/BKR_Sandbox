import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class GOBIS_VALLEY_DATA_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    #######################
    ### MATCHING PUZZLE ###
    #######################
    # Matching Puzzle
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/GV/code_9DB0.c
    # First Index 0xA80
    # Last Index 0xAF8
    # 0x0: Tile Count (0x190-0x19F)
    # 0x2: Tile Value (0-7)

    def _get_matching_puzzle_dict(self):
        matching_puzzle_dict = {}
        start_index = 0xA80
        end_index = 0xAF8
        for count, curr_index in enumerate(range(start_index, end_index + 1, 8)):
            matching_puzzle_dict[count] = {
                "Tile_Count": self._read_byte_list_to_int(curr_index, 2),
                "Tile_Value": self._read_byte_list_to_int(curr_index + 0x2, 2),
            }
        return matching_puzzle_dict
    
    def _set_matching_puzzle_dict(self, matching_puzzle_dict):
        start_index = 0xA80
        end_index = 0xAF8
        for count, curr_index in enumerate(range(start_index, end_index + 1, 8)):
            self._write_bytes(curr_index, 2, matching_puzzle_dict[count]["Tile_Count"])
            self._write_bytes(curr_index + 0x2, 2, matching_puzzle_dict[count]["Tile_Value"])

    def _set_matching_puzzle_jiggy_spawn_location(self, x_pos, y_pos, z_pos):
        self._write_float_bytes(0xB08, x_pos)
        self._write_float_bytes(0xB0C, y_pos)
        self._write_float_bytes(0xB10, z_pos)