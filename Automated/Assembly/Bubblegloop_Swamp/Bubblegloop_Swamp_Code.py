import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class BUBBLEGLOOP_SWAMP_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        '''
        Disables the anti-tampering functions for Bubblegloop Swamp
        Thank You, Wedarobi! <3
        '''
        self._write_bytes(0x86C0, 2, 0x1000)
    
    def _one_round_vile(self):
        '''
        Accepting to play Mr Vile's Game will start round 3, and supply a Jiggy if victorious.
        Mr. Vile will offer the bonus game afterwards,
        but beating this and talking to Mr Vile again will crash the game.
        '''
        # local->unkC--; -> local->unkC -= 3;
        self._write_byte(0x384B, 0xFD)
        # local->unkC++; -> local->unkC += 3;
        self._write_byte(0x3F4B, 3)
        # Spits out Jiggy after first round
        self._write_byte(0x4D1B, 9)