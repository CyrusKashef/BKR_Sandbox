import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class SPEECH_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._file_type = self._determine_speech_type()

    def _determine_speech_type(self):
        # Start with 01 03 00 05 00 or 01 01 02 05 00
        if(self._read_byte_list_to_int(0, 5) in [0x0103000500, 0x0101020500]):
            self._file_type = "Furnace Fun"
        # Start with 01 03 00
        elif(self._read_byte_list_to_int(0, 3) == 0x010300):
            self._file_type = "Other"
        else:
            print(f"Unknown Speech File Type Error")
            exit(0)