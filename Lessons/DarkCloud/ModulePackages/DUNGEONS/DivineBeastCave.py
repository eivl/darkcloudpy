# import modules
from dataclasses import dataclass

# dataclass
@dataclass(frozen=True)
class Divine_Beast_Cave():
    # globals
    global name # name of dungeon
    global current_floor # current floor the user is in 
    global location
    global key_name # the name of the key required to progress to next floor
    global total_floors # total floors in the divine beast cave
    global MASTER_JACKET # name of boss of the divine beast cave
    global back_floor_key 
    
    # boss name
    MASTER_JACKET = "Master Jacket"

    
    # fields/attrs
    key_name: str = "Dran's Crest Key"
    back_floor_key: str = "Tram Oil"
    current_floor: int
    name: str = "Divine Beast Cave"
    location: str = "Norune Village"
    total_floors: int = 8
    resident: str = "Dran"
    boss: str = MASTER_JACKET
    poi:str or int = ("B4", "B8")
    
    
    # class methods
    @classmethod
    def __dungeon_name__(self):
        # docstring
        """The dugeon name"""
        return name
        pass
    
    @classmethod
    def __dungeon_location__(self):
        # docstring
        """The dugeon location orgin"""
        return location
        pass
    
    @classmethod
    def __dungeon_current_floor__(self):
        # docstring
        """current Divine Beast Cave floor"""
        return current_floor
        pass
    
    @classmethod
    def __dungeon_total_floors__(self):
        # docstring
        """total Divine Beast Cave floors"""
        return total_floors
        pass
    
    @classmethod
    def __dungeon_key_name__(self):
        # docstring
        """Divine Beast Cave key name"""
        return key_name
        pass
    
    @classmethod
    def __dungeon_back_floor_key_name__(self):
        # docstring
        """back floor Divine Beast Cave key name"""
        return back_floor_key
        pass

# object instances/constructors/initalizers
DIVINE_BEAST_CAVE = Divine_Beast_Cave()