# importing modules
from dataclasses import dataclass, field
import logging, logging.handlers
from logging.handlers import SMTPHandler

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
    filename = r"GenesisGirLessonsVOL.4\Lessons\DarkCloud\Log\DarkCloud.log",
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

# dataclasses
@dataclass
class Player(): # player attributes/elements
    
    # docstring
    """The PlayerTraits class is responsible for keeping the user's username, attributes, Level, Experience points and much more like ablities
    """
    # global player trait variables
    global player_name
    global player_health
    global player_hunger
    global player_thirst
    global player_level
    global player_exp
    
    # global player trait status variables
    global player_status
    
    # player constants
    default_nickname = "Toan"
    full_health = 100
    full_hunger = 100
    quenched_thirst = 100
    default_level = 1
    default_xp = 0
    default_status = None
    
    # player status variables
    poison_condition = False
    gooey_condition = False
    curse_condition = False
    pumped_up_condition = False
    stop_condition = False
    
    # lists, tuples, dicts
    player_condition = [poison_condition , gooey_condition , curse_condition , pumped_up_condition, stop_condition ]
    
    # player fields/attributes
    player_name = default_nickname # default name set to 'Toan'
    player_health: int  = field(default_factory=full_health) # default player healh set to 100
    player_hunger: int  = field(default_factory=full_hunger) # default player hunger set to 100
    player_thirst: int  = field(default_factory=quenched_thirst) # default player thirst set to 100
    player_level: int  = field(default_factory=default_level) # default player level set to 1
    player_exp: int  = field(default_factory=default_xp) # default xp set to 0 xp
    
    # player status field
    player_status: str  = field(default_factory=default_status)# default status is None
    
    
    logging.info("player fields/attributes created")
    
    # class methods
    def __player_name__(self): 
        
        return player_name
    def __player_health__(self): 
        
        return player_health
    def __player_status__(self): 
        
        return player_status
    def __player_hunger__(self): 
        
        return player_hunger
    def __player_thirst__(self): 
        
        return player_thirst
    def __player_level__(self): 
        
        return player_level
    def __player_experience__(self): 
        
        return player_exp
    
    
    # < - will think of some behaviors in the future
    pass


# variables
NICKNAME = Player.__player_name__()
health = Player.__player_health__()
hunger = Player.__player_hunger__()
thirst = Player.__player_thirst__()
level = Player.__player_level__()
experience = Player.__player_experience__()

# object instances
player = Player(NICKNAME, health, hunger, thirst, level, experience)




























