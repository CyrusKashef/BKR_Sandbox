###################
### AREA OBJECT ###
###################

class AREA_OBJECT_CLASS():
    def __init__(self, area_dict):
        self._debug_name = area_dict["Debug_Name"]
        self._world_enum = area_dict["World_Enum"]
        self._map_enum = area_dict["Map_Enum"]
        self._entry_enum = area_dict["Entry_Enum"]
        self._accessible_warp_out_assembly_indices_list = area_dict["ASM_Index_List"]
        self._standard_complex_object_coord_list = area_dict["Standard_Complex_Coords"]
        self._standard_simple_object_coord_list = area_dict["Standard_Simple_Coords"]
        self._additional_complex_object_coord_list = area_dict["Additional_Complex_Coords"]
        self._additional_simple_object_coord_list = area_dict["Additional_Simple_Coords"]
        self._reachable_boolean = False
    
    def _set_reachable(self):
        self._reachable_boolean = True

###################
### WARP OBJECT ###
###################

class WARP_OBJECT_CLASS():
    def __init__(self, warp_dict):
        self._debug_name = warp_dict["Debug_Name"]
        self._map_enum = warp_dict["Map_Enum"]
        self._entry_enum = warp_dict["Entry_Enum"]
        self._can_be_coupled = warp_dict["Coupleable"]
        self._warp_used_boolean = False
    
    def _set_warp_used(self):
        self._warp_used_boolean = True