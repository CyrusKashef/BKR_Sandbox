import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class CORE_1_CODE_CLASS(GENERIC_FILE_CLASS):
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
    
    def _disable_anti_tamper(self):
        '''
        Disables the anti-tampering functions for Core 1 (in case calculating checksum doesn't work)
        Thank You, Wedarobi! <3
        '''
        self._write_bytes(0x10A1C, 4, 0x00000000)
        self._write_bytes(0x10A30, 2, 0x1000)
    
    def _patch_yum_yum_crash_fix(self):
        '''
        Fixes a vanilla bug: 
        When a yumyum in TTC tries to eat a sprite in a cube, the game treats it as an actor, derefs an invalid pointer, and segfaults.
        Thank You, Wedarobi! <3
        '''
        self._mmap.seek(0x1D5EC)
        self._mmap.write((0x03E0000800000000).to_bytes(8, "big"))
        self._mmap.write((0x1100000D000000008D0A0000000A4E0234010080552100083C098000012A4826).to_bytes(32, "big"))
        self._mmap.write((0x3C0100400121482A1120000300000000080E1C2200000000080E1C2800000000).to_bytes(32, "big"))
    
    def _booting_up_map(self, map_id):
        '''
        When loading the game, this is the location the player boots up at
        Typically used to skip the Rareware & N64 logo cutscene and the concert
        '''
        self._write_byte(0x18B, map_id)