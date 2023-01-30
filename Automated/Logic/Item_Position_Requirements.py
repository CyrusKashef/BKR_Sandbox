from Data_Files.Enums import Move_Enums, Room_Enums, Area_Enums

##################################################################
######################### FLOATING ITEMS #########################
##################################################################

FLOATING_ITEMS_DICT = {
    #######################
    ### Spiral Mountain ###
    #######################
	(Room_Enums.SM_MAIN, -7108, 1200, -3079): [ # Extra Life (Waterfall)
        [Area_Enums.SM_WATERFALL_ALCOVE],
		],
	(Room_Enums.SM_MAIN, 3656, 339, 6552): [ # Extra Life (Banjos House)
        [Area_Enums.SM_HOUSE_ROOF, Move_Enums.FLAP_FLIP],
		],
	(Room_Enums.SM_MAIN, -6725, 1300, -1803): [ # Empty Honeycomb (Waterfall)
        [Area_Enums.SM_WATERFALL_ALCOVE, Move_Enums.HIGH_JUMP, Move_Enums.FEATHERY_FLAP],
        [Area_Enums.SM_WATERFALL_ALCOVE, Move_Enums.TALON_TROT],
		],
	(Room_Enums.SM_MAIN, -2752, 1299, 37): [ # Empty Honeycomb (Tree)
        [Area_Enums.SM_TREE_NEAR_SWIM],
		],
	(Room_Enums.SM_MAIN, -1400, 99, 4824): [ # Empty Honeycomb (Stump)
        [Area_Enums.SM_STUMP_UP_RIGHT],
		],
	(Room_Enums.SM_MAIN, -264, -442, -651): [ # Empty Honeycomb (Underwater)
        [Area_Enums.SM_SPIRAL_MOAT],
		],
	(Room_Enums.SM_MAIN, -2336, 302, 973): [ # Bottles Mound (Swim)
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, -1999, 342, -2545): [ # Bottles Mound (Climb)
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, -164, -190, 3313): [ # Bottles Mound (Jump)
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 0, 1800, 0): [ # Bottles Mound (Top Of SM)
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 2250, -34, 2774): [ # Bottles Mound (Camera)
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 3271, -110, -2673): [ # Bottles Mound (Beak Barge)
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 3802, -500, 5259): [ # Bottles Mound (Start)
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 4675, 400, 511): [ # Bottles Mound (Attack)
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, -934, -190, 2995): [ # SM Yellow/Blue Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, -861, -190, 3035): [ # SM Yellow/Blue Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, -472, -188, 3028): [ # SM Yellow/Blue Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 210, -190, 3060): [ # SM Yellow/Blue Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 191, -188, 3157): [ # SM Yellow/Blue Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 273, -190, 3077): [ # SM Yellow/Blue Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 477, -190, 3048): [ # SM Yellow/Blue Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 550, -190, 3078): [ # SM Yellow/Blue Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 2095, -24, 2739): [ # SM Yellow/Blue Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, -820, -190, 2970): [ # SM Yellow Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, -395, -184, 3052): [ # SM Yellow Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 861, -189, 3058): [ # SM Yellow Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, -517, -190, 3068): [ # SM Purple Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, -431, -190, 3246): [ # SM Purple Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 787, -190, 3113): [ # SM Purple Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 2064, -21, 2966): [ # SM Purple Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 2326, -73, 3028): [ # SM Purple Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 2236, -73, 3136): [ # SM Purple Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, -407, -190, 3373): [ # SM Blue Flower
        [Area_Enums.SM_MAIN],
		],
	(Room_Enums.SM_MAIN, 2109, -40, 3063): [ # SM Blue Flower
        [Area_Enums.SM_MAIN],
		],
    #######################
    ### Mumbos Mountain ###
    #######################
	(Room_Enums.MM_MAIN, -5926, 200, 6213): [ # Bottles Mound (Eggs)
        [Area_Enums.MM_EGG_FIRING],
		],
	(Room_Enums.MM_MAIN, -4126, 145, 4566): [ # Orange (Congas Tree)
        [Area_Enums.MM_MAIN, Move_Enums.CLIMB],
		],
	(Room_Enums.MM_MAIN, -4431, 475, 6183): [ # Mumbo Token (Near Conga)
        [Area_Enums.MM_STUMP_TO_WITCH_SWITCH_2],
		],
	(Room_Enums.MM_MAIN, -4869, 2255, -2506): [ # Mumbo Token (Stonehenge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 5855, 0, 2169): [ # Mumbo Token (Pink Jinjo)
        [Area_Enums.MM_PINK_JINJO],
		],
	(Room_Enums.MM_MAIN, 5150, 2168, -2447): [ # Mumbo Token (Mumbos Skull)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -4060, 1355, 1092): [ # Yellow Jinjo
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -3699, 2438, -2113): [ # Jiggy (Stonehenge)
        [Area_Enums.MM_STONEHENGE_JIGGY],
		],
	(Room_Enums.MM_MAIN, 373, 4221, -906): [ # Jiggy (Tickers Tower)
        [Area_Enums.MM_ATOP_TICKERS_TOWER, Move_Enums.HIGH_JUMP],
        [Area_Enums.MM_ATOP_TICKERS_TOWER, Move_Enums.FLAP_FLIP],
        [Area_Enums.MM_ATOP_TICKERS_TOWER, Move_Enums.TALON_TROT],
        [Area_Enums.MM_ATOP_TICKERS_TOWER, Move_Enums.TERMITE_BK],
		],
	(Room_Enums.MM_MAIN, 4335, 1485, 794): [ # Jiggy (Slope Hill)
        [Area_Enums.MM_MAIN, Move_Enums.HIGH_JUMP],
        [Area_Enums.MM_MAIN, Move_Enums.FLAP_FLIP],
        [Area_Enums.MM_MAIN, Move_Enums.TALON_TROT],
        [Area_Enums.MM_MAIN, Move_Enums.TERMITE_BK],
		],
	(Room_Enums.MM_MAIN, 5580, 2756, -2708): [ # Jiggy (Mumbos Skull)
        [Area_Enums.MM_ATOP_MUMBOS_SKULL],
		],
	(Room_Enums.MM_MAIN, -3297, 2755, -1421): [ # Orange Jinjo
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -2550, 2255, -1217): [ # Bottles Mound (Talon Trot)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 985, 484, 1681): [ # Empty Honeycomb
        [Area_Enums.MM_EMPTY_HONEYCOMB_ALCOVE],
		],
	(Room_Enums.MM_MAIN, 4302, 2900, -1490): [ # Empty Honeycomb
        [Area_Enums.MM_JUJU_PLATFORM, Move_Enums.EGG_FIRING, Move_Enums.FLAP_FLIP],
		],
	(Room_Enums.MM_MAIN, 223, 3563, -382): [ # Extra Life
        [Area_Enums.MM_ATOP_TICKERS_TOWER],
		],
	(Room_Enums.MM_MAIN, 1702, -125, 2941): [ # Blue Jinjo
        [Area_Enums.MM_BLUE_JINJO],
		],
	(Room_Enums.MM_MAIN, 3943, 2155, -3422): [ # Bottles Mound (Beak Buster)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 5876, 299, 2369): [ # Pink Jinjo
        [Area_Enums.MM_MAIN, Move_Enums.FLAP_FLIP],
		],
	(Room_Enums.MM_MAIN, -5652, -199, 3685): [ # MM Blue Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -5718, -200, 3841): [ # MM Blue Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -5603, -214, 4757): [ # MM Blue Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -5229, -232, 5979): [ # MM Blue Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -2528, 0, 2410): [ # MM Blue Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1718, 0, 4296): [ # MM Blue Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -863, 50, 2488): [ # MM Blue Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -122, 5, 4544): [ # MM Blue Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 647, 43, 3414): [ # MM Blue Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -5277, 836, 1850): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -5185, 837, 1737): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -5099, 836, 1850): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -5238, 1489, 560): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -5154, 1489, 462): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -5068, 1489, 560): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -4497, 393, 2503): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -4583, 393, 2600): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -4417, 393, 2600): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -4260, 1839, 208): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -4342, 1839, 300): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -4179, 1839, 300): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -4649, 2755, -2009): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -4599, 2754, -2261): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -4542, 2755, -2495): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -4359, 2755, -2682): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -4161, 2755, -2858): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -4416, 2755, -1509): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -4539, 2755, -1746): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -4167, 2755, -1383): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -3730, 782, 1838): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -3624, 782, 1908): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -3776, 782, 1964): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -3394, 1910, 171): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -3293, 1910, 247): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -3469, 1910, 263): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -3053, 1397, 905): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -3885, 2755, -2901): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -3047, 2755, -2669): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -3603, 2755, -2923): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -3314, 2755, -2802): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -3892, 2755, -1284): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -3581, 2755, -1359): [ # Note (Stonehenge)
        [Area_Enums.MM_ATOP_STONEHENGE],
		],
	(Room_Enums.MM_MAIN, -2962, 1397, 813): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -2868, 1397, 890): [ # Note (Slope Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1518, 964, 706): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1523, 857, 932): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1523, 742, 1179): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1528, 638, 1424): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1497, 517, 1621): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1431, 346, 1784): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1373, 169, 1957): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1541, 1987, -1960): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1309, 1856, -1941): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1094, 1727, -1922): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1413, 1117, 500): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1284, 1295, 363): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1758, 2111, -1974): [ # Note (Staircase)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 850, -824, 2267): [ # Note (Underwater)
        [Area_Enums.MM_UNDERWATER],
		],
	(Room_Enums.MM_MAIN, 940, -824, 2223): [ # Note (Underwater)
        [Area_Enums.MM_UNDERWATER],
		],
	(Room_Enums.MM_MAIN, 854, -8, 3800): [ # Note (Bridge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 1027, -824, 2183): [ # Note (Underwater)
        [Area_Enums.MM_UNDERWATER],
		],
	(Room_Enums.MM_MAIN, 1937, -824, 2136): [ # Note (Underwater)
        [Area_Enums.MM_UNDERWATER],
		],
	(Room_Enums.MM_MAIN, 1149, -62, 3800): [ # Note (Bridge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 1441, -90, 3800): [ # Note (Bridge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 1721, -90, 3800): [ # Note (Bridge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 2034, -824, 2158): [ # Note (Underwater)
        [Area_Enums.MM_UNDERWATER],
		],
	(Room_Enums.MM_MAIN, 2128, -824, 2181): [ # Note (Underwater)
        [Area_Enums.MM_UNDERWATER],
		],
	(Room_Enums.MM_MAIN, 2012, -90, 3800): [ # Note (Bridge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 2298, -65, 3800): [ # Note (Bridge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 2585, -20, 3800): [ # Note (Bridge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3974, 747, 1411): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3793, 747, 1471): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3928, 747, 1522): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3202, 1247, 925): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3126, 1247, 1014): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3282, 1247, 1003): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3378, 2439, -2353): [ # Note (Huts)
        [Area_Enums.MM_ATOP_HUTS],
		],
	(Room_Enums.MM_MAIN, 3255, 2438, -1091): [ # Note (Huts)
        [Area_Enums.MM_ATOP_HUTS],
		],
	(Room_Enums.MM_MAIN, 3847, 2439, -715): [ # Note (Huts)
        [Area_Enums.MM_ATOP_HUTS],
		],
	(Room_Enums.MM_MAIN, 4782, 298, 1892): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 4867, 297, 1766): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 4971, 299, 1887): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 4137, 2439, -2649): [ # Note (Huts)
		],
	(Room_Enums.MM_MAIN, 5860, 1547, 62): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 5990, 1547, 169): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 5469, 1184, 549): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 5259, 1184, 656): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 5412, 1184, 681): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 5319, 2439, -1717): [ # Note (Huts)
        [Area_Enums.MM_ATOP_HUTS],
		],
	(Room_Enums.MM_MAIN, 5025, 2439, -814): [ # Note (Huts)
        [Area_Enums.MM_ATOP_HUTS],
		],
	(Room_Enums.MM_MAIN, 6430, 500, 1410): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 6546, 500, 1536): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 6310, 500, 1536): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 6098, 1547, 67): [ # Note (Sloped Ledge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -5967, 200, 5615): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_EGG_FIRING],
		],
	(Room_Enums.MM_MAIN, -5911, 200, 5764): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_EGG_FIRING],
		],
	(Room_Enums.MM_MAIN, -5927, 200, 5471): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_EGG_FIRING],
		],
	(Room_Enums.MM_MAIN, -5835, 201, 5896): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_EGG_FIRING],
		],
	(Room_Enums.MM_MAIN, -5858, 200, 5343): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_EGG_FIRING],
		],
	(Room_Enums.MM_MAIN, -5706, 200, 5962): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_EGG_FIRING],
		],
	(Room_Enums.MM_MAIN, -5732, 200, 5272): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_EGG_FIRING],
		],
	(Room_Enums.MM_MAIN, -5548, 200, 5984): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_EGG_FIRING],
		],
	(Room_Enums.MM_MAIN, -5061, 298, 6090): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_STUMP_TO_WITCH_SWITCH_1],
		],
	(Room_Enums.MM_MAIN, -4881, 299, 6135): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_STUMP_TO_WITCH_SWITCH_1],
		],
	(Room_Enums.MM_MAIN, -3827, 600, 5997): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_STUMP_TO_WITCH_SWITCH_3],
		],
	(Room_Enums.MM_MAIN, -3958, 600, 6084): [ # Blue Egg (Near Conga)
        [Area_Enums.MM_STUMP_TO_WITCH_SWITCH_3],
		],
	(Room_Enums.MM_MAIN, -2713, 2355, -2576): [ # Blue Egg (Stonehenge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -2743, 2355, -2538): [ # Blue Egg (Stonehenge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -2776, 2355, -2494): [ # Blue Egg (Stonehenge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -2811, 2355, -2445): [ # Blue Egg (Stonehenge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -2840, 2355, -2408): [ # Blue Egg (Stonehenge)
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -4033, 195, 4620): [ # Orange (2D)
        [Area_Enums.MM_MAIN, Move_Enums.CLIMB],
		],
	(Room_Enums.MM_MAIN, -4169, 196, 4631): [ # Orange (2D)
        [Area_Enums.MM_MAIN, Move_Enums.CLIMB],
		],
	(Room_Enums.MM_MAIN, -4055, 194, 4705): [ # Orange (2D)
        [Area_Enums.MM_MAIN, Move_Enums.CLIMB],
		],
	(Room_Enums.MM_MAIN, -4141, 203, 4715): [ # Orange (2D)
        [Area_Enums.MM_MAIN, Move_Enums.CLIMB],
		],
	(Room_Enums.MM_MAIN, -2470, 0, 2570): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -2795, 0, 2504): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1677, 0, 4430): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1276, 0, 4533): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -1225, 0, 4611): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -391, 4, 4604): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -160, 8, 4233): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 175, 5, 2905): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 575, 0, 3005): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 30, 1555, -2312): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 350, 1555, -2258): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 578, 1556, -2227): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 918, 1555, -2120): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 976, 1555, -2089): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 699, 1554, -1783): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 484, 1553, 910): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 570, 1554, 928): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 1023, 1555, -2051): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 1291, 1559, -668): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 1239, 1558, -598): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 1007, 1555, 733): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 1094, 1555, 777): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 1211, 1555, 646): [ # MM Orange Yellow Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -321, 1566, -2624): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -184, 1576, -2542): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -530, 1538, 902): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -278, 1555, 892): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, -191, 1555, 954): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 827, 1557, -162): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 427, 1560, 148): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 510, 1558, 40): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 246, 1555, 1041): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 13, 1555, 1077): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 1279, 1555, 322): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 2939, 0, 3042): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 2829, 21, 5284): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 2918, 42, 5379): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 2909, 19, 5185): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3488, 2, 2396): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3379, 2, 2489): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3106, 0, 3069): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3294, 1, 3089): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3868, 23, 4051): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3693, 24, 4165): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3992, 30, 4486): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3035, 68, 5512): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3944, 47, 5615): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 3591, 2155, -3453): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 4443, 1, 2467): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 4204, 2155, -3319): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 5607, 4, 2858): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 5832, 0, 2815): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 6224, 16, 2530): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 6638, 10, 3342): [ # MM Red Flower
        [Area_Enums.MM_MAIN],
		],
	(Room_Enums.MM_MAIN, 983, -830, 3215): [ # Seashell
        [Area_Enums.MM_UNDERWATER],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, -343, 345, -518): [ # Mumbo Token
        [Area_Enums.MM_TT_SLOPE_LEDGE_1],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, -10, 817, -125): [ # Note
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, -80, 817, -71): [ # Note
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, -3, 817, 52): [ # Note
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, -74, 817, 19): [ # Note
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, 60, 817, -87): [ # Note
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, 67, 817, 0): [ # Note
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, -10, 1507, -125): [ # Blue Egg
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, -80, 1503, -71): [ # Blue Egg
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, -74, 1521, 19): [ # Blue Egg
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, -3, 1510, 52): [ # Blue Egg
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, 60, 1510, -87): [ # Blue Egg
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_INSIDE_TICKERS_TOWER, 67, 1510, 0): [ # Blue Egg
        [Area_Enums.MM_TT_UPPER_FLOORS],
		],
	(Room_Enums.MM_MUMBOS_SKULL, -127, 0, -308): [ # Note
        [Area_Enums.MM_MS_MAIN],
		],
	(Room_Enums.MM_MUMBOS_SKULL, -288, 0, -154): [ # Note
        [Area_Enums.MM_MS_MAIN],
		],
	(Room_Enums.MM_MUMBOS_SKULL, 119, 0, -298): [ # Note
        [Area_Enums.MM_MS_MAIN],
		],
	(Room_Enums.MM_MUMBOS_SKULL, 286, 0, -155): [ # Note
        [Area_Enums.MM_MS_MAIN],
		],
	(Room_Enums.MM_MUMBOS_SKULL, -131, 398, -496): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, -362, 378, -362): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, -487, 398, -146): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, -493, 398, 101): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, -352, 398, 371): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, -131, 398, 496): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, 136, 398, -499): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, 361, 379, -363): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, 498, 394, -129): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, 495, 398, 133): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, 359, 398, 362): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
	(Room_Enums.MM_MUMBOS_SKULL, 134, 379, 497): [ # Blue Egg
        [Area_Enums.MM_MS_SHELF],
		],
    ###########################
    ### Treasure Trove Cove ###
    ###########################
	(Room_Enums.TTC_MAIN, -6620, 510, 4621): [ # Mumbo Token
		],
	(Room_Enums.TTC_MAIN, -4932, 1122, -1063): [ # Mumbo Token
		],
	(Room_Enums.TTC_MAIN, -2646, 2447, -6223): [ # Mumbo Token
		],
	(Room_Enums.TTC_MAIN, -2660, 2447, -6079): [ # Mumbo Token
		],
	(Room_Enums.TTC_MAIN, -783, 745, -3872): [ # Mumbo Token
		],
	(Room_Enums.TTC_MAIN, -221, 2029, 929): [ # Mumbo Token
		],
	(Room_Enums.TTC_MAIN, 565, 6917, -2776): [ # Mumbo Token
		],
	(Room_Enums.TTC_MAIN, 2462, 2217, 2957): [ # Mumbo Token
		],
	(Room_Enums.TTC_MAIN, 6480, 597, -258): [ # Mumbo Token
		],
	(Room_Enums.TTC_MAIN, -5116, 1417, -3915): [ # Jiggy
		],
	(Room_Enums.TTC_MAIN, -2760, 2053, -4733): [ # Jiggy
		],
	(Room_Enums.TTC_MAIN, -1575, 2597, -2500): [ # Jiggy
		],
	(Room_Enums.TTC_MAIN, 479, 8500, -2709): [ # Jiggy
		],
	(Room_Enums.TTC_MAIN, 2832, 2152, -1797): [ # Jiggy
		],
	(Room_Enums.TTC_MAIN, -5626, 3112, -2856): [ # Orange Jinjo
		],
	(Room_Enums.TTC_MAIN, -4303, 46, 115): [ # Empty Honeycomb
		],
	(Room_Enums.TTC_MAIN, 8473, 844, -2684): [ # Empty Honeycomb
		],
	(Room_Enums.TTC_MAIN, -2442, 3158, -1706): [ # Extra Life
		],
	(Room_Enums.TTC_MAIN, 4710, 323, -6007): [ # Extra Life
		],
	(Room_Enums.TTC_MAIN, 5864, 677, 7898): [ # Extra Life
		],
	(Room_Enums.TTC_MAIN, -875, 242, 7206): [ # Blue Jinjo
		],
	(Room_Enums.TTC_MAIN, -288, 2161, 1314): [ # Bottles Mound (Flight)
		],
	(Room_Enums.TTC_MAIN, -179, 3062, 889): [ # Green Jinjo
		],
	(Room_Enums.TTC_MAIN, -968, 5358, -776): [ # Yellow Jinjo
		],
	(Room_Enums.TTC_MAIN, 2698, 1517, 3338): [ # Bottles Mound (Shock Spring Jump)
		],
	(Room_Enums.TTC_MAIN, 4848, 1340, -240): [ # Pink Jinjo
		],
	(Room_Enums.TTC_MAIN, 4539, 1792, 1639): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 4539, 1667, 1639): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 4539, 1917, 1639): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -6798, 2481, 789): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -6798, 2331, 789): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -6798, 2181, 789): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -6798, 2031, 789): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -5459, 1304, -1593): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -5143, 1304, -1663): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -5458, 1299, -1063): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -5221, 1301, -638): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -4932, 1302, -1550): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -4698, 1305, -1687): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -4316, 1303, -1315): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -4851, 1295, -600): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -4503, 1300, -781): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -4676, 1180, 2690): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -4629, 1182, 2849): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -4518, 1208, 2645): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -4464, 1211, 2796): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -3699, 1218, 4959): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -3533, 1246, 4908): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -3740, 1217, 4793): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -3579, 1244, 4757): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -2928, 1988, 6064): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -2928, 1838, 6064): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -2928, 1688, 6064): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -2928, 1538, 6064): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -2139, 1215, 6068): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -2133, 1215, 6239): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -1809, 1016, -6717): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -1705, 1016, -6686): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -1598, 1016, -6659): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -1488, 1015, -6631): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -1971, 1241, 6064): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -1963, 1246, 6220): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -29, 1241, 5979): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -100, 1215, 6130): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -243, 2164, 925): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -202, 2165, 965): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -253, 2164, 869): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -140, 2165, 955): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -213, 2164, 825): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -98, 2165, 915): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -153, 2164, 806): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -113, 2164, 852): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 115, 1244, 6037): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 55, 1214, 6194): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 1567, 1988, 5783): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 1567, 1838, 5783): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 1567, 1688, 5783): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 1567, 1538, 5783): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 2971, 1256, 6249): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 2822, 1254, 6170): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 2902, 1282, 6026): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 2530, 2926, -7242): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 2530, 2776, -7242): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 2530, 2626, -7242): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 2530, 2476, -7242): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3686, 737, -3327): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3753, 737, -3322): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3674, 737, -3267): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3747, 737, -3261): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3664, 738, -3202): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3659, 745, -3143): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3742, 737, -3188): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3732, 738, -3131): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3676, 1917, -387): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3676, 1792, -387): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3676, 1667, -387): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3907, 1256, 5720): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3932, 1255, 5555): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3743, 1282, 5690): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3765, 1286, 5534): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 3044, 1284, 6092): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 4879, 1299, 2666): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 4933, 1326, 2828): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 4644, 1328, 3634): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 4538, 1324, 3517): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 4519, 1297, 3750): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 4411, 1299, 3623): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 4460, 1251, 4727): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 4401, 1279, 4566): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 4295, 1250, 4777): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 4254, 1278, 4616): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5431, 1241, -3787): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5296, 1237, -3869): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5344, 1210, -3637): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5204, 1212, -3733): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5502, 1213, -2815): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5614, 1240, -2691): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5381, 1214, -2701): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5499, 1242, -2580): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5691, 1238, -1723): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5553, 1210, -1816): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5609, 1240, -1587): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5462, 1212, -1677): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5555, 1299, 1831): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5437, 1327, 1709): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5426, 1297, 1944): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5323, 1325, 1813): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5082, 1325, 2777): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, 5040, 1299, 2619): [ # Red Feather
		],
	(Room_Enums.TTC_MAIN, -5154, 2470, -3256): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -5319, 2470, -2929): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -4413, 1412, -4482): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -4215, 1411, -4547): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -4051, 1190, 1706): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -4051, 1190, 1793): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -4749, 2470, -3780): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -4975, 2470, -3543): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -4410, 2470, -3814): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -4092, 2470, -3826): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -3978, 1312, -5163): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -3808, 1062, -5389): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -3580, 1062, -5526): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -3995, 1312, -4990): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -3976, 1054, 1750): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -3966, 1190, 1747): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -3882, 1190, 1795): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -3882, 1190, 1707): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -3957, 2470, -3586): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -2906, 1012, -6249): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -2941, 1011, -6045): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -1269, 5795, -2811): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -1147, 5822, -2700): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -1145, 5792, -2928): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -1037, 5818, -2802): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 720, 5819, -4297): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 869, 5820, -4332): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 750, 5791, -4131): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 918, 5793, -4172): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 687, 5822, -1177): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 843, 5819, -1172): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 857, 5793, -1336): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 689, 5794, -1347): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 864, 5826, -1874): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 648, 5857, -1874): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 743, 6580, -3494): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 944, 6625, -3436): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 1012, 5782, -2017): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 1077, 6667, -3226): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 2475, 5793, -2303): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 2357, 5791, -2182): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 2351, 5822, -2417): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, 2241, 5819, -2305): [ # Blue Egg
		],
	(Room_Enums.TTC_MAIN, -3001, 1840, -2007): [ # Note
		],
	(Room_Enums.TTC_MAIN, -3235, 1840, -1696): [ # Note
		],
	(Room_Enums.TTC_MAIN, -2906, 1840, -2329): [ # Note
		],
	(Room_Enums.TTC_MAIN, -2607, 1617, 3019): [ # Note
		],
	(Room_Enums.TTC_MAIN, -2548, 1617, 3217): [ # Note
		],
	(Room_Enums.TTC_MAIN, -2488, 1617, 3417): [ # Note
		],
	(Room_Enums.TTC_MAIN, -2638, 1617, 4933): [ # Note
		],
	(Room_Enums.TTC_MAIN, -2515, 1617, 4735): [ # Note
		],
	(Room_Enums.TTC_MAIN, -2760, 1617, 5135): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1147, 846, 6935): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1144, 846, 7476): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1055, 1490, 713): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1213, 1276, 665): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1364, 1084, 622): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1630, 1291, 2476): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1539, 1291, 2621): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1769, 1321, 2578): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1681, 1318, 2708): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1001, 2116, -6315): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1175, 2317, -6288): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1936, 2528, -6112): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1854, 2731, -5955): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1773, 2928, -5803): [ # Note
		],
	(Room_Enums.TTC_MAIN, -1691, 3130, -5647): [ # Note
		],
	(Room_Enums.TTC_MAIN, -603, 846, 6938): [ # Note
		],
	(Room_Enums.TTC_MAIN, -603, 846, 7478): [ # Note
		],
	(Room_Enums.TTC_MAIN, -85, 1313, -6564): [ # Note
		],
	(Room_Enums.TTC_MAIN, -263, 1516, -6564): [ # Note
		],
	(Room_Enums.TTC_MAIN, -653, 1713, -6370): [ # Note
		],
	(Room_Enums.TTC_MAIN, -826, 1913, -6343): [ # Note
		],
	(Room_Enums.TTC_MAIN, -734, 1915, 773): [ # Note
		],
	(Room_Enums.TTC_MAIN, -896, 1703, 753): [ # Note
		],
	(Room_Enums.TTC_MAIN, -319, 1617, 4160): [ # Note
		],
	(Room_Enums.TTC_MAIN, -520, 1617, 4172): [ # Note
		],
	(Room_Enums.TTC_MAIN, -719, 1617, 4183): [ # Note
		],
	(Room_Enums.TTC_MAIN, -569, 2131, 795): [ # Note
		],
	(Room_Enums.TTC_MAIN, -363, 6087, -2487): [ # Note
		],
	(Room_Enums.TTC_MAIN, -455, 6170, -2688): [ # Note
		],
	(Room_Enums.TTC_MAIN, -352, 6227, -2895): [ # Note
		],
	(Room_Enums.TTC_MAIN, 266, 911, -6564): [ # Note
		],
	(Room_Enums.TTC_MAIN, 86, 1117, -6563): [ # Note
		],
	(Room_Enums.TTC_MAIN, 414, 1916, 1000): [ # Note
		],
	(Room_Enums.TTC_MAIN, 603, 1702, 1027): [ # Note
		],
	(Room_Enums.TTC_MAIN, 788, 1486, 1082): [ # Note
		],
	(Room_Enums.TTC_MAIN, 966, 1289, 1138): [ # Note
		],
	(Room_Enums.TTC_MAIN, 417, 1291, 2891): [ # Note
		],
	(Room_Enums.TTC_MAIN, 251, 1292, 2927): [ # Note
		],
	(Room_Enums.TTC_MAIN, 448, 1318, 3052): [ # Note
		],
	(Room_Enums.TTC_MAIN, 297, 1321, 3090): [ # Note
		],
	(Room_Enums.TTC_MAIN, 688, 1617, 4709): [ # Note
		],
	(Room_Enums.TTC_MAIN, 700, 1617, 4907): [ # Note
		],
	(Room_Enums.TTC_MAIN, 713, 1617, 5104): [ # Note
		],
	(Room_Enums.TTC_MAIN, 222, 2132, 979): [ # Note
		],
	(Room_Enums.TTC_MAIN, 552, 8056, -2465): [ # Note
		],
	(Room_Enums.TTC_MAIN, 269, 8070, -2560): [ # Note
		],
	(Room_Enums.TTC_MAIN, 731, 8056, -2702): [ # Note
		],
	(Room_Enums.TTC_MAIN, 275, 8055, -2864): [ # Note
		],
	(Room_Enums.TTC_MAIN, 563, 8055, -2949): [ # Note
		],
	(Room_Enums.TTC_MAIN, 2660, 431, 4609): [ # Note
		],
	(Room_Enums.TTC_MAIN, 2497, 431, 4437): [ # Note
		],
	(Room_Enums.TTC_MAIN, 2497, 431, 4609): [ # Note
		],
	(Room_Enums.TTC_MAIN, 2497, 431, 4794): [ # Note
		],
	(Room_Enums.TTC_MAIN, 2318, 431, 4609): [ # Note
		],
	(Room_Enums.TTC_MAIN, 2911, 1917, 1203): [ # Note
		],
	(Room_Enums.TTC_MAIN, 2911, 1792, 1203): [ # Note
		],
	(Room_Enums.TTC_MAIN, 2911, 1667, 1203): [ # Note
		],
	(Room_Enums.TTC_MAIN, 2070, 2517, -2499): [ # Note
		],
	(Room_Enums.TTC_MAIN, 4499, 817, -7216): [ # Note
		],
	(Room_Enums.TTC_MAIN, 4631, 817, -7067): [ # Note
		],
	(Room_Enums.TTC_MAIN, 4646, 817, -6864): [ # Note
		],
	(Room_Enums.TTC_MAIN, 4656, 817, -6660): [ # Note
		],
	(Room_Enums.TTC_MAIN, 4858, 736, -2273): [ # Note
		],
	(Room_Enums.TTC_MAIN, 4783, 737, -2249): [ # Note
		],
	(Room_Enums.TTC_MAIN, 4802, 737, -2351): [ # Note
		],
	(Room_Enums.TTC_MAIN, 4803, 736, -2444): [ # Note
		],
	(Room_Enums.TTC_MAIN, 4730, 737, -2420): [ # Note
		],
	(Room_Enums.TTC_MAIN, 5670, 1817, -372): [ # Note
		],
	(Room_Enums.TTC_MAIN, 5682, 1817, 444): [ # Note
		],
	(Room_Enums.TTC_MAIN, 5447, 1817, 101): [ # Note
		],
	(Room_Enums.TTC_MAIN, 6244, 1817, -452): [ # Note
		],
	(Room_Enums.TTC_MAIN, 6498, 1817, 39): [ # Note
		],
	(Room_Enums.TTC_MAIN, 6246, 1817, 447): [ # Note
		],
	(Room_Enums.TTC_BLUBBERS, -145, -748, 221): [ # Blubber's Gold
		],
	(Room_Enums.TTC_BLUBBERS, 254, -748, -175): [ # Blubber's Gold
		],
	(Room_Enums.TTC_BLUBBERS, 610, -412, 31): [ # Mumbo Token
		],
	(Room_Enums.TTC_BLUBBERS, -870, -750, -60): [ # Note
		],
	(Room_Enums.TTC_BLUBBERS, -870, -750, -195): [ # Note
		],
	(Room_Enums.TTC_BLUBBERS, -871, -750, 198): [ # Note
		],
	(Room_Enums.TTC_BLUBBERS, -871, -750, 68): [ # Note
		],
	(Room_Enums.TTC_BLUBBERS, 870, -750, -64): [ # Note
		],
	(Room_Enums.TTC_BLUBBERS, 870, -746, -197): [ # Note
		],
	(Room_Enums.TTC_BLUBBERS, 870, -698, 200): [ # Note
		],
	(Room_Enums.TTC_BLUBBERS, 870, -750, 61): [ # Note
		],
	(Room_Enums.TTC_NIPPERS, 385, 227, 31): [ # Jiggy
		],
	(Room_Enums.TTC_NIPPERS, -127, -22, -1020): [ # Note
		],
	(Room_Enums.TTC_NIPPERS, -78, -21, 800): [ # Note
		],
	(Room_Enums.TTC_NIPPERS, -608, -21, 457): [ # Note
		],
	(Room_Enums.TTC_NIPPERS, 911, -22, -18): [ # Note
		],
	(Room_Enums.TTC_NIPPERS, 643, -22, -723): [ # Note
		],
	(Room_Enums.TTC_NIPPERS, 583, -21, 625): [ # Note
		],
	(Room_Enums.TTC_NIPPERS, -142, -23, 315): [ # Blue Egg
		],
	(Room_Enums.TTC_NIPPERS, -267, -23, 318): [ # Blue Egg
		],
	(Room_Enums.TTC_NIPPERS, -106, -23, 186): [ # Blue Egg
		],
	(Room_Enums.TTC_NIPPERS, -306, -23, 212): [ # Blue Egg
		],
	(Room_Enums.TTC_NIPPERS, -215, -23, 117): [ # Blue Egg
		],
	(Room_Enums.TTC_SANDCATLE, 0, 350, -987): [ # Jiggy
		],
	(Room_Enums.TTC_SANDCATLE, -536, -90, 727): [ # Note
		],
	(Room_Enums.TTC_SANDCATLE, -536, -90, 892): [ # Note
		],
	(Room_Enums.TTC_SANDCATLE, 537, -90, 727): [ # Note
		],
	(Room_Enums.TTC_SANDCATLE, 537, -90, 892): [ # Note
		],
    #######################
    ### Clankers Cavern ###
    #######################
	(Room_Enums.CC_MAIN, -9694, 5272, 1607): [ # Mumbo Token
		],
	(Room_Enums.CC_MAIN, 870, 2146, -3148): [ # Mumbo Token
		],
	(Room_Enums.CC_MAIN, 2028, 5456, 2344): [ # Mumbo Token
		],
	(Room_Enums.CC_MAIN, 9823, 4225, -19): [ # Mumbo Token
		],
	(Room_Enums.CC_MAIN, -4726, 5337, -110): [ # Yellow Jinjo
		],
	(Room_Enums.CC_MAIN, 90, 5962, -12): [ # Jiggy
		],
	(Room_Enums.CC_MAIN, 4629, 2151, 3082): [ # Jiggy
		],
	(Room_Enums.CC_MAIN, 10061, 5112, 3): [ # Jiggy
		],
	(Room_Enums.CC_MAIN, 1752, 5270, -2214): [ # Extra Life
		],
	(Room_Enums.CC_MAIN, 4570, 3727, 2783): [ # Extra Life
		],
	(Room_Enums.CC_MAIN, 7309, 4267, 2286): [ # Extra Life
		],
	(Room_Enums.CC_MAIN, 3718, 3311, 2519): [ # Empty Honeycomb
		],
	(Room_Enums.CC_MAIN, 7886, 4272, 1969): [ # Empty Honeycomb
		],
	(Room_Enums.CC_MAIN, 4326, 2146, -4080): [ # Blue Jinjo
		],
	(Room_Enums.CC_MAIN, 5017, -3085, -13): [ # Green Jinjo
		],
	(Room_Enums.CC_MAIN, 6138, 5087, 2637): [ # Orange Jinjo
		],
	(Room_Enums.CC_MAIN, -9112, 5243, -182): [ # Note
		],
	(Room_Enums.CC_MAIN, -8284, 5243, -911): [ # Note
		],
	(Room_Enums.CC_MAIN, -8573, 5244, -353): [ # Note
		],
	(Room_Enums.CC_MAIN, -7636, 5162, -1164): [ # Note
		],
	(Room_Enums.CC_MAIN, -7910, 5212, 804): [ # Note
		],
	(Room_Enums.CC_MAIN, -7038, 5212, 754): [ # Note
		],
	(Room_Enums.CC_MAIN, -6634, 5212, 238): [ # Note
		],
	(Room_Enums.CC_MAIN, -6065, 5211, 313): [ # Note
		],
	(Room_Enums.CC_MAIN, -2030, 2466, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, -2580, 2841, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, -1480, 2461, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, -930, 2437, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, -380, 2236, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 170, 2155, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 939, 5693, -17): [ # Note
		],
	(Room_Enums.CC_MAIN, 1533, 5693, 381): [ # Note
		],
	(Room_Enums.CC_MAIN, 1043, 5693, 377): [ # Note
		],
	(Room_Enums.CC_MAIN, 2240, 5262, -2473): [ # Note
		],
	(Room_Enums.CC_MAIN, 2036, 5693, -15): [ # Note
		],
	(Room_Enums.CC_MAIN, 3866, 1198, 2618): [ # Note
		],
	(Room_Enums.CC_MAIN, 3800, 4281, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 3500, 4269, 2): [ # Note
		],
	(Room_Enums.CC_MAIN, 3200, 4243, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 3013, 4827, 2477): [ # Note
		],
	(Room_Enums.CC_MAIN, 3013, 4437, 2477): [ # Note
		],
	(Room_Enums.CC_MAIN, 3013, 5117, 2477): [ # Note
		],
	(Room_Enums.CC_MAIN, 3013, 5407, 2477): [ # Note
		],
	(Room_Enums.CC_MAIN, 4220, -3085, -19): [ # Note
		],
	(Room_Enums.CC_MAIN, 4584, -3085, -906): [ # Note
		],
	(Room_Enums.CC_MAIN, 4583, -3085, 865): [ # Note
		],
	(Room_Enums.CC_MAIN, 4427, 1188, 2637): [ # Note
		],
	(Room_Enums.CC_MAIN, 4961, 1184, 2649): [ # Note
		],
	(Room_Enums.CC_MAIN, 4100, 4293, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 5469, -3085, -1273): [ # Note
		],
	(Room_Enums.CC_MAIN, 5468, -3085, 1225): [ # Note
		],
	(Room_Enums.CC_MAIN, 5417, 1184, 2626): [ # Note
		],
	(Room_Enums.CC_MAIN, 5881, 1184, 2600): [ # Note
		],
	(Room_Enums.CC_MAIN, 5300, 4209, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 5600, 4161, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 5899, 4106, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 5270, 5261, -2937): [ # Note
		],
	(Room_Enums.CC_MAIN, 6716, -3085, -18): [ # Note
		],
	(Room_Enums.CC_MAIN, 6361, -3085, -908): [ # Note
		],
	(Room_Enums.CC_MAIN, 6350, -3085, 866): [ # Note
		],
	(Room_Enums.CC_MAIN, 6804, 1184, 2361): [ # Note
		],
	(Room_Enums.CC_MAIN, 6342, 1184, 2485): [ # Note
		],
	(Room_Enums.CC_MAIN, 6200, 4072, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 6500, 4047, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 6800, 4063, 0): [ # Note
		],
	(Room_Enums.CC_MAIN, 6989, 4958, 2388): [ # Note
		],
	(Room_Enums.CC_MAIN, 6582, 5284, 2536): [ # Note
		],
	(Room_Enums.CC_MAIN, 6785, 5121, 2454): [ # Note
		],
	(Room_Enums.CC_MAIN, 7194, 4787, 2321): [ # Note
		],
	(Room_Enums.CC_MAIN, 7401, 4611, 2247): [ # Note
		],
	(Room_Enums.CC_MAIN, 8755, 4225, -1418): [ # Note
		],
	(Room_Enums.CC_MAIN, 8756, 4225, 1278): [ # Note
		],
	(Room_Enums.CC_MAIN, 9091, 4225, -1207): [ # Note
		],
	(Room_Enums.CC_MAIN, 9438, 4225, -978): [ # Note
		],
	(Room_Enums.CC_MAIN, 9636, 4225, -679): [ # Note
		],
	(Room_Enums.CC_MAIN, 9818, 4225, -377): [ # Note
		],
	(Room_Enums.CC_MAIN, 9818, 4225, 339): [ # Note
		],
	(Room_Enums.CC_MAIN, 9636, 4225, 630): [ # Note
		],
	(Room_Enums.CC_MAIN, 9449, 4225, 923): [ # Note
		],
	(Room_Enums.CC_MAIN, 9091, 4225, 1104): [ # Note
		],
	(Room_Enums.CC_MAIN, 13028, 3362, -761): [ # Note
		],
	(Room_Enums.CC_MAIN, 13540, 3362, -973): [ # Note
		],
	(Room_Enums.CC_MAIN, 13538, 3362, 931): [ # Note
		],
	(Room_Enums.CC_MAIN, 13018, 3362, 713): [ # Note
		],
	(Room_Enums.CC_MAIN, 14602, 3362, -732): [ # Note
		],
	(Room_Enums.CC_MAIN, 14096, 3362, -969): [ # Note
		],
	(Room_Enums.CC_MAIN, 14590, 3362, 702): [ # Note
		],
	(Room_Enums.CC_MAIN, 14105, 3361, 929): [ # Note
		],
	(Room_Enums.CC_MAIN, -9857, 5288, 555): [ # Gold Feather
		],
	(Room_Enums.CC_MAIN, -8657, 5288, 1757): [ # Gold Feather
		],
	(Room_Enums.CC_MAIN, 1891, 3662, -2142): [ # Gold Feather
		],
	(Room_Enums.CC_MAIN, 1779, 3662, -2076): [ # Gold Feather
		],
	(Room_Enums.CC_MAIN, 3767, 5266, -2911): [ # Gold Feather
		],
	(Room_Enums.CC_MAIN, 8408, 1194, -1531): [ # Gold Feather
		],
	(Room_Enums.CC_MAIN, 8058, 1194, -1801): [ # Gold Feather
		],
	(Room_Enums.CC_MAIN, -9431, 5241, 133): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, -8370, 5241, 1194): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, -5650, 5241, 662): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 2743, 5266, -2660): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 4772, 5266, -2939): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 7251, 1202, -212): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 7251, 1206, -212): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 7168, 1205, -463): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 7090, 1206, -710): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 7416, 1206, 280): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 7339, 1206, 30): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 8890, 5166, -122): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 8893, 5166, 82): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 9070, 5166, -220): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 9244, 5166, -119): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 9241, 5166, 83): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, 9068, 5166, 185): [ # Red Feather
		],
	(Room_Enums.CC_MAIN, -5274, 3269, -270): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, -5159, 3232, 178): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, -4392, 3051, -27): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, -4492, 3113, -449): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, -4937, 3221, -597): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, -4722, 3104, 299): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 1970, 3662, 1998): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 1895, 3662, 2117): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 2094, 3662, 1968): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 2293, 3662, 2354): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 2360, 3662, 2231): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 2329, 3662, 2107): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 2216, 3662, 2018): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 2588, 5456, 2596): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 2494, 5456, 2556): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 3854, 1202, -532): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 3692, 1202, -356): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 3529, 1202, -182): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 3369, 1207, -10): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 3206, 1202, 165): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 3247, 5262, -2842): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 4271, 5261, -2936): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 6785, 4876, 2454): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 6989, 4703, 2388): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 6379, 5087, 2586): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 6582, 5047, 2536): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 7194, 4526, 2321): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 14862, 3649, -17): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 14651, 3649, -20): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 14437, 3649, -20): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 14225, 3649, -20): [ # Blue Egg
		],
	(Room_Enums.CC_MAIN, 15075, 3648, -20): [ # Blue Egg
		],
	(Room_Enums.CC_BLOWHOLE, 10, -391, -2185): [ # Jiggy
		],
	(Room_Enums.CC_BLOWHOLE, 0, -425, -1390): [ # Note
		],
	(Room_Enums.CC_BLOWHOLE, 0, -425, -790): [ # Note
		],
	(Room_Enums.CC_BLOWHOLE, 0, -425, -190): [ # Note
		],
	(Room_Enums.CC_BLOWHOLE, 0, -425, 410): [ # Note
		],
	(Room_Enums.CC_BLOWHOLE, 0, -425, 1610): [ # Note
		],
	(Room_Enums.CC_BLOWHOLE, 0, -425, 1010): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, 532, 1424, 6632): [ # Mumbo Token
		],
	(Room_Enums.CC_BELLY_MOUTH, 3644, -474, 48): [ # Pink Jinjo
		],
	(Room_Enums.CC_BELLY_MOUTH, -2601, -8, -10): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, -2199, -351, -10): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, -1801, -493, -10): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, -1399, -539, -10): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, -998, -387, 0): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, -685, 990, 5391): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, -792, 1005, 6071): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, -566, 1015, 6712): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, 684, 999, 5391): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, 0, 1002, 5174): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, 780, 1004, 6071): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, 566, 1007, 6712): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, 0, 1008, 7036): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, 1600, 953, 20): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, 1999, 1241, 45): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, 2399, 1258, 45): [ # Note
		],
	(Room_Enums.CC_BELLY_MOUTH, -363, -62, -2032): [ # Red Feather
		],
	(Room_Enums.CC_BELLY_MOUTH, -363, -2, 2053): [ # Red Feather
		],
	(Room_Enums.CC_BELLY_MOUTH, 363, -62, -2033): [ # Red Feather
		],
	(Room_Enums.CC_BELLY_MOUTH, 363, -2, 2053): [ # Red Feather
		],
	(Room_Enums.CC_BELLY_MOUTH, -390, -160, -1300): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, -433, -214, -453): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, -476, -192, 480): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, -390, -116, 1316): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, 391, -160, -1300): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, 434, -214, -453): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, 476, -192, 480): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, 389, -116, 1316): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, 0, 2392, 5200): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, 0, 2293, 5276): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, 0, 2197, 5350): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, 0, 2099, 5425): [ # Blue Egg
		],
	(Room_Enums.CC_BELLY_MOUTH, -634, 1271, 1467): [ # Gold Feather
		],
	(Room_Enums.CC_BELLY_MOUTH, 0, 1630, -3050): [ # Gold Feather
		],
	(Room_Enums.CC_BELLY_MOUTH, 520, 1272, -1257): [ # Gold Feather
		],
	(Room_Enums.CC_BELLY_MOUTH, 637, 1272, 1003): [ # Gold Feather
		],
	(Room_Enums.CC_GOLD_FEATHER, -259, -500, 1413): [ # Bottles Mound (Wonderwing)
		],
	(Room_Enums.CC_GOLD_FEATHER, 0, -340, -1604): [ # Jiggy
		],
	(Room_Enums.CC_GOLD_FEATHER, -100, -471, -1629): [ # Gold Feather
		],
	(Room_Enums.CC_GOLD_FEATHER, -50, -471, -1629): [ # Gold Feather
		],
	(Room_Enums.CC_GOLD_FEATHER, 100, -471, -1630): [ # Gold Feather
		],
	(Room_Enums.CC_GOLD_FEATHER, 50, -471, -1630): [ # Gold Feather
		],
	(Room_Enums.CC_GOLD_FEATHER, 0, -471, -1630): [ # Gold Feather
		],
	(Room_Enums.CC_GOLD_FEATHER, 0, -500, -1335): [ # Note
		],
	(Room_Enums.CC_GOLD_FEATHER, 0, -500, -600): [ # Note
		],
	(Room_Enums.CC_GOLD_FEATHER, 0, -500, -20): [ # Note
		],
	(Room_Enums.CC_GOLD_FEATHER, 0, -500, 555): [ # Note
		],
	(Room_Enums.CC_GOLD_FEATHER, 0, -500, 1695): [ # Note
		],
	(Room_Enums.CC_GOLD_FEATHER, 0, -500, 1130): [ # Note
		],
    #########################
    ### Bubblegloop Swamp ###
    #########################
	(Room_Enums.BGS_MAIN, -6940, 1000, -5838): [ # Mumbo Token
		],
	(Room_Enums.BGS_MAIN, -3993, 1055, 1295): [ # Mumbo Token
		],
	(Room_Enums.BGS_MAIN, -1855, 0, 2835): [ # Mumbo Token
		],
	(Room_Enums.BGS_MAIN, 4278, 1400, -1302): [ # Mumbo Token
		],
	(Room_Enums.BGS_MAIN, 5049, 0, -5142): [ # Mumbo Token
		],
	(Room_Enums.BGS_MAIN, 5347, 0, -5055): [ # Mumbo Token
		],
	(Room_Enums.BGS_MAIN, 6546, 2992, -4697): [ # Mumbo Token
		],
	(Room_Enums.BGS_MAIN, -4382, 985, 2799): [ # Extra Life
		],
	(Room_Enums.BGS_MAIN, 7149, 0, -4353): [ # Extra Life
		],
	(Room_Enums.BGS_MAIN, -3061, 1146, -10052): [ # Blue Jinjo
		],
	(Room_Enums.BGS_MAIN, -3920, 1250, -7549): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -3920, 1350, -7549): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -3920, 1450, -7549): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 839, 1250, 2740): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 839, 1350, 2740): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 839, 1450, 2740): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -1606, 500, 2797): [ # Yellow Jinjo
		],
	(Room_Enums.BGS_MAIN, 1650, 1600, 1988): [ # Green Jinjo
		],
	(Room_Enums.BGS_MAIN, 4297, 100, 6286): [ # Bottles Mound (Stilt Stride)
		],
	(Room_Enums.BGS_MAIN, 5670, 0, -4158): [ # Pink Jinjo
		],
	(Room_Enums.BGS_MAIN, 5472, 0, 2853): [ # Orange Jinjo
		],
	(Room_Enums.BGS_MAIN, -8046, 991, -5201): [ # Note
		],
	(Room_Enums.BGS_MAIN, -8548, 991, -4204): [ # Note
		],
	(Room_Enums.BGS_MAIN, -8047, 991, -4700): [ # Note
		],
	(Room_Enums.BGS_MAIN, -8055, 991, -3200): [ # Note
		],
	(Room_Enums.BGS_MAIN, -8553, 991, -2207): [ # Note
		],
	(Room_Enums.BGS_MAIN, -7553, 991, -5702): [ # Note
		],
	(Room_Enums.BGS_MAIN, -7047, 985, -3702): [ # Note
		],
	(Room_Enums.BGS_MAIN, -6304, 992, -3449): [ # Note
		],
	(Room_Enums.BGS_MAIN, -6546, 992, -2193): [ # Note
		],
	(Room_Enums.BGS_MAIN, -6054, 992, -2704): [ # Note
		],
	(Room_Enums.BGS_MAIN, -6524, 1007, -4200): [ # Note
		],
	(Room_Enums.BGS_MAIN, -5548, 992, -2204): [ # Note
		],
	(Room_Enums.BGS_MAIN, -5293, 0, 3559): [ # Note
		],
	(Room_Enums.BGS_MAIN, -4920, 0, 3823): [ # Note
		],
	(Room_Enums.BGS_MAIN, -4017, 0, 3876): [ # Note
		],
	(Room_Enums.BGS_MAIN, -4544, 0, 4085): [ # Note
		],
	(Room_Enums.BGS_MAIN, -4105, 1450, -8802): [ # Note
		],
	(Room_Enums.BGS_MAIN, -4105, 1350, -8802): [ # Note
		],
	(Room_Enums.BGS_MAIN, -4105, 1250, -8802): [ # Note
		],
	(Room_Enums.BGS_MAIN, -3558, 0, -10911): [ # Note
		],
	(Room_Enums.BGS_MAIN, -3024, 0, -10719): [ # Note
		],
	(Room_Enums.BGS_MAIN, -3501, 0, 3668): [ # Note
		],
	(Room_Enums.BGS_MAIN, -2489, 0, -10528): [ # Note
		],
	(Room_Enums.BGS_MAIN, -2349, 0, -10049): [ # Note
		],
	(Room_Enums.BGS_MAIN, -2216, 0, -9596): [ # Note
		],
	(Room_Enums.BGS_MAIN, -1550, 652, -3828): [ # Note
		],
	(Room_Enums.BGS_MAIN, -1406, 517, -3718): [ # Note
		],
	(Room_Enums.BGS_MAIN, -1073, 318, -3495): [ # Note
		],
	(Room_Enums.BGS_MAIN, -1247, 405, -3608): [ # Note
		],
	(Room_Enums.BGS_MAIN, -1834, 92, -204): [ # Note
		],
	(Room_Enums.BGS_MAIN, -1591, 92, -179): [ # Note
		],
	(Room_Enums.BGS_MAIN, -1345, 92, -153): [ # Note
		],
	(Room_Enums.BGS_MAIN, -1006, 444, 3631): [ # Note
		],
	(Room_Enums.BGS_MAIN, -912, 347, -3385): [ # Note
		],
	(Room_Enums.BGS_MAIN, -74, 93, 920): [ # Note
		],
	(Room_Enums.BGS_MAIN, -82, 93, 720): [ # Note
		],
	(Room_Enums.BGS_MAIN, -68, 93, 1120): [ # Note
		],
	(Room_Enums.BGS_MAIN, -912, 479, 2851): [ # Note
		],
	(Room_Enums.BGS_MAIN, -862, 437, 2592): [ # Note
		],
	(Room_Enums.BGS_MAIN, -962, 524, 3114): [ # Note
		],
	(Room_Enums.BGS_MAIN, -984, 485, 3375): [ # Note
		],
	(Room_Enums.BGS_MAIN, 105, 93, -2559): [ # Note
		],
	(Room_Enums.BGS_MAIN, 287, 93, -2417): [ # Note
		],
	(Room_Enums.BGS_MAIN, 468, 93, -2275): [ # Note
		],
	(Room_Enums.BGS_MAIN, 207, 948, -2346): [ # Note
		],
	(Room_Enums.BGS_MAIN, 29, 899, -2061): [ # Note
		],
	(Room_Enums.BGS_MAIN, 587, 1023, -2412): [ # Note
		],
	(Room_Enums.BGS_MAIN, 847, 1049, -2243): [ # Note
		],
	(Room_Enums.BGS_MAIN, 228, 1101, 502): [ # Note
		],
	(Room_Enums.BGS_MAIN, 575, 1249, 703): [ # Note
		],
	(Room_Enums.BGS_MAIN, 918, 1200, 687): [ # Note
		],
	(Room_Enums.BGS_MAIN, 1161, 1099, -2187): [ # Note
		],
	(Room_Enums.BGS_MAIN, 1202, 1350, 656): [ # Note
		],
	(Room_Enums.BGS_MAIN, 2921, 93, -513): [ # Note
		],
	(Room_Enums.BGS_MAIN, 2261, 1075, -2275): [ # Note
		],
	(Room_Enums.BGS_MAIN, 2606, 1174, -2223): [ # Note
		],
	(Room_Enums.BGS_MAIN, 2904, 1125, -2136): [ # Note
		],
	(Room_Enums.BGS_MAIN, 2973, 1349, -237): [ # Note
		],
	(Room_Enums.BGS_MAIN, 2619, 1299, -284): [ # Note
		],
	(Room_Enums.BGS_MAIN, 2310, 1200, -229): [ # Note
		],
	(Room_Enums.BGS_MAIN, 2145, 1299, 442): [ # Note
		],
	(Room_Enums.BGS_MAIN, 2150, 1200, 54): [ # Note
		],
	(Room_Enums.BGS_MAIN, 3529, 93, -2607): [ # Note
		],
	(Room_Enums.BGS_MAIN, 3355, 93, -2460): [ # Note
		],
	(Room_Enums.BGS_MAIN, 3178, 93, -2312): [ # Note
		],
	(Room_Enums.BGS_MAIN, 3114, 93, -86): [ # Note
		],
	(Room_Enums.BGS_MAIN, 3020, 93, -304): [ # Note
		],
	(Room_Enums.BGS_MAIN, 3697, 176, 1632): [ # Note
		],
	(Room_Enums.BGS_MAIN, 3290, 1224, -1883): [ # Note
		],
	(Room_Enums.BGS_MAIN, 3425, 1200, -826): [ # Note
		],
	(Room_Enums.BGS_MAIN, 3308, 1299, -451): [ # Note
		],
	(Room_Enums.BGS_MAIN, 4793, 0, -4288): [ # Note
		],
	(Room_Enums.BGS_MAIN, 4789, 0, -4503): [ # Note
		],
	(Room_Enums.BGS_MAIN, 4351, 174, 955): [ # Note
		],
	(Room_Enums.BGS_MAIN, 4461, 168, 2373): [ # Note
		],
	(Room_Enums.BGS_MAIN, 5015, 0, -4288): [ # Note
		],
	(Room_Enums.BGS_MAIN, 5009, 0, -4507): [ # Note
		],
	(Room_Enums.BGS_MAIN, 5059, 170, 1758): [ # Note
		],
	(Room_Enums.BGS_MAIN, 7585, 0, -4798): [ # Note
		],
	(Room_Enums.BGS_MAIN, 7599, 0, -4481): [ # Note
		],
	(Room_Enums.BGS_MAIN, 7612, 0, -4165): [ # Note
		],
	(Room_Enums.BGS_MAIN, 7433, 0, -3931): [ # Note
		],
	(Room_Enums.BGS_MAIN, 7253, 0, -3699): [ # Note
		],
	(Room_Enums.BGS_MAIN, -7873, 1000, -6525): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -7591, 1000, -6568): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -7309, 1000, -6610): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -7017, 1000, -6552): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -6729, 1000, -6507): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -3403, 150, -761): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -3209, 150, -253): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -628, 0, -1744): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -404, 0, -1715): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -518, 0, -1728): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -427, 0, -1398): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -528, 0, -1380): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -635, 0, -1361): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 1889, 0, -3228): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 1497, 0, -3242): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 1501, 0, -3121): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 1857, 0, -3096): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 1506, 0, -3005): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 1813, 0, -2967): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4809, 0, -3711): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4814, 0, -3490): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4586, 0, -3710): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4592, 0, -3489): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4309, 100, 6025): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4368, 100, 6106): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4428, 100, 6198): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4484, 100, 6296): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4541, 100, 6389): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4343, 1400, -1422): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4412, 1400, -1304): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4208, 1400, -1422): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4342, 1400, -1184): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4207, 1400, -1184): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 4133, 1400, -1304): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 5917, 0, 2497): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 5705, 0, 2672): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 5087, 0, 3251): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, 5283, 0, 3047): [ # Blue Egg
		],
	(Room_Enums.BGS_MAIN, -5167, 1450, -7169): [ # Gold Feather
		],
	(Room_Enums.BGS_MAIN, -5167, 1350, -7169): [ # Gold Feather
		],
	(Room_Enums.BGS_MAIN, -5167, 1250, -7169): [ # Gold Feather
		],
	(Room_Enums.BGS_MAIN, -5180, 1004, -5816): [ # Gold Feather
		],
	(Room_Enums.BGS_MAIN, -3448, 150, -9796): [ # Gold Feather
		],
	(Room_Enums.BGS_MAIN, -35, 0, -582): [ # Gold Feather
		],
	(Room_Enums.BGS_MAIN, 901, 154, 2026): [ # Gold Feather
		],
	(Room_Enums.BGS_MAIN, 5551, 4, -5744): [ # Gold Feather
		],
	(Room_Enums.BGS_MAIN, 5854, 4, -5659): [ # Gold Feather
		],
	(Room_Enums.BGS_MAIN, -4250, 4, -2470): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, -4100, 4, -2470): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, -3950, 4, -2470): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 343, 1550, 5640): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 347, 1450, 5640): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 347, 1350, 5640): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 1879, 4, 1665): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 1855, 4, 1577): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 1830, 4, 1494): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 1504, 4, 1536): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 1399, 4, 1612): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 1300, 4, 1681): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 3929, 4, -1511): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 3826, 4, -1504): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 3919, 4, -1161): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 3813, 0, -1169): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 4045, 4, -1517): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 4012, 4, -1121): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 5947, 4, -5043): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 6141, 4, -5151): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 6252, 4, -4961): [ # Red Feather
		],
	(Room_Enums.BGS_MAIN, 6064, 4, -4843): [ # Red Feather
		],
	(Room_Enums.BGS_MR_VILE, 0, 300, -1754): [ # Mumbo Token
		],
	(Room_Enums.BGS_MR_VILE, -1189, 0, 0): [ # Blue Egg
		],
	(Room_Enums.BGS_MR_VILE, 1185, 0, 0): [ # Blue Egg
		],
	(Room_Enums.BGS_MR_VILE, -280, 125, -2070): [ # Note
		],
	(Room_Enums.BGS_MR_VILE, -219, 125, -1939): [ # Note
		],
	(Room_Enums.BGS_MR_VILE, -199, 125, -1810): [ # Note
		],
	(Room_Enums.BGS_MR_VILE, 280, 125, -2069): [ # Note
		],
	(Room_Enums.BGS_MR_VILE, 219, 125, -1941): [ # Note
		],
	(Room_Enums.BGS_MR_VILE, 200, 125, -1810): [ # Note
		],
	(Room_Enums.BGS_MR_VILE, -880, 4, -844): [ # Red Feather
		],
	(Room_Enums.BGS_MR_VILE, -880, 4, 912): [ # Red Feather
		],
	(Room_Enums.BGS_MR_VILE, 869, 4, -858): [ # Red Feather
		],
	(Room_Enums.BGS_MR_VILE, 881, 4, 922): [ # Red Feather
		],
	(Room_Enums.BGS_MR_VILE, 0, 4, 1274): [ # Gold Feather
		],
	(Room_Enums.BGS_TANKTUP, 0, 0, -1829): [ # Mumbo Token
		],
	(Room_Enums.BGS_TANKTUP, 0, 537, -1157): [ # Empty Honeycomb
		],
	(Room_Enums.BGS_TANKTUP, -1005, 0, -234): [ # Note
		],
	(Room_Enums.BGS_TANKTUP, -1022, 0, 0): [ # Note
		],
	(Room_Enums.BGS_TANKTUP, -1006, 0, 236): [ # Note
		],
	(Room_Enums.BGS_TANKTUP, 1005, 0, -236): [ # Note
		],
	(Room_Enums.BGS_TANKTUP, 1022, 0, 0): [ # Note
		],
	(Room_Enums.BGS_TANKTUP, 1006, 0, 235): [ # Note
		],
	(Room_Enums.BGS_TANKTUP, -150, 0, -1832): [ # Blue Egg
		],
	(Room_Enums.BGS_TANKTUP, -300, 0, -1831): [ # Blue Egg
		],
	(Room_Enums.BGS_TANKTUP, 300, 0, -1830): [ # Blue Egg
		],
	(Room_Enums.BGS_TANKTUP, 150, 0, -1829): [ # Blue Egg
		],
	(Room_Enums.BGS_MUMBOS_SKULL, 0, 0, -450): [ # Mumbo Token
		],
	(Room_Enums.BGS_MUMBOS_SKULL, 0, 600, 0): [ # Empty Honeycomb
		],
	(Room_Enums.BGS_MUMBOS_SKULL, -362, 383, -362): [ # Red Feather
		],
	(Room_Enums.BGS_MUMBOS_SKULL, -361, 402, 365): [ # Red Feather
		],
	(Room_Enums.BGS_MUMBOS_SKULL, 361, 383, -363): [ # Red Feather
		],
	(Room_Enums.BGS_MUMBOS_SKULL, 359, 402, 362): [ # Red Feather
		],
    ######################
    ### Freezeezy Peak ###
    ######################
	(Room_Enums.FP_MAIN, -7462, 250, 1324): [ # Bottles Mound (Beak Bomb)
		],
	(Room_Enums.FP_MAIN, -6851, 1193, 930): [ # Pink Jinjo
		],
	(Room_Enums.FP_MAIN, -5904, 260, 794): [ # Mumbo Token
		],
	(Room_Enums.FP_MAIN, -4527, 211, -803): [ # Mumbo Token
		],
	(Room_Enums.FP_MAIN, -4590, 350, 6344): [ # Mumbo Token
		],
	(Room_Enums.FP_MAIN, -2424, -168, -4235): [ # Mumbo Token
		],
	(Room_Enums.FP_MAIN, -1815, 4, -1019): [ # Mumbo Token
		],
	(Room_Enums.FP_MAIN, -793, 3020, 4389): [ # Mumbo Token
		],
	(Room_Enums.FP_MAIN, 634, 5, 769): [ # Mumbo Token
		],
	(Room_Enums.FP_MAIN, 1413, 18, 2802): [ # Mumbo Token
		],
	(Room_Enums.FP_MAIN, 5296, 2013, 2729): [ # Mumbo Token
		],
	(Room_Enums.FP_MAIN, -4450, 1591, -7407): [ # Extra Life
		],
	(Room_Enums.FP_MAIN, 6992, 1390, -3159): [ # Extra Life
		],
	(Room_Enums.FP_MAIN, -2588, 5684, 60): [ # Blue Jinjo
		],
	(Room_Enums.FP_MAIN, -1019, 5936, 2047): [ # Jiggy
		],
	(Room_Enums.FP_MAIN, 4295, 441, 1268): [ # Empty Honeycomb
		],
	(Room_Enums.FP_MAIN, 6083, 450, 2736): [ # Green Jinjo
		],
	(Room_Enums.FP_MAIN, -6630, 893, 900): [ # Note
		],
	(Room_Enums.FP_MAIN, -6190, 893, 899): [ # Note
		],
	(Room_Enums.FP_MAIN, -6409, 893, 900): [ # Note
		],
	(Room_Enums.FP_MAIN, -5971, 893, 900): [ # Note
		],
	(Room_Enums.FP_MAIN, -5579, 0, 6927): [ # Note
		],
	(Room_Enums.FP_MAIN, -5754, 0, 6022): [ # Note
		],
	(Room_Enums.FP_MAIN, -4394, 0, -1052): [ # Note
		],
	(Room_Enums.FP_MAIN, -4772, 0, -948): [ # Note
		],
	(Room_Enums.FP_MAIN, -4668, 0, -570): [ # Note
		],
	(Room_Enums.FP_MAIN, -4290, 0, -674): [ # Note
		],
	(Room_Enums.FP_MAIN, -4844, 0, 7451): [ # Note
		],
	(Room_Enums.FP_MAIN, -3705, 800, -4019): [ # Note
		],
	(Room_Enums.FP_MAIN, -3661, 800, -4459): [ # Note
		],
	(Room_Enums.FP_MAIN, -3920, 800, -4807): [ # Note
		],
	(Room_Enums.FP_MAIN, -3938, 800, -3704): [ # Note
		],
	(Room_Enums.FP_MAIN, -3430, 0, 6550): [ # Note
		],
	(Room_Enums.FP_MAIN, -3926, 0, 7284): [ # Note
		],
	(Room_Enums.FP_MAIN, -2176, 5, -559): [ # Note
		],
	(Room_Enums.FP_MAIN, -2337, 1669, -5188): [ # Note
		],
	(Room_Enums.FP_MAIN, -2704, 1958, -4154): [ # Note
		],
	(Room_Enums.FP_MAIN, -2000, 8492, 133): [ # Note
		],
	(Room_Enums.FP_MAIN, -1254, 5, -943): [ # Note
		],
	(Room_Enums.FP_MAIN, -1026, 5, -403): [ # Note
		],
	(Room_Enums.FP_MAIN, -1956, 5, -25): [ # Note
		],
	(Room_Enums.FP_MAIN, -1378, 5, 47): [ # Note
		],
	(Room_Enums.FP_MAIN, -1192, 2772, -4242): [ # Note
		],
	(Room_Enums.FP_MAIN, -1952, 2278, -3614): [ # Note
		],
	(Room_Enums.FP_MAIN, -1062, 4007, -4301): [ # Note
		],
	(Room_Enums.FP_MAIN, -1514, 5605, -99): [ # Note
		],
	(Room_Enums.FP_MAIN, -1046, 8503, -1179): [ # Note
		],
	(Room_Enums.FP_MAIN, -1804, 8434, -734): [ # Note
		],
	(Room_Enums.FP_MAIN, -1517, 8633, 860): [ # Note
		],
	(Room_Enums.FP_MAIN, -154, 5, 162): [ # Note
		],
	(Room_Enums.FP_MAIN, -515, 5, 629): [ # Note
		],
	(Room_Enums.FP_MAIN, -301, 4, 1176): [ # Note
		],
	(Room_Enums.FP_MAIN, -850, 0, 4201): [ # Note
		],
	(Room_Enums.FP_MAIN, -867, 578, 4693): [ # Note
		],
	(Room_Enums.FP_MAIN, -883, 1196, 5183): [ # Note
		],
	(Room_Enums.FP_MAIN, -900, 1727, 5675): [ # Note
		],
	(Room_Enums.FP_MAIN, -888, 1727, 6573): [ # Note
		],
	(Room_Enums.FP_MAIN, -843, 2725, 7475): [ # Note
		],
	(Room_Enums.FP_MAIN, -864, 2243, 7025): [ # Note
		],
	(Room_Enums.FP_MAIN, -615, 3247, -4985): [ # Note
		],
	(Room_Enums.FP_MAIN, -387, 3764, -3875): [ # Note
		],
	(Room_Enums.FP_MAIN, -820, 3149, 7926): [ # Note
		],
	(Room_Enums.FP_MAIN, -790, 3505, 8345): [ # Note
		],
	(Room_Enums.FP_MAIN, -631, 4267, -4977): [ # Note
		],
	(Room_Enums.FP_MAIN, -20, 4790, -3699): [ # Note
		],
	(Room_Enums.FP_MAIN, -140, 5225, -3101): [ # Note
		],
	(Room_Enums.FP_MAIN, -248, 5452, -2390): [ # Note
		],
	(Room_Enums.FP_MAIN, -353, 5101, -1787): [ # Note
		],
	(Room_Enums.FP_MAIN, -491, 5430, -1199): [ # Note
		],
	(Room_Enums.FP_MAIN, -583, 5605, -698): [ # Note
		],
	(Room_Enums.FP_MAIN, -941, 5605, 844): [ # Note
		],
	(Room_Enums.FP_MAIN, -195, 8574, -1023): [ # Note
		],
	(Room_Enums.FP_MAIN, -672, 8736, 1047): [ # Note
		],
	(Room_Enums.FP_MAIN, 426, 5, 244): [ # Note
		],
	(Room_Enums.FP_MAIN, 283, 4, 1246): [ # Note
		],
	(Room_Enums.FP_MAIN, 59, 3511, -4554): [ # Note
		],
	(Room_Enums.FP_MAIN, 42, 4530, -4557): [ # Note
		],
	(Room_Enums.FP_MAIN, 17, 5605, 266): [ # Note
		],
	(Room_Enums.FP_MAIN, 257, 8711, -275): [ # Note
		],
	(Room_Enums.FP_MAIN, 80, 8749, 591): [ # Note
		],
	(Room_Enums.FP_MAIN, 1892, 658, 6955): [ # Note
		],
	(Room_Enums.FP_MAIN, 2656, 658, 5687): [ # Note
		],
	(Room_Enums.FP_MAIN, 2271, 658, 6789): [ # Note
		],
	(Room_Enums.FP_MAIN, 2700, 658, 6100): [ # Note
		],
	(Room_Enums.FP_MAIN, 3763, 294, 320): [ # Note
		],
	(Room_Enums.FP_MAIN, 3505, 295, 679): [ # Note
		],
	(Room_Enums.FP_MAIN, 3467, 295, 1433): [ # Note
		],
	(Room_Enums.FP_MAIN, 3654, 295, 1906): [ # Note
		],
	(Room_Enums.FP_MAIN, 3865, 843, 3023): [ # Note
		],
	(Room_Enums.FP_MAIN, 3862, 844, 3237): [ # Note
		],
	(Room_Enums.FP_MAIN, 3860, 861, 3464): [ # Note
		],
	(Room_Enums.FP_MAIN, 4659, 840, -815): [ # Note
		],
	(Room_Enums.FP_MAIN, 4468, 844, -705): [ # Note
		],
	(Room_Enums.FP_MAIN, 4268, 865, -589): [ # Note
		],
	(Room_Enums.FP_MAIN, 4039, 294, 106): [ # Note
		],
	(Room_Enums.FP_MAIN, 4404, 294, 243): [ # Note
		],
	(Room_Enums.FP_MAIN, 4930, 294, 1918): [ # Note
		],
	(Room_Enums.FP_MAIN, 4559, 295, 2482): [ # Note
		],
	(Room_Enums.FP_MAIN, 4044, 295, 2411): [ # Note
		],
	(Room_Enums.FP_MAIN, -5280, -168, 5810): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -5069, -168, 6990): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -5424, -168, 6438): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -4753, -168, 5455): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -4112, -168, 5604): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -4440, -168, 7130): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -3128, -168, -4645): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -3887, -168, 6767): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -3753, -168, 6126): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -2165, -168, -5146): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -2367, -168, -5166): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -2552, -168, -5061): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -2759, -168, -4928): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -2939, -168, -4791): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -1979, -168, -5120): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -1897, -168, -4931): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -1824, -168, -4732): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -1758, -168, -4514): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -1734, 7166, -667): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -1961, 7227, 248): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -1465, 7354, 1066): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -948, 7201, -1175): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -33, 7313, -984): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 654, 18, -3169): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 404, 18, -2625): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 496, 7442, -179): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 278, 7505, 757): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 1410, 17, -2859): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 1185, 18, -2295): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 1545, 3505, 8981): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 1536, 3505, 9857): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 1606, 3505, 9635): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 1674, 3505, 9422): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, 1610, 3505, 9197): [ # Blue Egg
		],
	(Room_Enums.FP_MAIN, -5650, 229, -51): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -5651, 175, -200): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -5650, 69, -483): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -5649, 123, -341): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -5651, 278, 81): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -5651, 335, 237): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -5650, 384, 370): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -5649, 439, 521): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -5650, 493, 663): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -5650, 547, 813): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -4252, 4, 2800): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -4015, 4, 2389): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -3694, 4, 2325): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -3409, 4, 2537): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -3372, 4, 3060): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -2661, 1818, -4668): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -2409, 2113, -3722): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -1523, 1731, 5969): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -1513, 1731, 6305): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -1502, 2501, -3819): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -1184, 5609, -581): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -1421, 5609, 496): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -282, 1731, 5962): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -276, 1731, 6305): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -192, 3385, -4898): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -973, 3043, -4710): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -18, 3642, -4132): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -810, 3889, -3948): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -212, 4403, -4902): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -992, 4135, -4715): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -85, 4976, -3373): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -197, 5465, -2776): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -304, 5247, -2075): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -423, 5175, -1482): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -74, 5609, -344): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -540, 5601, -943): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -342, 5609, 757): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 852, -164, 2712): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 42, 4651, -4096): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 1735, -164, 2416): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 1195, -164, 2316): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 1944, -164, 2889): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 1060, -164, 3167): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 1602, -164, 3274): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 5809, 856, 2725): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 5617, 844, 2724): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 5425, 844, 2725): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, 6000, 881, 2726): [ # Red Feather
		],
	(Room_Enums.FP_MAIN, -5321, 1595, -6858): [ # Gold Feather
		],
	(Room_Enums.FP_MAIN, -4410, -164, 5536): [ # Gold Feather
		],
	(Room_Enums.FP_MAIN, -3463, 1595, -6865): [ # Gold Feather
		],
	(Room_Enums.FP_MAIN, -2217, 5962, -799): [ # Gold Feather
		],
	(Room_Enums.FP_MAIN, -2945, 5374, 971): [ # Gold Feather
		],
	(Room_Enums.FP_MAIN, -295, 6550, 913): [ # Gold Feather
		],
	(Room_Enums.FP_MAIN, -842, 6555, 1015): [ # Gold Feather
		],
	(Room_Enums.FP_MAIN, 859, 3936, 9450): [ # Gold Feather
		],
	(Room_Enums.FP_MAIN, 1582, 1004, -3792): [ # Gold Feather
		],
	(Room_Enums.FP_MAIN, 1606, 1004, -3741): [ # Gold Feather
		],
	(Room_Enums.FP_MAIN, 5126, 299, -2136): [ # Gold Feather
		],
	(Room_Enums.FP_IGLOO, 0, 10, -215): [ # Mumbo Token
		],
	(Room_Enums.FP_IGLOO, -150, 14, -149): [ # Red Feather
		],
	(Room_Enums.FP_IGLOO, -150, 14, 149): [ # Red Feather
		],
	(Room_Enums.FP_IGLOO, 150, 14, -150): [ # Red Feather
		],
	(Room_Enums.FP_IGLOO, 149, 14, 150): [ # Red Feather
		],
	(Room_Enums.FP_MUMBOS_SKULL, 0, 406, -511): [ # Yellow Jinjo
		],
	(Room_Enums.FP_MUMBOS_SKULL, -362, 379, -362): [ # Note
		],
	(Room_Enums.FP_MUMBOS_SKULL, -500, 398, 0): [ # Note
		],
	(Room_Enums.FP_MUMBOS_SKULL, -355, 398, 362): [ # Note
		],
	(Room_Enums.FP_MUMBOS_SKULL, 362, 378, -362): [ # Note
		],
	(Room_Enums.FP_MUMBOS_SKULL, 500, 387, 0): [ # Note
		],
	(Room_Enums.FP_MUMBOS_SKULL, 362, 398, 363): [ # Note
		],
	(Room_Enums.FP_TREE, -689, 600, -398): [ # Note
		],
	(Room_Enums.FP_TREE, -394, 600, -690): [ # Note
		],
	(Room_Enums.FP_TREE, -689, 600, 395): [ # Note
		],
	(Room_Enums.FP_TREE, -398, 600, 684): [ # Note
		],
	(Room_Enums.FP_TREE, -791, 600, 0): [ # Note
		],
	(Room_Enums.FP_TREE, 1, 600, -795): [ # Note
		],
	(Room_Enums.FP_TREE, 686, 600, -395): [ # Note
		],
	(Room_Enums.FP_TREE, 399, 600, -688): [ # Note
		],
	(Room_Enums.FP_TREE, 3, 600, 794): [ # Note
		],
	(Room_Enums.FP_TREE, 395, 600, 682): [ # Note
		],
	(Room_Enums.FP_TREE, 685, 600, 396): [ # Note
		],
	(Room_Enums.FP_TREE, 793, 600, 0): [ # Note
		],
	(Room_Enums.FP_TREE, -573, 1362, -4): [ # Red Feather
		],
	(Room_Enums.FP_TREE, -493, 1362, -288): [ # Red Feather
		],
	(Room_Enums.FP_TREE, -282, 1362, -498): [ # Red Feather
		],
	(Room_Enums.FP_TREE, -498, 1362, 285): [ # Red Feather
		],
	(Room_Enums.FP_TREE, -289, 1362, 490): [ # Red Feather
		],
	(Room_Enums.FP_TREE, 2, 1362, -570): [ # Red Feather
		],
	(Room_Enums.FP_TREE, 495, 1362, -285): [ # Red Feather
		],
	(Room_Enums.FP_TREE, 286, 1362, -494): [ # Red Feather
		],
	(Room_Enums.FP_TREE, 0, 1362, 570): [ # Red Feather
		],
	(Room_Enums.FP_TREE, 284, 1362, 495): [ # Red Feather
		],
	(Room_Enums.FP_TREE, 490, 1362, 286): [ # Red Feather
		],
	(Room_Enums.FP_TREE, 572, 1362, 0): [ # Red Feather
		],
	(Room_Enums.FP_TREE, -344, 2110, -200): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, -1, 2110, -399): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, -195, 2110, -343): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, -396, 2110, 0): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, -344, 2110, 198): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, -198, 2110, 347): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, 199, 2110, -346): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, 345, 2110, -199): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, 395, 2110, 1): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, 341, 2110, 196): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, 0, 2110, 393): [ # Blue Egg
		],
	(Room_Enums.FP_TREE, 199, 2110, 340): [ # Blue Egg
		],
	(Room_Enums.FP_WOZZAS, -7322, 0, 391): [ # Extra Life
		],
	(Room_Enums.FP_WOZZAS, -6531, 135, 422): [ # Empty Honeycomb
		],
	(Room_Enums.FP_WOZZAS, 629, 366, 859): [ # Orange Jinjo
		],
	(Room_Enums.FP_WOZZAS, -7119, 0, -113): [ # Blue Egg
		],
	(Room_Enums.FP_WOZZAS, -7166, 0, 926): [ # Blue Egg
		],
	(Room_Enums.FP_WOZZAS, -6559, 0, -291): [ # Blue Egg
		],
	(Room_Enums.FP_WOZZAS, -6599, 0, 1184): [ # Blue Egg
		],
	(Room_Enums.FP_WOZZAS, -7307, 0, 86): [ # Red Feather
		],
	(Room_Enums.FP_WOZZAS, -7331, 0, 686): [ # Red Feather
		],
	(Room_Enums.FP_WOZZAS, -6278, 0, -253): [ # Red Feather
		],
	(Room_Enums.FP_WOZZAS, -6270, 0, 1172): [ # Red Feather
		],
	(Room_Enums.FP_WOZZAS, -359, 15, -720): [ # Red Feather
		],
	(Room_Enums.FP_WOZZAS, -279, 15, -757): [ # Red Feather
		],
	(Room_Enums.FP_WOZZAS, -314, 10, 747): [ # Red Feather
		],
	(Room_Enums.FP_WOZZAS, -234, 13, 766): [ # Red Feather
		],
	(Room_Enums.FP_WOZZAS, 775, 8, -264): [ # Red Feather
		],
	(Room_Enums.FP_WOZZAS, 807, 8, -172): [ # Red Feather
		],
	(Room_Enums.FP_WOZZAS, -6854, 0, -244): [ # Gold Feather
		],
	(Room_Enums.FP_WOZZAS, -6918, 0, 1109): [ # Gold Feather
		],
	(Room_Enums.FP_WOZZAS, 758, 391, 894): [ # Gold Feather
		],
	(Room_Enums.FP_WOZZAS, 637, 391, 987): [ # Gold Feather
		],
    ####################
    ### Gobis Valley ###
    ####################
	(Room_Enums.GV_MAIN, -8948, 1332, 5500): [ # Extra Life
		],
	(Room_Enums.GV_MAIN, -230, 4820, -4421): [ # Extra Life
		],
	(Room_Enums.GV_MAIN, -6445, 2831, -822): [ # Bottles Mound (Turbo Talon Trot)
		],
	(Room_Enums.GV_MAIN, -5386, 1420, 10034): [ # Mumbo Token
		],
	(Room_Enums.GV_MAIN, -2149, 3340, 5867): [ # Mumbo Token
		],
	(Room_Enums.GV_MAIN, -230, 2843, -3091): [ # Mumbo Token
		],
	(Room_Enums.GV_MAIN, 91, 535, -860): [ # Mumbo Token
		],
	(Room_Enums.GV_MAIN, 64, 3484, 400): [ # Mumbo Token
		],
	(Room_Enums.GV_MAIN, 58, 535, 1570): [ # Blue Jinjo
		],
	(Room_Enums.GV_MAIN, 3067, 447, 10270): [ # Yellow Jinjo
		],
	(Room_Enums.GV_MAIN, 4952, 2538, 439): [ # Green Jinjo
		],
	(Room_Enums.GV_MAIN, -7082, 2372, 1091): [ # Note
		],
	(Room_Enums.GV_MAIN, -7105, 2371, 1247): [ # Note
		],
	(Room_Enums.GV_MAIN, -7123, 2371, 1404): [ # Note
		],
	(Room_Enums.GV_MAIN, -7148, 2371, 1568): [ # Note
		],
	(Room_Enums.GV_MAIN, -7178, 2372, 1754): [ # Note
		],
	(Room_Enums.GV_MAIN, -6724, 1233, 7210): [ # Note
		],
	(Room_Enums.GV_MAIN, -6367, 1281, 7928): [ # Note
		],
	(Room_Enums.GV_MAIN, -6046, 1329, 8619): [ # Note
		],
	(Room_Enums.GV_MAIN, -5385, 1780, -2843): [ # Note
		],
	(Room_Enums.GV_MAIN, -5713, 1379, 9342): [ # Note
		],
	(Room_Enums.GV_MAIN, -4958, 1781, -2855): [ # Note
		],
	(Room_Enums.GV_MAIN, -4541, 1780, -2871): [ # Note
		],
	(Room_Enums.GV_MAIN, -4116, 1780, -2895): [ # Note
		],
	(Room_Enums.GV_MAIN, -4276, 1402, 8984): [ # Note
		],
	(Room_Enums.GV_MAIN, -4829, 1415, 9510): [ # Note
		],
	(Room_Enums.GV_MAIN, -3026, 1781, -5048): [ # Note
		],
	(Room_Enums.GV_MAIN, -3017, 1781, -5496): [ # Note
		],
	(Room_Enums.GV_MAIN, -3028, 1781, -4591): [ # Note
		],
	(Room_Enums.GV_MAIN, -3037, 1781, -4148): [ # Note
		],
	(Room_Enums.GV_MAIN, -3054, 1781, -3695): [ # Note
		],
	(Room_Enums.GV_MAIN, -3752, 1781, -3161): [ # Note
		],
	(Room_Enums.GV_MAIN, -3401, 1780, -3430): [ # Note
		],
	(Room_Enums.GV_MAIN, -3083, 1666, 5488): [ # Note
		],
	(Room_Enums.GV_MAIN, -3096, 1664, 5106): [ # Note
		],
	(Room_Enums.GV_MAIN, -3035, 1663, 6675): [ # Note
		],
	(Room_Enums.GV_MAIN, -3048, 1665, 6316): [ # Note
		],
	(Room_Enums.GV_MAIN, -3165, 1378, 7933): [ # Note
		],
	(Room_Enums.GV_MAIN, -3720, 1390, 8460): [ # Note
		],
	(Room_Enums.GV_MAIN, -2098, 1830, -785): [ # Note
		],
	(Room_Enums.GV_MAIN, -2100, 1830, 112): [ # Note
		],
	(Room_Enums.GV_MAIN, -2111, 1830, 1016): [ # Note
		],
	(Room_Enums.GV_MAIN, -2814, 1605, 5292): [ # Note
		],
	(Room_Enums.GV_MAIN, -2776, 1606, 6486): [ # Note
		],
	(Room_Enums.GV_MAIN, -1182, 535, 457): [ # Note
		],
	(Room_Enums.GV_MAIN, -1455, 1830, -1432): [ # Note
		],
	(Room_Enums.GV_MAIN, -1289, 1259, 7119): [ # Note
		],
	(Room_Enums.GV_MAIN, -1168, 3324, -3242): [ # Note
		],
	(Room_Enums.GV_MAIN, -908, 535, -472): [ # Note
		],
	(Room_Enums.GV_MAIN, -807, 535, 1318): [ # Note
		],
	(Room_Enums.GV_MAIN, -584, 894, 7778): [ # Note
		],
	(Room_Enums.GV_MAIN, -251, 697, 8089): [ # Note
		],
	(Room_Enums.GV_MAIN, -800, 1830, -2068): [ # Note
		],
	(Room_Enums.GV_MAIN, -935, 1082, 7449): [ # Note
		],
	(Room_Enums.GV_MAIN, -464, 2770, 1610): [ # Note
		],
	(Room_Enums.GV_MAIN, -464, 2170, 2305): [ # Note
		],
	(Room_Enums.GV_MAIN, -828, 3821, -3580): [ # Note
		],
	(Room_Enums.GV_MAIN, -489, 4316, -4946): [ # Note
		],
	(Room_Enums.GV_MAIN, 928, 535, 1291): [ # Note
		],
	(Room_Enums.GV_MAIN, 88, 460, 8403): [ # Note
		],
	(Room_Enums.GV_MAIN, 110, 1830, -2068): [ # Note
		],
	(Room_Enums.GV_MAIN, 684, 2770, 1610): [ # Note
		],
	(Room_Enums.GV_MAIN, 685, 2170, 2305): [ # Note
		],
	(Room_Enums.GV_MAIN, 1055, 535, -458): [ # Note
		],
	(Room_Enums.GV_MAIN, 1234, 535, 411): [ # Note
		],
	(Room_Enums.GV_MAIN, 1019, 1830, -2068): [ # Note
		],
	(Room_Enums.GV_MAIN, 1671, 1830, -1416): [ # Note
		],
	(Room_Enums.GV_MAIN, 1214, 3821, -3576): [ # Note
		],
	(Room_Enums.GV_MAIN, 2307, 1837, -770): [ # Note
		],
	(Room_Enums.GV_MAIN, 2395, 2130, -300): [ # Note
		],
	(Room_Enums.GV_MAIN, 2395, 2130, 970): [ # Note
		],
	(Room_Enums.GV_MAIN, 2925, 3426, -6331): [ # Note
		],
	(Room_Enums.GV_MAIN, 3090, 2730, -300): [ # Note
		],
	(Room_Enums.GV_MAIN, 3090, 2730, 970): [ # Note
		],
	(Room_Enums.GV_MAIN, 3930, 2849, 324): [ # Note
		],
	(Room_Enums.GV_MAIN, 3792, 2656, 325): [ # Note
		],
	(Room_Enums.GV_MAIN, 3522, 3403, -6008): [ # Note
		],
	(Room_Enums.GV_MAIN, 4815, 2452, -714): [ # Note
		],
	(Room_Enums.GV_MAIN, 4215, 2452, -715): [ # Note
		],
	(Room_Enums.GV_MAIN, 4211, 3233, 324): [ # Note
		],
	(Room_Enums.GV_MAIN, 4070, 3040, 324): [ # Note
		],
	(Room_Enums.GV_MAIN, -5350, 1854, 5432): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -5311, 1855, 6465): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -5652, 2155, 5566): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -5620, 2155, 6335): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -5561, 3435, -856): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -5664, 3435, -737): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -5682, 3414, -971): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -5794, 3413, -848): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -4023, 3795, 91): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -4022, 3795, 231): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -3884, 3795, 89): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -3881, 3795, 225): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -2361, 3433, -2162): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -2517, 3413, -2121): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -2314, 3432, -2012): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -2478, 3410, -1960): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1434, 2436, 1776): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1442, 2436, 1618): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1605, 2414, 1787): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1611, 2415, 1620): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1345, 2774, 5562): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1497, 2774, 5555): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1299, 2774, 5410): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1548, 2774, 5411): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1425, 2774, 5324): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1425, 2773, 6394): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1277, 2774, 6336): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1526, 2774, 6287): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1296, 2774, 6183): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -1445, 2774, 6159): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -834, 3824, -5286): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -492, 4320, -3925): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 983, 1028, 7914): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 155, 1022, 9417): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 782, 1014, 10176): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 525, 4812, -4237): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 1755, 2434, 1823): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 1582, 2411, 1833): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 1747, 2434, 1665): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 1579, 2413, 1666): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 1199, 3329, -5622): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 2135, 1020, 8172): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 5790, 2728, -3767): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 5245, 2728, -3619): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 5991, 2728, -2884): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 5330, 2729, -2868): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 6237, 2729, -3350): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 6266, 2455, -49): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 6266, 2455, 949): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 6266, 2455, 800): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 6266, 2455, 650): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 6266, 2455, 100): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, 6266, 2455, 251): [ # Red Feather
		],
	(Room_Enums.GV_MAIN, -4689, 1662, 5017): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -4551, 1663, 5336): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -4402, 1618, 5076): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -4674, 1659, 6885): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -4379, 1623, 6824): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -4530, 1665, 6538): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -1137, 2432, -58): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -1056, 2432, 466): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -1168, 3325, -5619): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -342, 2730, -6645): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -814, 2431, -394): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -472, 2432, -752): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -985, 2432, 994): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 781, -51, 8805): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 845, -55, 9275): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 387, 2730, -6645): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 17, 2730, -6645): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 129, 2432, -740): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 740, 2432, -729): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 945, 2432, -392): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 861, 3821, -5292): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 523, 4316, -4952): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 526, 4316, -3580): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 1647, -56, 8820): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 1214, -51, 8493): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 1325, -59, 9447): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 1151, 2431, -43): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 1039, 2432, 970): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, 1099, 2432, 473): [ # Blue Egg
		],
	(Room_Enums.GV_MAIN, -4060, 2190, 5532): [ # Gold Feather
		],
	(Room_Enums.GV_MAIN, -4029, 2190, 6324): [ # Gold Feather
		],
	(Room_Enums.GV_MAIN, -3915, 4795, 179): [ # Gold Feather
		],
	(Room_Enums.GV_MAIN, 3142, 412, 9779): [ # Gold Feather
		],
	(Room_Enums.GV_MATCHING_PUZZLE, 715, 248, 0): [ # Mumbo Token
		],
	(Room_Enums.GV_MATCHING_PUZZLE, -450, 19, -450): [ # Note
		],
	(Room_Enums.GV_MATCHING_PUZZLE, -450, 19, 450): [ # Note
		],
	(Room_Enums.GV_MATCHING_PUZZLE, 450, 19, -450): [ # Note
		],
	(Room_Enums.GV_MATCHING_PUZZLE, 450, 19, 450): [ # Note
		],
	(Room_Enums.GV_KING_SANDYBUTT, -5008, 66, 62): [ # Jiggy
		],
	(Room_Enums.GV_KING_SANDYBUTT, -5514, 0, 138): [ # Mumbo Token
		],
	(Room_Enums.GV_KING_SANDYBUTT, -4964, 0, 700): [ # Pink Jinjo
		],
	(Room_Enums.GV_KING_SANDYBUTT, 1282, 18, 1971): [ # Extra Life
		],
	(Room_Enums.GV_KING_SANDYBUTT, -4957, 10, -414): [ # Gold Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, -4964, 0, 700): [ # Gold Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, -4964, 0, 700): [ # Gold Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, -1609, 25, 1688): [ # Gold Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, -1609, 25, 1584): [ # Gold Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, 1259, 28, 900): [ # Gold Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, 1259, 29, 1002): [ # Gold Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, -4002, 0, 43): [ # Note
		],
	(Room_Enums.GV_KING_SANDYBUTT, -3504, 0, -190): [ # Note
		],
	(Room_Enums.GV_KING_SANDYBUTT, -2735, 0, 203): [ # Note
		],
	(Room_Enums.GV_KING_SANDYBUTT, -1913, 3, 210): [ # Note
		],
	(Room_Enums.GV_KING_SANDYBUTT, 4729, 0, -45): [ # Note
		],
	(Room_Enums.GV_KING_SANDYBUTT, 4178, 0, 205): [ # Note
		],
	(Room_Enums.GV_KING_SANDYBUTT, 5400, 0, 326): [ # Note
		],
	(Room_Enums.GV_KING_SANDYBUTT, -1139, 25, 961): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, -1139, 25, 880): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, -1240, 25, 964): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, -1240, 24, 884): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, -856, 25, -1243): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, -775, 25, -1243): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, -855, 25, -1140): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, -775, 25, -1140): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, 511, 20, -1636): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, 612, 20, -1636): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, 712, 20, -1636): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, 517, 22, -1502): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, 612, 22, -1502): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, 712, 22, -1502): [ # Blue Egg
		],
	(Room_Enums.GV_KING_SANDYBUTT, -201, 28, -1250): [ # Red Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, -89, 29, -1250): [ # Red Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, -200, 29, -1169): [ # Red Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, -89, 29, -1169): [ # Red Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, 140, 29, 1560): [ # Red Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, 140, 29, 1660): [ # Red Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, 240, 29, 1560): [ # Red Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, 240, 28, 1660): [ # Red Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, 339, 29, 1560): [ # Red Feather
		],
	(Room_Enums.GV_KING_SANDYBUTT, 339, 28, 1659): [ # Red Feather
		],
	(Room_Enums.GV_WATER_PYRAMID, -1, 145, -23): [ # Jiggy
		],
	(Room_Enums.GV_WATER_PYRAMID, -300, 1439, -1194): [ # Mumbo Token
		],
	(Room_Enums.GV_WATER_PYRAMID, -5, 13, -757): [ # Note
		],
	(Room_Enums.GV_WATER_PYRAMID, -776, 13, -3): [ # Note
		],
	(Room_Enums.GV_WATER_PYRAMID, -14, 13, 734): [ # Note
		],
	(Room_Enums.GV_WATER_PYRAMID, 729, 13, -11): [ # Note
		],
	(Room_Enums.GV_WATER_PYRAMID, -393, 13, -663): [ # Red Feather
		],
	(Room_Enums.GV_WATER_PYRAMID, -666, 13, 375): [ # Red Feather
		],
	(Room_Enums.GV_WATER_PYRAMID, 621, 13, -376): [ # Red Feather
		],
	(Room_Enums.GV_WATER_PYRAMID, 353, 13, 647): [ # Red Feather
		],
	(Room_Enums.GV_WATER_PYRAMID, -671, 13, -369): [ # Blue Egg
		],
	(Room_Enums.GV_WATER_PYRAMID, -390, 13, 655): [ # Blue Egg
		],
	(Room_Enums.GV_WATER_PYRAMID, 354, 13, -645): [ # Blue Egg
		],
	(Room_Enums.GV_WATER_PYRAMID, 645, 13, 384): [ # Blue Egg
		],
	(Room_Enums.GV_RUBEE, -3, 1359, 15): [ # Jiggy
		],
	(Room_Enums.GV_RUBEE, 0, 107, -602): [ # Mumbo Token
		],
	(Room_Enums.GV_RUBEE, -685, 0, -743): [ # Note
		],
	(Room_Enums.GV_RUBEE, -495, 0, -880): [ # Note
		],
	(Room_Enums.GV_RUBEE, -913, 0, 428): [ # Note
		],
	(Room_Enums.GV_RUBEE, -986, 0, 201): [ # Note
		],
	(Room_Enums.GV_RUBEE, 496, 0, -878): [ # Note
		],
	(Room_Enums.GV_RUBEE, 679, 0, -744): [ # Note
		],
	(Room_Enums.GV_RUBEE, 915, 0, 421): [ # Note
		],
	(Room_Enums.GV_RUBEE, 988, 0, 195): [ # Note
		],
	(Room_Enums.GV_JINXY, -2550, 0, -51): [ # Mumbo Token
		],
	(Room_Enums.GV_JINXY, -2250, 1970, -49): [ # Jiggy
		],
	(Room_Enums.GV_JINXY, 2078, 1122, -50): [ # Orange Jinjo
		],
	(Room_Enums.GV_JINXY, -3310, 0, -850): [ # Note
		],
	(Room_Enums.GV_JINXY, -3317, 0, 748): [ # Note
		],
	(Room_Enums.GV_JINXY, -1195, 1592, -50): [ # Note
		],
	(Room_Enums.GV_JINXY, 95, 911, -50): [ # Note
		],
	(Room_Enums.GV_JINXY, 1295, 274, -50): [ # Note
		],
	(Room_Enums.GV_JINXY, 2249, 0, -829): [ # Note
		],
	(Room_Enums.GV_JINXY, 2265, 0, 753): [ # Note
		],
	(Room_Enums.GV_JINXY, -2850, 0, -50): [ # Blue Egg
		],
	(Room_Enums.GV_JINXY, -2756, 0, -272): [ # Blue Egg
		],
	(Room_Enums.GV_JINXY, -2550, 0, -349): [ # Blue Egg
		],
	(Room_Enums.GV_JINXY, -2359, 0, -293): [ # Blue Egg
		],
	(Room_Enums.GV_JINXY, -2251, 0, -50): [ # Blue Egg
		],
	(Room_Enums.GV_JINXY, -2757, 0, 137): [ # Blue Egg
		],
	(Room_Enums.GV_JINXY, -2550, 0, 251): [ # Blue Egg
		],
	(Room_Enums.GV_JINXY, -2347, 0, 159): [ # Blue Egg
		],
	(Room_Enums.GV_JINXY, 1997, 1142, -179): [ # Red Feather
		],
	(Room_Enums.GV_JINXY, 1995, 1142, 83): [ # Red Feather
		],
	(Room_Enums.GV_JINXY, 2161, 1142, -182): [ # Red Feather
		],
	(Room_Enums.GV_JINXY, 2158, 1142, 83): [ # Red Feather
		],
    ###########################
    ### Mad Monster Mansion ###
    ###########################
	(Room_Enums.MMM_MAIN, -4700, 175, -5149): [ # Mumbo Token
		],
	(Room_Enums.MMM_MAIN, -4250, 0, 352): [ # Mumbo Token
		],
	(Room_Enums.MMM_MAIN, -2800, 1475, -1363): [ # Mumbo Token
		],
	(Room_Enums.MMM_MAIN, -1643, 25, -1026): [ # Mumbo Token
		],
	(Room_Enums.MMM_MAIN, 173, 350, -3610): [ # Mumbo Token
		],
	(Room_Enums.MMM_MAIN, 1796, 857, -4243): [ # Mumbo Token
		],
	(Room_Enums.MMM_MAIN, 3950, -175, 325): [ # Mumbo Token
		],
	(Room_Enums.MMM_MAIN, 5900, -275, 798): [ # Mumbo Token
		],
	(Room_Enums.MMM_MAIN, -4265, 0, 2668): [ # Orange Jinjo
		],
	(Room_Enums.MMM_MAIN, -2800, 3175, -1601): [ # Jiggy
		],
	(Room_Enums.MMM_MAIN, 1437, 2100, 248): [ # Green Jinjo
		],
	(Room_Enums.MMM_MAIN, 5900, 300, 1050): [ # Blue Jinjo
		],
	(Room_Enums.MMM_MAIN, -5079, 175, -4515): [ # SM Purple Flower
		],
	(Room_Enums.MMM_MAIN, -2700, 175, -5492): [ # SM Purple Flower
		],
	(Room_Enums.MMM_MAIN, -4084, 175, -3417): [ # SM Yellow Flower
		],
	(Room_Enums.MMM_MAIN, -4400, 1051, -2900): [ # Note
		],
	(Room_Enums.MMM_MAIN, -4000, 1054, -2900): [ # Note
		],
	(Room_Enums.MMM_MAIN, -3300, 0, -131): [ # Note
		],
	(Room_Enums.MMM_MAIN, -3300, 0, 25): [ # Note
		],
	(Room_Enums.MMM_MAIN, -3455, 0, 1780): [ # Note
		],
	(Room_Enums.MMM_MAIN, -3455, 0, 1445): [ # Note
		],
	(Room_Enums.MMM_MAIN, -3199, 1060, -2900): [ # Note
		],
	(Room_Enums.MMM_MAIN, -3600, 1057, -2900): [ # Note
		],
	(Room_Enums.MMM_MAIN, -3148, 2075, -1948): [ # Note
		],
	(Room_Enums.MMM_MAIN, -3146, 2075, -1253): [ # Note
		],
	(Room_Enums.MMM_MAIN, -2186, 662, -2498): [ # Note
		],
	(Room_Enums.MMM_MAIN, -2050, 7, 1755): [ # Note
		],
	(Room_Enums.MMM_MAIN, -2250, 0, 2655): [ # Note
		],
	(Room_Enums.MMM_MAIN, -2800, 1063, -3301): [ # Note
		],
	(Room_Enums.MMM_MAIN, -2800, 1063, -3699): [ # Note
		],
	(Room_Enums.MMM_MAIN, -2800, 1063, -2135): [ # Note
		],
	(Room_Enums.MMM_MAIN, -2800, 1063, -2500): [ # Note
		],
	(Room_Enums.MMM_MAIN, -2800, 1063, -2900): [ # Note
		],
	(Room_Enums.MMM_MAIN, -2452, 2075, -1948): [ # Note
		],
	(Room_Enums.MMM_MAIN, -2453, 2075, -1253): [ # Note
		],
	(Room_Enums.MMM_MAIN, -200, 225, -3525): [ # Note
		],
	(Room_Enums.MMM_MAIN, -201, 225, -3700): [ # Note
		],
	(Room_Enums.MMM_MAIN, -200, 225, -3876): [ # Note
		],
	(Room_Enums.MMM_MAIN, -428, 700, -1249): [ # Note
		],
	(Room_Enums.MMM_MAIN, -428, 700, 1743): [ # Note
		],
	(Room_Enums.MMM_MAIN, 556, 75, 2111): [ # Note
		],
	(Room_Enums.MMM_MAIN, 734, 75, 2236): [ # Note
		],
	(Room_Enums.MMM_MAIN, 63, 1600, -796): [ # Note
		],
	(Room_Enums.MMM_MAIN, 63, 1600, 1303): [ # Note
		],
	(Room_Enums.MMM_MAIN, 1824, 987, -4460): [ # Note
		],
	(Room_Enums.MMM_MAIN, 1575, 988, -4460): [ # Note
		],
	(Room_Enums.MMM_MAIN, 1266, 75, 2236): [ # Note
		],
	(Room_Enums.MMM_MAIN, 1444, 75, 2110): [ # Note
		],
	(Room_Enums.MMM_MAIN, 1936, 1600, -797): [ # Note
		],
	(Room_Enums.MMM_MAIN, 1936, 1600, 1294): [ # Note
		],
	(Room_Enums.MMM_MAIN, 2325, 988, -4460): [ # Note
		],
	(Room_Enums.MMM_MAIN, 2075, 988, -4460): [ # Note
		],
	(Room_Enums.MMM_MAIN, 2436, 700, -1244): [ # Note
		],
	(Room_Enums.MMM_MAIN, 2436, 702, 1743): [ # Note
		],
	(Room_Enums.MMM_MAIN, 4201, -275, -3475): [ # Note
		],
	(Room_Enums.MMM_MAIN, 4200, -275, -3325): [ # Note
		],
	(Room_Enums.MMM_MAIN, 5378, -75, 521): [ # Note
		],
	(Room_Enums.MMM_MAIN, 5372, -75, 1571): [ # Note
		],
	(Room_Enums.MMM_MAIN, 6428, -75, 529): [ # Note
		],
	(Room_Enums.MMM_MAIN, 6423, -75, 1579): [ # Note
		],
	(Room_Enums.MMM_MAIN, 7150, -275, -3474): [ # Note
		],
	(Room_Enums.MMM_MAIN, 7150, -275, -3325): [ # Note
		],
	(Room_Enums.MMM_MAIN, -3428, 175, -5504): [ # SM Yellow/Blue Flower
		],
	(Room_Enums.MMM_MAIN, -3679, 4, -38): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, -3150, 4, 2485): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, -3150, 4, 2332): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, 538, 1904, -323): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, 538, 1904, 817): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, 1455, 1904, -328): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, 1455, 1904, 817): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, 4825, -271, -4200): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, 4675, -271, -4200): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, 6683, -271, -4200): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, 6517, -271, -4199): [ # Red Feather
		],
	(Room_Enums.MMM_MAIN, -2250, 2, -129): [ # Gold Feather
		],
	(Room_Enums.MMM_MAIN, -176, 178, -5086): [ # Gold Feather
		],
	(Room_Enums.MMM_MAIN, 5288, -450, -3350): [ # Gold Feather
		],
	(Room_Enums.MMM_MAIN, 6112, -450, -3350): [ # Gold Feather
		],
	(Room_Enums.MMM_MAIN, -2446, 0, 760): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, -1951, 0, 2655): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, -1750, 0, 2410): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 50, 1100, -760): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 50, 1100, 1255): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 1950, 1099, -758): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 1942, 1100, 1255): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 4200, -275, -2474): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 4200, -275, -2324): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 7150, -273, -2383): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 7149, -273, -2233): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 7173, -175, -103): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 7173, -175, 452): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 7173, -175, 1008): [ # Blue Egg
		],
	(Room_Enums.MMM_MAIN, 7174, -175, 1564): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -1, 2263, -3465): [ # Extra Life
		],
	(Room_Enums.MMM_CHURCH, 0, 583, -1300): [ # Mumbo Token
		],
	(Room_Enums.MMM_CHURCH, 0, 4806, 341): [ # Mumbo Token
		],
	(Room_Enums.MMM_CHURCH, 0, 5163, 2400): [ # Empty Honeycomb
		],
	(Room_Enums.MMM_CHURCH, -2299, 588, 820): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -2299, 588, 2370): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -2100, 4839, -2065): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -2100, 4839, -1465): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -2100, 4838, -1764): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -2100, 4813, 2730): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -2100, 4813, 2430): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -2100, 4813, 2129): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -949, 588, 820): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -949, 588, 2370): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, 950, 588, 819): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, 950, 588, 2369): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, 2300, 588, 819): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, 2300, 588, 2369): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, 2070, 4885, -2065): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, 2069, 4885, -1464): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, 2069, 4885, -1765): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, 2070, 4768, 2720): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, 2070, 4768, 2420): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, 2070, 4768, 2119): [ # Blue Egg
		],
	(Room_Enums.MMM_CHURCH, -1625, 690, 820): [ # Note
		],
	(Room_Enums.MMM_CHURCH, -1623, 690, 2373): [ # Note
		],
	(Room_Enums.MMM_CHURCH, -1062, 2450, -3199): [ # Note
		],
	(Room_Enums.MMM_CHURCH, -150, 230, -1693): [ # Note
		],
	(Room_Enums.MMM_CHURCH, -529, 2750, -3200): [ # Note
		],
	(Room_Enums.MMM_CHURCH, 150, 131, -1698): [ # Note
		],
	(Room_Enums.MMM_CHURCH, 519, 2750, -3200): [ # Note
		],
	(Room_Enums.MMM_CHURCH, 1625, 690, 816): [ # Note
		],
	(Room_Enums.MMM_CHURCH, 1623, 690, 2371): [ # Note
		],
	(Room_Enums.MMM_CHURCH, 1054, 2450, -3199): [ # Note
		],
	(Room_Enums.MMM_CHURCH, -797, 2604, -3201): [ # Red Feather
		],
	(Room_Enums.MMM_CHURCH, -266, 2904, -3199): [ # Red Feather
		],
	(Room_Enums.MMM_CHURCH, 264, 2904, -3200): [ # Red Feather
		],
	(Room_Enums.MMM_CHURCH, 789, 2604, -3199): [ # Red Feather
		],
	(Room_Enums.MMM_CHURCH, -12, 4901, -2930): [ # Gold Feather
		],
	(Room_Enums.MMM_CHURCH, -13, 4802, 4530): [ # Gold Feather
		],
	(Room_Enums.MMM_BASEMENT, -507, 30, 199): [ # Mumbo Token
		],
	(Room_Enums.MMM_BASEMENT, -516, 30, 477): [ # Jiggy
		],
	(Room_Enums.MMM_BASEMENT, 511, 38, 203): [ # Pink Jinjo
		],
	(Room_Enums.MMM_BASEMENT, -524, 40, -473): [ # Blue Egg
		],
	(Room_Enums.MMM_BASEMENT, -495, 40, -474): [ # Blue Egg
		],
	(Room_Enums.MMM_BASEMENT, -464, 40, -473): [ # Blue Egg
		],
	(Room_Enums.MMM_BASEMENT, -375, 300, 1274): [ # Note
		],
	(Room_Enums.MMM_BASEMENT, -126, 300, 1275): [ # Note
		],
	(Room_Enums.MMM_BASEMENT, 375, 300, 1275): [ # Note
		],
	(Room_Enums.MMM_BASEMENT, 125, 300, 1275): [ # Note
		],
	(Room_Enums.MMM_BASEMENT, 475, 40, -200): [ # Gold Feather
		],
	(Room_Enums.MMM_TUMBLAR, 48, 0, -58): [ # Jiggy
		],
	(Room_Enums.MMM_TUMBLAR, -701, 0, -725): [ # Note
		],
	(Room_Enums.MMM_TUMBLAR, -700, 0, 688): [ # Note
		],
	(Room_Enums.MMM_TUMBLAR, 700, 0, -725): [ # Note
		],
	(Room_Enums.MMM_TUMBLAR, 700, 0, 688): [ # Note
		],
	(Room_Enums.MMM_WELL, -732, 0, -109): [ # Mumbo Token
		],
	(Room_Enums.MMM_WELL, 1, 179, 0): [ # Jiggy
		],
	(Room_Enums.MMM_WELL, -475, 0, -617): [ # Note
		],
	(Room_Enums.MMM_WELL, -613, 0, 411): [ # Note
		],
	(Room_Enums.MMM_WELL, -714, 0, 171): [ # Note
		],
	(Room_Enums.MMM_WELL, -217, 0, 131): [ # Note
		],
	(Room_Enums.MMM_WELL, 694, 0, -186): [ # Note
		],
	(Room_Enums.MMM_WELL, 79, 0, -201): [ # Note
		],
	(Room_Enums.MMM_WELL, 681, 0, 182): [ # Note
		],
	(Room_Enums.MMM_DINING_ROOM, -160, 190, -2599): [ # Mumbo Token
		],
	(Room_Enums.MMM_DINING_ROOM, 1, 511, 24): [ # Jiggy
		],
	(Room_Enums.MMM_DINING_ROOM, 0, 1326, 145): [ # Extra Life
		],
	(Room_Enums.MMM_DINING_ROOM, -176, 550, -2499): [ # Blue Egg
		],
	(Room_Enums.MMM_DINING_ROOM, -350, 550, -2499): [ # Blue Egg
		],
	(Room_Enums.MMM_DINING_ROOM, 349, 550, -2500): [ # Blue Egg
		],
	(Room_Enums.MMM_DINING_ROOM, 174, 550, -2500): [ # Blue Egg
		],
	(Room_Enums.MMM_DINING_ROOM, 0, 550, -2500): [ # Blue Egg
		],
	(Room_Enums.MMM_DINING_ROOM, -13, 286, -1751): [ # Note
		],
	(Room_Enums.MMM_DINING_ROOM, -737, 286, -1): [ # Note
		],
	(Room_Enums.MMM_DINING_ROOM, -738, 286, -499): [ # Note
		],
	(Room_Enums.MMM_DINING_ROOM, -738, 286, 499): [ # Note
		],
	(Room_Enums.MMM_DINING_ROOM, 11, 286, -1102): [ # Note
		],
	(Room_Enums.MMM_DINING_ROOM, 736, 286, -500): [ # Note
		],
	(Room_Enums.MMM_DINING_ROOM, 737, 286, 0): [ # Note
		],
	(Room_Enums.MMM_DINING_ROOM, 736, 286, 499): [ # Note
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_2_BLUE_EGGS, -437, 150, -336): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_2_BLUE_EGGS, -302, 150, -336): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_2_BLUE_EGGS, -36, 0, 350): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_2_BLUE_EGGS, -442, 160, 331): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_2_BLUE_EGGS, 450, 0, -35): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_2_BLUE_EGGS, 446, 135, -339): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_2_BLUE_EGGS, 450, 0, 36): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_2_BLUE_EGGS, 35, 0, 351): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_1_NOTES, -450, 0, -75): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_1_NOTES, -438, 195, -336): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_1_NOTES, -450, 0, 0): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_1_NOTES, -450, 0, 75): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_1_NOTES, -440, 150, 337): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_1_NOTES, -75, 0, 350): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_1_NOTES, 429, 222, -233): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_1_NOTES, 0, 0, 350): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_1_NOTES, 75, 0, 350): [ # Note
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, -462, 229, -35): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, -35, 4, 400): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, -462, 229, 35): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, 450, 4, -36): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, 434, 203, -292): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, 430, 154, 385): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, 430, 154, 260): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, 35, 4, 399): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, 450, 4, 35): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 0, 13, 615): [ # Extra Life
		],
	(Room_Enums.MMM_SECRET_ROOM, -701, 0, -80): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 0, -280): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 0, -480): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, -600, 0, 619): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 0, 520): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, -400, 0, 620): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, -199, 0, 621): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 0, 320): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 0, 121): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 0, -78): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 0, -279): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 0, -481): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, 600, 0, 620): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 0, 519): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, 401, 0, 620): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, 200, 0, 620): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 0, 320): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 0, 120): [ # Blue Egg
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 4, -180): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 4, -381): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, -699, 4, -580): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 4, 620): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, -500, 4, 619): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, -301, 4, 620): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 4, 420): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, -99, 4, 619): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 4, 219): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 4, -181): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 4, -379): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 4, -579): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 4, 620): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 500, 4, 620): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 301, 4, 620): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 99, 4, 620): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 4, 422): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 4, 221): [ # Red Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, -700, 4, 21): [ # Gold Feather
		],
	(Room_Enums.MMM_SECRET_ROOM, 700, 4, 21): [ # Gold Feather
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_2_LOGGO, 52, 104, 512): [ # Mumbo Token
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_2_LOGGO, -450, 57, -200): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_2_LOGGO, -450, 46, -100): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_2_LOGGO, -450, 72, 0): [ # Red Feather
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_2_BEDROOM, -250, 540, 300): [ # Yellow Jinjo
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_2_BEDROOM, 696, 0, -397): [ # Mumbo Token
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_2_BEDROOM, -650, 175, 450): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_2_BEDROOM, -650, 175, 300): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_2_BEDROOM, -650, 175, 150): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_2_BEDROOM, -632, 0, 1383): [ # Gold Feather
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_2_BEDROOM, 760, 207, -100): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_2_BEDROOM, 700, 207, -200): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_2_BEDROOM, 640, 200, -100): [ # Note
		],
	(Room_Enums.MMM_FLOOR_3_ROOM_2_BEDROOM, 700, 207, 0): [ # Note
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, -51, -135, 52): [ # Empty Honeycomb
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, -442, -135, -390): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, -268, -135, -390): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, -103, -135, -390): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, 61, -135, -390): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, 225, -135, -390): [ # Blue Egg
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, -267, -131, 500): [ # Gold Feather
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, -101, -131, 497): [ # Gold Feather
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, -100, 4, 495): [ # Gold Feather
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, -545, 0, 0): [ # Gold Feather
		],
	(Room_Enums.MMM_FLOOR_2_ROOM_1_HONEYCOMB, 67, -131, 500): [ # Gold Feather
		],
	(Room_Enums.MMM_INSIDE_GUTTER, 2, 288, -4): [ # Jiggy
		],
	(Room_Enums.MMM_INSIDE_GUTTER, -267, 0, -153): [ # Note
		],
	(Room_Enums.MMM_INSIDE_GUTTER, -266, 0, 152): [ # Note
		],
	(Room_Enums.MMM_INSIDE_GUTTER, 270, 0, -154): [ # Note
		],
	(Room_Enums.MMM_INSIDE_GUTTER, 0, 0, -310): [ # Note
		],
	(Room_Enums.MMM_INSIDE_GUTTER, 268, 0, 152): [ # Note
		],
	(Room_Enums.MMM_MUMBOS_SKULL, -293, 0, -157): [ # Note
		],
	(Room_Enums.MMM_MUMBOS_SKULL, 294, 0, -157): [ # Note
		],
	(Room_Enums.MMM_MUMBOS_SKULL, 0, 402, 510): [ # Gold Feather
		],
	(Room_Enums.MMM_INSIDE_LOGGO, -518, 295, -468): [ # Jiggy
		],
	(Room_Enums.MMM_INSIDE_LOGGO, 424, 170, 304): [ # Mumbo Token
		],
	(Room_Enums.MMM_INSIDE_LOGGO, -540, 233, -59): [ # Gold Feather
		],
	(Room_Enums.MMM_INSIDE_LOGGO, -540, 233, -90): [ # Gold Feather
		],
	(Room_Enums.MMM_INSIDE_LOGGO, -16, 233, -490): [ # Gold Feather
		],
	(Room_Enums.MMM_INSIDE_LOGGO, 15, 233, -490): [ # Gold Feather
		],
    ########################
    ### Rusty Bucket Bay ###
    ########################
	(Room_Enums.RBB_MAIN, -8615, -1000, -3555): [ # Green Jinjo
		],
	(Room_Enums.RBB_MAIN, -8738, -1253, 4032): [ # Yellow Jinjo
		],
	(Room_Enums.RBB_MAIN, -7401, -1000, -3425): [ # Mumbo Token
		],
	(Room_Enums.RBB_MAIN, -6200, 150, 0): [ # Mumbo Token
		],
	(Room_Enums.RBB_MAIN, -3299, -457, 3800): [ # Mumbo Token
		],
	(Room_Enums.RBB_MAIN, 1000, 2750, 0): [ # Mumbo Token
		],
	(Room_Enums.RBB_MAIN, 6200, 400, 0): [ # Mumbo Token
		],
	(Room_Enums.RBB_MAIN, 7053, -985, -1672): [ # Mumbo Token
		],
	(Room_Enums.RBB_MAIN, -4900, 0, 0): [ # Jiggy
		],
	(Room_Enums.RBB_MAIN, -2006, 2700, -2): [ # Jiggy
		],
	(Room_Enums.RBB_MAIN, 7750, -2007, 0): [ # Jiggy
		],
	(Room_Enums.RBB_MAIN, 7850, -2613, 4026): [ # Pink Jinjo
		],
	(Room_Enums.RBB_MAIN, 8903, -800, -2894): [ # Orange Jinjo
		],
	(Room_Enums.RBB_MAIN, -8144, -969, -2026): [ # Note
		],
	(Room_Enums.RBB_MAIN, -7843, -986, -3205): [ # Note
		],
	(Room_Enums.RBB_MAIN, -7679, -986, -2363): [ # Note
		],
	(Room_Enums.RBB_MAIN, -7501, -800, 1554): [ # Note
		],
	(Room_Enums.RBB_MAIN, -7128, -800, 1554): [ # Note
		],
	(Room_Enums.RBB_MAIN, -6755, -800, 1554): [ # Note
		],
	(Room_Enums.RBB_MAIN, -6755, -800, 2150): [ # Note
		],
	(Room_Enums.RBB_MAIN, -6755, -800, 2797): [ # Note
		],
	(Room_Enums.RBB_MAIN, -5199, -200, -2900): [ # Note
		],
	(Room_Enums.RBB_MAIN, -4600, -200, -2900): [ # Note
		],
	(Room_Enums.RBB_MAIN, -4900, -200, -2900): [ # Note
		],
	(Room_Enums.RBB_MAIN, -3399, 800, -600): [ # Note
		],
	(Room_Enums.RBB_MAIN, -3399, 800, 600): [ # Note
		],
	(Room_Enums.RBB_MAIN, -1050, 406, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -717, 285, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -384, 164, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -50, 43, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -950, 1200, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -650, 1200, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -350, 1200, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -50, 1200, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -50, 2207, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -350, 2207, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -650, 2207, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, -950, 2207, 0): [ # Note
		],
	(Room_Enums.RBB_MAIN, 800, -482, 1775): [ # Note
		],
	(Room_Enums.RBB_MAIN, 800, -389, 1450): [ # Note
		],
	(Room_Enums.RBB_MAIN, 800, -575, 2102): [ # Note
		],
	(Room_Enums.RBB_MAIN, 800, -667, 2424): [ # Note
		],
	(Room_Enums.RBB_MAIN, 800, -760, 2751): [ # Note
		],
	(Room_Enums.RBB_MAIN, 3900, -200, -2900): [ # Note
		],
	(Room_Enums.RBB_MAIN, 4200, -200, -2900): [ # Note
		],
	(Room_Enums.RBB_MAIN, 4500, -200, -2900): [ # Note
		],
	(Room_Enums.RBB_MAIN, 6950, -1175, 3050): [ # Note
		],
	(Room_Enums.RBB_MAIN, 6950, -1175, 4050): [ # Note
		],
	(Room_Enums.RBB_MAIN, 7800, -800, -1325): [ # Note
		],
	(Room_Enums.RBB_MAIN, 7800, -800, 1325): [ # Note
		],
	(Room_Enums.RBB_MAIN, 8750, -1175, 3050): [ # Note
		],
	(Room_Enums.RBB_MAIN, 8750, -1175, 4050): [ # Note
		],
	(Room_Enums.RBB_MAIN, 8050, -800, -1001): [ # Note
		],
	(Room_Enums.RBB_MAIN, 8149, -799, -300): [ # Note
		],
	(Room_Enums.RBB_MAIN, 8149, -799, 300): [ # Note
		],
	(Room_Enums.RBB_MAIN, 8050, -800, 1001): [ # Note
		],
	(Room_Enums.RBB_MAIN, -4185, -185, -1678): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, -3721, -185, -1677): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, -3953, -185, -1677): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, -1200, -450, 3899): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, -1750, -650, 3300): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, -750, -800, -3726): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, -750, -800, -3651): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, -49, -800, -3726): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, -50, -800, -3651): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, -550, -650, 3549): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 1549, -500, 3250): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 1900, -200, 3800): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 4500, -250, -1150): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 4100, -250, 1150): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 4650, 150, 1050): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 5050, 50, -1050): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 6976, -2613, 3550): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 6976, -2613, 3075): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 6975, -2613, 4025): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 8726, -2613, 3075): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 8726, -2613, 3550): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, 8726, -2613, 4025): [ # Blue Egg
		],
	(Room_Enums.RBB_MAIN, -4890, 2004, -3515): [ # Gold Feather
		],
	(Room_Enums.RBB_MAIN, -3939, -180, 1677): [ # Gold Feather
		],
	(Room_Enums.RBB_MAIN, -3000, -457, 3800): [ # Gold Feather
		],
	(Room_Enums.RBB_MAIN, -3601, -457, 3800): [ # Gold Feather
		],
	(Room_Enums.RBB_MAIN, 4207, 2004, -3514): [ # Gold Feather
		],
	(Room_Enums.RBB_MAIN, -3150, 1104, -450): [ # Red Feather
		],
	(Room_Enums.RBB_MAIN, -3650, 1104, -450): [ # Red Feather
		],
	(Room_Enums.RBB_MAIN, -3650, 1104, 450): [ # Red Feather
		],
	(Room_Enums.RBB_MAIN, -3150, 1104, 451): [ # Red Feather
		],
	(Room_Enums.RBB_MAIN, 6200, 404, -300): [ # Red Feather
		],
	(Room_Enums.RBB_MAIN, 6200, 404, -150): [ # Red Feather
		],
	(Room_Enums.RBB_MAIN, 6200, 404, 300): [ # Red Feather
		],
	(Room_Enums.RBB_MAIN, 6200, 404, 150): [ # Red Feather
		],
	(Room_Enums.RBB_ENGINE_ROOM, -2551, 1065, -2650): [ # Extra Life
		],
	(Room_Enums.RBB_ENGINE_ROOM, -2450, 1100, -400): [ # Mumbo Token
		],
	(Room_Enums.RBB_ENGINE_ROOM, -319, 12, 1899): [ # Mumbo Token
		],
	(Room_Enums.RBB_ENGINE_ROOM, 2450, 1100, -400): [ # Mumbo Token
		],
	(Room_Enums.RBB_ENGINE_ROOM, 1, 809, -3718): [ # Jiggy
		],
	(Room_Enums.RBB_ENGINE_ROOM, 0, 360, 3541): [ # Empty Honeycomb
		],
	(Room_Enums.RBB_ENGINE_ROOM, -3648, 1064, -3492): [ # Gold Feather
		],
	(Room_Enums.RBB_ENGINE_ROOM, -3039, 1160, -2485): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, -3370, 1160, -2484): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, -3038, 1160, -2817): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, -3374, 1160, -2817): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, -1700, 809, -600): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, -1499, 809, -601): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, -1700, 809, -200): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, -1499, 809, -199): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, -200, 809, -2200): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, -200, 809, -2600): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, 200, 809, -2600): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, 200, 809, -2200): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, 1700, 809, -600): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, 1501, 809, -600): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, 1700, 809, -199): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, 1500, 809, -199): [ # Note
		],
	(Room_Enums.RBB_ENGINE_ROOM, -2550, 1059, -3001): [ # Blue Egg
		],
	(Room_Enums.RBB_ENGINE_ROOM, -2550, 1059, -2300): [ # Blue Egg
		],
	(Room_Enums.RBB_ENGINE_ROOM, -2550, 1059, -2475): [ # Blue Egg
		],
	(Room_Enums.RBB_ENGINE_ROOM, -2550, 1059, -2825): [ # Blue Egg
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, -950, 1045, -50): [ # Extra Life
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, 850, 850, -1150): [ # Jiggy
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, -726, 575, 125): [ # Blue Egg
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, -537, 575, 125): [ # Blue Egg
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, -350, 575, 125): [ # Blue Egg
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, -163, 575, 125): [ # Blue Egg
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, 25, 575, 124): [ # Blue Egg
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, 785, 650, 1356): [ # Note
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, 785, 650, 1045): [ # Note
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, 1005, 650, 1355): [ # Note
		],
	(Room_Enums.RBB_CHUMP_WAREHOUSE, 1005, 650, 1045): [ # Note
		],
	(Room_Enums.RBB_BOAT, -1724, -996, -825): [ # Red Feather
		],
	(Room_Enums.RBB_BOAT, -1725, -996, 824): [ # Red Feather
		],
	(Room_Enums.RBB_BOAT, 0, -996, -825): [ # Red Feather
		],
	(Room_Enums.RBB_BOAT, 0, -996, 826): [ # Red Feather
		],
	(Room_Enums.RBB_BOAT, 1725, -996, -826): [ # Red Feather
		],
	(Room_Enums.RBB_BOAT, 1725, -996, 826): [ # Red Feather
		],
	(Room_Enums.RBB_BOAT, -415, -60, 0): [ # Gold Feather
		],
	(Room_Enums.RBB_BOAT, 348, -72, 0): [ # Gold Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_1_CHOMPA, -650, 562, -35): [ # Mumbo Token
		],
	(Room_Enums.RBB_BLUE_CONTAINER_1_CHOMPA, -650, 560, -645): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_1_CHOMPA, -630, 175, -419): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_1_CHOMPA, -170, 140, -804): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_1_CHOMPA, -650, 560, 560): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_1_CHOMPA, -236, 105, 316): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_1_CHOMPA, 0, 595, -860): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_1_CHOMPA, 492, 525, -677): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_1_CHOMPA, 593, 105, -105): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, -651, 140, -1064): [ # Blue Egg
		],
	(Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, -520, 140, -1064): [ # Blue Egg
		],
	(Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, -390, 140, -1064): [ # Blue Egg
		],
	(Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, -651, 140, -959): [ # Blue Egg
		],
	(Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, -520, 140, -959): [ # Blue Egg
		],
	(Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, -389, 140, -959): [ # Blue Egg
		],
	(Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, 531, 140, 664): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, 659, 140, 665): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, 530, 140, 520): [ # Note
		],
	(Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, 660, 140, 519): [ # Note
		],
	(Room_Enums.RBB_CABINS, 583, 323, -70): [ # Mumbo Token
		],
	(Room_Enums.RBB_CABINS, -271, 0, -496): [ # Note
		],
	(Room_Enums.RBB_CABINS, -245, 0, 563): [ # Note
		],
	(Room_Enums.RBB_CABINS, 270, 0, -496): [ # Note
		],
	(Room_Enums.RBB_CABINS, 245, 0, 561): [ # Note
		],
	(Room_Enums.RBB_CABINS, -500, 155, -466): [ # Red Feather
		],
	(Room_Enums.RBB_CABINS, -500, 355, -466): [ # Red Feather
		],
	(Room_Enums.RBB_CABINS, -500, 156, 136): [ # Red Feather
		],
	(Room_Enums.RBB_CABINS, -500, 355, 136): [ # Red Feather
		],
	(Room_Enums.RBB_CABINS, 500, 155, -467): [ # Red Feather
		],
	(Room_Enums.RBB_CABINS, 500, 356, -467): [ # Red Feather
		],
	(Room_Enums.RBB_CABINS, 501, 155, 136): [ # Red Feather
		],
	(Room_Enums.RBB_CABINS, 501, 355, 136): [ # Red Feather
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 376, 199, 0): [ # Jiggy
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1338, 0, -1140): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1002, 0, -1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1338, 0, -854): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1339, 0, -569): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1339, 0, -283): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1339, 0, 852): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1339, 0, 282): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1339, 0, 569): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1339, 0, 1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1001, 0, 1138): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -1, 0, -1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -334, 0, -1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -669, 0, -1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -334, 0, 1138): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, -669, 0, 1138): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 671, 0, -1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 334, 0, -1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1, 0, 1138): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 338, 0, 1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 671, 0, 1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1338, 0, -1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1003, 0, -1139): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1338, 0, -856): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1338, 0, -572): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1338, 0, -288): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1338, 0, 0): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1338, 0, 859): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1338, 0, 287): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1338, 0, 573): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1338, 0, 1138): [ # Blue Egg
		],
	(Room_Enums.RBB_BOSS_KABOOM_BOSS, 1004, 0, 1138): [ # Blue Egg
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -435, 300, -435): [ # Mumbo Token
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 654, -449): [ # Red Feather
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 654, -325): [ # Red Feather
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 654, -200): [ # Red Feather
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 654, -75): [ # Red Feather
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 654, 51): [ # Red Feather
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 400, -49): [ # Blue Egg
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 400, 450): [ # Blue Egg
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 400, 324): [ # Blue Egg
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 400, 199): [ # Blue Egg
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -399, 400, 74): [ # Blue Egg
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 750, 924): [ # Note
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 750, 800): [ # Note
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 750, 675): [ # Note
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 750, 550): [ # Note
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -400, 750, 1050): [ # Note
		],
	(Room_Enums.RBB_MIDDLE_PIPE, -450, 4, 1055): [ # Gold Feather
		],
	(Room_Enums.RBB_MIDDLE_PIPE, 0, 468, -436): [ # Gold Feather
		],
	(Room_Enums.RBB_KITCHEN, -771, 238, -293): [ # Mumbo Token
		],
	(Room_Enums.RBB_KITCHEN, -313, 213, -1046): [ # Note
		],
	(Room_Enums.RBB_KITCHEN, -400, 163, 738): [ # Note
		],
	(Room_Enums.RBB_KITCHEN, -398, 163, 149): [ # Note
		],
	(Room_Enums.RBB_KITCHEN, 593, 213, -898): [ # Note
		],
	(Room_Enums.RBB_KITCHEN, 389, 163, 740): [ # Note
		],
	(Room_Enums.RBB_KITCHEN, 758, 213, -600): [ # Blue Egg
		],
	(Room_Enums.RBB_KITCHEN, 702, 213, -596): [ # Blue Egg
		],
	(Room_Enums.RBB_KITCHEN, 647, 213, -601): [ # Blue Egg
		],
	(Room_Enums.RBB_KITCHEN, 758, 213, -503): [ # Blue Egg
		],
	(Room_Enums.RBB_KITCHEN, 705, 213, -503): [ # Blue Egg
		],
	(Room_Enums.RBB_KITCHEN, 645, 213, -501): [ # Blue Egg
		],
	(Room_Enums.RBB_KITCHEN, 760, 213, -408): [ # Blue Egg
		],
	(Room_Enums.RBB_KITCHEN, 700, 213, -407): [ # Blue Egg
		],
	(Room_Enums.RBB_KITCHEN, 646, 213, -404): [ # Blue Egg
		],
	(Room_Enums.RBB_NAVIGATION, -656, 0, -222): [ # Mumbo Token
		],
	(Room_Enums.RBB_NAVIGATION, -270, 0, -719): [ # Note
		],
	(Room_Enums.RBB_NAVIGATION, -87, 0, -720): [ # Note
		],
	(Room_Enums.RBB_NAVIGATION, 96, 0, -720): [ # Note
		],
	(Room_Enums.RBB_NAVIGATION, 279, 0, -719): [ # Note
		],
	(Room_Enums.RBB_NAVIGATION, -740, 340, 50): [ # Blue Egg
		],
	(Room_Enums.RBB_NAVIGATION, -740, 340, 230): [ # Blue Egg
		],
	(Room_Enums.RBB_NAVIGATION, -740, 340, 409): [ # Blue Egg
		],
	(Room_Enums.RBB_NAVIGATION, -740, 340, 590): [ # Blue Egg
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -193, 0, -979): [ # Blue Jinjo
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -278, 710, -557): [ # Mumbo Token
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -860, 319, -790): [ # Gold Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -860, 319, -700): [ # Gold Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -859, 319, -610): [ # Gold Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -910, 4, 597): [ # Red Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -910, 4, 733): [ # Red Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -430, 319, 0): [ # Red Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -770, 669, 102): [ # Red Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -239, 319, 0): [ # Red Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -770, 669, 249): [ # Red Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, -50, 319, 0): [ # Red Feather
		],
	(Room_Enums.RBB_BLUE_CONTAINER_2_SEAMAN_GRUBLIN, 630, 214, -560): [ # Red Feather
		],
	(Room_Enums.RBB_CAPTAIN_ROOM, -997, 273, 355): [ # Jiggy
		],
	(Room_Enums.RBB_CAPTAIN_ROOM, -1020, 0, -315): [ # Note
		],
	(Room_Enums.RBB_CAPTAIN_ROOM, -1020, 0, -103): [ # Note
		],
	(Room_Enums.RBB_CAPTAIN_ROOM, -1020, 0, 108): [ # Note
		],
	(Room_Enums.RBB_CAPTAIN_ROOM, -90, 160, -220): [ # Gold Feather
		],
	(Room_Enums.RBB_CAPTAIN_ROOM, 110, 158, -220): [ # Gold Feather
		],
	(Room_Enums.RBB_ANCHOR, -450, 0, -750): [ # Blue Egg
		],
	(Room_Enums.RBB_ANCHOR, -450, 0, 750): [ # Blue Egg
		],
	(Room_Enums.RBB_ANCHOR, 450, 0, -751): [ # Blue Egg
		],
	(Room_Enums.RBB_ANCHOR, 450, 0, 750): [ # Blue Egg
		],
	(Room_Enums.RBB_ANCHOR, 3500, 449, -501): [ # Note
		],
	(Room_Enums.RBB_ANCHOR, 3499, 449, 499): [ # Note
		],
	(Room_Enums.RBB_ANCHOR, 4499, 449, -500): [ # Note
		],
	(Room_Enums.RBB_ANCHOR, 4500, 449, 499): [ # Note
		],
    ########################
    ### Click Clock Wood ###
    ########################
	(Room_Enums.CCW_LOBBY, -808, 52, -3268): [ # Red Feather
		],
	(Room_Enums.CCW_LOBBY, -345, 6, -3463): [ # Red Feather
		],
	(Room_Enums.CCW_LOBBY, 808, 35, -3268): [ # Red Feather
		],
	(Room_Enums.CCW_LOBBY, 346, 6, -3463): [ # Red Feather
		],
	(Room_Enums.CCW_LOBBY, -818, 8, 3275): [ # Note
		],
	(Room_Enums.CCW_LOBBY, -342, 2, 3477): [ # Note
		],
	(Room_Enums.CCW_LOBBY, 816, 8, 3277): [ # Note
		],
	(Room_Enums.CCW_LOBBY, 342, 2, 3477): [ # Note
		],
	(Room_Enums.CCW_LOBBY, 0, -94, 1365): [ # Gold Feather
		],
	(Room_Enums.CCW_LOBBY, 3270, 103, -815): [ # Blue Egg
		],
	(Room_Enums.CCW_LOBBY, 3483, 109, -341): [ # Blue Egg
		],
	(Room_Enums.CCW_LOBBY, 3270, 121, 815): [ # Blue Egg
		],
	(Room_Enums.CCW_LOBBY, 3483, 99, 342): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -4993, 2896, -944): [ # Extra Life
		],
	(Room_Enums.CCW_SPRING_MAIN, 5100, 425, 0): [ # Extra Life
		],
	(Room_Enums.CCW_SPRING_MAIN, -4053, 2894, 587): [ # Mumbo Token
		],
	(Room_Enums.CCW_SPRING_MAIN, -2649, 0, -395): [ # Mumbo Token
		],
	(Room_Enums.CCW_SPRING_MAIN, -2750, 4586, -513): [ # Mumbo Token
		],
	(Room_Enums.CCW_SPRING_MAIN, 0, 3513, -5240): [ # Mumbo Token
		],
	(Room_Enums.CCW_SPRING_MAIN, 1904, 105, -2706): [ # Mumbo Token
		],
	(Room_Enums.CCW_SPRING_MAIN, 1000, 105, 5300): [ # Mumbo Token
		],
	(Room_Enums.CCW_SPRING_MAIN, 6134, 4244, 306): [ # Mumbo Token
		],
	(Room_Enums.CCW_SPRING_MAIN, -50, 1050, -2750): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 0, 5760, -3330): [ # Green Jinjo
		],
	(Room_Enums.CCW_SPRING_MAIN, 0, 7625, 3100): [ # Jiggy
		],
	(Room_Enums.CCW_SPRING_MAIN, -6660, 604, -625): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -6330, 604, -375): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -6660, 603, 625): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -6330, 604, 375): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -2431, 4573, 355): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -2182, 4522, 1122): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -1857, 4473, 1591): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -1355, 4423, 2009): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -879, 4423, 2278): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, 0, 3354, -3150): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, 0, 3314, -2950): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, 0, 3314, -2750): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, 4806, -592, -741): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, 4355, -596, 295): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, 5837, -587, -305): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, 5397, -589, 741): [ # Red Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -5468, 4900, -315): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -5018, 4900, -773): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -5468, 4900, 314): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -5018, 4900, 773): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -4378, 4900, -764): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -4378, 4900, 764): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -3930, 4900, -315): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -3930, 4900, 316): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -2579, 900, 980): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -2750, 900, 0): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -2579, 1100, -980): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -2140, 2938, -1157): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -1950, 937, -1950): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -1950, 1350, 1950): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -1072, 3157, -2180): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -1696, 3050, -1731): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -975, 900, -2575): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -977, 900, 2573): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 975, 900, -2574): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 0, 900, 2750): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 975, 900, 2573): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 790, 3300, -2345): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 1950, 900, -1949): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 1950, 900, 1950): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 1427, 3300, -1995): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 1873, 3899, -1580): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 2568, 900, -968): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 2566, 900, 968): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 2750, 900, 0): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 2267, 3963, -1018): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 2450, 4019, -394): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 3653, 3719, 1587): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 3080, 3719, 2063): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 4366, -599, -311): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 4769, -600, 726): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 4302, 3719, 583): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 4214, 3719, 1076): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 5404, -593, -734): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, 5831, -589, 301): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MAIN, -3912, 863, -3912): [ # Gold Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -3855, 1395, 3839): [ # Gold Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -3700, 2921, -40): [ # Gold Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, 4050, 4236, 1010): [ # Gold Feather
		],
	(Room_Enums.CCW_SPRING_MAIN, -3325, 300, -3325): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, -3150, 307, -3150): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, -3100, 921, 3100): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, -2975, 300, -2975): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, -2700, 900, 2700): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, -2900, 900, 2900): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, -500, 52, -5850): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, -500, 48, -4950): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, 500, 52, -5850): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, 500, 59, -4950): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, 2875, 894, 2875): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, 2826, 1275, -2825): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, 3075, 876, 3075): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, 3275, 845, 3274): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, 3225, 1275, -3225): [ # Note
		],
	(Room_Enums.CCW_SPRING_MAIN, 3025, 1275, -3025): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, -6838, 600, 509): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4343, 2834, 301): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_SUMMER_MAIN, -3153, 300, -3174): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_SUMMER_MAIN, -1600, 4019, 4300): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_SUMMER_MAIN, -89, 0, 3179): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_SUMMER_MAIN, 1264, 0, -3120): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_SUMMER_MAIN, 3157, 4085, 115): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_SUMMER_MAIN, 6256, -600, 30): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4661, 2800, -1248): [ # Mumbo Token
		],
	(Room_Enums.CCW_SUMMER_MAIN, -3578, 40, -4259): [ # Mumbo Token
		],
	(Room_Enums.CCW_SUMMER_MAIN, -3855, 1428, 3840): [ # Mumbo Token
		],
	(Room_Enums.CCW_SUMMER_MAIN, -1861, 4469, 1583): [ # Mumbo Token
		],
	(Room_Enums.CCW_SUMMER_MAIN, 2700, -600, 0): [ # Mumbo Token
		],
	(Room_Enums.CCW_SUMMER_MAIN, 2043, 3534, 1799): [ # Mumbo Token
		],
	(Room_Enums.CCW_SUMMER_MAIN, -3602, 0, 4266): [ # Yellow Jinjo
		],
	(Room_Enums.CCW_SUMMER_MAIN, 2215, 2616, 2142): [ # Jiggy
		],
	(Room_Enums.CCW_SUMMER_MAIN, 6070, 4244, -113): [ # Jiggy
		],
	(Room_Enums.CCW_SUMMER_MAIN, 3604, 22, -4012): [ # Extra Life
		],
	(Room_Enums.CCW_SUMMER_MAIN, 5848, 4244, 612): [ # Extra Life
		],
	(Room_Enums.CCW_SUMMER_MAIN, -5428, 2881, -775): [ # Gold Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -5917, 2587, 10): [ # Gold Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -3901, 856, -3901): [ # Gold Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 1273, 4547, 3647): [ # Gold Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -5471, 4904, -319): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -5020, 4904, -774): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -5470, 4904, 320): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -5020, 4904, 774): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4760, 2745, -1741): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4449, 2838, -846): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4969, 2788, 1195): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4380, 4904, -775): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4380, 4904, 775): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -3691, 2836, -788): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -3603, 2786, 1444): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -3930, 4904, -321): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -3930, 4904, 320): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -2570, 904, 970): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -2750, 904, 0): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -2590, 1104, -978): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -1950, 941, -1950): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -1950, 1354, 1950): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -970, 904, -2570): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -970, 904, 2570): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -50, 1050, -2750): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 970, 904, -2570): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 0, 904, 2750): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 970, 904, 2570): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 1951, -600, 0): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 1951, 904, -1950): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 1949, 904, 1950): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 2336, -596, -1937): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 2449, -600, 0): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 2332, -596, 1942): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 2570, 904, -970): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 2570, 904, 970): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 2750, 904, 0): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 3967, -596, 3497): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 3458, 4111, -565): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 3641, 4108, 454): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 3371, 4107, 1037): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 4166, -596, -3854): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, 4509, 4216, -978): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4815, 125, -201): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4585, 125, -200): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4930, 125, 0): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4815, 125, 200): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4585, 125, 200): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -4470, 125, 0): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -2047, 4019, 4303): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -1603, 4019, 3851): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -1920, 4019, 3996): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -1599, 4019, 4747): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -1284, 4019, 4611): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -1153, 4019, 4293): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -635, 5, -6006): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -727, 5, -5426): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -633, 5, -4826): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, 9, 5, -6099): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, 634, 5, -6008): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, 726, 5, -5426): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, 636, 5, -4834): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, 9, 5, -4734): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MAIN, -123, 308, 3059): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, -700, 4819, 4750): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, -400, 4819, 4450): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 115, 608, 3056): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 0, 3350, -3150): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 0, 3300, -2750): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 0, 3310, -2950): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 700, 4819, 4750): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 0, 4819, 4400): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 400, 4819, 4450): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 1700, -589, 0): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 2201, -600, 0): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 4728, 4244, -522): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 4671, 4243, -329): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 4562, 4243, 54): [ # Note
		],
	(Room_Enums.CCW_SUMMER_MAIN, 4507, 4244, 249): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -5929, 2586, 61): [ # Mumbo Token
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 500, 166, 5125): [ # Mumbo Token
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 153, 1857, 2677): [ # Mumbo Token
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 0, 5830, -3325): [ # Mumbo Token
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 3405, 4107, 1003): [ # Mumbo Token
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -5475, 4900, 0): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -4042, 2894, 586): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3388, 900, -4173): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -2842, 900, -58): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 0, 3747, -4730): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 0, 5670, -2812): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 1592, 899, -5982): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 1380, 700, 5790): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 3884, 635, 3862): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 4290, 3719, -145): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -2377, 3490, 3524): [ # CCW Acorn
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 63, 3819, 5000): [ # CCW Acorn
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 0, 4868, 5000): [ # CCW Acorn
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 0, 5143, 5600): [ # CCW Acorn
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -1592, 900, -6073): [ # Orange Jinjo
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -225, 640, 506): [ # Extra Life
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 4050, 4284, 1010): [ # Extra Life
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 240, 600, 75): [ # Jiggy
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 2215, 2616, 2140): [ # Jiggy
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 6037, 4244, -157): [ # Jiggy
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -5700, 40, -1000): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -5500, 40, -500): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -5350, 40, 0): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -5370, 2882, -787): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -4431, 2830, -882): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -4356, 2821, 356): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -4920, 2778, 1222): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3735, 2828, -787): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3615, 2773, 1411): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -2181, 4519, 1118): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -1860, 4469, 1580): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -1362, 4419, 2014): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -113, 304, 3001): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 536, 758, 628): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 825, 758, 531): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 682, 758, 583): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 115, 605, 3001): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 3513, 4102, -541): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 3595, 4104, 478): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -5471, 4900, -313): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -5024, 4900, -766): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -5471, 4900, 312): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -5024, 4900, 766): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -4376, 4900, -766): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -4375, 4900, 765): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3801, 1452, 3790): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3801, 1532, 3790): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3801, 1612, 3790): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3929, 4900, -313): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3929, 4900, 312): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -2750, 900, 0): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -2577, 900, 972): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -2584, 1100, -971): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -1950, 937, -1950): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -1950, 1350, 1950): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -950, 10, -6531): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -475, 10, -6599): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -970, 900, -2570): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -968, 900, 2578): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -50, 1100, -2750): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 0, 10, -6640): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 475, 10, -6599): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 950, 10, -6531): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 970, 900, -2569): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 613, 998, 664): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 768, 998, 596): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 0, 900, 2750): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 969, 900, 2569): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 1905, 170, -2705): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 1905, 250, -2705): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 1905, 330, -2705): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 1950, 900, -1950): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 1950, 900, 1950): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 2570, 900, -970): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 2569, 900, 969): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 2750, 900, 0): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -4806, 2735, -1718): [ # Gold Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3906, 860, -3907): [ # Gold Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -1384, 704, 5801): [ # Gold Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 4501, 4210, -935): [ # Gold Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3287, 6, 3713): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3116, 6, 3430): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3587, 6, 4251): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -3391, 6, 4014): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -2882, 6, 3196): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -696, 4823, 4997): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -518, 4823, 4572): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, -525, 4823, 5422): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 518, 4823, 4573): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 696, 4823, 5000): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 525, 4823, 5422): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 1946, 20, 4673): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 2384, 20, 4564): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 2799, 20, 4466): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 3255, 20, 4325): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MAIN, 3661, 20, 4206): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, -6775, 1301, 0): [ # Blue Jinjo
		],
	(Room_Enums.CCW_WINTER_MAIN, -3157, 300, -3149): [ # Mumbo Token
		],
	(Room_Enums.CCW_WINTER_MAIN, 0, 105, -5400): [ # Mumbo Token
		],
	(Room_Enums.CCW_WINTER_MAIN, 0, 3138, -3696): [ # Mumbo Token
		],
	(Room_Enums.CCW_WINTER_MAIN, 40, 3969, 5000): [ # Mumbo Token
		],
	(Room_Enums.CCW_WINTER_MAIN, 5950, -46, 0): [ # Mumbo Token
		],
	(Room_Enums.CCW_WINTER_MAIN, -1600, 4019, 4300): [ # Extra Life
		],
	(Room_Enums.CCW_WINTER_MAIN, 3078, -338, 3076): [ # Extra Life
		],
	(Room_Enums.CCW_WINTER_MAIN, 694, 998, 632): [ # Empty Honeycomb
		],
	(Room_Enums.CCW_WINTER_MAIN, 240, 600, 75): [ # Jiggy
		],
	(Room_Enums.CCW_WINTER_MAIN, 0, 7610, 3100): [ # Jiggy
		],
	(Room_Enums.CCW_WINTER_MAIN, -6161, 2604, 186): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, -5387, 2704, -1571): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, -5186, 2903, -867): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, -4781, 2804, 1416): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, -3854, 1361, 3840): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, -3690, 2889, -74): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, 0, 5756, -3325): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, 1901, 544, -2705): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, 1000, 243, 5300): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, 4050, 4205, 1010): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, 5147, 436, -144): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_MAIN, -4654, 2800, -1243): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -4034, 2899, -939): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -4652, 2800, 647): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -4040, 2894, 583): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -2308, 4869, -1528): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -2637, 4569, -871): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -2051, 4019, 4300): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -1599, 4019, 3851): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -1599, 4019, 4750): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -1150, 4019, 4300): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -1691, 5210, -2199): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, -764, 5590, -2634): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, 4741, 4958, -106): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, 5987, 4958, 252): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, 5571, 4957, 132): [ # Note
		],
	(Room_Enums.CCW_WINTER_MAIN, 5156, 4957, 13): [ # Note
		],
	(Room_Enums.CCW_SPRING_MUMBOS_SKULL, -500, 398, 0): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MUMBOS_SKULL, 0, 398, -520): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MUMBOS_SKULL, 0, 398, 520): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_MUMBOS_SKULL, 510, 387, 0): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_MUMBOS_SKULL, 0, 416, 500): [ # Mumbo Token
		],
	(Room_Enums.CCW_SUMMER_MUMBOS_SKULL, -127, 4, -308): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MUMBOS_SKULL, -288, 4, -154): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MUMBOS_SKULL, 119, 4, -298): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_MUMBOS_SKULL, 286, 4, -155): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_MUMBOS_SKULL, 84, 0, -105): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_MUMBOS_SKULL, -359, 379, -359): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MUMBOS_SKULL, -360, 398, 375): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MUMBOS_SKULL, 362, 379, -365): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_MUMBOS_SKULL, 363, 398, 364): [ # Note
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, -131, 402, -496): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, -362, 383, -362): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, -490, 402, -131): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, -493, 383, 126): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, -131, 402, 496): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, -361, 402, 365): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, 361, 383, -363): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, 498, 398, -129): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, 136, 402, -499): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, 495, 401, 133): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, 359, 402, 362): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_MUMBOS_SKULL, 134, 383, 497): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_ZUBBA, 0, 0, 125): [ # Jiggy
		],
	(Room_Enums.CCW_SPRING_ZUBBA, -225, 1039, -1100): [ # Pink Jinjo
		],
	(Room_Enums.CCW_SPRING_ZUBBA, 0, 0, 125): [ # Jiggy
		],
	(Room_Enums.CCW_AUTUMN_ZUBBA, 0, -18, 124): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_ZUBBA, -674, -1, 925): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_ZUBBA, -674, 0, -900): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_ZUBBA, 675, -2, 925): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_ZUBBA, 675, 0, -674): [ # Note
		],
	(Room_Enums.CCW_SPRING_NABNUT, -575, 300, -139): [ # Mumbo Token
		],
	(Room_Enums.CCW_SPRING_NABNUT, 287, 413, -357): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_NABNUT, 383, 413, -295): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_NABNUT, 472, 413, -237): [ # Blue Egg
		],
	(Room_Enums.CCW_SUMMER_NABNUT, -646, 517, -5): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_NABNUT, -577, 517, -109): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_NABNUT, -505, 517, -205): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_NABNUT, -395, 517, -281): [ # Red Feather
		],
	(Room_Enums.CCW_SUMMER_NABNUT, -286, 517, -354): [ # Red Feather
		],
	(Room_Enums.CCW_AUTUMN_NABNUT, -508, 513, -199): [ # CCW Acorn
		],
	(Room_Enums.CCW_AUTUMN_NABNUT, 608, 150, 52): [ # CCW Caterpillar
		],
	(Room_Enums.CCW_AUTUMN_NABNUT, 288, 413, -357): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_NABNUT, 382, 413, -296): [ # Note
		],
	(Room_Enums.CCW_AUTUMN_NABNUT, 471, 413, -235): [ # Note
		],
	(Room_Enums.CCW_WINTER_NABNUT, -285, 513, -354): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_NABNUT, -646, 513, -5): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_NABNUT, -395, 513, -280): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_NABNUT, -577, 513, -110): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_NABNUT, -504, 513, -205): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_NABNUT, -581, 304, -137): [ # Gold Feather
		],
	(Room_Enums.CCW_WINTER_NABNUT, 495, 417, -221): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_NABNUT, 419, 417, -271): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_NABNUT, 345, 417, -322): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_NABNUT, 269, 417, -373): [ # Red Feather
		],
	(Room_Enums.CCW_WINTER_FLOODED_ATTIC, 640, 513, -202): [ # Empty Honeycomb
		],
	(Room_Enums.CCW_WINTER_FLOODED_ATTIC, -531, 450, -430): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_FLOODED_ATTIC, 244, 150, -509): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_FLOODED_ATTIC, 88, 250, 682): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_FLOODED_ATTIC, 0, -500, 0): [ # CCW Acorn
		],
	(Room_Enums.CCW_AUTUMN_FLOODED_ATTIC, -170, 0, -700): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_FLOODED_ATTIC, 0, -20, -630): [ # Blue Egg
		],
	(Room_Enums.CCW_AUTUMN_FLOODED_ATTIC, 170, 0, -699): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_ACORN_STORAGE, -624, -499, -254): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_ACORN_STORAGE, -262, -500, -619): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_ACORN_STORAGE, -622, -499, 259): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_ACORN_STORAGE, -254, -500, 621): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_ACORN_STORAGE, 253, -500, -621): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_ACORN_STORAGE, 617, -499, -263): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_ACORN_STORAGE, 258, -500, 624): [ # Blue Egg
		],
	(Room_Enums.CCW_WINTER_ACORN_STORAGE, 621, -499, 254): [ # Blue Egg
		],
	(Room_Enums.CCW_SPRING_WHIPCRACKS, -310, 730, -855): [ # Extra Life
		],
	(Room_Enums.CCW_SPRING_WHIPCRACKS, -693, 2, 528): [ # Extra Life
		],
	(Room_Enums.CCW_SPRING_WHIPCRACKS, 0, 17, 225): [ # Jiggy
		],
	(Room_Enums.CCW_SUMMER_WHIPCRACKS, 0, 17, 225): [ # Jiggy
		],
	(Room_Enums.CCW_SUMMER_WHIPCRACKS, 833, 441, 133): [ # Extra Life
		],
	(Room_Enums.CCW_AUTUMN_WHIPCRACKS, -310, 730, -856): [ # Extra Life
		],
	(Room_Enums.CCW_AUTUMN_WHIPCRACKS, 0, 17, 225): [ # Jiggy
		],
	(Room_Enums.CCW_WINTER_WHIPCRACKS, 0, 17, 225): [ # Jiggy
		],
    #######################
    ### GRUNTILDAS LAIR ###
    #######################
	(Room_Enums.GL_MM_ENTRANCE, -2068, 1131, -3779): [ # Bottles Mound (Note Door)
		],
	(Room_Enums.GL_MM_ENTRANCE, -1505, 600, 123): [ # Jiggy
        [Move_Enums.HIGH_JUMP],
        [Move_Enums.FEATHERY_FLAP],
        [Move_Enums.FLAP_FLIP],
        [Move_Enums.RAT_A_TAP_RAP],
        [Move_Enums.TALON_TROT],
		],
	(Room_Enums.GL_MM_ENTRANCE, 2928, 0, -2054): [ # MM Red Flower
		],
	(Room_Enums.GL_MM_ENTRANCE, 3736, 0, -1617): [ # MM Red Flower
		],
	(Room_Enums.GL_MM_ENTRANCE, 3148, 0, -844): [ # MM Red Flower
		],
	(Room_Enums.GL_MM_ENTRANCE, 3214, 0, -2238): [ # MM Orange Yellow Flower
		],
	(Room_Enums.GL_MM_ENTRANCE, 3769, 0, -1235): [ # MM Orange Yellow Flower
		],
	(Room_Enums.GL_TTC_CC_PUZZLES, 162, -750, 4611): [ # Mumbo Token
		],
	(Room_Enums.GL_TTC_CC_PUZZLES, -1410, -749, 3551): [ # Blue Egg
		],
	(Room_Enums.GL_TTC_CC_PUZZLES, -1412, -750, 4335): [ # Blue Egg
		],
	(Room_Enums.GL_TTC_CC_PUZZLES, -885, -749, 3037): [ # Blue Egg
		],
	(Room_Enums.GL_TTC_CC_PUZZLES, -98, -749, 3041): [ # Blue Egg
		],
	(Room_Enums.GL_TTC_CC_PUZZLES, -864, -750, 4881): [ # Blue Egg
		],
	(Room_Enums.GL_TTC_CC_PUZZLES, -114, -750, 4871): [ # Blue Egg
		],
	(Room_Enums.GL_TTC_CC_PUZZLES, 418, -750, 3577): [ # Blue Egg
		],
	(Room_Enums.GL_TTC_CC_PUZZLES, 422, -750, 4333): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_PUZZLE, 3599, -478, 2424): [ # Extra Life
		],
	(Room_Enums.GL_CCW_PUZZLE, 4936, -478, 286): [ # Mumbo Token
		],
	(Room_Enums.GL_CCW_PUZZLE, -9, -1395, 1178): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_PUZZLE, -185, -1395, 1477): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_PUZZLE, 820, -1395, 1183): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_PUZZLE, 382, -1395, 1090): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_PUZZLE, 820, -1395, 1692): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_PUZZLE, 445, -1395, 1832): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_PUZZLE, 27, -1395, 1781): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_PUZZLE, 4808, -474, 2371): [ # Gold Feather
		],
	(Room_Enums.GL_CAULDRON_PIPE, -180, 351, -750): [ # Mumbo Token
		],
	(Room_Enums.GL_CAULDRON_PIPE, 261, 717, 988): [ # Gold Feather
		],
	(Room_Enums.GL_TTC_ENTRANCE, -1160, 609, -1945): [ # Red Feather
		],
	(Room_Enums.GL_TTC_ENTRANCE, -37, 609, -1945): [ # Red Feather
		],
	(Room_Enums.GL_TTC_ENTRANCE, -413, 609, -1945): [ # Red Feather
		],
	(Room_Enums.GL_TTC_ENTRANCE, -786, 609, -1945): [ # Red Feather
		],
	(Room_Enums.GL_TTC_ENTRANCE, 950, 904, -1945): [ # Red Feather
		],
	(Room_Enums.GL_TTC_ENTRANCE, 335, 609, -1945): [ # Red Feather
		],
	(Room_Enums.GL_TTC_ENTRANCE, 565, 904, -1945): [ # Red Feather
		],
	(Room_Enums.GL_TTC_ENTRANCE, 1335, 904, -1945): [ # Red Feather
		],
	(Room_Enums.GL_GV_ENTRANCE, -1486, 0, -922): [ # Mumbo Token
		],
	(Room_Enums.GL_GV_ENTRANCE, -1290, 514, -787): [ # Jiggy
		],
	(Room_Enums.GL_GV_ENTRANCE, 1860, -137, 2920): [ # Red Feather
		],
	(Room_Enums.GL_GV_ENTRANCE, 1640, -137, 4119): [ # Red Feather
		],
	(Room_Enums.GL_GV_ENTRANCE, 1143, -137, 4151): [ # Red Feather
		],
	(Room_Enums.GL_GV_ENTRANCE, 2334, -137, 3540): [ # Red Feather
		],
	(Room_Enums.GL_GV_ENTRANCE, 2113, -137, 3242): [ # Red Feather
		],
	(Room_Enums.GL_GV_ENTRANCE, 2120, -137, 4086): [ # Red Feather
		],
	(Room_Enums.GL_GV_ENTRANCE, 2799, 0, -2071): [ # Blue Egg
		],
	(Room_Enums.GL_GV_ENTRANCE, 2911, 0, -1907): [ # Blue Egg
		],
	(Room_Enums.GL_GV_ENTRANCE, 3120, 0, -1616): [ # Blue Egg
		],
	(Room_Enums.GL_GV_ENTRANCE, 3016, 0, -1764): [ # Blue Egg
		],
	(Room_Enums.GL_FP_ENTRANCE, 2954, 1247, 100): [ # Extra Life
		],
	(Room_Enums.GL_FP_ENTRANCE, 4155, 1485, 6270): [ # Mumbo Token
		],
	(Room_Enums.GL_FP_ENTRANCE, 4126, 2392, 6559): [ # Jiggy
		],
	(Room_Enums.GL_FP_ENTRANCE, 594, 1453, 4846): [ # Gold Feather
		],
	(Room_Enums.GL_FP_ENTRANCE, 50, 2009, -1065): [ # Blue Egg
		],
	(Room_Enums.GL_FP_ENTRANCE, 50, 2009, -605): [ # Blue Egg
		],
	(Room_Enums.GL_FP_ENTRANCE, 50, 2009, -145): [ # Blue Egg
		],
	(Room_Enums.GL_FP_ENTRANCE, 50, 2009, 315): [ # Blue Egg
		],
	(Room_Enums.GL_FP_ENTRANCE, 50, 2009, 775): [ # Blue Egg
		],
	(Room_Enums.GL_FP_ENTRANCE, 50, 2009, 1235): [ # Blue Egg
		],
	(Room_Enums.GL_FP_ENTRANCE, 4021, 301, 7249): [ # Red Feather
		],
	(Room_Enums.GL_FP_ENTRANCE, 4042, 301, 7185): [ # Red Feather
		],
	(Room_Enums.GL_FP_ENTRANCE, 4058, 301, 7125): [ # Red Feather
		],
	(Room_Enums.GL_FP_ENTRANCE, 4074, 301, 7065): [ # Red Feather
		],
	(Room_Enums.GL_CC_ENTRANCE, 0, 850, -2450): [ # Mumbo Token
		],
	(Room_Enums.GL_CC_ENTRANCE, -7264, 496, -1392): [ # Blue Egg
		],
	(Room_Enums.GL_CC_ENTRANCE, -7018, 426, -1640): [ # Blue Egg
		],
	(Room_Enums.GL_CC_ENTRANCE, -7264, 495, 389): [ # Blue Egg
		],
	(Room_Enums.GL_CC_ENTRANCE, -7018, 426, 641): [ # Blue Egg
		],
	(Room_Enums.GL_CC_ENTRANCE, -6732, 277, -1767): [ # Blue Egg
		],
	(Room_Enums.GL_CC_ENTRANCE, -6392, 122, -1749): [ # Blue Egg
		],
	(Room_Enums.GL_CC_ENTRANCE, -6732, 277, 765): [ # Blue Egg
		],
	(Room_Enums.GL_CC_ENTRANCE, -6392, 122, 744): [ # Blue Egg
		],
	(Room_Enums.GL_CC_ENTRANCE, -1700, 582, -1101): [ # Red Feather
		],
	(Room_Enums.GL_CC_ENTRANCE, -1700, 582, -100): [ # Red Feather
		],
	(Room_Enums.GL_CC_ENTRANCE, -1700, 582, -435): [ # Red Feather
		],
	(Room_Enums.GL_CC_ENTRANCE, -1700, 582, -766): [ # Red Feather
		],
	(Room_Enums.GL_BGS_ENTRANCE, -1992, 878, -3052): [ # Extra Life
		],
	(Room_Enums.GL_BGS_ENTRANCE, -2099, -195, 701): [ # Gold Feather
		],
	(Room_Enums.GL_BGS_ENTRANCE, 166, 650, -6941): [ # Gold Feather
		],
	(Room_Enums.GL_BGS_ENTRANCE, 2726, -176, -6393): [ # Blue Egg
		],
	(Room_Enums.GL_BGS_ENTRANCE, 2986, -176, -6339): [ # Blue Egg
		],
	(Room_Enums.GL_BGS_ENTRANCE, 3277, -176, -6332): [ # Blue Egg
		],
	(Room_Enums.GL_BGS_ENTRANCE, 3552, -176, -6394): [ # Blue Egg
		],
	(Room_Enums.GL_GV_PUZZLE, 6869, 813, -270): [ # Gold Feather
		],
	(Room_Enums.GL_GV_PUZZLE, 6314, 813, -984): [ # Gold Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, -8689, -1781, -3192): [ # Extra Life
		],
	(Room_Enums.GL_MMM_ENTRANCE, -8860, -2087, -2444): [ # Red Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, -8532, -2021, -2269): [ # Red Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, -8204, -1955, -3732): [ # Red Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, -7871, -1888, -3549): [ # Red Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, -3164, 478, 1720): [ # Red Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, -537, -48, 3134): [ # Red Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, -399, -553, 4743): [ # Red Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, -710, -485, 4155): [ # Red Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, 1702, -515, 3503): [ # Red Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, 1806, 114, 804): [ # Red Feather
		],
	(Room_Enums.GL_MMM_ENTRANCE, -458, -768, 6764): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_ENTRANCE, -300, -792, 6800): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_ENTRANCE, 888, -802, 6826): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_ENTRANCE, 1004, -800, 6827): [ # Blue Egg
		],
	(Room_Enums.GL_640_NOTE_DOOR, 1256, 2582, 0): [ # Mumbo Token
		],
	(Room_Enums.GL_640_NOTE_DOOR, -1028, -1096, -279): [ # Red Feather
		],
	(Room_Enums.GL_640_NOTE_DOOR, -1025, -1096, 273): [ # Red Feather
		],
	(Room_Enums.GL_640_NOTE_DOOR, -753, -1096, -758): [ # Red Feather
		],
	(Room_Enums.GL_640_NOTE_DOOR, -756, -1096, 757): [ # Red Feather
		],
	(Room_Enums.GL_640_NOTE_DOOR, -264, -1096, 1028): [ # Red Feather
		],
	(Room_Enums.GL_640_NOTE_DOOR, 757, -1095, -755): [ # Red Feather
		],
	(Room_Enums.GL_640_NOTE_DOOR, 756, -1096, 752): [ # Red Feather
		],
	(Room_Enums.GL_640_NOTE_DOOR, 275, -1093, 1034): [ # Red Feather
		],
	(Room_Enums.GL_640_NOTE_DOOR, 1027, -1096, -275): [ # Red Feather
		],
	(Room_Enums.GL_640_NOTE_DOOR, 1032, -1096, 275): [ # Red Feather
		],
	(Room_Enums.GL_640_NOTE_DOOR, -566, 1332, 1650): [ # Gold Feather
		],
	(Room_Enums.GL_RBB_ENTRANCE, 1764, -1400, -1136): [ # Mumbo Token
		],
	(Room_Enums.GL_RBB_ENTRANCE, -1630, 0, 310): [ # Blue Egg
		],
	(Room_Enums.GL_RBB_ENTRANCE, -1630, 0, 180): [ # Blue Egg
		],
	(Room_Enums.GL_RBB_ENTRANCE, -1499, 0, 310): [ # Blue Egg
		],
	(Room_Enums.GL_RBB_ENTRANCE, -1499, 0, 180): [ # Blue Egg
		],
	(Room_Enums.GL_RBB_ENTRANCE, -1371, 754, 332): [ # Red Feather
		],
	(Room_Enums.GL_RBB_ENTRANCE, -1447, 754, 191): [ # Red Feather
		],
	(Room_Enums.GL_RBB_ENTRANCE, -1615, 1450, 1927): [ # Gold Feather
		],
	(Room_Enums.GL_MMM_PUZZLE, -1140, 707, 1973): [ # Mumbo Token
		],
	(Room_Enums.GL_MMM_PUZZLE, -838, 1950, 835): [ # Extra Life
		],
	(Room_Enums.GL_MMM_PUZZLE, -1344, -1492, -1346): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, -1832, -1486, -499): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, -1835, -1486, 485): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, -1335, -1482, 1349): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, -499, -1492, -1836): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, 491, -1490, -1832): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, 1342, -1486, -1349): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, 1833, -1492, -491): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, 1846, -1492, 503): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, 1341, -1492, 1361): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, 7900, 1750, -1358): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, 7900, 1750, -1445): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_PUZZLE, 6900, 1754, -1711): [ # Red Feather
		],
	(Room_Enums.GL_MMM_PUZZLE, 6900, 1754, -1588): [ # Red Feather
		],
	(Room_Enums.GL_MMM_PUZZLE, 7833, 2004, -860): [ # Gold Feather
		],
	(Room_Enums.GL_CCW_ENTRANCE, 0, 1600, -3700): [ # Extra Life
		],
	(Room_Enums.GL_CCW_ENTRANCE, -1874, 804, 1884): [ # Red Feather
		],
	(Room_Enums.GL_CCW_ENTRANCE, -1673, 804, 2120): [ # Red Feather
		],
	(Room_Enums.GL_CCW_ENTRANCE, -1480, 804, 2326): [ # Red Feather
		],
	(Room_Enums.GL_CCW_ENTRANCE, 1874, 804, 1884): [ # Red Feather
		],
	(Room_Enums.GL_CCW_ENTRANCE, 1673, 804, 2120): [ # Red Feather
		],
	(Room_Enums.GL_CCW_ENTRANCE, 1480, 804, 2327): [ # Red Feather
		],
	(Room_Enums.GL_CCW_ENTRANCE, 0, -546, 4229): [ # Gold Feather
		],
	(Room_Enums.GL_CCW_ENTRANCE, 3, 440, 1899): [ # Gold Feather
		],
	(Room_Enums.GL_CCW_ENTRANCE, 0, 800, 3600): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_ENTRANCE, 0, 800, 4800): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_ENTRANCE, 0, 800, 4400): [ # Blue Egg
		],
	(Room_Enums.GL_CCW_ENTRANCE, 0, 800, 4001): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_SHED, 1488, 249, 0): [ # Mumbo Token
		],
	(Room_Enums.GL_MMM_SHED, -126, 0, -637): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_SHED, -898, 0, -630): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_SHED, -112, 0, 630): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_SHED, -899, 0, 630): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_SHED, 671, 0, -637): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_SHED, 671, 0, 631): [ # Blue Egg
		],
	(Room_Enums.GL_MMM_SHED, -331, 10, 0): [ # Gold Feather
		],
	(Room_Enums.GL_FURNACE_FUN, -1250, 0, -1450): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, -1750, 0, -200): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, -1750, 0, 800): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, -1750, 0, 300): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, -750, 0, -950): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, -250, 0, -450): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, -250, 0, 300): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, -750, 0, 800): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, -250, 0, 1050): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, -750, 0, 1800): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, 500, 0, -1450): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, 0, 0, 1800): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, 250, 0, 1300): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, 1500, 0, -450): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, 1000, 0, 550): [ # Honeycomb
		],
	(Room_Enums.GL_FURNACE_FUN, -1500, 0, 1800): [ # Extra Life
		],
	(Room_Enums.GL_FURNACE_FUN, 1000, 0, -1450): [ # Extra Life
		],
	(Room_Enums.GL_FURNACE_FUN, 1750, 0, -1450): [ # Extra Life
		],
	(Room_Enums.GL_FINAL_ROOM, -80, 235, -519): [ # Extra Life
		],
	(Room_Enums.FINAL_BATTLE_ARENA, -2061, 4, -1101): [ # Red Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, -1630, 4, 290): [ # Red Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, -1100, 4, 2060): [ # Red Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, -290, 4, -1631): [ # Red Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, 286, 4, 1630): [ # Red Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, 1100, 0, -2061): [ # Red Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, 1630, 4, -290): [ # Red Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, 2060, 4, 1100): [ # Red Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, -2061, 0, 1099): [ # Blue Egg
		],
	(Room_Enums.FINAL_BATTLE_ARENA, -1099, 0, -2060): [ # Blue Egg
		],
	(Room_Enums.FINAL_BATTLE_ARENA, -1630, 0, -290): [ # Blue Egg
		],
	(Room_Enums.FINAL_BATTLE_ARENA, -290, 0, 1630): [ # Blue Egg
		],
	(Room_Enums.FINAL_BATTLE_ARENA, 289, 0, -1630): [ # Blue Egg
		],
	(Room_Enums.FINAL_BATTLE_ARENA, 1631, 0, 290): [ # Blue Egg
		],
	(Room_Enums.FINAL_BATTLE_ARENA, 1101, 0, 2061): [ # Blue Egg
		],
	(Room_Enums.FINAL_BATTLE_ARENA, 2060, 0, -1101): [ # Blue Egg
		],
	(Room_Enums.FINAL_BATTLE_ARENA, -1990, 4, -1990): [ # Gold Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, -1991, 4, 1991): [ # Gold Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, 1992, 4, -1990): [ # Gold Feather
		],
	(Room_Enums.FINAL_BATTLE_ARENA, 1990, 4, 1990): [ # Gold Feather
		],
	}

###############################################################################
######################### ADDITIONAL OBJECT LOCATIONS #########################
###############################################################################

ADDITIONAL_OBJECT_LOCATIONS_DICT = {
    #######################
    ### Spiral Mountain ###
    #######################
    (Room_Enums.SM_MAIN, -2975, 1291, -1821): [ # Tree 1
        ], 
    (Room_Enums.SM_MAIN, -344, 835, -2224): [ # Tree 2
        ],
    (Room_Enums.SM_MAIN, 966, 750, 1807): [ # Tree 3
        ],
    (Room_Enums.SM_MAIN, 3, 49, 4847): [ # Stump 1
        ],
    (Room_Enums.SM_MAIN, 1018, 99, 4770): [ # Stump 2
        ],
    (Room_Enums.SM_MAIN, 1181, 49, 3994): [ # Stump 3
        ],
    (Room_Enums.SM_MAIN, -2, -50, 3977): [ # Stump 4
        ],
    (Room_Enums.SM_MAIN, -779, 49, 3581): [ # Stump 5
        ],
    (Room_Enums.SM_MAIN, -3429, 575, -1015): [ # Under Stone Bridge
        ],
    (Room_Enums.SM_MAIN, -5765, 50, -1681): [ # In Pond
        ],
    (Room_Enums.SM_BANJOS_HOUSE, 61, 6, -66): [ # Rug
        ],
    #######################
    ### Mumbos Mountain ###
    #######################
    (Room_Enums.MM_MAIN, 5147, 788, 2874): [ # Tree 1
        ],
    (Room_Enums.MM_MAIN, 3459, 755, 2636): [ # Tree 2
        ],
    (Room_Enums.MM_MAIN, 5818, 2354, -3218): [ # Behind Skull
        ],
    (Room_Enums.MM_MAIN, 5274, 2756, -2905): [ # Other Mumbos Eye
        ],
    (Room_Enums.MM_MAIN, 5595, 3089, -2972): [ # Atop Mumbos Skull
        ],
    (Room_Enums.MM_INSIDE_TICKERS_TOWER, -10, 0, -26): [ # Floor 1
        ],
    (Room_Enums.MM_INSIDE_TICKERS_TOWER, -10, 817, -26): [ # Floor 2
        ],
    (Room_Enums.MM_INSIDE_TICKERS_TOWER, -10, 1507, -26): [ # Floor 3
        ],
    (Room_Enums.MM_MUMBOS_SKULL, 0, 600, 0): [ # Ceiling
        ],
    ###########################
    ### Treasure Trove Cove ###
    ###########################
    (Room_Enums.TTC_MAIN, 4118, -14, -7566): [ # Underwater Gap
        ],
    #######################
    ### Clankers Cavern ###
    #######################
    (Room_Enums.CC_MAIN, -9586, 4045, 1480): [ # Underneath Entrance
        ],
    (Room_Enums.CC_MAIN, 6768, 2145, 3500): [ # Middle Of Long Pipe
        ],
    (Room_Enums.CC_MAIN, 14177, 3231, -21): [ # Mutie Snippets Under Pipe
        ],
    #########################
    ### Bubblegloop Swamp ###
    #########################
    (Room_Enums.BGS_MAIN, -6592, 1717, -5498): [ # Atop Mumbos Skull
        ],
    (Room_Enums.BGS_MAIN, -8885, 0, -6143): [ # Corner Under Maze Switch
        ],
    (Room_Enums.BGS_MAIN, -3360, 0, -2192): [ # Corner Near Path To Maze
        ],
    (Room_Enums.BGS_MAIN, -6569, 1360, -5214): [ # Mumbos Eye 1
        ],
    (Room_Enums.BGS_MAIN, -6301, 1360, -5462): [ # Mumbos Eye 2
        ],
    (Room_Enums.BGS_MAIN, 4702, 601, -3587): [ # Hut 1
        ],
    (Room_Enums.BGS_MAIN, 4895, 1101, -4381): [ # Hut 2
        ],
    (Room_Enums.BGS_MAIN, 5202, 1901, -5092): [ # Hut 3
        ],
    (Room_Enums.BGS_MAIN, 6084, 2401, -4983): [ # Hut 4
        ],
    (Room_Enums.BGS_MAIN, -7552, 1599, -3445): [ # Atop Maze
        ],
    ######################
    ### Freezeezy Peak ###
    ######################
    (Room_Enums.FP_MAIN, 6853, 1050, -3316): [ # Mumbos Eye 1
        ],
    (Room_Enums.FP_MAIN, 7049, 1050, -2958): [ # Mumbos Eye 2
        ],
    (Room_Enums.FP_MAIN, 4834, 449, -929): [ # Behind House
        ],
    (Room_Enums.FP_MUMBOS_SKULL, 0, 600, 0): [ # Ceiling
        ],
    (Room_Enums.FP_WOZZAS, -3194, -365, -215): [ # Middle Of Tunnel
        ],
    (Room_Enums.FP_WOZZAS, -1617, -361, -340): [ # Behind Green Crystal
        ],
    ####################
    ### Gobis Valley ###
    ####################
    (Room_Enums.GV_MAIN, -5965, 1980, 5941): [ # Jinxy Butt
        ],
    (Room_Enums.GV_WATER_PYRAMID, 5, 2200, -7): [ # Top Entrance
        ],
    ###########################
    ### Mad Monster Mansion ###
    ###########################
    (Room_Enums.MMM_MAIN, 5699, 400, -3349): [ # Above Well
        ],
    (Room_Enums.MMM_MAIN, -650, 460, -4798): [ # Mumbos Eye 1
        ],
    (Room_Enums.MMM_MAIN, -454, 460, -4598): [ # Mumbos Eye 2
        ],
    (Room_Enums.MMM_MAIN, -437, 745, -4822): [ # Atop Mumbos
        ],
    (Room_Enums.MMM_MAIN, -1304, 0, -1042): [ # Atop Mumbos
        ],
    (Room_Enums.MMM_MAIN, 685, 1099, 1259): [ # Mansion Floor 2 #1
        ],
    (Room_Enums.MMM_MAIN, 1350, 1099, 1265): [ # Mansion Floor 2 #2
        ],
    (Room_Enums.MMM_MAIN, 681, 1099, -751): [ # Mansion Floor 2 #3
        ],
    (Room_Enums.MMM_MAIN, -1203, 174, -1425): [ # Tall Grass Corner 1
        ],
    (Room_Enums.MMM_MAIN, 3053, 174, -2991): [ # Tall Grass Corner 2
        ],
    (Room_Enums.MMM_MAIN, 3060, 174, -1993): [ # Tall Grass Corner 3
        ],
    (Room_Enums.MMM_MAIN, 3096, 174, -1704): [ # Tall Grass Corner 4
        ],
    (Room_Enums.MMM_MAIN, 3529, 29, 2506): [ # Corner 1
        ],
    (Room_Enums.MMM_MAIN, 3529, 29, 2506): [ # Corner 2
        ],
    (Room_Enums.MMM_MAIN, 1681, 29, 3742): [ # Corner 3
        ],
    (Room_Enums.MMM_MAIN, 323, 29, 3764): [ # Corner 4
        ],
    (Room_Enums.MMM_MAIN, -1236, 29, 2678): [ # Corner 5
        ],
    (Room_Enums.MMM_MAIN, -175, 174, 439): [ # Mansion Corner 1
        ],
    (Room_Enums.MMM_MAIN, -183, 174, 35): [ # Mansion Corner 2
        ],
    (Room_Enums.MMM_MAIN, -2911, 449, 1320): [ # Atop Maze
        ],
    (Room_Enums.MMM_INSIDE_LOGGO, 531, 136, -478): [ # Loggo Corner 1
        ],
    (Room_Enums.MMM_CHURCH, 2243, 0, 4462): [ # Corner 1
        ],
    (Room_Enums.MMM_CHURCH, -2304, 0, 4493): [ # Corner 2
        ],
    (Room_Enums.MMM_CHURCH, -1639, 288, 2080): [ # Chair 1
        ],
    (Room_Enums.MMM_CHURCH, -1624, 288, 498): [ # Chair 2
        ],
    (Room_Enums.MMM_CHURCH, 1624, 288, 2067): [ # Chair 3
        ],
    (Room_Enums.MMM_CHURCH, 1619, 288, 507): [ # Chair 4
        ],
    (Room_Enums.MMM_CHURCH, 1876, 200, -3450): [ # Side Of Organ 1
        ],
    (Room_Enums.MMM_CHURCH, -1874, 200, -3450): [ # Side Of Organ 2
        ],
    (Room_Enums.MMM_BASEMENT, -466, 31, -195): [ # Barrel 1
        ],
    (Room_Enums.MMM_BASEMENT, 474, 31, 480): [ # Barrel 2
        ],
    (Room_Enums.MMM_BASEMENT, -513, 0, -784): [ # Corner 1
        ],
    (Room_Enums.MMM_BASEMENT, 520, 0, -771): [ # Corner 2
        ],
    (Room_Enums.MMM_WELL, 5, 2000, 10): [ # Rope
        ],
    (Room_Enums.MMM_DINING_ROOM, 1465, 0, 2282): [ # Corner 1
        ],
    (Room_Enums.MMM_DINING_ROOM, -1465, 0, 2282): [ # Corner 2
        ],
    (Room_Enums.MMM_DINING_ROOM, 1468, 0, -2466): [ # Corner 3
        ],
    (Room_Enums.MMM_DINING_ROOM, -1468, 0, -2466): [ # Corner 4
        ],
    (Room_Enums.MMM_DINING_ROOM, 0, 200, 0): [ # Under Dining Table
        ],
    (Room_Enums.MMM_FLOOR_1_ROOM_2_BLUE_EGGS, 424, 0, 339): [ # Corner
        ],
    (Room_Enums.MMM_FLOOR_3_ROOM_1_NOTES, 408, 0, 319): [ # Corner
        ],
    (Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, -426, 0, 380): [ # Corner 1
        ],
    (Room_Enums.MMM_FLOOR_1_ROOM_1_RED_FEATHERS, -426, 0, -375): [ # Corner 2
        ],
    (Room_Enums.MMM_SECRET_ROOM, 0, 0, -600): [ # Between Windows
        ],
    (Room_Enums.MMM_MUMBOS_SKULL, 0, 600, 0): [ # Ceiling
        ],
    ########################
    ### Rusty Bucket Bay ###
    ########################
    (Room_Enums.RBB_MAIN, 1000, -800, 5885): [ # Behind Start Pad
        ],
    (Room_Enums.RBB_MAIN, -2797, -457, -3361): [ # Above Toll 4 Bridge
        ],
    (Room_Enums.RBB_MAIN, 2319, -457, -3366): [ # Above Toll 6 Bridge
        ],
    (Room_Enums.RBB_MAIN, 6644, -457, 3236): [ # Above Toll 8 Bridge
        ],
    (Room_Enums.RBB_MAIN, 9287, -1200, 864): [ # Atop Floating Crate
        ],
    (Room_Enums.RBB_MAIN, 0, -2601, 0): [ # Under Boat
        ],
    (Room_Enums.RBB_MAIN, 8100, -150, 0): [ # Atop Rareware Flag
        ],
    (Room_Enums.RBB_MAIN, 4200, 900, 0): [ # Bottom Of TNT Rope
        ],
    (Room_Enums.RBB_ANCHOR, -1350, 700, 0): [ # Behind Chain Above Water
        ],
    (Room_Enums.RBB_ENGINE_ROOM, -1600, 1100, -3850): [ # Above Rotating Pipe 1
        ],
    (Room_Enums.RBB_ENGINE_ROOM, 1600, 1100, -3850): [ # Above Rotating Pipe 2
        ],
    (Room_Enums.RBB_ENGINE_ROOM, -4028, 1059, -1968): [ # Control Room Corner
        ],
    (Room_Enums.RBB_CHUMP_WAREHOUSE, 0, -1000, 0): [ # Underwater
        ],
    (Room_Enums.RBB_BOAT, 0, -1000, 0): [ # Under The Boat
        ],
    (Room_Enums.RBB_BLUE_CONTAINER_3_KABOOM_BOX, 550, 0, -950): [ # Corner
        ],
    (Room_Enums.RBB_CABINS, -583, 323, -70): [ # Another Bunk Bed
        ],
    ########################
    ### Click Clock Wood ###
    ########################
    #######################
    ### GRUNTILDAS LAIR ###
    #######################
}