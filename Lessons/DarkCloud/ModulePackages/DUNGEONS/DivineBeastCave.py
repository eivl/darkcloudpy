# import modules
from dataclasses import dataclass

# sub package module imports
from ModulePackages.BOSS.Boss import *

# dataclass
@dataclass(frozen=True)
class Divine_Beast_Cave():
    
    # globals
    global MASTER_JACKET # name of boss of the divine beast cave
    global current_floor
    
    
    # dungeon variables
    current_floor = 0
    
    # fields/attrs
    current_dungeon_floor: int
    key_name: str = "Dran's Crest Key"
    back_floor_key: str = "Tram Oil"
    name: str = "Divine Beast Cave"
    location: str = "Norune Village"
    total_floors: int = 8
    resident: str = "Dran"
    boss: str = MASTER_JACKET.name
    poi:str or int = ("B4", "B8")
    
    
    # class methods
    @classmethod
    def __dungeon_name__(self):
        # docstring
        """The dugeon name"""
        
        # global
        global name
        return name
        pass
    
    @classmethod
    def __dungeon_location__(self):
        # docstring
        """The dugeon location orgin"""
        
        # global
        global location
        return location
        pass
    
    @classmethod
    def __dungeon_current_floor__(self):
        # docstring
        """current Divine Beast Cave floor"""
        
        # global
        global current_floor
        return current_floor
        pass
    
    @classmethod
    def __dungeon_total_floors__(self):
        # docstring
        """total Divine Beast Cave floors"""
        
        # global
        global total_floors
        return total_floors
        pass
    
    @classmethod
    def __dungeon_key_name__(self):
        # docstring
        """Divine Beast Cave key name"""
        
        # global
        global key_name
        return key_name
        pass
    
    @classmethod
    def __dungeon_back_floor_key_name__(self):
        # docstring
        """back floor Divine Beast Cave key name"""
        
        # global
        global back_floor_key
        return back_floor_key
        pass

# object instances/constructors/initalizers
DIVINE_BEAST_CAVE = Divine_Beast_Cave(current_dungeon_floor=current_floor)
