import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class FURNACE_FUN_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
        # 0 = Blank, 1 = BK, 2 = Picture, 3 = Sound,
        # 4 = Minigame, 5 = Gruntilda, 6 = Skull, 8 = Joker
        # 7 isn't used, but in the decomp, Joker = 7 instead
        # _ _ _ _ _ _ _ 6 _ _ _ _ _ _ _ _
        # 2 6 0 _ _ _ 6 5 1 0 2 0 6 6 0 _
        # 8 _ 1 _ _ _ 1 _ _ _ _ 6 _ _ _ _
        # _ _ 5 5 0 3 4 _ _ _ _ 6 _ _ _ _
        # _ _ 2 _ _ _ 2 _ _ _ _ 6 _ _ _ _
        # _ _ 1 _ _ _ 0 1 6 2 3 4 1 0 _ _
        # 0 3 4 3 6 _ _ _ 6 _ _ _ _ 3 5 8
        # 3 _ _ _ 2 _ _ _ 5 _ _ _ _ 2 _ _
        # 0 _ _ _ 5 1 0 1 4 3 2 5 1 2 _ _
        # 5 2 1 3 6 _ _ _ _ _ _ 0 _ _ _ _
        # 0 _ _ _ 0 _ _ _ _ _ _ 6 _ _ _ _
        # 8 _ _ _ 5 4 0 1 4 2 1 3 5 1 _ _
        # _ _ _ _ _ 1 _ _ 0 _ _ _ _ 1 _ _
        # _ _ _ _ _ 2 _ _ 1 _ _ _ _ 8 _ _
        # _ 0 6 8 0 3 1 0 5 _ _ _ _ _ _ _
        # _ _ _ _ _ _ _ 2 _ _ _ _ _ _ _ _
        # _ _ _ _ _ _ _ 1 _ _ _ _ _ _ _ _
        self._TILE_TEXTURE_OFFSETS = {
            "BK_Tile": 0x97A0,
            "Sound_Tile": 0x9FC0,
            "Blank_Tile": 0xA7E0,
            "Gruntilda_Tile": 0xB000,
            "Skull_Tile": 0xB820,
            "Eye_Tile": 0xC040,
            "Timer_Tile": 0xC860,
            "Joker_Tile": 0xD080,
        }
        # TILE NUMBERING
        # ___ ___ ___ ___ ___ ___ ___ 05E (Skull Tile)    ___ ___ ___ ___
        # 052 053 054 ___ ___ ___ 055 056 057 058 059 05A 05B 05C 05D ___
        # 04E ___ 04F ___ ___ ___ 050 ___ ___ ___ ___ 051 ___ ___ ___ ___
        # ___ ___ 048 049 04A 04B 04C ___ ___ ___ ___ 04D ___ ___ ___ ___
        # ___ ___ 045 ___ ___ ___ 046 ___ ___ ___ ___ 047 ___ ___ ___ ___
        # ___ ___ 03C ___ ___ ___ 03D 03E 03F 040 041 042 043 044 ___ ___
        # 033 034 035 036 037 ___ ___ ___ 038 ___ ___ ___ ___ 039 03A 03B
        # 02F ___ ___ ___ 030 ___ ___ ___ 031 ___ ___ ___ ___ 032 ___ ___
        # 024 ___ ___ ___ 025 026 027 028 029 02A 02B 02C 02D 02E ___ ___
        # 01E 01F 020 021 022 ___ ___ ___ ___ ___ ___ 023 ___ ___ ___ ___
        # 01B ___ ___ ___ 01C ___ ___ ___ ___ ___ ___ 01D ___ ___ ___ ___
        # 010 ___ ___ ___ 011 012 013 014 015 016 017 018 019 01A ___ ___
        # ___ ___ ___ ___ ___ 00D ___ ___ 00E ___ ___ ___ ___ 00F ___ ___
        # ___ ___ ___ ___ ___ 00A ___ ___ 00B ___ ___ ___ ___ 00C ___ ___
        # ___ 002 003 004 005 006 007 008 009 ___ ___ ___ ___ ___ ___ ___
        # ___ ___ ___ ___ ___ ___ ___ 001 ___ ___ ___ ___ ___ ___ ___ ___
        # ___ ___ ___ ___ ___ ___ ___ 000 (BK TILE)   ___ ___ ___ ___ ___
        #                           ENTRANCE
        self._TILE_SEGMENTED_ADDRESSES = {
            # BK Tiles
            0x00: 0x7720, 0x07: 0x7780, 0x0B: 0x77E0, 0x0D: 0x7840, 0x0F: 0x78A0,
            0x14: 0x7900, 0x17: 0x7960, 0x1A: 0x79C0, 0x20: 0x7A20, 0x26: 0x7A80,
            0x28: 0x7AE0, 0x2D: 0x7B40, 0x3C: 0x7BA0, 0x3E: 0x7C00, 0x43: 0x7C60,
            0x4F: 0x7CC0, 0x50: 0x7D20, 0x57: 0x7D80,
            # Sound Tile
            0x06: 0x9340, 0x18: 0x9400, 0x21: 0x9220, 0x2A: 0x90A0, 0x2F: 0x93A0,
            0x34: 0x91C0, 0x36: 0x9160, 0x39: 0x92E0, 0x41: 0x9280, 0x4B: 0x9100,
            # Blank Tile
            0x02: 0x84A0, 0x05: 0x82C0, 0x08: 0x8320, 0x0E: 0x8620, 0x13: 0x85C0,
            0x1B: 0x86E0, 0x1C: 0x8740, 0x23: 0x8380, 0x24: 0x83E0, 0x27: 0x8440,
            0x33: 0x8500, 0x3D: 0x8560, 0x44: 0x8680, 0x4A: 0x87A0, 0x54: 0x8800,
            0x58: 0x8860, 0x5A: 0x88C0, 0x5D: 0x8920,
            # Gruntilda Tile
            0x09: 0x97C0, 0x11: 0x9700, 0x19: 0x9580, 0x1E: 0x9760, 0x25: 0x9820,
            0x2C: 0x95E0, 0x31: 0x9520, 0x3A: 0x9640, 0x48: 0x9460, 0x49: 0x94C0,
            0x56: 0x96A0,
            # Skull Tile
            0x03: 0x8A40, 0x1D: 0x8C20, 0x22: 0x8CE0, 0x37: 0x8980, 0x38: 0x89E0,
            0x3F: 0x8AA0, 0x47: 0x8B00, 0x4D: 0x8B60, 0x51: 0x8BC0, 0x53: 0x8C80,
            0x55: 0x8D40, 0x5B: 0x8DA0, 0x5C: 0x8E00, 0x5E: 0x8E60,
            # Eye Tile
            0x01: 0x7E40, 0x0A: 0x7F00, 0x16: 0x7DE0, 0x1F: 0x7EA0, 0x2B: 0x7F60,
            0x2E: 0x7FC0, 0x30: 0x8020, 0x32: 0x8080, 0x40: 0x80E0, 0x45: 0x8140,
            0x46: 0x81A0, 0x52: 0x8200, 0x59: 0x8260,
            # Timer Tile
            0x12: 0x9A00, 0x15: 0x9940, 0x29: 0x9A60, 0x35: 0x9880, 0x42: 0x99A0,
            0x4C: 0x98E0,
            # Joker Tile
            0x04: 0x8F20, 0x0C: 0x9040, 0x10: 0x8F80, 0x3B: 0x8FE0, 0x4E: 0x8EC0,
        }
    
    def _translate_ff_tile_dict(self, ff_tile_dict):
        ff_texture_tile_dict = {
            "BK_Tile": [],
            "Sound_Tile": [],
            "Blank_Tile": [],
            "Gruntilda_Tile": [],
            "Skull_Tile": [],
            "Eye_Tile": [],
            "Timer_Tile": [],
            "Joker_Tile": [],
        }
        for ff_tile_count in ff_tile_dict:
            ff_tile_value = ff_tile_dict[ff_tile_count]
            ff_tile_segmented_address = self._TILE_SEGMENTED_ADDRESSES[ff_tile_count]
            f3dex_command = 0x040079DF01000000 + ff_tile_segmented_address
            ff_texture_tile_dict[ff_tile_value].append(f3dex_command)
        return ff_texture_tile_dict

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
        self._insert_display_list_command(start_count + following_count, 0xB10002040006080A)
        self._insert_display_list_command(start_count + following_count, new_dlist_command_line)

    def _reassign_ff_tile_textures(self, ff_tile_dict):
        ff_texture_tile_dict = self._translate_ff_tile_dict(ff_tile_dict)
        for category in self._TILE_TEXTURE_OFFSETS:
            dlist_command_line = 0xFD10000002000000 + self._TILE_TEXTURE_OFFSETS[category]
            self._remove_following_texture_placements(dlist_command_line, following_count=4)
        for category in self._TILE_TEXTURE_OFFSETS:
            dlist_command_line = 0xFD10000002000000 + self._TILE_TEXTURE_OFFSETS[category]
            for new_dlist_command_line in ff_texture_tile_dict[category]:
                self._add_following_texture_placements(dlist_command_line, new_dlist_command_line, following_count=4)
        if(self._vertex_setup_offset % 0x10 == 0x8):
            starting_index = self._display_list_setup_offset + 0x8 + self._display_list_command_count * 0x8
            self._change_model_file_size(starting_index, 8)
    
    def _lower_invisible_barriers(self):
        for count in range(self._vertex_count):
            vertex_info_index_start, x_position, y_position, z_position, u_mapping, v_mapping, red_val, green_val, blue_val, alpha_val = self._get_vertex_info(count)
            refactored_x_position = self._possible_negative(x_position, 2)
            refactored_z_position = self._possible_negative(z_position, 2)
            if(alpha_val < 0xFF and
               refactored_x_position > -2000 and refactored_x_position < 2200 and
               refactored_z_position > -2500 and refactored_z_position < 2500):
                self._set_vertex_xyz_coords(count, x_position, 0xFFBB, z_position)

if __name__ == '__main__':
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/Furnace_Fun/"
    ORIGINAL_FILE_NAME = "A795B8"
    COPY_EXT = "-Copy"
    from shutil import copy
    from random import choice
    copy(f"{FILE_DIR}{ORIGINAL_FILE_NAME}.bin", f"{FILE_DIR}{ORIGINAL_FILE_NAME}{COPY_EXT}.bin")
    furnace_fun_model_obj = FURNACE_FUN_MODEL_CLASS(FILE_DIR, f"{ORIGINAL_FILE_NAME}{COPY_EXT}")
    # furnace_fun_model_obj._lower_invisible_barriers()
    ff_tile_dict = {}
    for count in range(0, 0x5F):
        ff_tile_dict[count] = choice([0, 1, 2, 3, 4, 5, 6, 8])
    furnace_fun_model_obj._reassign_ff_tile_textures(ff_tile_dict)