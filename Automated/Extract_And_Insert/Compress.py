'''
Directly After Compression We Need To Remove:
    Header:
        TLDR: Decompressed file name
        * When compressing a file, the decompressed file's name will appear at the top
        * We can always find it for removal by looking for the ".bin" portion
    Footer:
        TLDR: Last 8 bytes
        * First 4 bytes are the crc32 calculation for the decompressed file in little endian
        * Second 4 bytes are the decompressed file size in little endian
Need To Add These Before Inserting Into ROM:
    Lead:
        TLDR: 1172 + Decompressed File Size
        * Compressed BK files begin with 11 72
        * Next 4 bytes are the decompressed file size in big endian
    Tail:
        TLDR: Trailing 0xAA (sometimes 0x00) used for padding
        * Compressed files are read 8 bytes (quadword) at a time
        * When a compressed file's size isn't divisible by 8, padding is added until it is
'''

###############
### IMPORTS ###
###############

from mmap import mmap
import subprocess
from os.path import exists
from os import unlink
from shutil import copy
import zlib

######################
### COMPRESS CLASS ###
######################

class COMPRESS_CLASS():
    def __init__(self, file_dir, pointer):
        ### CONSTANTS ###
        self._BK_COMPRESSED_FILE_HEADER = b"\x11\x72"
        self._DOT_BIN_BINARY = b'\x2E\x62\x69\x6E\x00'
        self._FOOTER_LEN = 8
        # self._GZIP = "Tools/GZIP/GZIP.EXE"
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        self._COMPRESSED_BIN_EXTENSION = "-Compressed.bin"
        self._DECOMPRESSED_BIN_EXTENSION = "-Decompressed.bin"
        self._RAW_BIN_EXTENSION = "-Raw.bin"
        self._TEMPORARY_BIN = "tmp.bin"
    
        ### VARIABLES ###
        self._file_dir = file_dir
        self._pointer_str = str(hex(pointer))[2:].upper()
    
    def _check_if_decompressed_file_exists(self):
        return exists(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._pointer_str}{self._DECOMPRESSED_BIN_EXTENSION}")
    
    def _check_if_raw_file_exists(self):
        return exists(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._pointer_str}{self._RAW_BIN_EXTENSION}")

    def _compress_file(self, padding=b"\xAA", alignment=8):
        src = f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._pointer_str}{self._DECOMPRESSED_BIN_EXTENSION}"
        dst = f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._pointer_str}{self._COMPRESSED_BIN_EXTENSION}"

        try:
            with open(src, "rb") as f:
                dec    = f.read()
                declen = len(dec)

            ## Deflate
            cmp = zlib.compressobj(wbits=-15).compress(dec)

            ## Align in-game postinflate buffer to 16
            if declen % 0x10:
                declen += 0x10 - (declen % 0x10)

            ## Build final deflated file
            output = self._BK_COMPRESSED_FILE_HEADER + declen.to_bytes(4, "big") + cmp
            ## Align to 8 with standard padding
            if len(output) % alignment:
                output += padding * (alignment - (len(output) % alignment))

            ## Commit output
            with open(dst, "wb") as f:
                f.write(output)

            ## Remove source file, as standard gzip
            if exists(src):
                unlink(src)

        except Exception as e:
            ## Failed somehow, remove output file if exists
            if exists(dst):
                unlink(dst)

    def _copy_raw(self):
        copy(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._pointer_str}{self._RAW_BIN_EXTENSION}",
            f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._pointer_str}{self._COMPRESSED_BIN_EXTENSION}")

    def _compress_main(self, padding=b"\xAA", alignment=8):
        if self._check_if_decompressed_file_exists():
            self._compress_file(padding, alignment)
            return True

        elif self._check_if_raw_file_exists():
            self._copy_raw()
            return True

        return False


if __name__ == '__main__':
    pass