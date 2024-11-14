# For refrence, there's two types of locations, transition rooms and search rooms. Search rooms can have the tome in them, and transition rooms are how you reach the search rooms
# I use the term "Level" to mean a transition room with all of its search rooms

class location:
    def __init__ (self, name):
        self.name = name

        
class search_room(location):
    def __init__ (self, name, items):
        super().__init__(name)
        self.items = items


class transition_room(location):
    def __init__ (self, name):
        super().__init__(name)


# Locations! The search rooms are all seperated by the trasition room they belong to
lower_floor_rooms = [search_room("Lecture Hall A", []), search_room("Lecture Hall B", []), search_room("Dining Hall", []), search_room("Lower Lab", []), search_room("Gym", []), search_room("Kitchen", [])]
upper_floor_rooms = [search_room("Classroom A", []), search_room("Classroom B", []), search_room("Libary", []), search_room("Planatory", []), search_room("Lounge", []), search_room("Upper Lab", [])]
outside_rooms = [search_room("Graveyard", []), search_room("Garden", []), search_room("Tool Shed", []), search_room("Outdoor Classroom", []), search_room("Playground", []), search_room("Woods", [])]
# Player must be in one of these when they leave a room. Enemies can not be in here. Not yet anyways ;)
transition_rooms = [transition_room("Lower Central Hall") , transition_room("Upper Central Hall"), transition_room("Outdoor Sidewalk")]