import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class GRUNTILDAS_LAIR_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        pass
    
    def _cauldron_warps(self):
        pass

    def _note_doors_to_honeycomb_doors(self):
        # Default: 0x0C0D1BBB
        self._write_bytes(0x1504, 4, 0x0C0C8527)
    
    def _note_door_to_jiggy_doors(self):
        # Default: 0x0C0D1BBB
        self._write_bytes(0x1504, 4, 0x0C0C848F)