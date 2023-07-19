import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class CLANKERS_CAVERN_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        '''
        Disables the anti-tampering functions for Clanker's Cavern
        Thank You, Wedarobi! <3
        '''
        self._write_bytes(0x1984, 2, 0x1000)
    
    #############
    ### WARPS ###
    #############

    def _reassign_cc_main_to_cc_clanker_blowhole_warp(self, map_id, exit_id):
        '''
        https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/CC/code_1F70.c#L385
        0x2101
        '''
        self._write_byte(0x2E56, 2, map_id)
        self._write_byte(0x2E6E, 2, exit_id)
    
    def _reassign_cc_main_to_cc_clanker_left_tooth_warp(self, map_id, exit_id):
        '''
        Issue: Conflicts with CC Clanker Right Tooth
        https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/CC/code_BF0.c#L142
        0x2207
        '''
        self._write_bytes(0x10D2, 2, map_id)
        self._write_bytes(0x10F6, 2, exit_id)

    def _reassign_cc_main_to_cc_clanker_right_tooth_warp(self, map_id, exit_id):
        '''
        Issue: Conflicts with CC Clanker Left Tooth
        https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/CC/code_BF0.c#L142
        0x2206
        '''
        self._write_bytes(0x10D2, 2, map_id)
        self._write_bytes(0x10EE, 2, exit_id)

    def _reassign_cc_main_to_cc_clanker_left_gill_warp(self, map_id, exit_id):
        '''
        https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/CC/code_1F70.c#L394
        0x2205
        '''
        self._write_bytes(0x2EA2, 2, map_id)
        self._write_bytes(0x2EA6, 2, exit_id)

    def _reassign_cc_main_to_cc_clanker_right_gill_warp(self, map_id, exit_id):
        '''
        https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/CC/code_1F70.c#L398
        0x2204
        '''
        self._write_bytes(0x2ED2, 2, map_id)
        self._write_bytes(0x2ED6, 2, exit_id)

    def _reassign_cc_clanker_left_tooth_to_cc_main_warp(self, map_id, exit_id):
        '''
        0xb01
        '''
        self._write_bytes(0x286E, 2, map_id)
        self._write_bytes(0x2876, 2, exit_id)

    def _reassign_cc_clanker_right_tooth_to_cc_main_warp(self, map_id, exit_id):
        '''
        0xb02
        '''
        self._write_bytes(0x2896, 2, map_id)
        self._write_bytes(0x289E, 2, exit_id)

    def _reassign_cc_clanker_left_gill_to_cc_main_warp(self, map_id, exit_id):
        '''
        0xb03
        '''
        self._write_bytes(0x281E, 2, map_id)
        self._write_bytes(0x2826, 2, exit_id)

    def _reassign_cc_clanker_right_gill_to_cc_main_warp(self, map_id, exit_id):
        '''
        0xb04
        '''
        self._write_bytes(0x2846, 2, map_id)
        self._write_bytes(0x284E, 2, exit_id)