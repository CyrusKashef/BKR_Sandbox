import os
from shutil import rmtree

class CLEAN_UP_CLASS():
    def __init__(self, file_dir):
        ### CONSTANTS ###
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        self._BIN_EXTENSION = ".bin"
        self._COMPRESSED_BIN_EXTENSION = "-Compressed.bin"
        self._DECOMPRESSED_BIN_EXTENSION = "-Decompressed.bin"
        self._Z64_EXTENSION = ".z64"
        self._JSON_EXTENSION = ".json"
        self._TEMPORARY_BIN = "tmp.bin"

        ### VARIABLES ###
        self._file_dir = file_dir

    def _clear_compressed_files(self):
        randomized_rom_dir = f"{self._file_dir}{self._EXTRACTED_FILES_DIR}"
        for filename in os.listdir(randomized_rom_dir):
            if(filename.endswith(self._COMPRESSED_BIN_EXTENSION)):
                os.remove(randomized_rom_dir + filename)

    def _clear_bin_files(self):
        randomized_rom_dir = f"{self._file_dir}{self._EXTRACTED_FILES_DIR}"
        for filename in os.listdir(randomized_rom_dir):
            if(filename.endswith(self._BIN_EXTENSION)):
                try:
                    os.remove(randomized_rom_dir, filename)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (filename, e))
                    pass

    def _clear_extracted_files_folder(self):
        randomized_rom_dir = f"{self._file_dir}{self._EXTRACTED_FILES_DIR}"
        for filename in os.listdir(randomized_rom_dir):
            file_path = os.path.join(randomized_rom_dir, filename)
            try:
                if(os.path.isdir(file_path)):
                    rmtree(file_path)
                else:
                    os.remove(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))