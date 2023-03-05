class WARP_OBJECT_CLASS():
    def __init__(self, debug_name, warp_id, warp_to_area_id, transformation_enum):
        self._debug_name = debug_name
        self._warp_id = warp_id
        self._warp_to_area_id = warp_to_area_id
        self._transformation_enum = transformation_enum
        self._allocated = False

class AREA_OBJECT_CLASS():
    def __init__(self, debug_name, area_id, associated_room_id, warp_count):
        self._debug_name = debug_name
        self._area_id = area_id
        self._associated_room_id = associated_room_id
        self._warp_dict = {}
        for curr_count in range(warp_count):
            self._warp_dict[curr_count] = None
        self._reachable = False

class ROOM_OBJECT_CLASS():
    def __init__(self, debug_name, room_id, area_dict):
        self._debug_name = debug_name
        self._room_id = room_id
        self._area_dict = {}
        for area_id in area_dict:
            debug_string = area_dict[area_id]["Debug_String"]
            associated_room_id = area_dict[area_id]["Associated_Room_Id"]
            warp_count = area_dict[area_id]["Warp_Count"]
            self._area_dict[area_id] = AREA_OBJECT_CLASS(debug_string, area_id, associated_room_id, warp_count)