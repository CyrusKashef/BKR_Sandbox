import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class TREASURE_TROVE_COVE_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        # Thank You, Wedarobi! <3
        self._write_bytes(0x31B4, 4, 0x00000000)
    
    def _patch_yum_yum_crash_fix(self):
        # Thank You, Wedarobi! <3
        self._mmap.seek(0xC90)
        self._mmap.write((0x08096C05).to_bytes(4, "big"))
    
    ##############################
    ### SANDCASTLE CHEAT CODES ###
    ##############################
    
    def _unlimited_cheat_codes(self):
        '''
        Decomp: https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/TTC/code_3E30.c
        The game checks how many "illegal" cheats the player has used.
        At zero, it runs the cheat and adds to the counter.
        At one, it runs the cheat and adds to the counter,
          but Gruntilda also warns the player that if they use one more,
          she will erase their save file.
        At two, Bottles asks the player if they want to continue with the cheat,
          and if yes, Gruntilda deletes the save file,
          but the game continues to play as normal.
        Current Solution:
          Always use case 0 and never add to the counter.
        '''
        # Case 0
        self._write_bytes(0x5840, 4, 0x10000007)
        # No Add To Counter
        self._write_byte(0x5867, 0x0)
    
    ########################
    ### SHARKFOOD ISLAND ###
    ########################

    def _raise_sharkfood_island(self):
        '''
        Decomp: https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/TTC/code_26D0.c#L143
        When Sharkfood Island is underwater, it's at y=-1000.0f.
        When Sharkfood Island is raised, it's at y=700.0f.
        Afterwards, the game sets everything else depending on the island's y position.
        Solution: Make it always y=700.0f.
        '''
        self._write_float_bytes(0x2A7A, 700, 2)

    def _reassign_ttc_main_to_ttc_sharkfood_island_warp(self, map_id, exit_id):
        '''
        0x8f01
        '''
        self._write_bytes(0x2B46, 2, map_id)
        self._write_bytes(0x2B66, 2, exit_id)