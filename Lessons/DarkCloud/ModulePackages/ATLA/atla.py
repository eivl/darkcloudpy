"""
▄▀█ ▀█▀ █░░ ▄▀█ █▀
█▀█ ░█░ █▄▄ █▀█ ▄█

This is the .py script for the atlas items within the darkcloud.py project and all of their respective object instances can be found here and edited,
removed, added onto and tweaked! 
"""

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
    logger.setLevel(logging.INFO) # set logger level

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

# import modules
from dataclasses import dataclass,field
from ModulePackages.LOCATIONS.dark_cloud_locations import *
from ModulePackages.PLAYER.Player import *


# dataclasses
@dataclass
class Atlas:
    
    # docstring
    """The atlas class is responsible for the attributes of the atlas within the game and the methods, behaviors, variables, constants
    and much more! and keeps track if the player has unlocked the specific atlas.
    """
    
    # global
    
    # class variables
    
    #class constants
    
    # field/attributes
    name: str = field(default_factory=None, repr=True)
    description: str = field(default_factory=None, repr=True)
    location: str = field(default_factory=None, repr=True)
    unlocked_status: bool = field(default_factory=False, repr=True)
    
    # class methods
    pass

# object instance/constructors

# atlas npc object instants
MACHO = Atlas(name="Macho", description="Macho like his name. Never skips training.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
RENEE = Atlas(name=PLAYER_NICKNAME, description=f"{PLAYER_NICKNAME}'s mother.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
KOMACHO = Atlas(name="Komacho", description="Short big brother to Macho.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
CLAUDE = Atlas(name="Claude", description="likeable guy. Loves eating & sleeping", location=DIVINE_BEAST_CAVE, unlocked_status=False)
ODD_GAFFER = Atlas(name="Odd Gaffer", description="Gaffer who owns the local store.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
PIKE = Atlas(name="Pike", description="Paige's fsther good at pysical labor", location=DIVINE_BEAST_CAVE,unlocked_status=False)
STRAY_CAT = Atlas(name="Stray Cat", description="It may be good luck to have it in the house", location=DIVINE_BEAST_CAVE, unlocked_status=False)

# atlas location/building/attachments object instants
MACHOS_HOUSE = Atlas(name="Macho's House", description="Macho brothers house.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
PAIGES_HOUSE = Atlas(name="Paige's House", description="House of angler Pike & daughter Paige.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
ANNEX_ROOM = Atlas(name="Annex Room", description="Sperate room.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
CABIN = Atlas(name="Cabin", description="Storage Space.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
FENCE = Atlas(name="Fence", description="Place around houses.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
LAMP = Atlas(name="Lamp", description="Essential light to pass the night.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
WINDMILL_VANES = Atlas(name="Windmill Vanes", description="Vanes of small windmills.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
KEG = Atlas(name="Keg", description="contains premium aged spirits", location=DIVINE_BEAST_CAVE, unlocked_status=False)
WHEEL = Atlas(name="Wheel", description="Part essential for vehicles.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
SIGN = Atlas(name="Sign", description="Maker placed in front of buildings.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
CANDY_BOX = Atlas(name="Candy Box", description="A box filled with sweets", location=DIVINE_BEAST_CAVE,unlocked_status=False)
BENCH = Atlas(name="Bench", description="A place for sitting and relaxing", location=DIVINE_BEAST_CAVE, unlocked_status=False)
SMALL_WINDMILL_1 = Atlas(name="Small Windmill 1", description="Small Windmill. Also serves as watchtower.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
MY_HOUSE = Atlas(name="My House", description="Renee & {player_nickname}'s house", location=DIVINE_BEAST_CAVE, unlocked_status=False)
UPSTAIRS_STORAGE = Atlas(name="Upstairs Storage", description="Storage area for the second floor", location=DIVINE_BEAST_CAVE, unlocked_status=False)
BRIDGE = Atlas(name="Bridge", description="Needed for crossing rivers", location=DIVINE_BEAST_CAVE, unlocked_status=False)
GAFFER_BUGGY = Atlas(name="Gaffer's Buggy", description="Odd Gaffer's Buggy. Local Merchant", location=DIVINE_BEAST_CAVE, unlocked_status=False)
CHIMNEY = Atlas(name="Chimney",description="Releases smoke of fire places.",location=DIVINE_BEAST_CAVE,unlocked_status=False)
SUPPLIES = Atlas(name="Supplies",description="Filled with goods sold by Odd Gaffer",location=DIVINE_BEAST_CAVE, unlocked_status=False)
LLAMA = Atlas(name="Llama", description="{player_nickname}'s Llama. Important livestock", location=DIVINE_BEAST_CAVE, unlocked_status=False)
LADDER = Atlas(name="Ladder", description="Used to climb high places.", location=DIVINE_BEAST_CAVE, unlocked_status=False)

# atlas nature object instants
TREES = Atlas(name="Trees", description="Nest for birds.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
ROAD = Atlas(name="Road", description="Interconnects town's people and homes.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
RIVER = Atlas(name="road", description="Stream of water across the land.", location=DIVINE_BEAST_CAVE, unlocked_status=False)
BARBELL = Atlas(name="Barbell", description="Exercising tool", location=DIVINE_BEAST_CAVE, unlocked_status=False)