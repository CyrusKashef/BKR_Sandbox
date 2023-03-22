import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class MUMBOS_MOUNTAIN_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        # Thank You, Wedarobi! <3
        self._write_bytes(0x1B7C, 2, 0x1000)
        # Just in case, I found this
        # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/MM/ch/conga.c#L183
        # self._write_bytes(0x1050, 4, 0x00000000)
    
    #############
    ### CONGA ###
    #############
    # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/MM/ch/conga.c#L59
    # plyrPos[1] < 300.0f
    # 600.0f < plyrPos[1]
    # 52900.0f < (plyrPos[0]- -5011.0f)*(plyrPos[0]- -5011.0f) + (plyrPos[2]- 5029.0f)*(plyrPos[2]- 5029.0f)
    # 230 ** 2 < (player_x + 5011) ** 2 + (player_z - 5029) ** 2
    # jk fuck this i can't figure numbers out, just gonna make it return true

    def _stonehenge_conga(self):
        # Map
        # self._write_byte(0xAF3, 0x02)
        # Min Y
        self._write_float_bytes(0xB2A, 2605, byte_count=2)
        # Max Y
        self._write_float_bytes(0xB36, 2905, byte_count=2)
        # Return True
        self._write_bytes(0xBAC, 4, 0x24020001)