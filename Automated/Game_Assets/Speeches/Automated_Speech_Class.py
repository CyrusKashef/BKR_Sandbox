import sys

sys.path.append(".")
from Automated.Game_Assets.Speeches.Non_Furnace_Fun_Speech_Class import NON_FURNACE_FUN_SPEECH_CLASS
from Automated.Game_Assets.Speeches.Furnace_Fun_Speech_Class import FURNACE_FUN_SPEECH_CLASS

class AUTOMATED_SPEECH_CLASS():
    def __init__(self, file_dir):
        self._file_dir = file_dir
        # CONSTANTS
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        self._DECOMPRESSED_EXTENSION = "-Decompressed"

    def _replace_non_furnace_fun_speech(self, speech_list):
        for pointer in speech_list:
            speech_obj = NON_FURNACE_FUN_SPEECH_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, f"{pointer}{self._DECOMPRESSED_EXTENSION}")
            for section_num in speech_list[pointer]:
                speech_obj._replace_section(section_num, new_line=speech_list[pointer][section_num])
            speech_obj._recontruct_speech_file()