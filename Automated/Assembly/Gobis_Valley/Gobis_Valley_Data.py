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

    def _set_matching_puzzle_tile(self, start_index, tile_val):
        self._write_byte(start_index + 0x4, tile_val)

    def _set_matching_puzzle_jiggy_spawn_location(self, x_pos, y_pos, z_pos):
        self._write_float_bytes(0xB08, x_pos)
        self._write_float_bytes(0xB0C, y_pos)
        self._write_float_bytes(0xB10, z_pos)