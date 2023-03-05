import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class MATCHING_PUZZLE_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        # https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/GV/matchinggame.c#L14
        # The count starts in the bottom right corner, bottom to top, then right to left, like so
        #  |--------|--------|--------|--------|
        #  |  019F  |  019B  |  0197  |  0193  |
        #  |  0007  |  0001  |  0004  |  0004  |
        #  |--------|--------|--------|--------|
        #  |  019E  |  019A  |  0196  |  0192  |
        #  |  0002  |  0006  |  0000  |  0003  |
        #  |--------|--------|--------|--------|
        #  |  019D  |  0199  |  0195  |  0191  |
        #  |  0005  |  0002  |  0007  |  0005  |
        #  |--------|--------|--------|--------|
        #  |  019C  |  0198  |  0194  |  0190  |
        #  |  0006  |  0000  |  0003  |  0001  |
        #  |--------|--------|--------|--------|
        # Orientation To Make This Easier To Debug
        #  |--------|--------|--------|--------|
        #  |  019C  |  0198  |  0194  |  0190  |
        #  |  0006  |  0000  |  0003  |  0001  |
        #  |--------|--------|--------|--------|
        #  |  019D  |  0199  |  0195  |  0191  |
        #  |  0005  |  0002  |  0007  |  0005  |
        #  |--------|--------|--------|--------|
        #  |  019E  |  019A  |  0196  |  0192  |
        #  |  0002  |  0006  |  0000  |  0003  |
        #  |--------|--------|--------|--------|
        #  |  019F  |  019B  |  0197  |  0193  |
        #  |  0007  |  0001  |  0004  |  0004  |
        #  |--------|--------|--------|--------|
        self._TILE_TEXTURE_OFFSETS = {
            "Jinjo": 0x0000,
            "Note": 0x1000,
            "Red_Feather": 0x2420,
            "Blue_Egg": 0x2C20,
            "Banjo": 0x3C20,
            "Kazooie": 0x4420,
            "Honeycomb": 0x9C80,
            "Mumbo": 0xA480,
        }
        self._TILE_TEXTURE_BIT_SIZES = {
            "Jinjo": 0x18,
            "Note": 0x10,
            "Red_Feather": 0x10,
            "Blue_Egg": 0x18,
            "Banjo": 0x10,
            "Kazooie": 0x18,
            "Honeycomb": 0x10,
            "Mumbo": 0x18,
        }
        self._TILE_TEXTURE_FOLLOW_COUNT = {
            "Jinjo": 7,
            "Note": 7,
            "Red_Feather": 9,
            "Blue_Egg": 8,
            "Banjo": 9,
            "Kazooie": 7,
            "Honeycomb": 9,
            "Mumbo": 7,
        }
        self._TILE_TRANSLATOR_DICT = {
            0: "Banjo",
            1: "Blue_Egg",
            2: "Red_Feather",
            3: "Honeycomb",
            4: "Jinjo",
            5: "Kazooie",
            6: "Note",
            7: "Mumbo",
        }
        self._TILE_SEGMENTED_ADDRESSES = {
            # Banjo
            0x6: 0x1450,
            0x8: 0x1490,
            # Blue Egg
            0x0: 0x0F10,
            0xB: 0x0ED0,
            # Red Feather
            0x9: 0x1690,
            0xE: 0x1650,
            # Honeycomb
            0x2: 0x10D0,
            0x4: 0x1110,
            # Jinjo
            0x3: 0x11D0,
            0x7: 0x1210,
            # Kazooie
            0x1: 0x0FD0,
            0xD: 0x1010,
            # Note
            0xA: 0x1790,
            0xC: 0x1750,
            # Mumbo
            0x5: 0x1390,
            0xF: 0x1350,
        }
    
    def _translate_gv_mp_tile_dict(self, gv_mp_tile_dict):
        gv_mp_texture_tile_dict = {
            "Banjo": [],
            "Blue_Egg": [],
            "Red_Feather": [],
            "Honeycomb": [],
            "Jinjo": [],
            "Kazooie": [],
            "Note": [],
            "Mumbo": [],
        }
        for gv_mp_tile_count in gv_mp_tile_dict:
            gv_mp_tile_value = gv_mp_tile_dict[gv_mp_tile_count]
            gv_mp_tile_str = self._TILE_TRANSLATOR_DICT[gv_mp_tile_value]
            gv_mp_tile_segmented_address = self._TILE_SEGMENTED_ADDRESSES[gv_mp_tile_count]
            f3dex_command = 0x040079DF01000000 + gv_mp_tile_segmented_address
            gv_mp_texture_tile_dict[gv_mp_tile_str].append(f3dex_command)
        return gv_mp_texture_tile_dict

    def _remove_following_texture_placements(self, dlist_command_line, following_count=1):
        start_count = self._find_display_list_command_count(dlist_command_line)
        remove_line_count = 0
        for count in range(start_count + following_count, self._display_list_command_count):
            display_list_command, display_list_command_parameters = self._get_display_list_command_info(count)
            if(display_list_command == 0x04 or display_list_command == 0xB1):
                remove_line_count += 1
            else:
                break
        starting_index = self._display_list_setup_offset + 0x8 + (start_count + remove_line_count + following_count) * 0x8
        index_diff = - (remove_line_count * 0x8)
        self._change_model_file_size(starting_index, index_diff)
        self._adjust_display_list_command_count(-remove_line_count)
    
    def _add_following_texture_placements(self, dlist_command_line, new_dlist_command_line, following_count=1):
        start_count = self._find_display_list_command_count(dlist_command_line)
        self._insert_display_list_command(start_count + following_count, 0xB100020400040600)
        self._insert_display_list_command(start_count + following_count, new_dlist_command_line)

    def _reassign_gv_mp_tile_textures(self, gv_mp_tile_dict):
        gv_mp_texture_tile_dict = self._translate_gv_mp_tile_dict(gv_mp_tile_dict)
        for category in self._TILE_TEXTURE_OFFSETS:
            bit_size = self._TILE_TEXTURE_BIT_SIZES[category] * 0x1000000000000
            texture_offset = self._TILE_TEXTURE_OFFSETS[category]
            dlist_command_line = 0xFD00000000000000 + bit_size + 0x000002000000 + texture_offset
            follow_count = self._TILE_TEXTURE_FOLLOW_COUNT[category]
            self._remove_following_texture_placements(dlist_command_line, following_count=follow_count)
        for category in self._TILE_TEXTURE_OFFSETS:
            bit_size = self._TILE_TEXTURE_BIT_SIZES[category] * 0x1000000000000
            texture_offset = self._TILE_TEXTURE_OFFSETS[category]
            dlist_command_line = 0xFD00000000000000 + bit_size + 0x000002000000 + texture_offset
            follow_count = self._TILE_TEXTURE_FOLLOW_COUNT[category]
            for new_dlist_command_line in gv_mp_texture_tile_dict[category]:
                self._add_following_texture_placements(dlist_command_line, new_dlist_command_line, following_count=follow_count)
        if(self._vertex_setup_offset % 0x10 == 0x8):
            starting_index = self._display_list_setup_offset + 0x8 + self._display_list_command_count * 0x8
            self._change_model_file_size(starting_index, 8)

if __name__ == '__main__':
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/GV_Matching_Puzzle/"
    ORIGINAL_FILE_NAME = "646058" # 10248
    COPY_EXT = "-Copy"
    from shutil import copy
    from random import choice
    copy(f"{FILE_DIR}{ORIGINAL_FILE_NAME}.bin", f"{FILE_DIR}{ORIGINAL_FILE_NAME}{COPY_EXT}.bin")
    matching_puzzle_model_obj = MATCHING_PUZZLE_MODEL_CLASS(FILE_DIR, f"{ORIGINAL_FILE_NAME}{COPY_EXT}")
    gv_mp_tile_dict = {}
    tile_choices = [count for count in range(8)] * 2
    for count in range(0x10):
        selection = choice(tile_choices)
        gv_mp_tile_dict[count] = selection
        tile_choices.remove(selection)
    matching_puzzle_model_obj._reassign_gv_mp_tile_textures(gv_mp_tile_dict)