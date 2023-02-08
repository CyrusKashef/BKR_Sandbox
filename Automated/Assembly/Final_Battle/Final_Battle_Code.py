import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class FINAL_BATTLE_CODE_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    def _disable_anti_tamper(self):
        '''No known anti-tampering for the Final Battle'''
        pass

    def _adjust_final_battle_phases(self,
                                    phase1_hits=None,
                                    phase2_hits=None, phase2_spots=None,
                                    phase3_hits=None,
                                    phase4_num_of_jinjos=None, phase4_egg_per_jinjo=None,
                                    phase5_eggs_per_hole=None):
        # Phase 1 (Complete)
        if(phase1_hits != None):
            self._write_byte(0x2147, phase1_hits) # honeycomb
            self._write_byte(0x2DBF, phase1_hits) # next phase
        # Phase 2 (Complete)
        if(phase2_hits != None):
            self._write_byte(0x5683, phase2_hits)
        if(phase2_spots != None):
            self._write_byte(0x3297, phase2_spots)
        # Phase 3 (Complete)
        if(phase3_hits != None):
            self._write_byte(0x39EB, phase3_hits) # next phase
            self._write_byte(0x576F, phase3_hits) # honeycomb
        # Phase 4
        if(phase4_num_of_jinjos != None):
            self._write_byte(0x42E3, phase4_num_of_jinjos)
        if(phase4_egg_per_jinjo != None):
            self._write_byte(0x709B, phase4_egg_per_jinjo)
        # Phase 5
        if(phase5_eggs_per_hole != None):
            self._write_byte(0x7F9B, phase5_eggs_per_hole)