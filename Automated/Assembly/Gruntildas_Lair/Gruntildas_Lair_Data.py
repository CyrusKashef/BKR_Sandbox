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
        '''Gets the required count for every note door'''
        note_door_list = []
        for curr_index in range(0x7CC, 0x7E4, 0x2):
            note_door_list.append(self._read_byte_list_to_int(curr_index, 2))
        return note_door_list
    
    def _modify_note_door_values(self, replacement_list):
        '''Modifies the required count for every note door'''
        for index_count, curr_index in enumerate(range(0x7CC, 0x7E4, 0x2)):
            if(replacement_list[index_count] != None):
                self._write_bytes(curr_index, 2, replacement_list[index_count])
    
    ###########################
    ### JIGSAW PUZZLE COSTS ###
    ###########################

    def _read_jigsaw_puzzle_costs(self):
        '''Gets the required count for every world jigsaw puzzle'''
        jigsaw_puzzle_list = []
        for curr_index in range(0x1B48, 0x1B74, 0x4):
            jigsaw_puzzle_list.append(self._read_byte(curr_index))
        return jigsaw_puzzle_list

    def _modify_jigsaw_puzzle_costs(self, replacement_list):
        '''
        Modifies the number of Jiggies required for each world's jigsaw puzzle
        Also adjusts the bit requirement used to save the number of Jiggies if the player leaves the lair
        '''
        total_bit_requirement = 0
        current_bit_offset = 0x5D
        for index_count, curr_index in enumerate(range(0x1B48, 0x1B74, 0x4)):
            if(replacement_list[index_count] != None):
                puzzle_cost = replacement_list[index_count]
                needed_bits = max(puzzle_cost.bit_length(), 1)
                total_bit_requirement += needed_bits
                self._write_byte(curr_index, puzzle_cost)
                self._write_byte(curr_index + 0x1, needed_bits)
                self._write_bytes(curr_index + 0x2, 2, current_bit_offset)
                current_bit_offset += needed_bits
            else:
                needed_bits = self._read_byte(curr_index + 0x1)
                total_bit_requirement += needed_bits
                self._write_bytes(curr_index + 0x2, 2, current_bit_offset)
                current_bit_offset += needed_bits
        if(total_bit_requirement > 37):
            print("Not Enough Bits For Jigsaw Puzzle Requirements")
            raise SystemError("Not Enough Bits For Jigsaw Puzzle Requirements")
    
    ###################
    ### FURNACE FUN ###
    ###################

    ### TILES
    # You read the board bottom left to top right,
    # with the first one being the first bk square,
    # then going to the first eye square,
    # then going to the extra life tile on the bottom left.
    #                             191 (Finish?)
    # ___ ___ ___ ___ ___ ___ ___ 1EF (Skull Tile)    ___ ___ ___ ___
    # 1E3 1E4 1E5 ___ ___ ___ 1E6 1E7 1E8 1E9 1EA 1EB 1EC 1ED 1EE ___
    # 1DF ___ 1E0 ___ ___ ___ 1E1 ___ ___ ___ ___ 1E2 ___ ___ ___ ___
    # ___ ___ 1D9 1DA 1DB 1DC 1DD ___ ___ ___ ___ 1DE ___ ___ ___ ___
    # ___ ___ 1D6 ___ ___ ___ 1D7 ___ ___ ___ ___ 1D8 ___ ___ ___ ___
    # ___ ___ 1CD ___ ___ ___ 1CE 1CF 1D0 1D1 1D2 1D3 1D4 1D5 ___ ___
    # 1C4 1C5 1C6 1C7 1C8 ___ ___ ___ 1C9 ___ ___ ___ ___ 1CA 1CB 1CC
    # 1C0 ___ ___ ___ 1C1 ___ ___ ___ 1C2 ___ ___ ___ ___ 1C3 ___ ___
    # 1B5 ___ ___ ___ 1B6 1B7 1B8 1B9 1BA 1BB 1BC 1BD 1BE 1BF ___ ___
    # 1AF 1B0 1B1 1B2 1B3 ___ ___ ___ ___ ___ ___ 1B4 ___ ___ ___ ___
    # 1AC ___ ___ ___ 1AD ___ ___ ___ ___ ___ ___ 1AE ___ ___ ___ ___
    # 1A1 ___ ___ ___ 1A2 1A3 1A4 1A5 1A6 1A7 1A8 1A9 1AA 1AB ___ ___
    # ___ ___ ___ ___ ___ 19E ___ ___ 19F ___ ___ ___ ___ 1A0 ___ ___
    # ___ ___ ___ ___ ___ 19B ___ ___ 19C ___ ___ ___ ___ 19D ___ ___
    # ___ 193 194 195 196 197 198 199 19A ___ ___ ___ ___ ___ ___ ___
    # ___ ___ ___ ___ ___ ___ ___ 192 ___ ___ ___ ___ ___ ___ ___ ___
    # ___ ___ ___ ___ ___ ___ ___ 0?? (BK TILE)   ___ ___ ___ ___ ___
    #                           ENTRANCE

    def _get_board_dict(self):
        board_dict = {}
        starting_index = 0xAB0
        ending_index = 0x168F
        for count, index in enumerate(range(starting_index, ending_index, 0x20)):
            board_dict[count] = {
                "Tile_Below": self._read_byte_list_to_int(index, 2),
                "Tile_Left": self._read_byte_list_to_int(index + 0x2, 2),
                "Tile_Above": self._read_byte_list_to_int(index + 0x4, 2),
                "Tile_Right": self._read_byte_list_to_int(index + 0x6, 2),
                "Tile_Type": self._read_byte(index + 0x8),
                "Unk6": self._read_byte(index + 0x9),
                "Unk7": self._read_byte(index + 0xA),
                "Unk8": self._read_byte(index + 0xB),
                "Unk9": self._read_byte_list_to_float(index + 0xC, 4),
                "Unk10": self._read_byte(index + 0x10),
                "Unk11": self._read_byte(index + 0x11),
                "Unk12": self._read_byte(index + 0x12),
                "Unk13": self._read_byte(index + 0x13),
                "Unk14": self._read_byte(index + 0x14),
                "Unk15": self._read_byte(index + 0x15),
                "Unk16": self._read_byte(index + 0x16),
                "Unk17": self._read_byte(index + 0x17),
                "Unk18": self._read_byte(index + 0x18),
                "Unk19": self._read_byte(index + 0x19),
                "Unk20": self._read_byte(index + 0x1A),
                "Unk21": self._read_byte(index + 0x1B),
                "Unk22": self._read_byte(index + 0x1C),
                "Unk23": self._read_byte(index + 0x1D),
                "Unk24": self._read_byte(index + 0x1E),
                "Unk25": self._read_byte(index + 0x1F),
            }
        return board_dict
    
    def _set_board_dict(self, board_dict):
        for count in board_dict:
            curr_index = 0xAB0 + count * 0x20
            self._write_bytes(curr_index, 2, board_dict[count]["Tile_Below"])
            self._write_bytes(curr_index + 0x2, 2, board_dict[count]["Tile_Left"])
            self._write_bytes(curr_index + 0x4, 2, board_dict[count]["Tile_Above"])
            self._write_bytes(curr_index + 0x6, 2, board_dict[count]["Tile_Right"])
            self._write_byte(curr_index + 0x8, board_dict[count]["Tile_Type"])
            self._write_byte(curr_index + 0x9, board_dict[count]["Unk6"])
            self._write_byte(curr_index + 0xA, board_dict[count]["Unk7"])
            self._write_byte(curr_index + 0xB, board_dict[count]["Unk8"])
            self._write_float_bytes(curr_index + 0xC, board_dict[count]["Unk9"])
            self._write_byte(curr_index + 0x10, board_dict[count]["Unk10"])
            self._write_byte(curr_index + 0x11, board_dict[count]["Unk11"])
            self._write_byte(curr_index + 0x12, board_dict[count]["Unk12"])
            self._write_byte(curr_index + 0x13, board_dict[count]["Unk13"])
            self._write_byte(curr_index + 0x14, board_dict[count]["Unk14"])
            self._write_byte(curr_index + 0x15, board_dict[count]["Unk15"])
            self._write_byte(curr_index + 0x16, board_dict[count]["Unk16"])
            self._write_byte(curr_index + 0x17, board_dict[count]["Unk17"])
            self._write_byte(curr_index + 0x18, board_dict[count]["Unk18"])
            self._write_byte(curr_index + 0x19, board_dict[count]["Unk19"])
            self._write_byte(curr_index + 0x1A, board_dict[count]["Unk20"])
            self._write_byte(curr_index + 0x1B, board_dict[count]["Unk21"])
            self._write_byte(curr_index + 0x1C, board_dict[count]["Unk22"])
            self._write_byte(curr_index + 0x1D, board_dict[count]["Unk23"])
            self._write_byte(curr_index + 0x1E, board_dict[count]["Unk24"])
            self._write_byte(curr_index + 0x1F, board_dict[count]["Unk25"])

    ### SOUND QUESTIONS

    def _get_sound_question_dict(self):
        sound_question_dict = {}
        starting_index = 0x16A4
        ending_index = 0x1907
        for count, index in enumerate(range(starting_index, ending_index, 0xC)):
            sound_question_dict[count] = {
                "Unk1": self._read_byte(index),
                # 00
                "Sound_Enum": self._read_bytes(index + 0x2, 2),
                "Unk3": self._read_bytes(index + 0x4, 2),
                # 00 00
                "Unk4": self._read_byte_list_to_float(index + 0x8, 4),
            }
        return sound_question_dict
    
    def _set_sound_question_dict(self, sound_question_dict):
        for count in sound_question_dict:
            curr_index = 0x16A4 + count * 0xC
            self._write_byte(curr_index, sound_question_dict[count]["Unk1"])
            # 00
            self._write_bytes(curr_index + 0x2, 2, sound_question_dict[count]["Sound_Enum"])
            self._write_bytes(curr_index + 0x4, 2, sound_question_dict[count]["Unk3"])
            # 00 00
            self._write_float_bytes(curr_index + 0x8, sound_question_dict[count]["Unk4"])
    
    ### MINI GAMES

    def _get_mini_game_dict(self):
        mini_game_dict = {}
        starting_index = 0x1908
        ending_index = 0x191F
        for count, index in enumerate(range(starting_index, ending_index, 0x4)):
            mini_game_dict[count] = {
                "Map": self._read_byte_list_to_int(index, 2),
                "State": self._read_byte_list_to_int(index + 0x2, 2),
            }
    
    def _set_mini_game_dict(self, mini_game_dict):
        for count in mini_game_dict:
            curr_index = 0x1908 + count * 0x4
            self._write_bytes(curr_index, 2, mini_game_dict[count]["Map"])
            self._write_bytes(curr_index, 2, mini_game_dict[count]["State"])
    
    ### PICTURE QUESTIONS

    def _get_picture_question_dict(self):
        picture_question_dict = {}
        starting_index = 0x1920
        ending_index = 0x1AF7
        for count, index in enumerate(range(starting_index, ending_index, 0x4)):
            picture_question_dict[count] = {
                "Map": self._read_byte_list_to_int(index, 2),
                "Camera": self._read_byte_list_to_int(index + 0x2, 2),
            }
    
    def _set_picture_question_dict(self, picture_question_dict):
        for count in picture_question_dict:
            curr_index = 0x1920 + count * 0x4
            self._write_bytes(curr_index, 2, picture_question_dict[count]["Map"])
            self._write_bytes(curr_index, 2, picture_question_dict[count]["Camera"])