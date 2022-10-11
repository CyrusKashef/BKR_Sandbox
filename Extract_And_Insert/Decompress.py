###############
### IMPORTS ###
###############

import zlib
from shutil import copy

########################
### DECOMPRESS CLASS ###
########################

class DECOMPRESS_CLASS():
    def __init__(self, file_dir, pointer):
        ### CONSTANTS ###
        self._WBITS = -15
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        self._COMPRESSED_BIN_EXTENSION = "-Compressed.bin"
        self._DECOMPRESSED_BIN_EXTENSION = "-Decompressed.bin"
        self._RAW_BIN_EXTENSION = "-Raw.bin"

        ### VARIABLES ###
        self._file_dir = file_dir
        self._pointer_str = str(hex(pointer))[2:].upper()
        self._compressed_data = None

    def _read_compressed_data(self):
        with open(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._pointer_str}{self._COMPRESSED_BIN_EXTENSION}", "rb") as f:
            self._compressed_data = f.read()
            if(not len(self._compressed_data)):
                return "Empty"
            elif(self._compressed_data[:2] == b'\x11\x72'):
                self._compressed_data = self._compressed_data[2:]
                return "Continue"
            return "Raw"

    def _runzip(self):
        d = zlib.decompressobj(wbits=self._WBITS)
        res = d.decompress(self._compressed_data[4:])
        with open(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._pointer_str}{self._DECOMPRESSED_BIN_EXTENSION}", "wb+") as o:
            o.write(res)
        
    def _raw(self):
        copy(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._pointer_str}{self._COMPRESSED_BIN_EXTENSION}",
             f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._pointer_str}{self._RAW_BIN_EXTENSION}")

    def _decompress_main(self):
        decompress_progress = self._read_compressed_data()
        if(decompress_progress == "Continue"):
            self._runzip()
        elif(decompress_progress == "Raw"):
            self._raw()

if __name__ == '__main__':
    pass