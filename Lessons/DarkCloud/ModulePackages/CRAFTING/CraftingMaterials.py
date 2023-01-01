"""
                                █▀▀ █▀█ ▄▀█ █▀▀ ▀█▀ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ ▀█▀ █▀▀ █▀█ █ ▄▀█ █░░ █▀
                                █▄▄ █▀▄ █▀█ █▀░ ░█░ █ █░▀█ █▄█   █░▀░█ █▀█ ░█░ ██▄ █▀▄ █ █▀█ █▄▄ ▄█

                Crafting materials are items in Dark Chronicle that are used for making inventions and Georama parts. 
They can also be used as a substitute for crystals, if one wishes to quickly upgrade a weapon with synthesis, as they are relatively cheap. 
They are commonly dropped by or stolen from enemies, found in treasure chests in relatively large quantities, and are easily purchased for a 
low price from various shops, notably Conda sells a majority of materials. There is a carry limit of 999 for each of them, due to how common they are.

A Gold Bullion, known as a Gold Bar in the sequel, is the only recurring item from Dark Cloud, in which its sole purpose was to allow the player to 
"bank" money in storage. Exiting a dungeon early would lead to the loss of half the Gilda in your inventory, thus buying gold bars was the only way to 
store money, for its buy and sell price are both 1,000 Gilda. This function still remains in Dark Chronicle, but Gold Bars are also a common item 
required for the highest quality inventions.


This module contains all the classes, functions, variables and constants for the crafting materials in the DarkCloud project!
"""

# import modules
from dataclasses import dataclass

# Spectrum variable types
CYCLONE = "Cyclone"
EXORCISM = "Exorcism"
CHILL = "Chill"
LIGHTNING = "Lightning"
FLAME = "Flame"
SMASH = "Smash"
DURABLE = "Durable"
BEAST = "Beast"

# tuples
""" < - spectrum index guide

This guide was created for those without knowledge of how indexes work with sequence data types and is a guideline for the spectrum
crafting material types and can be found here to reference from.

SPECTRUM[0] = Cyclone
SPECTRUM[1] = Exorcism
SPECTRUM[2] = Chill
SPECTRUM[3] = Lighting
SPECTRUM[4] = Flame
"""
SPECTRUM = (CYCLONE, EXORCISM, CHILL, LIGHTNING, FLAME, SMASH, DURABLE, BEAST)
# dataclass
@dataclass
class Crafting_Materials():
    
    # fields
    name: str
    description: str
    Spectrum_int: int
    Spectrum_type: str
    sound_filepath: str = r""
    
    # methods
    def __material_name__(self): 
        
        return Crafting_Materials.name
    def __material_description__(self): 
        
        return Crafting_Materials.description
    def __spectrum_int_value__(self): 
        
        return Crafting_Materials.Spectrum_int
    def __spectrum_type__(self): 
        
        return Crafting_Materials.Spectrum_type
    def __sound_filepath__(self): 
        
        return Crafting_Materials.sound_filepath
    
    
    pass

# object instances/constructors

# cyclone Spectrum
BUNDLE_OF_HAY = Crafting_Materials("Bundle of Hay", "Bunch of hay.", 2, SPECTRUM[0]) 
FOREST_DEW = Crafting_Materials("Forest Dew", "Dew of the forest caught in a bottle.", 2, SPECTRUM[0])

# lighting Spectrum
GOLD_BAR = Crafting_Materials("Gold Bar", "The only item with the same buying and selling price.", 2, SPECTRUM[3])
POISON = Crafting_Materials("Poison", "Don't drink this by accident.", 2, SPECTRUM[3])
HUNK_OF_COPPER = Crafting_Materials("Hunk of Copper", "Lump of pure copper.", 2, SPECTRUM[3])

# smash Spectrum
ROLLING_LOG = Crafting_Materials("Rolling Log", "Log cut from only the strongest tree.", 2, SPECTRUM[5])

# exorcism Spectrum
UNKNOWN_BONE = Crafting_Materials("Unknown Bone", "Can't guess what creature this belonged to.", 2, SPECTRUM[1])
FLOUR = Crafting_Materials("Flour", "Use this to bake when you get hungry.", 2, SPECTRUM[1])

# chill Spectrum
GLASS_MATERIAL = Crafting_Materials("Glass Material", "Ingredient for glass.", 2, SPECTRUM[2])

# flame Spectrum
GUNPOWDER = Crafting_Materials("Gunpowder", "Dangerous stuff if you're not careful.", 2, SPECTRUM[4])
















