import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class SPIRAL_MOUNTAIN_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        # Thank You, Wedarobi! <3
        self._write_bytes(0x1D4, 2, 0x1000)
        self._write_bytes(0x1EC, 2, 0x1000)
        self._write_bytes(0x204, 2, 0x1000)
        self._write_bytes(0x3FA4, 4, 0x00000000)

    def _bottles_skip_tutorial_moves(self, move_value_list):
        self._write_byte(0x2ACF, move_value_list[0])
        self._write_byte(0x2AD7, move_value_list[1])
        self._write_byte(0x2ADF, move_value_list[2])
        self._write_byte(0x2AE7, move_value_list[3])
        self._write_bytes(0x2AEC, 3, 0x240400)
        self._write_byte(0x2AEF, move_value_list[4])
        self._write_byte(0x2AF7, move_value_list[5])
        self._write_byte(0x2AFF, move_value_list[6])
        self._write_byte(0x2B07, move_value_list[7])
        self._write_byte(0x2B0F, move_value_list[8])
    
    def _check_moves_as_used(self, move_value_list):
        self._write_byte(0x2A67, 0x3) # Camera Control
        self._write_bytes(0x2A6C, 3, 0x240400)
        self._write_byte(0x2A6F, move_value_list[0])
        self._write_byte(0x2A77, move_value_list[1])
        self._write_byte(0x2A7F, move_value_list[2])
        self._write_byte(0x2A87, move_value_list[3])
        self._write_byte(0x2A8F, move_value_list[4])
        self._write_byte(0x2A97, move_value_list[5])
        self._write_byte(0x2A9F, move_value_list[6])
        self._write_byte(0x2AA7, move_value_list[7])
        self._write_byte(0x2AAF, move_value_list[8])