# import modules
from dataclasses import dataclass




# dataclass
@dataclass
class Divine_Beast_Cave():
    # globals
    global name
    global floors
    global current_floor
    global location
    global key_name
    global total_floors
    global MASTER_JACKET
    global back_floor_key
    
    # boss constant
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
    def __dungeon_name__(self):
        # docstring
        """The dugeon name"""
        return name
        pass
    def __dungeon_location__(self):
        # docstring
        """The dugeon location orgin"""
        return location
        pass
    def __dungeon_current_floor__(self):
        # docstring
        """current Divine Beast Cave floor"""
        return current_floor
        pass
    def __dungeon_total_floors__(self):
        # docstring
        """total Divine Beast Cave floors"""
        return total_floors
        pass
    def __dungeon_key_name__(self):
        # docstring
        """Divine Beast Cave key name"""
        return key_name
        pass
    def __dungeon_back_floor_key_name__(self):
        # docstring
        """back floor Divine Beast Cave key name"""
        return back_floor_key
        pass
    pass






