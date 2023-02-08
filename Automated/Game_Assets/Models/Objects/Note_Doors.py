import sys

sys.path.append(".")
from Automated.Game_Assets.Models.Generic_Model import GENERIC_MODEL_CLASS

class NOTE_DOOR_CLASS(GENERIC_MODEL_CLASS):
    def __init__(self, file_dir, file_name):
        super().__init__(file_dir, file_name)
        self._NOTE_DOOR_TEXTURE_OFFSETS = {
            "Wooden_Door": 0x0,
            "Note_Symbol": 0x820,
            0: 0x1820,
            "Glitter": 0x2820,
            1: 0x3040,
            2: 0x4040,
            3: 0x5040,
            4: 0x6040,
            5: 0x7040,
            6: 0x8040,
            7: 0x9040,
            8: 0xA040,
            # 9: 0x8040,
            }
        self._NOTE_DOOR_INDICES = {
            0: { # 50
                10: {
                    "Door_Vertices": [0xBE50, 0xBE60, 0xBE70, 0xBE80],
                    "Overlay_Textures": 0xB2CE,
                    },
                1: {
                    "Door_Vertices": [0xBE90, 0xBEA0, 0xBEB0, 0xBEC0],
                    "Overlay_Textures": 0xB326,
                    },
                },
            1: { # 180
                100: {
                    "Door_Vertices": [0xBED0, 0xBEE0, 0xBEF0, 0xBF00],
                    "Overlay_Textures": 0xB376,
                    },
                10: {
                    "Door_Vertices": [0xBF10, 0xBF20, 0xBF30, 0xBF40],
                    "Overlay_Textures": 0xB3CE,
                    },
                1: {
                    "Door_Vertices": [0xBF50, 0xBF60, 0xBF70, 0xBF80],
                    "Overlay_Textures": 0xB3FE,
                    },
                },
            2: { # 260
                100: {
                    "Door_Vertices": [0xBF90, 0xBFA0, 0xBFB0, 0xBFC0],
                    "Overlay_Textures": 0xB44E,
                    },
                10: {
                    "Door_Vertices": [0xBFD0, 0xBFE0, 0xBFF0, 0xC000],
                    "Overlay_Textures": 0xB4A6,
                    },
                1: {
                    "Door_Vertices": [0xC010, 0xC020, 0xC030, 0xC040],
                    "Overlay_Textures": 0xB4D6,
                    },
                },
            3: { # 350
                100: {
                    "Door_Vertices": [0xC050, 0xC060, 0xC070, 0xC080],
                    "Overlay_Textures": 0xB526,
                    },
                10: {
                    "Door_Vertices": [0xC090, 0xC0A0, 0xC0B0, 0xC0C0],
                    "Overlay_Textures": 0xB57E,
                    },
                1: {
                    "Door_Vertices": [0xC0D0, 0xC0E0, 0xC0F0, 0xC100],
                    "Overlay_Textures": 0xB5AE,
                    },
                },
            4: { # 450
                100: {
                    "Door_Vertices": [0xC110, 0xC120, 0xC130, 0xC140],
                    "Overlay_Textures": 0xB5FE,
                    },
                10: {
                    "Door_Vertices": [0xC150, 0xC160, 0xC170, 0xC180],
                    "Overlay_Textures": 0xB656,
                    },
                1: {
                    "Door_Vertices": [0xC190, 0xC1A0, 0xC1B0, 0xC1C0],
                    "Overlay_Textures": 0xB686,
                    },
                },
            5: { # 640
                100: {
                    "Door_Vertices": [0xC1D0, 0xC1E0, 0xC1F0, 0xC200],
                    "Overlay_Textures": 0xB6D6,
                    },
                10: {
                    "Door_Vertices": [0xC210, 0xC220, 0xC230, 0xC240],
                    "Overlay_Textures": 0xB72E,
                    },
                1: {
                    "Door_Vertices": [0xC250, 0xC260, 0xC270, 0xC280],
                    "Overlay_Textures": 0xB75E,
                    },
                },
            6: { # 765
                100: {
                    "Door_Vertices": [0xC290, 0xC2A0, 0xC2B0, 0xC2C0],
                    "Overlay_Textures": 0xB7AE,
                    },
                10: {
                    "Door_Vertices": [0xC2D0, 0xC2E0, 0xC2F0, 0xC300],
                    "Overlay_Textures": 0xB806,
                    },
                1: {
                    "Door_Vertices": [0xC310, 0xC320, 0xC330, 0xC340],
                    "Overlay_Textures": 0xB836,
                    },
                },
            7: { # 810
                100: {
                    "Door_Vertices": [0xC350, 0xC360, 0xC370, 0xC380],
                    "Overlay_Textures": 0xB886,
                    },
                10: {
                    "Door_Vertices": [0xC390, 0xC3A0, 0xC3B0, 0xC3C0],
                    "Overlay_Textures": 0xB8DE,
                    },
                1: {
                    "Door_Vertices": [0xC3D0, 0xC3E0, 0xC3F0, 0xC400],
                    "Overlay_Textures": 0xB90E,
                    },
                },
            8: { # 828
                100: {
                    "Door_Vertices": [0xC410, 0xC420, 0xC430, 0xC440],
                    "Overlay_Textures": 0xB95E,
                    },
                10: {
                    "Door_Vertices": [0xC450, 0xC460, 0xC470, 0xC480],
                    "Overlay_Textures": 0xB9B6,
                    },
                1: {
                    "Door_Vertices": [0xC490, 0xC4A0, 0xC4B0, 0xC4C0],
                    "Overlay_Textures": 0xB9E6,
                    },
                },
            9: { # 846
                100: {
                    "Door_Vertices": [0xC4D0, 0xC4E0, 0xC4F0, 0xC500],
                    "Overlay_Textures": 0xBA36,
                    },
                10: {
                    "Door_Vertices": [0xC510, 0xC520, 0xC530, 0xC540],
                    "Overlay_Textures": 0xBA8E,
                    },
                1: {
                    "Door_Vertices": [0xC550, 0xC560, 0xC570, 0xC580],
                    "Overlay_Textures": 0xBABE,
                    },
                },
            10: { # 864
                100: {
                    "Door_Vertices": [0xC590, 0xC5A0, 0xC5B0, 0xC5C0],
                    "Overlay_Textures": 0xBB0E,
                    },
                10: {
                    "Door_Vertices": [0xC5D0, 0xC5E0, 0xC5F0, 0xC600],
                    "Overlay_Textures": 0xBB66,
                    },
                1: {
                    "Door_Vertices": [0xC610, 0xC620, 0xC630, 0xC640],
                    "Overlay_Textures": 0xBB96,
                    },
                },
            11: { # 882
                100: {
                    "Door_Vertices": [0xC650, 0xC660, 0xC670, 0xC680],
                    "Overlay_Textures": 0xBBE6,
                    },
                10: {
                    "Door_Vertices": [0xC690, 0xC6A0, 0xC6B0, 0xC6C0],
                    "Overlay_Textures": 0xBBE6,
                    },
                1: {
                    "Door_Vertices": [0xC6D0, 0xC6E0, 0xC6F0, 0xC700],
                    "Overlay_Textures": 0xBC46,
                    },
                },
            }
    
    def _debug_print(self, message):
        print(message)
        raise SystemError(message)
    
    def _flip_texture(self, vertex_index_list, x_axis=True, y_axis=True):
        for vertex_index in vertex_index_list:
            if(x_axis):
                v_value = 0x10000 - self._read_byte_list_to_int(vertex_index + 0xA, 2)
                self._write_bytes(vertex_index + 0xA, 2, v_value)
            if(y_axis):
                u_value = 0x10000 - self._read_byte_list_to_int(vertex_index + 0x8, 2)
                self._write_bytes(vertex_index + 0x8, 2, u_value)
    
    def _set_digit(self, door_num, count_value, digit_place):
        if(digit_place == 100):
            digit_value = count_value // 100
        elif(digit_place == 10):
            digit_value = (count_value // 10) % 10
        elif(digit_place == 1):
            digit_value = count_value % 10
        else:
            self._debug_print("Digit place must be 1, 10, or 100")
        index_start = self._NOTE_DOOR_INDICES[door_num][digit_place]["Overlay_Textures"]
        if(digit_value == 9):
            texture_offset = self._NOTE_DOOR_TEXTURE_OFFSETS[6]
            self._flip_texture(self._NOTE_DOOR_INDICES[door_num][digit_place]["Door_Vertices"], x_axis=True, y_axis=True)
        else:
            texture_offset = self._NOTE_DOOR_TEXTURE_OFFSETS[digit_value]
        self._write_bytes(index_start, 2, texture_offset)

    def _modify_door_count_requirement(self, door_num, count_value):
        # Note Door Value Conditions
        if(door_num < 0 or door_num > 11):
            self._debug_print("Door numbers are between 0 and 11, inclusively")
        if(door_num == 0 and (count_value >= 100 or count_value < 0)):
            self._debug_print("Count for the first door must be between 0 and 99, inclusively")
        elif(count_value >= 1000 or count_value < 0):
            self._debug_print("Count for the first door must be between 0 and 999, inclusively")
        hundreds_value = count_value // 100
        tens_value = (count_value // 10) % 10
        if(door_num == 11 and hundreds_value != tens_value and hundreds_value not in [6, 9] and tens_value not in [6, 9]):
            self._debug_print("Until we figure out how to modify display lists, the hundreds need to match the tens for door 11")
        # Setting Value
        if(door_num > 0):
            self._set_digit(door_num, count_value, 100)
        self._set_digit(door_num, count_value, 10)
        self._set_digit(door_num, count_value, 1)
    
    def _replace_note_symbol(self, new_image):
        pass