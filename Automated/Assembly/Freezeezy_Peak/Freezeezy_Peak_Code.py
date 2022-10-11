import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class FREEZEEZY_PEAK_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        pass