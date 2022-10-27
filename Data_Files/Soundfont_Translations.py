BANJO_TOOIE_SOUNDFONT_DICT = {
    69: 70, # Pizzicato Strings
    70: 71, # RBB Ambience
    71: 72, # Mumbo Vox
    72: 73, # Drum Kit
    73: 74, # Vibrato Strings
    74: 75, # Lab Electricity
    75: 76, # Clave
    76: 78, # Pan Flute
    77: 79, # Taiko Drum
    78: 39, # Cheering
    79: 2, # Strings
    80: 11, # Tambourine
    81: 70, # Pizzicato Strings
    82: 58, # Muted Bass
    83: 56, # Church Organ 2
    84: 12, # Harmonica
    85: 48, # Fiddle
    86: 12, # Harmonica
    87: 4, # Fender Thumb Bass
    88: 6, # Flute
    89: 22, # Pan Flute
    90: 79, # Some Kind Of Drum Roll 1?
    91: 2, # Strings
    92: 69, # Burp + Fart
    93: 81, # Robotic Noises?
    94: 16, # Terrydactyl Land Noises?
    95: 1, # Marimba
    96: 17, # Trombone
    97: 22, # Pan Flute
    98: 6, # Flute
    99: 63, # Shenai
    100: 18, # Trumpet
    101: 8, # Baritone Sax
    102: 1, # Marimba
    103: 76, # Honey B Hive Noises?
    104: 29, # Bassoon
    105: 39, # Waves
    106: 79, # Some Kind Of Drum Roll 2?
    107: 28, # Rattling Noise?
    108: 17, # Trombone
    109: 26, # Chirp
    110: 38, # Fire In Cave?
    111: 11, # Tambourine
    112: 84, # Stepping In Noisy Grass?
    113: 61, # Cheato Voice?
    114: 82, # Sirens?
    115: 56, # Eletric Piano?
    116: 50, # Animal Noises?
    117: 13, # Maracas
    118: 62, # Beat And Clap?
}

for i in range(1, 69):
    if(i not in BANJO_TOOIE_SOUNDFONT_DICT):
        BANJO_TOOIE_SOUNDFONT_DICT[i] = i