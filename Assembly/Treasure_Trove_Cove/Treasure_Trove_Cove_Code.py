import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class TREASURE_TROVE_COVE_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        # Thank You, Wedarobi! <3
        self._write_bytes(0x31B4, 4, 0x00000000)
    
    def _patch_yum_yum_crash_fix(self):
        # Thank You, Wedarobi! <3
        self._mmap.seek(0xC90)
        self._mmap.write((0x08096C05).to_bytes(4, "big"))