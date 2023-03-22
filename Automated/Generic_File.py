import struct
from mmap import mmap
from json import load
from random import seed, randint, uniform, choice, triangular

class GENERIC_FILE_CLASS():
    def __init__(self, file_dir, file_name):
        self._file_name = file_name
        self._read_mmap(file_dir, file_name)
        self._seed = None

    ##########################
    ######## BIN FILE ########
    ##########################
    
    def _read_mmap(self, file_dir, file_name):
        with open(f"{file_dir}{file_name}.bin", "rb+") as bin_file:
            self._mmap = mmap(bin_file.fileno(), 0)
    
    def _read_byte(self, index_start):
        return self._mmap[index_start]
    
    def _read_bytes(self, index_start, byte_count):
        return self._mmap[index_start:index_start+byte_count]

    def _write_byte(self, index_start, new_val):
        self._mmap[index_start] = new_val

    def _write_bytes(self, index_start, byte_count, new_val):
        byte_list = self._int_to_byte_list(new_val, byte_count)
        for count, int_val in enumerate(byte_list):
            self._write_byte(index_start + count, int_val)

    def _write_float_bytes(self, index_start, float_val, byte_count=4):
        byte_list = self._float_to_byte_list(float_val)[:byte_count]
        for count, int_val in enumerate(byte_list):
            self._write_byte(index_start + count, int_val)
    
    ###########################
    ######## JSON FILE ########
    ###########################

    def _read_json(self, file_dir, file_name):
        with open(f"{file_dir}{file_name}.json", "r") as jf:
            self._json_data = load(jf)

    ###########################
    ######## INTERPRET ########
    ###########################

    # SINGLE VALUE MANIPULATION
    def _possible_negative(self, int_val, byte_count):
        max_val = (0x1 << (byte_count * 8))
        if(int_val > (max_val / 2)):
            int_val -= max_val
        return int_val
    
    def _possible_negative_to_positive(self, int_val, byte_count):
        if(int_val < 0):
            max_val = (0x1 << (byte_count * 8))
            int_val += max_val
        return int_val
    
    def _leading_zeros(self, str_val, str_len):
        return str_val.zfill(str_len)

    def _int_to_hex_str(self, int_val, str_len=0):
        hex_str = str(hex(int_val))[2:].upper()
        return self._leading_zeros(hex_str, str_len)

    def _hex_str_to_float(self, hex_str_val):
        try:
            return struct.unpack('!f', bytes.fromhex(hex_str_val))[0]
        except ValueError as e:
            print(f"Hex Str Val: {hex_str_val}")
            raise e

    # BYTE LIST
    def _byte_list_to_int(self, byte_list):
        int_val = 0
        for curr_byte in byte_list:
            int_val = (int_val * 256) + curr_byte
        return int_val

    def _byte_list_to_hex_str(self, byte_list):
        int_val = self._byte_list_to_int(byte_list)
        return self._int_to_hex_str(int_val, len(byte_list) * 2)

    def _byte_list_to_float(self, byte_list):
        int_val = self._byte_list_to_int(byte_list)
        hex_str_val = self._int_to_hex_str(int_val, len(byte_list) * 2)
        return self._hex_str_to_float(hex_str_val)

    # READ BYTE LIST
    def _read_byte_list_to_int(self, index_start, byte_count):
        byte_list = self._read_bytes(index_start, byte_count)
        return self._byte_list_to_int(byte_list)

    def _read_byte_list_to_hex_str(self, index_start, byte_count):
        byte_list = self._read_bytes(index_start, byte_count)
        return self._byte_list_to_hex_str(byte_list)

    def _read_byte_list_to_float(self, index_start, byte_count):
        byte_list = self._read_bytes(index_start, byte_count)
        return self._byte_list_to_float(byte_list)
    
    # NUMBER TO BYTE LIST
    def _int_to_byte_list(self, int_val, byte_count):
        hex_str = self._int_to_hex_str(int_val, byte_count * 2)
        byte_list = []
        for char_index in range(0, len(hex_str), 2):
            int_val = int(hex_str[char_index:char_index+2], 16)
            byte_list.append(int_val)
        return byte_list
    
    def _float_to_byte_list(self, float_val):
        hex_float = hex(struct.unpack('<I', struct.pack('<f', float_val))[0])
        hex_str = self._leading_zeros(str(hex_float)[2:].upper(), 8)
        byte_list = []
        for char_index in range(0, len(hex_str), 2):
            int_val = int(hex_str[char_index:char_index+2], 16)
            byte_list.append(int_val)
        return byte_list
    
    #####################
    ### MMAP SPECIFIC ###
    #####################

    def _find_int(self, search_int, byte_count, endian="big", start_index=0, end_index=None):
        search_bytes = search_int.to_bytes(byte_count, endian)
        if(not end_index):
            end_index = len(self._mmap)
        found_index = self._mmap.find(search_bytes, start_index, end_index)
        return found_index

    def _reverse_find_int(self, search_int, byte_count, endian="big", start_index=0, end_index=None):
        search_bytes = search_int.to_bytes(byte_count, endian)
        if(not end_index):
            end_index = len(self._mmap)
        found_index = self._mmap.rfind(search_bytes, start_index, end_index)
        return found_index

    ########################
    ### RANDOM FUNCTIONS ###
    ########################

    def _set_seed(self, seed_val):
        self._seed = seed_val

    def _rand_int(self, lower, upper, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return randint(lower, upper)

    def _rand_int_triangular(self, lower, upper, mode, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return round(triangular(lower, upper, mode))
        
    def _rand_float(self, lower, upper, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return uniform(lower, upper)
    
    def _rand_choice(self, list, add_val=0):
        if(self._seed):
            seed(a=(self._seed + add_val))
        return choice(list)