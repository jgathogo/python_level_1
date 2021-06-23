import os
import sys

"""
Notes:
- Great job construction the dictionary! I'll later show you how to do this.
- In solving part (b) think as follows
    consider a colour like #F64A8A
    suppose the use chooses 'r'
    we know that the red channel is non-zero (F6)
    so we should iterate all keys (colours) and find those 
    with indexes 1 and 2 not equal to zero; these colours have red
"""


def main():
    colours = """Absolute Zero 	#0048BA 
    Acid green 	#B0BF1A 
    Aero 	#7CB9E8 
    Aero blue 	#C0E8D5 
    African violet 	#B284BE 
    Air superiority blue 	#72A0C1 
    Alabaster 	#EDEAE0 
    Alice blue 	#F0F8FF 
    Alloy orange 	#C46210 
    Almond 	#EFDECD 
    Amaranth 	#E52B50 
    Amaranth (M&P) 	#9F2B68 
    Amaranth pink 	#F19CBB 
    Amaranth purple 	#AB274F 
    Amaranth red 	#D3212D 
    Amazon 	#3B7A57 
    Amber 	#FFBF00 
    Amber (SAE/ECE) 	#FF7E00 
    Amethyst 	#9966CC 
    Android green 	#3DDC84 
    Antique brass 	#CD9575 
    Antique bronze 	#665D1E 
    Antique fuchsia 	#915C83 
    Antique ruby 	#841B2D 
    Antique white 	#FAEBD7 
    Ao (English) 	#008000 
    Apple green 	#8DB600 
    Apricot 	#FBCEB1 
    Aqua 	#00FFFF 
    Aquamarine 	#7FFFD4 
    Arctic lime 	#D0FF14 
    Army green 	#4B5320 
    Artichoke 	#8F9779 
    Arylide yellow 	#E9D66B 
    Ash gray 	#B2BEB5 
    Asparagus 	#87A96B 
    Atomic tangerine 	#FF9966 
    Auburn 	#A52A2A 
    Aureolin 	#FDEE00 
    Avocado 	#568203 
    Azure 	#007FFF 
    Azure (X11/web color) 	#F0FFFF 
    Baby blue 	#89CFF0 
    Baby blue eyes 	#A1CAF1 
    Baby pink 	#F4C2C2 
    Baby powder 	#FEFEFA 
    Baker-Miller pink 	#FF91AF 
    Banana Mania 	#FAE7B5 
    Barbie Pink 	#DA1884 
    Barn red 	#7C0A02 
    Battleship grey 	#848482 
    Beau blue 	#BCD4E6 
    Beaver 	#9F8170 
    Beige 	#F5F5DC 
    B'dazzled blue 	#2E5894 
    Big dip o’ruby 	#9C2542 
    Bisque 	#FFE4C4 
    Bistre 	#3D2B1F 
    Bistre brown 	#967117 
    Bitter lemon 	#CAE00D 
    Bitter lime 	#BFFF00 
    Bittersweet 	#FE6F5E 
    Bittersweet shimmer 	#BF4F51 
    Black 	#000000 
    Black bean 	#3D0C02 
    Black chocolate 	#1B1811 
    Black coffee 	#3B2F2F 
    Black coral 	#54626F 
    Black olive 	#3B3C36 
    Black Shadows 	#BFAFB2 
    Blanched almond 	#FFEBCD 
    Blast-off bronze 	#A57164 
    Bleu de France 	#318CE7 
    Blizzard blue 	#ACE5EE 
    Blond 	#FAF0BE 
    Blood red 	#660000 
    Blue 	#0000FF 
    Blue (Crayola) 	#1F75FE 
    Blue (Munsell) 	#0093AF 
    Blue (NCS) 	#0087BD 
    Blue (Pantone) 	#0018A8 
    Blue (pigment) 	#333399 
    Blue (RYB) 	#0247FE 
    Blue bell 	#A2A2D0 
    Blue-gray 	#6699CC 
    Blue-green 	#0D98BA 
    Blue-green (color wheel) 	#064E40 
    Blue jeans 	#5DADEC 
    Blue sapphire 	#126180 
    Blue-violet 	#8A2BE2 
    Blue-violet (Crayola) 	#7366BD 
    Blue-violet (color wheel) 	#4D1A7F 
    Blue yonder 	#5072A7 
    Bluetiful 	#3C69E7 
    Blush 	#DE5D83 
    Bole 	#79443B 
    Bone 	#E3DAC9 
    Bottle green 	#006A4E 
    Brandy 	#87413F 
    Brick red 	#CB4154 
    Bright green 	#66FF00 
    Bright lilac 	#D891EF 
    Bright maroon 	#C32148 
    Bright navy blue 	#1974D2 
    Bright yellow (Crayola) 	#FFAA1D 
    Brilliant rose 	#FF55A3 
    Brink pink 	#FB607F 
    British racing green 	#004225 
    Bronze 	#CD7F32 
    Brown 	#88540B 
    Brown sugar 	#AF6E4D 
    Brunswick green 	#1B4D3E 
    Bud green 	#7BB661 
    Buff 	#FFC680 
    Burgundy 	#800020 
    Burlywood 	#DEB887 
    Burnished brown 	#A17A74 
    Burnt orange 	#CC5500 
    Burnt sienna 	#E97451 
    Burnt umber 	#8A3324 
    Byzantine 	#BD33A4 
    Byzantium 	#702963 
    Cadet 	#536872 
    Cadet blue 	#5F9EA0 
    Cadet blue (Crayola) 	#A9B2C3 
    Cadet grey 	#91A3B0 
    Cadmium green 	#006B3C 
    Cadmium orange 	#ED872D 
    Cadmium red 	#E30022 
    Cadmium yellow 	#FFF600 
    Café au lait 	#A67B5B 
    Café noir 	#4B3621 
    Cambridge blue 	#A3C1AD 
    Camel 	#C19A6B 
    Cameo pink 	#EFBBCC 
    Canary 	#FFFF99 
    Canary yellow 	#FFEF00 
    Candy apple red 	#FF0800 
    Candy pink 	#E4717A 
    Capri 	#00BFFF 
    Caput mortuum 	#592720 
    Cardinal 	#C41E3A 
    Caribbean green 	#00CC99 
    Carmine 	#960018 
    Carmine (M&P) 	#D70040 
    Carnation pink 	#FFA6C9 
    Carnelian 	#B31B1B 
    Carolina blue 	#56A0D3 
    Carrot orange 	#ED9121 
    Castleton green 	#00563F 
    Catawba 	#703642 
    Cedar Chest 	#C95A49 
    Celadon 	#ACE1AF 
    Celadon blue 	#007BA7 
    Celadon green 	#2F847C 
    Celeste 	#B2FFFF 
    Celtic blue 	#246BCE 
    Cerise 	#DE3163 
    Cerulean 	#007BA7 
    Cerulean blue 	#2A52BE 
    Cerulean frost 	#6D9BC3 
    Cerulean (Crayola) 	#1DACD6 
    CG blue 	#007AA5 
    CG red 	#E03C31 
    Champagne 	#F7E7CE 
    Champagne pink 	#F1DDCF 
    Charcoal 	#36454F 
    Charleston green 	#232B2B 
    Charm pink 	#E68FAC 
    Chartreuse (traditional) 	#DFFF00 
    Chartreuse (web) 	#7FFF00 
    Cherry blossom pink 	#FFB7C5 
    Chestnut 	#954535 
    Chili red 	#E23D28 
    China pink 	#DE6FA1 
    China rose 	#A8516E 
    Chinese red 	#AA381E 
    Chinese violet 	#856088 
    Chinese yellow 	#FFB200 
    Chocolate (traditional) 	#7B3F00 
    Chocolate (web) 	#D2691E 
    Chocolate Cosmos 	#58111A 
    Chrome yellow 	#FFA700 
    Cinereous 	#98817B 
    Cinnabar 	#E34234 
    Cinnamon Satin 	#CD607E 
    Citrine 	#E4D00A 
    Citron 	#9FA91F 
    Claret 	#7F1734 
    Cobalt blue 	#0047AB 
    Cocoa brown 	#D2691E 
    Coffee 	#6F4E37 
    Columbia Blue 	#B9D9EB 
    Congo pink 	#F88379 
    Cool grey 	#8C92AC 
    Copper 	#B87333 
    Copper (Crayola) 	#DA8A67 
    Copper penny 	#AD6F69 
    Copper red 	#CB6D51 
    Copper rose 	#996666 
    Coquelicot 	#FF3800 
    Coral 	#FF7F50 
    Coral pink 	#F88379 
    Cordovan 	#893F45 
    Corn 	#FBEC5D 
    Cornell red 	#B31B1B 
    Cornflower blue 	#6495ED 
    Cornsilk 	#FFF8DC 
    Cosmic cobalt 	#2E2D88 
    Cosmic latte 	#FFF8E7 
    Coyote brown 	#81613C 
    Cotton candy 	#FFBCD9 
    Cream 	#FFFDD0 
    Crimson 	#DC143C 
    Crimson (UA) 	#9E1B32 
    Crystal 	#A7D8DE 
    Cultured 	#F5F5F5 
    Cyan 	#00FFFF 
    Cyan (process) 	#00B7EB 
    Cyber grape 	#58427C 
    Cyber yellow 	#FFD300 
    Cyclamen 	#F56FA1 
    Dark blue-gray 	#666699 
    Dark brown 	#654321 
    Dark byzantium 	#5D3954 
    Dark cornflower blue 	#26428B 
    Dark cyan 	#008B8B 
    Dark electric blue 	#536878 
    Dark goldenrod 	#B8860B 
    Dark green 	#013220 
    Dark green (X11) 	#006400 
    Dark jungle green 	#1A2421 
    Dark khaki 	#BDB76B 
    Dark lava 	#483C32 
    Dark liver 	#534B4F 
    Dark liver (horses) 	#543D37 
    Dark magenta 	#8B008B 
    Dark moss green 	#4A5D23 
    Dark olive green 	#556B2F 
    Dark orange 	#FF8C00 
    Dark orchid 	#9932CC 
    Dark pastel green 	#03C03C 
    Dark purple 	#301934 
    Dark red 	#8B0000 
    Dark salmon 	#E9967A 
    Dark sea green 	#8FBC8F 
    Dark sienna 	#3C1414 
    Dark sky blue 	#8CBED6 
    Dark slate blue 	#483D8B 
    Dark slate gray 	#2F4F4F 
    Dark spring green 	#177245 
    Dark turquoise 	#00CED1 
    Dark violet 	#9400D3 
    Dartmouth green 	#00703C 
    Davy's grey 	#555555 
    Deep cerise 	#DA3287 
    Deep champagne 	#FAD6A5 
    Deep chestnut 	#B94E48 
    Deep jungle green 	#004B49 
    Deep pink 	#FF1493 
    Deep saffron 	#FF9933 
    Deep sky blue 	#00BFFF 
    Deep Space Sparkle 	#4A646C 
    Deep taupe 	#7E5E60 
    Denim 	#1560BD 
    Denim blue 	#2243B6 
    Desert 	#C19A6B 
    Desert sand 	#EDC9AF 
    Dim gray 	#696969 
    Dodger blue 	#1E90FF 
    Dogwood rose 	#D71868 
    Drab 	#967117 
    Duke blue 	#00009C 
    Dutch white 	#EFDFBB 
    Earth yellow 	#E1A95F 
    Ebony 	#555D50 
    Ecru 	#C2B280 
    Eerie black 	#1B1B1B 
    Eggplant 	#614051 
    Eggshell 	#F0EAD6 
    Egyptian blue 	#1034A6 
    Eigengrau 	#16161D 
    Electric blue 	#7DF9FF 
    Electric green 	#00FF00 
    Electric indigo 	#6F00FF 
    Electric lime 	#CCFF00 
    Electric purple 	#BF00FF 
    Electric violet 	#8F00FF 
    Emerald 	#50C878 
    Eminence 	#6C3082 
    English green 	#1B4D3E 
    English lavender 	#B48395 
    English red 	#AB4B52 
    English vermillion 	#CC474B 
    English violet 	#563C5C 
    Erin 	#00FF40 
    Eton blue 	#96C8A2 
    Fallow 	#C19A6B 
    Falu red 	#801818 
    Fandango 	#B53389 
    Fandango pink 	#DE5285 
    Fashion fuchsia 	#F400A1 
    Fawn 	#E5AA70 
    Feldgrau 	#4D5D53 
    Fern green 	#4F7942 
    Field drab 	#6C541E 
    Fiery rose 	#FF5470 
    Firebrick 	#B22222 
    Fire engine red 	#CE2029 
    Fire opal 	#E95C4B 
    Flame 	#E25822 
    Flax 	#EEDC82 
    Flirt 	#A2006D 
    Floral white 	#FFFAF0 
    Fluorescent blue 	#15F4EE 
    Forest green (Crayola) 	#5FA777 
    Forest green (traditional) 	#014421 
    Forest green (web) 	#228B22 
    French beige 	#A67B5B 
    French bistre 	#856D4D 
    French blue 	#0072BB 
    French fuchsia 	#FD3F92 
    French lilac 	#86608E 
    French lime 	#9EFD38 
    French mauve 	#D473D4 
    French pink 	#FD6C9E 
    French raspberry 	#C72C48 
    French rose 	#F64A8A 
    French sky blue 	#77B5FE 
    French violet 	#8806CE 
    Frostbite 	#E936A7 
    Fuchsia 	#FF00FF 
    Fuchsia (Crayola) 	#C154C1 
    Fuchsia purple 	#CC397B 
    Fuchsia rose 	#C74375 
    Fulvous 	#E48400 
    Fuzzy Wuzzy 	#87421F"""

    # Convert data to a dictionary
    colours_l = colours.replace(" \n", '').replace("\t", "").split("    ")
    colours_d = {}
    # very good!
    for i in colours_l:
        colours_d[i[-7:]] = i[0:-7]

    c = input("Input r, g or b: ")

    name_d = {'r': 'Red',
              'g': 'Green',
              'b': 'Blue'}

    if c not in name_d:
        sys.exit("Invalid character. Enter values r g or b")

    # This did not work, I don't know why.
    # if c != "r" or c != "g" or c != "b":
    #     sys.exit("Invalid character. Enter values r g or b")

    pos_d = {'r': 1,
             'g': 3,
             'b': 5}

    c_pos = pos_d[c]
    c_name = name_d[c]
    print(f"The following have non-zero values in the {c_name} channel")
    for colour in colours_d:
        # todo: compare each position independently
        if colour[c_pos:c_pos + 2] != '00':
            print(f"{colour} - {colours_d[colour]}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
