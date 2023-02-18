def logger(): # Genesis Gir's typical logger preset! 🪵
    
    # importing modules
    import logging, logging.handlers
    from logging.handlers import SMTPHandler
    
    
    # create the logger and set severity
    logger = logging.getLogger(__name__)
    logger.propagate = False  # prevent events from being passed to the root logger
    logger.setLevel(logging.DEBUG) # set logger level

    # create handles and set their severity
    
    #File Handlers
    file_handler = logging.FileHandler( 
    filename = r"GenesisGir-Lessons-VOL.4\Lessons\DarkCloud\Log\logger.log",
    mode = 'w', # filemode 
    encoding = 'utf-8', # set encoding format
    delay = False, 
    errors = None)
    file_handler.setLevel(logging.DEBUG) # severity level

    
    # create formatter
    formatter = logging.Formatter("%(asctime)s [%(name)s] [%(levelname)s] [Lvl:%(levelno)s] [%(funcName)s] [%(lineno)d] %(message)s",
    datefmt='%m/%d/%Y %I:%M:%S %p')

    # add formatter to handles
    file_handler.setFormatter(formatter)
    
    # adding the handler
    logger.addHandler(file_handler)
    
    # prevent logging events to stdout/stream by removing the handler
    logger.removeHandler(logging.StreamHandler)
    
    return logger
    pass
# logger variable
logger = logger()

# import modules
from dataclasses import dataclass, fields

# dataclass
@dataclass
class DarkPlayer:
    """ # DarkPlayer
    DarkPlayer class contains the methods that are capable of transmitting music & sound effects within the program such as the 'dark_player_ost' method for
    music and the 'dark_player_fx' responsible for ommiting sound fx.
    """
    
    # class methods
    def dark_player_ost(filepath: str, volume: float = 0.2, x: int = -1, y: int = 0, z: int = 0):
        # docstring
        """The dark player is a function that ommits music to play in the backround of the the program and has a parameter called 'filepath'
        where the arguement should be the filepath to the .wav file you wish to playback. The volume parameter controls the volume of the
        song, the x = loop int, y = maxtime int, z = fadeout ms int.


                                        █▀▄ ▄▀█ █▀█ █▄▀   █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█
                                        █▄▀ █▀█ █▀▄ █░█   █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄

                                        ⣿⣿⣿⣿⣿⣿⠟⠋⠁⣀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿
                                        ⣿⣿⣿⣿⠋⠁⠀⠀⠺⠿⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿
                                        ⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⠀⠀⠀⠀⠀⣤⣦⣄⠀⠀
                                        ⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⠏⣿⣿⣿⣿⣿⣁⠀⠀⠀⠛⠙⠛⠋⠀⠀
                                        ⡿⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⣰⣿⣿⣿⣿⡄⠘⣿⣿⣿⣿⣷⠄⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⡇⠀⠀⠀⠀⠀⠀⠀⠸⠇⣼⣿⣿⣿⣿⣿⣷⣄⠘⢿⣿⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠁⠀⠀⠀⣴⣿⠀⣐⣣⣸⣿⣿⣿⣿⣿⠟⠛⠛⠀⠌⠻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⣶⣮⣽⣰⣿⡿⢿⣿⣿⣿⣿⣿⡀⢿⣤⠄⢠⣄⢹⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⣿⣿⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⠿⣶⣶⣾⣿⣿⡆⢻⣿⣿⠃⢠⠖⠛⣛⣷⠀   ℬℰ𝒮𝒯𝒪𝒲 𝒜 ℋ𝒜ℛℳ𝒪𝒩𝒴 𝒰𝒩ℒℐ𝒦ℰ 𝒩𝒪 𝒪𝒯ℋℰℛ
                                        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣮⣝⡻⠿⠿⢃⣄⣭⡟⢀⡎⣰⡶⣪⣿⠀   
                                        ⠀⠀⠘⣿⣿⣿⠟⣛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⢁⣾⣿⢿⣿⣿⠏⠀        σԋ ԋҽαʋҽɳɬყ ടσᥙɳԃ 𝓬ᥙɾҽ 𝓶ҽ
                                        ⠀⠀⠀⣻⣿⡟⠘⠿⠿⠎⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣿⣿⠧⣷⠟⠁⠀⠀
                                        ⡇⠀⠀⢹⣿⡧⠀⡀⠀⣀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢰⣿⠀⠀⠀⠀                𝓶ᥙടι𝓬 𝜏σ 𝜏ԋყ ҽαɾട
                                        ⡇⠀⠀⠀⢻⢰⣿⣶⣿⡿⠿⢂⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⡏⠀⠀⠁⠀⠀⠀⠀
                                        ⣷⠀⠀⠀⠀⠈⠿⠟⣁⣴⣾⣿⣿⠿⠿⣛⣋⣥⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⡀

        """
        
        # globals
        global logger
        
        # import modules
        import pygame
        from pygame import mixer

        # file path
        path = filepath # wav file path

        # initalize mixer
        pygame.mixer.init()

        # create sound buffer object
        song = pygame.mixer.music(path) 

        """ <- pygame.mixer.music docstring

    █▀█ █▄█ █▀▀ ▄▀█ █▀▄▀█ █▀▀ ░ █▀▄▀█ █ ▀▄▀ █▀▀ █▀█ ░ █▀▄▀█ █░█ █▀ █ █▀▀
    █▀▀ ░█░ █▄█ █▀█ █░▀░█ ██▄ ▄ █░▀░█ █ █░█ ██▄ █▀▄ ▄ █░▀░█ █▄█ ▄█ █ █▄▄


    The music module is closely tied to pygame.mixerpygame module for loading and playing sounds. Use the music module to control the playback of music
    in the sound mixer.

    The difference between the music playback and regular Sound playback is that the music is streamed, and never actually loaded all at once.
    The mixer system only supports a single music stream at once.

    On older pygame versions, MP3 support was limited under Mac and Linux. 
    This changed in pygame v2.0.2 which got improved MP3 support. 
    Consider using OGG file format for music as that can give slightly better compression than MP3 in most cases.
    """

        # set volume for .wav
        song.set_volume(volume) # set the playback volume for this Sound

        # playback
        pygame.mixer.music.play(
            song, 
            loops=x, 
            maxtime=y, 
            fade_ms=z

                                ) # begin sound playback play(loops=0, maxtime=0, fade_ms=0) -> Channel

        # log info
        logger.info(".wav rendered!")
        pass

    def dark_player_fx(filepath: str, volume: float = 0.2, x: int = -1, y: int = 0, z: int = 0):
        # docstring
        """The dark player fx is a function that emmits sounds to play in the the program and has the same parameters as DP. filepath = .wav path. 
        The volume parameter controls the volume of the song, the x = loop int, y = maxtime int, z = fadeout ms int.


                                        █▀▄ ▄▀█ █▀█ █▄▀   █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█
                                        █▄▀ █▀█ █▀▄ █░█   █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄ 
                                                        █▀▀ ▀▄▀
                                                        █▀░ █░█

                                        ⣿⣿⣿⣿⣿⣿⠟⠋⠁⣀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿
                                        ⣿⣿⣿⣿⠋⠁⠀⠀⠺⠿⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿
                                        ⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⠀⠀⠀⠀⠀⣤⣦⣄⠀⠀
                                        ⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⠏⣿⣿⣿⣿⣿⣁⠀⠀⠀⠛⠙⠛⠋⠀⠀
                                        ⡿⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⣰⣿⣿⣿⣿⡄⠘⣿⣿⣿⣿⣷⠄⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⡇⠀⠀⠀⠀⠀⠀⠀⠸⠇⣼⣿⣿⣿⣿⣿⣷⣄⠘⢿⣿⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀
                                        ⠁⠀⠀⠀⣴⣿⠀⣐⣣⣸⣿⣿⣿⣿⣿⠟⠛⠛⠀⠌⠻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⣶⣮⣽⣰⣿⡿⢿⣿⣿⣿⣿⣿⡀⢿⣤⠄⢠⣄⢹⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
                                        ⠀⠀⠀⣿⣿⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⠿⣶⣶⣾⣿⣿⡆⢻⣿⣿⠃⢠⠖⠛⣛⣷⠀   ℬℰ𝒮𝒯𝒪𝒲 𝒜 ℋ𝒜ℛℳ𝒪𝒩𝒴 𝒰𝒩ℒℐ𝒦ℰ 𝒩𝒪 𝒪𝒯ℋℰℛ
                                        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣮⣝⡻⠿⠿⢃⣄⣭⡟⢀⡎⣰⡶⣪⣿⠀   
                                        ⠀⠀⠘⣿⣿⣿⠟⣛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⢁⣾⣿⢿⣿⣿⠏⠀        σԋ ԋҽαʋҽɳɬყ ടσᥙɳԃ 𝓬ᥙɾҽ 𝓶ҽ
                                        ⠀⠀⠀⣻⣿⡟⠘⠿⠿⠎⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣿⣿⠧⣷⠟⠁⠀⠀
                                        ⡇⠀⠀⢹⣿⡧⠀⡀⠀⣀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢰⣿⠀⠀⠀⠀                𝓶ᥙടι𝓬 𝜏σ 𝜏ԋყ ҽαɾട
                                        ⡇⠀⠀⠀⢻⢰⣿⣶⣿⡿⠿⢂⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⡏⠀⠀⠁⠀⠀⠀⠀
                                        ⣷⠀⠀⠀⠀⠈⠿⠟⣁⣴⣾⣿⣿⠿⠿⣛⣋⣥⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⡀

        """
        
        # import modules
        import pygame
        from pygame import mixer

        # file path
        path = filepath # wav file path

        # initalize mixer
        pygame.mixer.init()

        # create sound object/buffer
        sound = pygame.mixer.Sound(path) # Create a new Sound object from a file or buffer object

        """ <- pygame.mixer.Sound docstring

    █▀█ █▄█ █▀▀ ▄▀█ █▀▄▀█ █▀▀ ░ █▀▄▀█ █ ▀▄▀ █▀▀ █▀█ ░ █▀ █▀█ █░█ █▄░█ █▀▄
    █▀▀ ░█░ █▄█ █▀█ █░▀░█ ██▄ ▄ █░▀░█ █ █░█ ██▄ █▀▄ ▄ ▄█ █▄█ █▄█ █░▀█ █▄▀

    Load a new sound buffer from a filename, a python file object or a readable buffer object. Limited resampling will be performed to help the sample 
    match the initialize arguments for the mixer. A Unicode string can only be a file pathname. A bytes object can be either a pathname or a buffer object. 
    Use the 'file' or 'buffer' keywords to avoid ambiguity; otherwise Sound may guess wrong. If the array keyword is used, the object is expected to export
    a new buffer interface (The object is checked for a buffer interface first.)

    The Sound object represents actual sound sample data. Methods that change the state of the Sound object will the all instances of the Sound playback.
    A Sound object also exports a new buffer interface.

    The Sound can be loaded from an OGG audio file or from an uncompressed WAV.
    Note: The buffer will be copied internally, no data will be shared between it and the Sound object.

    For now buffer and array support is consistent with sndarray.make_sound for Numeric arrays, in that sample sign and byte order are ignored.
    This will change, either by correctly handling sign and byte order, or by raising an exception when different. Also, source samples are truncated 
    to fit the audio sample size. This will not change.

    New in pygame 1.8: pygame.mixer.Sound(buffer)
    New in pygame 1.9.2: pygame.mixer.SoundCreate a new Sound object from a file or buffer object keyword arguments and array interface support
    New in pygame 2.0.1: pathlib.Path support on Python 3.
        """

        # set volume for .wav
        sound.set_volume(volume) # set the playback volume for this Sound

        # playback
        pygame.mixer.Sound.play(
            sound, 
            loops=x, 
            maxtime=y, 
            fade_ms=z) # begin sound playback play(loops=0, maxtime=0, fade_ms=0) -> Channel

        # [INFO] [20]
        logger.info('.wav rendered')

# object instance/constructor
DP = DarkPlayer()