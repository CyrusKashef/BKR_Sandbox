import sys
from random import seed, shuffle

sys.path.append(".")

from Automated.Game_Assets.Sounds.BK_Sound import BK_SOUND_CLASS

class SOUND_CLASS():
    def __init__(self, file_dir):
        # CONSTANTS
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        # VARIABLES
        self._file_dir = file_dir
    
    def _rand_shuffle(self, list, add_val=0, this_seed=None):
        if(this_seed):
            seed(a=(this_seed + add_val))
        return shuffle(list)
    
    def _randomize_music_instruments(self, sound_file_pointer, this_seed):
        file_name = str(hex(sound_file_pointer))[2:].upper() + "-Decompressed"
        music_obj = BK_SOUND_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, file_name)
        music_obj._get_tracks_offsets()
        instrument_list = []
        for track_num in range(0x1, 0x10):
            # new_instrument = self._rand_choice(list(ALLOWED_INSTRUMENTS), sound_file_pointer + track_num)
            instrument_val = music_obj._get_instrument(track_num)
            instrument_list.append(instrument_val)
        self._rand_shuffle(instrument_list, sound_file_pointer, this_seed)
        for track_num in range(0x1, 0x10):
            music_obj._replace_instrument(track_num, instrument_list[track_num - 1])
    
    def _remove_music_sound(self, sound_file_pointer):
        file_name = str(hex(sound_file_pointer))[2:].upper() + "-Decompressed"
        music_obj = BK_SOUND_CLASS(self._file_dir + self._EXTRACTED_FILES_DIR, file_name)
        music_obj._get_tracks_offsets()
        music_obj._set_music_volume(1, 0x0)
        music_obj._set_music_reverb(1, 0x0)