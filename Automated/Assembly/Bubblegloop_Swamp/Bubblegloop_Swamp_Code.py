import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class BUBBLEGLOOP_SWAMP_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        '''
        Disables the anti-tampering functions for Bubblegloop Swamp
        Thank You, Wedarobi! <3
        '''
        self._write_bytes(0x86C0, 2, 0x1000)
    
    def _round_three_vile_only(self):
        '''
        Doesn't Work :(
        '''
        # initialize local->unkC
        self._write_byte(0x4A1B, 3)
        # initialize local->unkD
        # We want this less than 4
        self._write_byte(0x4A37, 3)
        # First 'Next State'
        self._write_byte(0x4ABB, 5)