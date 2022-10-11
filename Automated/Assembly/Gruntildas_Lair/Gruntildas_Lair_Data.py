import sys

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class GRUNTILDAS_LAIR_DATA_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
    
    ########################
    ### NOTE DOOR VALUES ###
    ########################

    def _read_note_door_values(self):
        note_door_list = []
        for curr_index in range(0x7CC, 0x7E4, 0x2):
            note_door_list.append(self._read_byte_list_to_int(curr_index, 2))
        return note_door_list
    
    def _modify_note_door_values(self, replacement_list):
        for index_count, curr_index in enumerate(range(0x7CC, 0x7E4, 0x2)):
            if(replacement_list[index_count] != None):
                self._write_bytes(curr_index, 2, replacement_list[index_count])
    
    ###########################
    ### JIGSAW PUZZLE COSTS ###
    ###########################

    def _read_jigsaw_puzzle_costs(self):
        jigsaw_puzzle_list = []
        for curr_index in range(0x1B46, 0x1B71, 0x4):
            jigsaw_puzzle_list.append(self._read_byte(curr_index + 0x2))
        return jigsaw_puzzle_list

    def _modify_jigsaw_puzzle_costs(self, replacement_list):
        for index_count, curr_index in enumerate(range(0x1B46, 0x1B71, 0x4)):
            if(replacement_list[index_count] != None):
                self._write_byte(curr_index + 0x2, replacement_list[index_count])