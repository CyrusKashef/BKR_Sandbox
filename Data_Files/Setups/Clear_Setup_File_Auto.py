import sys
sys.path.append(".")

from Data_Files.Setups.Object_Dicts import *

list_path = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Data_Files/Setups/Clear_Setup_File_Lists.py"

complex_list = []
simple_list = []

# Complex
for item in ACTOR_OBJECT_DICT:
    target = ACTOR_OBJECT_DICT[item]
    if(target not in complex_list):
        complex_list.append(target)
for item in TIMED_OBJECT_DICT:
    target = TIMED_OBJECT_DICT[item]
    if(target not in complex_list):
        complex_list.append(target)
for item in RADIUS_OBJECT_ID_DICT:
    target = RADIUS_OBJECT_ID_DICT[item]
    if(target not in complex_list):
        complex_list.append(target)
for category in RADIUS_ASSOCIATED_ID_DICT:
    for item in RADIUS_ASSOCIATED_ID_DICT[category]:
        target = RADIUS_ASSOCIATED_ID_DICT[category][item]
        if(target not in complex_list):
            complex_list.append(target)
for item in MISC_OBJECT_DICT:
    target = MISC_OBJECT_DICT[item]
    if(target not in complex_list):
        complex_list.append(target)
# Simple
for item in SPRITE_OBJECT_DICT:
    target = SPRITE_OBJECT_DICT[item]
    if(target not in simple_list):
        simple_list.append(target)
for item in STATIC_OBJECT_DICT:
    target = STATIC_OBJECT_DICT[item]
    if(target not in simple_list):
        simple_list.append(target)

with open(list_path, "w+") as f:
    f.write("from numpy import array\n\n")
    f.write("CLEAR_SETUP_FILE_COMPLEX_LIST = array([\n")
    for item in complex_list:
        f.write(f'\t"{item}",\n')
    f.write("])\n\n")
    f.write("CLEAR_SETUP_FILE_SIMPLE_LIST = array([\n")
    for item in simple_list:
        f.write(f'\t"{item}",\n')
    f.write("])")