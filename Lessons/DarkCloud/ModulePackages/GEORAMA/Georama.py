# from import statements
from dataclasses import dataclass, field

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
    filename = r"",
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


@dataclass
class Georama:
    
    # globals
    global georama_analysis
    global request_analysis
    global georama_percentage
    global request_percentage
    global georama_percentage_backup
    global request_percentage_backup
    
    # analysis/request variables
    georama_percentage = 0
    request_percentage = 0
    
    # analysis/request backup variables
    georama_percentage_backup = 0
    request_percentage_backup = 0
    
    # fields/attr
    atla_creator: str = field(default="Fairy King")
    georama_analysis: int or float = field(default_factory=str(georama_percentage)+"%") # default georama analysis set to 0
    request_analysis: int or float = field(default_factory=str(request_percentage)+"%") # default request analysis set to 0
    
    # exception handle to check for invalid percentage values
    try: # check for exceptions
        
        # backup percentages
        georama_percentage_backup = georama_percentage
        request_percentage_backup = request_percentage
        
        # check percentages for invalid values
        while True: # check percentages
            
            # check values
            georama_percentage
            request_percentage
            
            if georama_percentage or request_percentage < 0:
                raise ValueError

            elif georama_percentage or request_percentage > 100:
                raise ValueError
            
            else:
                break
            
    except ValueError:
        
        # [ERROR] [40]
        logger.error("one or more of the gemorama percentages reached under the expected values attempting to resolve!")
        
        # variable
        attempt_counter = 0 # keeps track of attempts iterated to fix percentage value
        
        while True: # reset percent values
            
            # check values
            georama_percentage
            georama_percentage_backup
            request_percentage
            request_percentage_backup
            
            # flows
            if georama_percentage and request_percentage == range(0,101): # percentage falls in range of values
                
                # [INFO] [20]
                logger.info(f"values of variables 'georama_percentage' and 'request_percentage' have been reset to 0. loop satisfied attempts [{attempt_counter}]")
                attempts = 0 # reset attempt int
                break
                pass
            
            elif georama_percentage and request_percentage != range(0, 101): # percentage does not fall in range of values
                
                # overwrite percentages w/backup variables
                georama_percentage = georama_percentage_backup
                request_percentage = request_percentage_backup
                
                attempt_counter += 1 # increase attempt by 1
                continue # re-iterate while loop
            
            # [DEBUG] [10]
            logger.debug(f"Attempting to reset values of variables 'georama_percentage' and 'request_percentage' to 0. looping until satisfied, current attempts [{attempt_counter}]")

# objects/constructors
GEORAMA = Georama()

