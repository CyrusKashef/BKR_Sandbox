import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class CLANKERS_CAVERN_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        '''
        Disables the anti-tampering functions for Clanker's Cavern
        Thank You, Wedarobi! <3
        '''
        self._write_bytes(0x1984, 2, 0x1000)