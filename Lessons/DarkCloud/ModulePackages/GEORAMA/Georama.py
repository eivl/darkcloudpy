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


@dataclass
class Georama_Analysis:
    
    # docstring
    """ # georama
    
    🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 
    
    This screen shows progress though the reconstruction of the current region your in.
    Collection — This is the per- centage of objects recovered for this region.
    Complete — Shows the percentage of elements placed for this region.
    Request — The people you bring back will have requests for you, if you ask them. This graph represents the percentage of requests you have fulfilled.
    
        ────▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    ▀▀▀█─▄▄▄▄▄▄─▄─▄─▄─█
    ───█─█────█─▄▀▄▀▄─█
    ───█─█▄▄▄▄█─▄▀▄▀▄─█
    ───▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀ doc strings are useful to have in your code to display a sense of understanding to the user or person looking at your code!

    🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
    """
    
    # globals
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
    
    
    """ <- exception handling tips!
    🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
    
    
                    ▀█▀ █▀█ █▄█   ▄▀█ █▄░█ █▀▄   █▀▀ ▀▄▀ █▀▀ █▀▀ █▀█ ▀█▀
                    ░█░ █▀▄ ░█░   █▀█ █░▀█ █▄▀   ██▄ █░█ █▄▄ ██▄ █▀▀ ░█░
    
                                ██████████████                                                    
                            ████            ██████                                              
                        ▓▓██                      ▓▓                                            
                        ██                            ██                                          
                        ██            ░░░░▓▓              ██                                        
                    ██░░      ░░░░░░░░░░░░▓▓            ░░██                                      
                    ██    ░░░░░░░░████████████            ██                                      
                    ██    ██░░██████░░░░░░░░▒▒▒▒██          ██                                      
                    ██    ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████          ░░██                                    
                    ██    ██▒▒▒▒▒▒██████░░░░░░░░░░██        ░░██                                    
                ██      ██▒▒████░░░░░░░░░░░░░░░░██        ░░░░██                                  
                ██    ██▒▒██░░░░░░░░░░░░▒▒▒▒▒▒░░░░██    ░░░░░░██                                  
                ██    ████░░░░░░░░    ▒▒░░░░░░░░░░██    ░░░░░░██                                  
                ██    ████░░░░        ░░░░██████░░██    ░░░░░░██                                  
                ██    ██░░░░            ██  ▓▓▓▓░░██  ░░░░░░░░░░██                                
                ██    ██░░▒▒▒▒▒▒        ░░  ░░░░░░░░██░░░░░░░░░░██                                
                ██    ██▒▒░░░░░░░░              ░░░░██░░░░░░██░░██                                
                ██    ████░░████                ░░░░██░░░░░░██░░▓▓           x o x o    ㇄🝗七丂 ﾁ讠〤 セ卄闩セ 讠丂丂ㄩ🝗     x o x o                           
                ██    ██░░██▓▓▓▓░░                ░░██░░░░░░██░░░░▓▓                              
                ██  ██░░██  ░░    ██░░          ░░██░░░░░░████████                              
                ██████░░██                ▒▒    ██  ░░░░░░██░░░░░░██                 ʀᴀɪsᴇ , ʀᴀɪsᴇ , ʀᴀɪsᴇ!           
                ██░░░░░░░░██          ▒▒▒▒░░    ██  ░░░░▓▓░░░░░░  ░░██                          
                ██░░░░░░░░░░██          ░░    ░░██  ░░░░██░░░░        ██               ʟᴇᴛ ᴛʜᴇ ᴄᴏᴅᴇ sᴘᴇᴀᴋ ᴛᴏ ʏᴏᴜ         
                ██  ░░░░░░░░░░████          ░░████  ░░░░██░░░░          ██                      
                ██░░  ░░░░░░░░░░░░░░▓▓████▓▓▓▓▒▒░░██  ░░░░██░░░░          ██               'ғɪɴᴀʟʟʏ' ʙʀᴜʜ       
                ██    ░░  ░░░░░░░░░░░░░░░░░░░░██░░██  ░░░░████░░            ██                    
                ██    ░░  ░░░░░░░░░░░░░░░░░░██░░██    ░░░░████░░            ██                    
                ██  ░░░░  ░░░░░░░░░░░░░░▓▓▓▓░░▓▓██    ░░░░████░░░░          ░░██                  
            ▓▓    ░░  ░░░░░░░░░░██████░░░░██░░██    ░░░░██▒▒██░░            ██                  
            ██  ░░░░  ░░░░░░░░██  ░░░░████░░░░██    ░░░░██▒▒██░░            ░░██                
            ██    ░░  ░░░░░░░░██  ░░██▓▓░░░░░░░░██    ██░░██▒▒▒▒██░░          ░░██                
            ██  ░░░░░░░░░░░░████████░░░░░░░░░░░░██    ██░░██▒▒▒▒▓▓░░            ░░█              
        ██  ░░░░░░░░░░████░░░░██░░░░░░░░░░░░▒▒██    ██░░██▒▒▒▒▒▒██░░          ░░██              
        ██  ░░░░░░████░░░░░░██░░░░░░░░░░░░░░▒▒██  ████░░░░██▒▒▒▒██░░            ░░██            
        ██  ░░░░▓▓▓▓░░▒▒░░░░░░██░░░░░░░░░░░░▒▒▒▒██  ██▒▒██░░██▒▒▒▒▒▒██░░          ░░██            
        ██  ░░██░░░░░░░░░░░░▒▒██▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒████▒▒██░░██▒▒▒▒▒▒████          ░░░░█          
        ██  ██░░░░░░░░░░░░░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██▒▒▒▒▒▒████░░          ░░█          
    ██  ░░██░░░░░░░░░░░░▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒██  ██          ░░██          
    ██  ██░░░░░░░░░░░░▒▒▒▒▒▒▒▒██▒▒██████████████████▒▒▒▒▒▒▒▒▒▒▒▒██    ██░░        ░░░░██        
    ██  ██▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░██████▒▒▒▒▒▒██      ██░░      ░░░░██        
    ██  ░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████░░████░░░░░░░░░░████░░░░░░████▒▒██        ██░░    ░░░░░░██      
    ██  ░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒████░░░░██░░░░██████████░░░░░░░░░░░░░░██          ██░░░░  ░░░░░░██      
    ██  ░░░░██▒▒▒▒▒▒▒▒▒▒██░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██            ██░░░░░░░░░░░░██    
    ██  ░░░░██▒▒▒▒▒▒▒▒██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██              ██░░░░░░░░░░░░██    
    ██  ░░░░░░▓▓▒▒▒▒██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                ██░░░░░░░░░░██    
        ██░░░░░░░░████░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                    ██░░░░░░░░░░██  
        ██░░░░░░░░░░░░██████░░░░░░            ░░░░░░░░░░░░░░░░██                    ██░░░░░░░░░░██  
        ▓▓░░░░░░░░░░░░░░██                      ░░░░░░░░░░░░██                      ▓▓░░░░░░░░░░▓▓

                    丂ㄖㄩ尺⼕🝗 ⼕ㄖᗪ🝗 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂Ꮆ讠尺
    
    Nice your program is running smoothly but you always if not 100% of the time want to make sure it doesn't crash and great ways are to be a
    perfectionist and steer away from the problems but this is coding . problems will persist to render out of nowhere and great ways to 
    get rid of them is with exception handling! The 'try' and 'except' statments will come in handy in the thicc of it all and trust me
    you will need that edge when it comes. There is also a 'finnaly' statement but make sure to do some digging on the web on what it does
    I don't want you to rely on a computer scientist nerd as myself for everything I want you to understand that co-dependacy will lead to failure
    make sure to do alot of the research you wish to study ON YOUR OWN, the internet is a vast sea of knowledge and inforamtion to download via your 
    brain so have at it.
    
    below is an example of how basic exception handling can be implemented in code.
    ᴇxᴀᴍᴘʟᴇ #1
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    try:
        print("Hello, Genesis!")
        raise ValueErrror

    except:
        pass
        
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    ɢᴇɴᴇsɪs ᴅᴏᴄᴜᴍᴇɴᴛᴀɪᴏɴ sᴜᴍᴍᴇʀʏ
    
    We used the 'raise' statement to intentionally raise an exeption to throw the program execution into the except clause,
    once inside this clause we can rectify any errors that persist inside the program and avoiding a rudimentary errors/exceptions
    this way we can stop pesky crashes from happening prematurely inside our script. we put the code we wish to check for exceptions inside the 
    'try' clause and python does a check for any 'raise' statements or any errors. Rememeber, You the programmer have to insight where a error
    has occured within the clause tho the try clause can do backround checks as well 
    
    The end goal to achieve is python scripts that are less prone to crashes.
    check my code presets vol.1 for all the error statments that you can use within the exception handles or search via google!
    
    🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
    """
    
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
GEORAMA = Georama_Analysis(
    
    atla_creator='Fairy King',
        georama_analysis=georama_percentage,
            request_analysis=request_percentage)