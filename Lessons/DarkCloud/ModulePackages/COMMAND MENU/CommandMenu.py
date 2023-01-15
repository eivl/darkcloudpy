# importing modules
from dataclasses import dataclass, field
import logging, logging.handlers

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


# dataclass
@dataclass
class Command_Menu:
    
    
    # globals
    
    # variables
    
    # constants
    
    # fields/attrs
    category: str = field(default_factory= None)
    active_items: str = field(default_factory= None)
    
    #  command menu methods/functions
    @classmethod
    def __items_menu__(self):
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
        # command menu classes
        class Items_Menu:
            
            
            # global fields/attrs
            active_item_slots: str or int
            cash: int
            item_bag: str
            item_bag_slot_used: int = field(default_factory=0) # how many items are currently in the item bag slots
            item_bag__slot_capcity: int = field(default_factory=50) # the capacity of items that can be stored in bag the deafult is '50' slots
            weapon_pouch: str
            attachment_box: str
            trash_can: str or int = field(default_factory=None)
            
            # player item fields/attributes
            player_name: str
            equipped_player_weapon_name_gui: str or int
            equipped_player_weapon_damage_gui: str or int
            player_health_bar_gui: int
            player_weapon_durability_gui: int
            player_defense_power: int 
            player_thrist_bar_gui: int or str
            
            
            # ally item fields/attributes
            ally_name: str
            equipped_ally_weapon_name_gui: str or int
            equipped_ally_weapon_damage_gui: str or int
            ally_health_bar_gui: int
            ally_weapon_durability_gui: int
            ally_defense_power: int 
            ally_thrist_bar_gui: int or str
            
            
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
            
            pass
        pass
    
    @classmethod
    def __weapons_menu__(self):
        # docstring
        """ # weapons Command menu
        View your weapons and attachments in the Weapons inventory.
        """
        
        # import modules
        from dataclasses import dataclass, field
        import logging, logging.handlers
        
        # command menu classes
        def weapon_menu():
            
            # gloabls
            
            # variables
            
            # constants
            
            # fields/attributes
            # global fields/attributes
            weapon_slot_capacity: int = field(default_factory=10)
            repair_powder_amount: str or int = field(default_factory=0)
            powerup_powder_amount: str or int = field(default_factory=0)
            
            # equipped weapon fields
            equipped_weapon: str = field(default_factory=None) # insert the 'dagger' as defualt factory
            equipped_weapon_description_gui: str
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
            
            
            # class methods
            @classmethod
            class Equip_Weapon():
                # docstring
                """ # Equip Weapon Function
                
                """
                pass
            
            @classmethod
            class Customize_Weapon():
                # docstring
                """ # Customize Weapon Function
                
                """
                pass
            
            @classmethod
            class Equip_Attributes():
                # docstring
                """ # Equip Attributes Function
                
                """
                pass
            
            @classmethod
            class Repair_Weapon():
                # docstring
                """ # Repair Weapons Function
                
                """
                pass
            
            pass
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    @classmethod
    def __Georama_menu__(self):
        # docstring
        """ # options Command menu
        Begin the re-assembly of your world after you have collected Atla. Use this option when in Edit Mode or in a Dungeon only. 
        You can view Georama in Walking Mode, but you will be unable to edit them.
        """
        pass
    
    
    @classmethod
    def __allies_menu__(self):
        # docstring
        """ # allies Command menu
        Change your Allies while in the dungeons.
        """
        pass
    
    @classmethod
    def __leave_menu__(self):
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

    @classmethod
    def __options_menu__(self):
        # docstring
        """ # options Command menu
        Change game options during play.
        """
        pass
    pass



























