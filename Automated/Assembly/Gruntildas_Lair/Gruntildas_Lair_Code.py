import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class GRUNTILDAS_LAIR_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        '''No known anti-tampering for Gruntilda's Lair'''
        pass

    def _note_doors_to_honeycomb_doors(self):
        '''Replaces Notes with Empty Honeycombs in order to open note doors'''
        # Default: 0x0C0D1BBB
        self._write_bytes(0x1504, 4, 0x0C0C8527)
    
    def _note_door_to_jiggy_doors(self):
        '''Replaces Notes with Jiggies in order to open note doors'''
        # Default: 0x0C0D1BBB
        self._write_bytes(0x1504, 4, 0x0C0C848F)
    
    #################
    ### CAULDRONS ###
    #################
    # Decomp: https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/lair/ch/cauldron.c#L284

    def _set_pink_cauldron_1_map(self, new_map):
        self._write_byte(0x4E1F, new_map)

    def _set_pink_cauldron_2_map(self, new_map):
        self._write_byte(0x4E43, new_map)

    def _set_teal_cauldron_1_map(self, new_map):
        self._write_byte(0x4E67, new_map)

    def _set_teal_cauldron_2_map(self, new_map):
        self._write_byte(0x4E8B, new_map)

    def _set_amber_cauldron_1_map(self, new_map):
        self._write_byte(0x4EAF, new_map)

    def _set_amber_cauldron_2_map(self, new_map):
        self._write_byte(0x4ED3, new_map)

    def _set_gold_cauldron_1_map(self, new_map):
        self._write_byte(0x4EF7, new_map)

    def _set_gold_cauldron_2_map(self, new_map):
        self._write_byte(0x4F1B, new_map)