import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class FURNACE_FUN_MODEL_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._get_object_texture_header_info()
        self._get_object_vertex_header_info()
    
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
    FILE_DIR = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/Rando3_Test/"
    FILE_NAME = "A795B8-Default"
    furnace_fun_model_obj = FURNACE_FUN_MODEL_CLASS(FILE_DIR, FILE_NAME)
    furnace_fun_model_obj._lower_invisible_barriers()