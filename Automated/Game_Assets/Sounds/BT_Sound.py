import sys
from mmap import mmap

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

class BT_SOUND_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._file_dir = file_dir
        self._track_info_dict = {}
    
    def _get_header_info(self):
        num_of_tracks = self._read_byte_list_to_int(0x04, 4)
        for track_num in range(num_of_tracks):
            self._tracks_offset_dict[track_num]["Offset"] = self._read_byte_list_to_int(track_num * 0x4 + 0x8, 4)
        for track_num in range(num_of_tracks, 16):
            self._tracks_offset_dict[track_num]["Offset"] = 0
            self._track_info_dict[track_num]["Info"] = None
        return num_of_tracks

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

    def _convert_to_bk_sound_file(self, new_file_name):
        num_of_tracks = self._convert_to_bk_header()
        for track_num in range(num_of_tracks):
            self._get_track_info(track_num)