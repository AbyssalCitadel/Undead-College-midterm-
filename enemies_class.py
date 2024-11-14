from random import choice, randrange
from location_class import lower_floor_rooms, upper_floor_rooms, outside_rooms
# All enemies require a name, description, and a counter
# Counter is how long until that enemy moves

class enemy: 
    def __init__(self, name, description, counter, enemy_location):
        self.name = name
        self.description = description
        self.counter = counter
        self.enemy_location = enemy_location


class wanderer(enemy):
    def __init__(self, name, description, counter, level, enemy_location):
        super().__init__(name, description, counter, enemy_location)
        self.level = level
# Hunters' prefered level is whatever level the player is on. In the future, I want to make them sometimes target fellow enemies if the lose track of Embers.
# So, self.target will become important in the future
class hunter(enemy):
    def __init__(self, name, description, counter, target, current_level, enemy_location):
        super().__init__(name, description, counter, enemy_location)
        self.target = target
        self.current_level = current_level

    # How hunter's switch to Ember's level. Also has set up for hunters targeting other enemies
    def target_level(self, target, last_location):
        if target == "Embers":
            if last_location == "0":
                return lower_floor_rooms
            elif last_location == "1":
                return upper_floor_rooms
            else:
                return outside_rooms
        else:
            return target.level
        
        
    # During an esacpe with a hunter, if the hunter leaves the room, they go to a random room at a ramdom level
    def room_scramble():
        random_level = randrange(1, 4)
        if random_level == 1:
            return choice(lower_floor_rooms)
        elif random_level == 2:
            return choice(upper_floor_rooms)
        else:
            return choice(outside_rooms)


# A empty list for enemies, they will get added to this list so its easy to check if they are in the same room as the player, using the loop list check
enemy_list = []

# Enemies! For now, they each have their own level
Pigskins = wanderer("Pigskins", "a zombie with its head replaced with that of a boar. It's dressed in school merch.", 3, lower_floor_rooms, choice(lower_floor_rooms))
Ms_Wobbles = wanderer("Ms. Wobbles", "a bundle of stiched-together limbs resembling a long necked bird. Looks like one of the kids decided to play Frankistein.", 4, upper_floor_rooms, choice(upper_floor_rooms))
Church_Grim = wanderer("Church Grim", "a skeleton hound, reanimated and set to guard. Looks like it has a wasp nest built into its ribcage.", 2 , outside_rooms, choice(outside_rooms))

Trite = hunter("Clawed Horror", "a  large spider-like monster, unusally fast for its size. Based on the collar wrapped around it's neck, it used to be a class pet.", 3, "Embers", outside_rooms, choice(outside_rooms))
Eyesore = hunter("Eyesore", "a security system consisting of a large zombie covered with a large amount of eyes. By some stroke of enginering, the zombie has wings that allow it to just barely lift itself off the ground.", 3, "Embers", outside_rooms, choice(outside_rooms))

enemy_list.append(Pigskins)
enemy_list.append(Ms_Wobbles)
enemy_list.append(Church_Grim)
enemy_list.append(Trite)
enemy_list.append(Eyesore)