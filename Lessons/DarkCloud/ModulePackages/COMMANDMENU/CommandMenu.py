# importing modules
from dataclasses import dataclass, field # class modules
import pygame
from pygame import mixer, mixer_music # audio modules responsible ommitting playback of wav files
import logging, logging.handlers # logger modules
from ModulePackages.PLAYER.Player import * # sub package module imports

# <- insert mmore modules here

""" GenesisGirs typical logger preset
〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ


                    ░██████╗░███████╗███╗░░██╗███████╗░██████╗██╗░██████╗░██████╗░██╗██████╗░
                    ██╔════╝░██╔════╝████╗░██║██╔════╝██╔════╝██║██╔════╝██╔════╝░██║██╔══██╗
                    ██║░░██╗░█████╗░░██╔██╗██║█████╗░░╚█████╗░██║╚█████╗░██║░░██╗░██║██████╔╝
                    ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░░╚═══██╗██║░╚═══██╗██║░░╚██╗██║██╔══██╗
                    ╚██████╔╝███████╗██║░╚███║███████╗██████╔╝██║██████╔╝╚██████╔╝██║██║░░██║
                    ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═╝╚═════╝░░╚═════╝░╚═╝╚═╝░░╚═╝

Loggers are a fundamental part of coding and this logger is a great entry point for beginner's and pros alike
pop this into your code to have the logger track events. Ready with all the bell's and whistle's start logging your
program now! Logging information will tell it to check for exceptions and errors that occur within your program you can check the 
log files and see whats wrong. It's very important to have them in your software or games as well. The general rule is learn about 
loggers as much as you can from my pack and see if you can create your very own loggers!

                                    ⣿⣯⣿⣟⣟⡼⣿⡼⡿⣷⣿⣿⣿⠽⡟⢋⣿⣿⠘⣼⣷⡟⠻⡿⣷⡼⣝⡿⡾⣿
                                    ⣿⣿⣿⣿⢁⣵⡇⡟⠀⣿⣿⣿⠇⠀⡇⣴⣿⣿⣧⣿⣿⡇⠀⢣⣿⣷⣀⡏⢻⣿
                                    ⣿⣿⠿⣿⣿⣿⠷⠁⠀⠛⠛⠋⠀⠂⠹⠿⠿⠿⠿⠿⠉⠁⠀⠘⠛⠛⠛⠃⢸⣯ GIBE ME YOUR LOGGER!!!!
                                    ⣿⡇⠀⣄⣀⣀⣈⣁⠈⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠠⠎⠈⠀⣀⣁⣀⣀⡠⠈⠉
                                    ⣿⣯⣽⡿⢟⡿⠿⠛⠛⠿⣶⣄⠀⠀⠀⠀⠀⠀⠈⢠⣴⣾⠛⠛⠿⠻⠛⠿⣷⣶   I KNOW HOW TO TRACK STUFF YAYAYA!!
                                    ⣿⣿⣿⠀⠀⠀⣿⡿⣶⣿⣫⠉⠀⠀⠀⠀⠀⠀⠀⠈⠰⣿⠿⠾⣿⡇⠀⠀⢺⣿
                                    ⣿⣿⠻⡀⠀⠀⠙⠏⠒⡻⠃⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠐⡓⢚⠟⠁⠀⠀⡾⢫
                                    ⣿⣿⠀⠀⡀⠀⠀⡈⣉⡀⡠⣐⣅⣽⣺⣿⣯⡡⣴⣴⣔⣠⣀⣀⡀⢀⡀⡀⠀⣸
                                    ⣿⣿⣷⣿⣟⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⢾⣷⣿
                                    ⣿⣿⣟⠫⡾⠟⠫⢾⠯⡻⢟⡽⢶⢿⣿⣿⡛⠕⠎⠻⠝⠪⢖⠝⠟⢫⠾⠜⢿⣿
                                    ⣿⣿⣿⠉⠀⠀⠀⠀⠈⠀⠀⠀⠀⣰⣋⣀⣈⣢⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⢸⣿
                                    ⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿
                                    ⣿⣿⣿⣿⣦⡔⠀⠀⠀⠀⠀⠀⢻⣿⡿⣿⣿⢽⣿⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿
                                    ⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠘⠛⢅⣙⣙⠿⠉⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣅⠀⠓⠀⠀⣀⣠⣴⣺⣿⣿⣿⣿⣿⣿⣿⣿ ɢ∈ﬡ∈⟆⫯⟆ɢ⫯ᖇ


                                    𝖈𝖔𝖉𝖊 𝖜𝖆𝖘 𝖕𝖗𝖔𝖉𝖚𝖈𝖊𝖉 𝖇𝖞 Ꮆ🝗𝓝🝗丂讠丂Ꮆ讠尺

〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ〤ㄖ〤ㄖ〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ 〤ㄖ〤ㄖ
"""

def logger(): # GenesisGir's typical logger preset! 🪵
    
    # importing modules
    import logging, logging.handlers
    from logging.handlers import SMTPHandler
    
    # create the logger and set severity
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) # set logger level

    # create handles and set their severity
    
    # File Handlers
    file_handler = logging.FileHandler( 
    filename = r"GenesisGirLessonsVOL.4\Lessons\DarkCloud\Log\logger.log",
    mode = 'w', # filemode 
    encoding = 'utf-8', # set encoding format
    delay = False, 
    errors = None)
    file_handler.setLevel(logging.DEBUG) # severity level
    
    # Stream Handlers
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.CRITICAL)

    
    # create formatter
    formatter = logging.Formatter("%(asctime)s [%(name)s] [%(levelname)s] [Lvl:%(levelno)s] [%(funcName)s] [%(lineno)d] %(message)s",
    datefmt='%m/%d/%Y %I:%M:%S %p')

    # add formatter to handles
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    
    
    # adding the handler
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    return logger
    pass
    
# logger variable
logger = logger()

""" <- dataclass tips!
█▀▄ ▄▀█ ▀█▀ ▄▀█ █▀▀ █░░ ▄▀█ █▀ █▀ █▀▀ █▀
█▄▀ █▀█ ░█░ █▀█ █▄▄ █▄▄ █▀█ ▄█ ▄█ ██▄ ▄█ 

⠤⠤⠤⠤⠤⠤⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⠶⠶⠶⠦⠤⠤⠤⠤⠤⢤⣤⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠄⢂⣠⣭⣭⣕⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠤⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉
⠀⠀⢀⠜⣳⣾⡿⠛⣿⣿⣿⣦⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣍⣀⣦⠦⠄⣀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⣄⣽⣿⠋⠀⡰⢿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠛⠛⡿⠿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣁⣂⣤⡄⠀⠀⠀⠀⠀⠀
⢳⣶⣼⣿⠃⠀⢀⠧⠤⢜⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⡇⠀⣀⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠁⠐⠀⣀⠀⠀
⠀⠙⠻⣿⠀⠀⠀⠀⠀⠀⢹⣿⣿⡝⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠋⠀⠀⠀⠀⠠⠃⠁⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⡿⠋⠀⠀
⠀⠀⠀⠙⡄⠀⠀⠀⠀⠀⢸⣿⣿⡃⢼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⡏⠉⠉⠻⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠀⠀⠰⡒⠊⠻⠿⠋⠐⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣇⡀⠀⠑⢄⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢖⠠⠤⠤⠔⠙⠻⠿⠋⠱⡑⢄⠀⢠⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠻⠶⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠡⢀⡵⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⣀⠀⠀⠀⠀⠀⢀⣤⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠙⠛⠓⠒⠲⠿⢍⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀██ ██ ▛ ⠀

Dataclasses are a great way to make less boiler-plate code and makes the process of making a object instance databases quicker and is very useful.
I use this method alot in my coding and productions. Dataclasses allow you to do everything normal classes do but without the need to make the 
intializer __init__ dunder method, I mean its okay to go both routes and sometimes you like to do whatever you'd like in your code no wrong answers!
you need to also consider convention for not only you but the people who will be reviewing your code and digging into your projects as well, readablity goes miles
when it comes to programming and you will get that edge with dataclasses.

🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 

example 1.
# import modules
from dataclasses import dataclass

@dataclass
class Dagger:
    
    #fields/attributes
    size: str
    color: str
    weapon_level: int

    # class methods
    def __stab__(self):
        
        print("You stab the enemy with your dagger!")
        
    
# object constructors/instances of dagger class
DIVINE_BLADE = Dagger(size='medium', color='redish tint', weapon_level=5)

🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 

The example above is a great way to see dataclasses and how you could use them in your code productions to create a blueprint for a specific
type of object and give them their own unique attributes, elements and descriptions, traits etc. This is called (OOP) object oriented 
programming and something I want you to pratice on just by looking at my code try to look up documentation on object oriented programming
online or the python docs to get a full scale resolution of what the method does! This is a step up from using just common variables and
constants where you can only give a object one value and thats the end of need all. In (OOP) you can give the object any trait you wish
and can come up with or conjure in your head. 
"""
# dataclasses
@dataclass
class Command_Menu:
    
    
    # globals
    # <-
    # variables
    # <-
    # constants
    # <-
    # fields/attrs
    category: str = field(default_factory= None)
    active_items: str = field(default_factory= None)
    
    #  command menu methods
@dataclass
class Items_Menu:
    
    # docstring
    """ # Items Command menu
    Item
    In the Items inventory you can:
    • Make items active by dragging them to one of the Active Item slots or highlight them and press the ® button. You can hold up to nine identical items in one slot.
    • Press the ® button on the item and attachment inventories to auto-sort.
    • Discard items by dragging them to the trash.
    """
    
    # import modules
    from dataclasses import dataclass, field
    import logging, logging.handlers
    
    # global fields/attrs
    active_item_slots: str or int
    cash: int # cash in-game currency
    item_bag: str
    weapon_pouch: str
    attachment_box: str

    # player item fields/attributes
    player_name: str
    equipped_player_weapon_name_gui: str or int
    equipped_player_weapon_damage_gui: str or int
    player_health_bar_gui: int
    player_weapon_durability_gui: int
    player_defense_power: int 
    player_thrist_bar_gui: int or str
    
    
    # ally item fields/attributes
    ally_name: str # name of ally on items menu
    equipped_ally_weapon_name_gui: str or int
    equipped_ally_weapon_damage_gui: str or int
    ally_health_bar_gui: int
    ally_weapon_durability_gui: int
    ally_defense_power: int 
    ally_thrist_bar_gui: int or str
    
    # item bag fields/attrs
    item_bag_slot_used: int = field(default_factory=0) # how many items are currently in the item bag slots
    item_bag__slot_capcity: int = field(default_factory=50) # the capacity of items that can be stored in bag the deafult is '50' slots
    
    # trash can field/attributes
    trash_can: str or int = field(default_factory=None)
    
    # class methods
    @classmethod
    def __trash_can_item_menu_function__(self):
        # docstring
        """" # trash can function
        discard unnecessary items.
        """
        pass
    
    @classmethod
    def __organize_items_item_menu_function__(self):
        # docstring
        """" # organize function
        organize items with the sort() method with lists
        """
        pass

@dataclass
class Weapons_Menu:
    # docstring
    """ # weapons Command menu
    View your weapons and attachments in the Weapons inventory.
    """
    
    # import modules
    from dataclasses import dataclass, field
    import logging, logging.handlers
    
    # gloabls
    
    # variables
    selected_weapon = None
    selected_weapon_attribute = None
    # <- insert more
    # constants
    # <- insert more
    # fields/attributes
    # <- insert more
    # equipped weapon fields
    equipped_weapon_description_gui: str
    equipped_weapon: str = field(default_factory=None) # insert the 'dagger' as defualt factory
    equipped_weapon_attribute: str = field(default_factory=None)
    equipped_weapon_attribute_attachment_gui: str = field(default_factory=None)
    equipped_weapon_attk_int: int or str = field(default_factory=None)
    equipped_weapon_edurance_int: int or str = field(default_factory=None)
    equipped_weapon_speed_int: int or str = field(default_factory=None)
    equipped_weapon_magic_power_int: int or str = field(default_factory=None)
    equipped_weapon_whp_int: int or str = field(default_factory=None)
    equipped_weapon_abs_int: int or str = field(default_factory=None)
    
    # non selected weapon fields/attrs
    weapon_name: str = field(default_factory=None)
    weapon_attk_int: int or str = field(default_factory=None)
    weapon_edurance_int: int or str = field(default_factory=None)
    weapon_speed_int: int or str = field(default_factory=None)
    weapon_magic_power_int: int or str = field(default_factory=None)
    weapon_whp_int: int or str = field(default_factory=None)
    weapon_abs_int: int or str = field(default_factory=None)
    
    
    # global fields/attributes
    weapon_slot_capacity: int = field(default_factory=10)
    repair_powder_amount: str or int = field(default_factory=0)
    powerup_powder_amount: str or int = field(default_factory=0)

@dataclass
class Equip_Weapon:
    
    # class audio render methods
    @classmethod
    def __equip_wav__():
        
        # docstring
        """ # __equip_wav__ 
        Equips the currently selected weapon to the player. This function can be used to equip a weapon to the player and plays equip.wav"""
        
        # reference global variable/const
        global selected_weapon
        
        # render sound .wav!
        # file path
        file_path = r"GenesisGirLessonsVOL.4\Lessons\DarkCloud\resources\Audio Resources\MENU FX\equip.wav" # wav file path
        
        # initalize mixer
        pygame.mixer.init
        
        # create sound buffer
        equip_sound = pygame.mixer.Sound(file_path) # Create a new Sound object from a file or buffer object
        # set volume for .wav
        equip_sound.set_volume(0.2) # set the playback volume for this Sound
        # playback
        pygame.mixer.Sound.play(equip_sound, loops=0, maxtime=0, fade_ms=0) # begin sound playback play(loops=0, maxtime=0, fade_ms=0) -> Channel
        
        # log info
        logger.info("equip.wav rendered!")
        pass
        
        # render equip .wav!
        pygame.mixer.Sound.play(equip_sound, loops=0, maxtime=0, fade_ms=0) # begin sound playback play(loops=0, maxtime=0, fade_ms=0) -> Channel
        
        # equip the player with selected weapon
        player_equipped_weapon = selected_weapon
        
        # [INFO] [20]
        logger.info(f"Player has equipped the {player_equipped_weapon} weapon")
        pass
            
@dataclass
class Customize_Weapon:
    # docstring
    """ # Customize Weapon Function
    
    """
    pass

@dataclass
class Equip_Attributes:
    # docstring
    """ # Equip Attributes Function
    
    """
    
    # class methods
    @classmethod
    def __equip_attr__():
        # docstring
        """# __equip_attr__ 
        equips the player with the currently selected attribute and plays the attach.wav"""
        
        # refer to global variable/const
        global selected_weapon_attribute
        
        # render sound .wav!
        # file path
        file_path = r"GenesisGirLessonsVOL.4\Lessons\DarkCloud\resources\Audio Resources\MENU FX\attach.wav" # wav file path

        # initalize mixer
        pygame.mixer.init
        # create sound buffer
        attach_sound = pygame.mixer.Sound(file_path) # Create a new Sound object from a file or buffer obje
        # set volume for .wav
        attach_sound.set_volume(0.2) # set the playback volume for this Sou
        # playback
        pygame.mixer.Sound.play(attach_sound, loops=0, maxtime=0, fade_ms=0) # begin sound playback play(loops=0, maxtime=0, fade_ms=0) -> Channel
        # log info
        logger.info("attach.wav rendered!")
        pass

                
        # render attach .wav!
        pygame.mixer.Sound.play(attach_sound, loops=0, maxtime=0, fade_ms=0) # begin sound playback play(loops=0, maxtime=0, fade_ms=0) -> Channel
        
        # attach attribute to currently selected player weapon
        equipped_weapon_attribute = selected_weapon_attribute
        pass

@dataclass
class Repair_Weapon:
    # docstring
    """ # Repair Weapons Function"""
    pass

@dataclass
class Georama_Menu:
    # docstring
    """ # options Command menu
    Begin the re-assembly of your world after you have collected Atla. Use this option when in Edit Mode or in a Dungeon only. 
    You can view Georama in Walking Mode, but you will be unable to edit them.
    """
    
    # import modules
    from dataclasses import dataclass, field
    import logging, logging.handlers
    
    # gloabls
    
    # variables
    
    # constants
    
    # fields/attrs
    config_assemble: str 
    
    # class  methods
    @classmethod
    def config_assembly():
        # docstring
        """ # config assembly
        Configure/Assemble georama parts. This is the functionality that reverse engineers the config/assembly function from Dark Cloud
        """
        pass
    
@dataclass
class Allies_Menu:
    # docstring
    """ # allies Command menu
    Change your Allies while in the dungeons.
    """
    pass
    
@dataclass
class Leave_Menu:
    # docstring
    """ # leave building/dungeon Command menu
    Use this to leave the building/dungeon you are in.
    """
    
    # class methods
    @classmethod
    def leave_building():
        pass
    
    @classmethod
    def leave_dungeon():
        pass
    
    pass

@dataclass
class Options_Menu:
    # docstring
    """ # options Command menu
    Change game options during play.
    """
    pass




























