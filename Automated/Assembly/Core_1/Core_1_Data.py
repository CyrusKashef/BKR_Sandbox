import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class CORE_1_DATA_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)

    def _calculate_checksum(self):
        '''Runs through algorithm to calculate the new checksum (Might not work?)'''
        crc1 = 0
        crc2 = 0xFFFFFFFF
        for val in self._mmap:
            byte = int.from_bytes(val, "big")
            crc1 = crc1 + byte
            crc2 = crc2 ^ (byte << (crc1 & 0x17))
        return crc1, crc2

    def _set_checksum(self, crc):
        '''Sets the checksum located in Core 1's Data'''
        self._write_bytes(0xF64, 4, crc)