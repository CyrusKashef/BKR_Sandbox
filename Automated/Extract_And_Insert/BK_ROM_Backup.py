import sys
from mmap import mmap

sys.path.append(".")
from Automated.Generic_File import GENERIC_FILE_CLASS

from Data_Files.Asset_Table_Pointer_Dict import ASSET_TABLE_POINTER_DICT
from Data_Files.Bootloader_Assembly_Dict import BOOTLOADER_ASSEMBLY_DICT

class BK_ROM_CLASS(GENERIC_FILE_CLASS):
    def __init__(self, file_dir, bk_rom_path):
        ### CONSTANTS ###
        self._ASSET_TABLE_OFFSET = 0x10CD0
        self._EXTRACTED_FILES_DIR = "Extracted_Files/"
        self._COMPRESSED_BIN_EXTENSION = "-Compressed.bin"
        self._ASM_END = 0xFDAA10
        self._CIC = 0xA3886759
        self._CIC_DICT = {
            '6101': 0x00000000, # nope
            '6102': 0xF8CA4DDC,
            '6103': 0xA3886759,
            '6105': 0xDF26F436,
            '6106': 0x1FEA617A
        }
        self._HEADER_ITEMS = {
            'CRC1':             [0x0010, 0x0014],
            'CRC2':             [0x0014, 0x0018],
            'Boot Code':        [0x0040, 0x1000],
        }

        ### VARIABLES ###
        with open(bk_rom_path, "rb+") as bin_file:
            self._mmap = mmap(bin_file.fileno(), 0)
        self._file_dir = file_dir
        self._changes_made_during_session = []

    ########################
    ### INDIVIDUAL FILES ###
    ########################

    def _write_compressed_file(self, file_name, start_index, end_index):
        with open(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{file_name}{self._COMPRESSED_BIN_EXTENSION}", "wb+") as comp_file:
            comp_file.write(self._mmap[start_index:end_index])

    def _read_asm_address(self, asm_section):
        upper = self._read_byte_list_to_int(BOOTLOADER_ASSEMBLY_DICT[asm_section]["ROM_Offset_Upper"], 2)
        lower = self._read_byte_list_to_int(BOOTLOADER_ASSEMBLY_DICT[asm_section]["ROM_Offset_Lower"], 2)
        if(lower > 0x7FFF):
            upper -= 1
        address = upper * 0x10000 + lower
        return address

    def _extract_all_asm(self):
        # print("Extract By ASM Pointer")
        asm_pointer_address_dict = {}
        previous_asm_section = ""
        previous_address = None
        for asm_section in sorted(BOOTLOADER_ASSEMBLY_DICT):
            code_address = self._read_asm_address(asm_section)
            if(previous_address):
                data_address = self._find_int(0x117200, 3, start_index=previous_address+1, end_index=code_address)
                # print(f"Data Address: {self._int_to_hex_str(data_address)}")
                if(data_address < 0):
                    # print("Couldn't Find 1172 For ASM Data")
                    raise SystemError("Couldn't Find 1172 For ASM Data")
                self._write_compressed_file(self._int_to_hex_str(previous_address), previous_address, data_address)
                self._write_compressed_file(self._int_to_hex_str(data_address), data_address, code_address)
                asm_pointer_address_dict[BOOTLOADER_ASSEMBLY_DICT[previous_asm_section]["Name"]] = {
                    "Code": previous_address,
                    "Data": data_address,
                }
            previous_asm_section = asm_section
            previous_address = code_address
        data_address = self._find_int(0x117200, 3, start_index=previous_address+1, end_index=self._ASM_END)
        if(data_address < 0):
            # print("Couldn't Find 1172 For ASM Data")
            raise SystemError("Couldn't Find 1172 For ASM Data")
        self._write_compressed_file(self._int_to_hex_str(previous_address), previous_address, data_address)
        self._write_compressed_file(self._int_to_hex_str(data_address), data_address, self._ASM_END)
        asm_pointer_address_dict[BOOTLOADER_ASSEMBLY_DICT[asm_section]["Name"]] = {
            "Code": previous_address,
            "Data": data_address,
        }
        return asm_pointer_address_dict

    def _extract_by_asset_pointer(self, pointer):
        index_start = self._read_byte_list_to_int(pointer, 4) + self._ASSET_TABLE_OFFSET
        index_end = self._read_byte_list_to_int(pointer + 0x8, 4) + self._ASSET_TABLE_OFFSET
        self._write_compressed_file(self._int_to_hex_str(pointer), index_start, index_end)

    def _write_asm_address(self, asm_section, new_address):
        upper = new_address // 0x10000
        lower = new_address % 0x10000
        if(lower > 0x7FFF):
            upper += 1
        self._write_bytes(BOOTLOADER_ASSEMBLY_DICT[asm_section]["ROM_Offset_Upper"], 2, upper)
        self._write_bytes(BOOTLOADER_ASSEMBLY_DICT[asm_section]["ROM_Offset_Lower"], 2, lower)

    def _insert_file_by_index(self, comp_content, index_start):
        for index_add, comp_byte in enumerate(comp_content):
            try:
                self._mmap[index_start + index_add] = comp_byte
            except Exception as e:
                raise e
        return index_start + index_add + 1

    def _add_trailing_padding(self, padding_address, padding=0xAA, padding_interval=0x8):
        while(padding_address % padding_interval != 0):
            self._mmap[padding_address] = padding
            padding_address += 1
        return padding_address

    def _insert_asm(self, curr_address, old_code_index_start, old_data_index_start):
        # print(f"Code Address: {self._int_to_hex_str(curr_address)}")
        with open(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._int_to_hex_str(old_code_index_start)}{self._COMPRESSED_BIN_EXTENSION}", "rb+") as code_comp_file:
            code_comp_content = code_comp_file.read()
        with open(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{self._int_to_hex_str(old_data_index_start)}{self._COMPRESSED_BIN_EXTENSION}", "rb+") as data_comp_file:
            data_comp_content = data_comp_file.read()
        data_address = self._insert_file_by_index(code_comp_content, curr_address)
        padding_address = self._insert_file_by_index(data_comp_content, data_address)
        next_address = self._add_trailing_padding(padding_address, padding=0x00, padding_interval=0x10)
        # print(f"Next Address: {self._int_to_hex_str(next_address)}")
        return next_address

    def _insert_by_asset_pointer(self, pointer):
        file_name = self._int_to_hex_str(pointer)
        index_start = self._read_byte_list_to_int(pointer, 4) + self._ASSET_TABLE_OFFSET
        with open(f"{self._file_dir}{self._EXTRACTED_FILES_DIR}{file_name}{self._COMPRESSED_BIN_EXTENSION}", "rb+") as comp_file:
            comp_content = comp_file.read()
        index_end = self._insert_file_by_index(comp_content, index_start)
        next_pointer_index = index_end - self._ASSET_TABLE_OFFSET
        return next_pointer_index

    def _skip_pointer(self, pointer):
        # print(f"Skip Pointer: {self._int_to_hex_str(pointer)}")
        pointer_index = self._read_byte_list_to_int(pointer, 4)
        self._write_bytes(pointer + 0x8, 4, pointer_index)

    def _adjust_asset_pointer(self, pointer, pointer_index):
        self._write_bytes(pointer, 4, pointer_index)
    
    ######################
    ### CRC CALCULATOR ###
    ######################
    
    def _unsigned_long(self, int_val):
        return int_val & 0xFFFFFFFF
    
    def _ROL(self, j, b):
        return self._unsigned_long(j << b) | (j >> (-b & 0x1F))

    def _int_of_4_byte_aligned_region(self, bytes, byteorder = 'big'):
        return int.from_bytes(bytes, byteorder = byteorder, signed = False)
    
    def _get_8_bit_ints_from_32_bit_int(self, int):
        return (int & 0xFF000000) >> 24, (int & 0xFF0000) >> 16, (int & 0xFF00) >> 8, int & 0xFF

    def _split_and_store_bytes(self, int_word, index, add_to_changes=False):
        ints = self._get_8_bit_ints_from_32_bit_int(int_word)
        changed_already = index in self._changes_made_during_session
        if add_to_changes:
            if not changed_already:
                self._changes_made_during_session.append(index)
        else:
            if changed_already:
                self._changes_made_during_session.pop(self._changes_made_during_session.index(index))
        index <<= 2
        for i in range(4):
            self._mmap[index + i] = ints[i]

    def _calculate_new_crc(self):
        check_part = self._mmap[0x1000:0x101000]
        t1 = t2 = t3 = t4 = t5 = t6 = self._CIC
        for i in range(0, len(check_part), 4):
            d = int.from_bytes(check_part[i:i+4], 'big', signed=False)
            t6d = self._unsigned_long(t6 + d)
            if(t6d < t6):
                t4 = self._unsigned_long(t4 + 1)
            t6 = t6d
            t3 ^= d
            r = self._ROL(d, d & 0x1F)
            t5 = self._unsigned_long(t5 + r)
            if(t2 > d):
                t2 ^= r
            else:
                t2 ^= t6 ^ d
            if(self._CIC == self._CIC_DICT['6105']):
                byte_place = self._HEADER_ITEMS['Boot Code'][0] + 0x0710 + (i & 0xFF)
                t1 = self._unsigned_long(t1 + (self._int_of_4_byte_aligned_region(self._mmap[byte_place:byte_place+4]) ^ d))
            else:
                t1 = self._unsigned_long(t1 + (t5 ^ d))
        if(self._CIC == self._CIC_DICT['6103']):
            crc1 = self._unsigned_long((t6 ^ t4) + t3)
            crc2 = self._unsigned_long((t5 ^ t2) + t1)
        elif(self._CIC == self._CIC_DICT['6106']):
            crc1 = self._unsigned_long((t6 * t4) + t3)
            crc2 = self._unsigned_long((t5 * t2) + t1)
        else:
            crc1 = t6 ^ t4 ^ t3
            crc2 = t5 ^ t2 ^ t1
        self._split_and_store_bytes(crc1, self._HEADER_ITEMS['CRC1'][0] >> 2)
        self._split_and_store_bytes(crc2, self._HEADER_ITEMS['CRC2'][0] >> 2)
        return crc1, crc2

    def _set_new_crc(self, crc1, crc2):
        self._write_bytes(0x10, 4, crc1)
        self._write_bytes(0x14, 4, crc2)

    ##########################
    ### BIG CHUNGY WUNGIES ###
    ##########################

    def _extract_pointer_table_assets(self, pointer_start, pointer_end):
        for pointer in range(pointer_start, pointer_end+1, 0x8):
            self._extract_by_asset_pointer(pointer)

    def _insert_pointer_table_assets(self, pointer_start, pointer_end, skip_pointer_list=[]):
        for pointer in range(pointer_start, pointer_end+1, 0x8):
            if(pointer in skip_pointer_list):
                self._skip_pointer(pointer)
            else:
                next_pointer_index = self._insert_by_asset_pointer(pointer)
                if(pointer < 0x10CB0):
                    self._adjust_asset_pointer(pointer + 0x8, next_pointer_index)
    
    def _adjust_crc(self):
        crc1, crc2 = self._calculate_new_crc()
        self._set_new_crc(crc1, crc2)

if __name__ == '__main__':
    from shutil import copy
    FILE_DIR = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/"
    FILE_NAME = "Banjo-Kazooie"
    NEW_FILE_NAME = "Banjo-Kazooie-NEW"
    copy(FILE_DIR + FILE_NAME + ".z64", FILE_DIR + NEW_FILE_NAME + ".z64")
    bk_rom_obj = BK_ROM_CLASS(FILE_DIR, NEW_FILE_NAME)
    # bk_rom_obj._extract_pointer_table_assets(0x74E0, 0x9770)
    # bk_rom_obj._insert_pointer_table_assets(0x74E0, 0x9770, [])
    bk_rom_obj._extract_by_asm_pointer()