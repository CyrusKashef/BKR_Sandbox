import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class MAD_MONSTER_MANSION_DATA_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    ###############
    ### MOTZAND ###
    ###############
    # Motzand
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/MMM/ch/motzhand.c
    # Organ
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/MMM/code_3420.c

    def _set_motzands_first_song(self, keys_list):
        # What Motzand Presses
        for count, index in enumerate(range(0xD4, 0xD9)): # 56C4
            self._write_byte(index, keys_list[count])
        # What The Player Actually Needs To Press For The Solution
        for count, index in enumerate(range(0x7EC, 0x7F1)):
            self._write_byte(index, keys_list[count])
    
    def _set_motzands_first_song(self, keys_list):
        # What Motzand Presses
        for count, index in enumerate(range(0xDC, 0xE6)):
            self._write_byte(index, keys_list[count])
        # What The Player Actually Needs To Press For The Solution
        for count, index in enumerate(range(0x7F4, 0x7FE)):
            self._write_byte(index, keys_list[count])
    
    def _set_motzand_jiggy_spawn_location(self, x_pos, y_pos, z_pos):
        self._write_float_bytes(0x800, x_pos)
        self._write_float_bytes(0x804, y_pos)
        self._write_float_bytes(0x808, z_pos)

    ###############
    ### TUMBLAR ###
    ###############
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/MMM/code_3D50.c#L21
    # First Index 0x810 (Count 0x1)
    # Last Index 0x900 (Count 0x1F)
    # X Is Grunty Tile, Every Other Letter Is For The Puzzle
    # Counts Start At 0x1, End At 0x1F
    # Counts 0x4, 0xC, 0x14, & 0x1C are corners

    def _get_tumblar_tile_value(self, index_start):
        count = self._read_byte(index_start + 0x1)
        letter = self._read_byte(index_start + 0x2)
        return count, letter
    
    def _set_tumblar_tile_value(self, index_start):
        self._write_byte(index_start + 0x1)
        self._write_byte(index_start + 0x2)