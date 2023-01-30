import sys
import time

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class BK_SOUND_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._num_of_tracks = 16
        self._tracks_offset_dict = {}
        self._track_info_dict = {}

    def _get_tracks_offsets(self):
        for track_num in range(self._num_of_tracks):
            self._tracks_offset_dict[track_num] = self._read_byte_list_to_int(track_num * 0x4, 4)

    def _set_music_tempo(self, new_tempo):
        pass

    def _set_music_volume(self, track_num, new_volume):
        if(self._tracks_offset_dict[track_num] == 0):
            print("Track Does Not Exist")
            return
        search_val = 0x01B007 + track_num * 0x100
        if((track_num < 0xF) and (self._tracks_offset_dict[track_num + 1] != 0)):
            command_index = self._mmap.find(search_val.to_bytes(3, 'big'), self._tracks_offset_dict[track_num], self._tracks_offset_dict[track_num + 1])
        else:
            command_index = self._mmap.find(search_val.to_bytes(3, 'big'), self._tracks_offset_dict[track_num])
        if(command_index == -1):
            search_val = 0x0107
            if((track_num < 0xF) and (self._tracks_offset_dict[track_num + 1] != 0)):
                command_index = self._mmap.find(search_val.to_bytes(2, 'big'), self._tracks_offset_dict[track_num], self._tracks_offset_dict[track_num + 1])
            else:
                command_index = self._mmap.find(search_val.to_bytes(2, 'big'), self._tracks_offset_dict[track_num])
            if(command_index == -1):
                print("Volume Does Not Exist")
                return
            else:
                self._mmap[command_index + 2] = new_volume
        else:
            self._mmap[command_index + 3] = new_volume
        return

    def _set_music_reverb(self, track_num, new_reverb):
        if(self._tracks_offset_dict[track_num] == 0):
            print("Track Does Not Exist")
            return
        search_val = 0x015B
        if((track_num < 0xF) and (self._tracks_offset_dict[track_num + 1] != 0)):
            command_index = self._mmap.find(search_val.to_bytes(2, 'big'), self._tracks_offset_dict[track_num], self._tracks_offset_dict[track_num + 1])
        else:
            command_index = self._mmap.find(search_val.to_bytes(2, 'big'), self._tracks_offset_dict[track_num])
        if(command_index == -1):
            print("Reverb Does Not Exist")
            return
        else:
            self._mmap[command_index + 2] = new_reverb
        return
    
    def _get_instrument(self, track_num):
        if(self._tracks_offset_dict[track_num] == 0):
            print("Track Does Not Exist")
            return False
        leading_val = self._mmap[self._tracks_offset_dict[track_num]]
        search_val = leading_val * 0x100 + 0xC0 + track_num
        if(track_num < 0xF):
            command_index = self._mmap.find(search_val.to_bytes(2, 'big'), self._tracks_offset_dict[track_num], self._tracks_offset_dict[track_num + 1])
        else:
            command_index = self._mmap.find(search_val.to_bytes(2, 'big'), self._tracks_offset_dict[track_num])
        if(command_index == -1):
            print("Instrument Does Not Exist")
            return False
        return self._mmap[command_index + 2]
    
    def _replace_instrument(self, track_num, new_instrument):
        if(self._tracks_offset_dict[track_num] == 0):
            print("Track Does Not Exist")
            return
        leading_val = self._mmap[self._tracks_offset_dict[track_num]]
        search_val = leading_val * 0x100 + 0xC0 + track_num
        if(track_num < 0xF):
            command_index = self._mmap.find(search_val.to_bytes(2, 'big'), self._tracks_offset_dict[track_num], self._tracks_offset_dict[track_num + 1])
        else:
            command_index = self._mmap.find(search_val.to_bytes(2, 'big'), self._tracks_offset_dict[track_num])
        if(command_index == -1):
            print("Instrument Does Not Exist")
            return
        self._mmap[command_index + 2] = new_instrument
        return
    
    #################
    ### BREAKDOWN ###
    #################

    def _get_header_info(self, track_num):
        self._track_info_dict[track_num]["Offset"] = self._read_byte_list_to_int(track_num * 0x4, 4)
    
    def _get_track_info(self, track_num):
        track_start = self._track_info_dict[track_num]
        if(self._track_info_dict[track_num]["Offset"] == 0):
            self._track_info_dict[track_num]["Info"] = None
            return
        elif((track_num == 15) or (self._track_info_dict[track_num + 1]["Offset"] == 0)):
            track_end = len(self._mmap)
        else:
            track_end = self._track_info_dict[track_num + 1]
        self._track_info_dict[track_num]["Info"] = self._read_byte_list_to_hex_str(track_start, track_end - track_start)
    
    def _breakdown_main(self):
        for track_num in range(16):
            self._track_info_dict[track_num] = {}
            self._get_header_info(track_num)
            self._get_track_info(track_num)
    
    ###############
    ### CONVERT ###
    ###############

    def _bt_to_bk_sound(self, tooie_dict):
        additional_offset = 0x44 - tooie_dict[0]["Offset"]
        for track_num in range(16):
            if(tooie_dict[track_num]["Offset"] == 0):
                self._track_info_dict[track_num]["Offset"] = 0
                self._track_info_dict[track_num]["Info"] = None
            else:
                self._track_info_dict[track_num]["Offset"] = tooie_dict[track_num]["Offset"] + additional_offset
                self._track_info_dict[track_num]["Info"] = tooie_dict[track_num]["Info"]