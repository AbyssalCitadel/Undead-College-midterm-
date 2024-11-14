from random import choice, randrange
from location_class import lower_floor_rooms, upper_floor_rooms, outside_rooms
from enemies_class import Pigskins, Ms_Wobbles, Church_Grim, Eyesore, Trite

# Items! So far, only the tome and two potions.
class items:
    def __init__(self, name, discription):
        self.discription = discription
        self.name = name

# Picks a room, then appends the current item to that room's inventory
    def pick_room(self, item):
        random_floor = randrange(0, 3)

        if random_floor == 0:
            random_room = choice(lower_floor_rooms)
        elif random_floor == 1:
            random_room = choice(upper_floor_rooms)
        else:
            random_room = choice(outside_rooms)
        random_room.items.append(item)
    
# NOTE: I name the classes like this so they don't get confused with their objects when transfering them between files

class tome_class(items):
    def __init__(self, name, discription):
        super().__init__(name, discription)
        

class inv_potion_class(items):
    def __init__(self, name, discription):
        super().__init__(name, discription)

    def use(self, user):
        #Yea, I know I can't spell
        print("Embers turned invisable! Stealth back to full!")
        user.stealth_bar = 100

class sight_potion_class(items):
    def __init__(self, name, discription):
        super().__init__(name, discription)
    
    def use(self):
        print(f"Embers can now see where every undead is! \nThere are undead in the {Pigskins.enemy_location}, {Ms_Wobbles.enemy_location}, {Church_Grim.enemy_location}, {Trite.enemy_location}, and the {Eyesore.enemy_location}")
    
    
inv_potion = inv_potion_class('invisibility potion', "a light blue glittery liquid in a small vial. A torn label says 'invisibility potion'.")
sight_potion = sight_potion_class('sight potion', "a dirty bottle filled with moss green slime. A tag attached to the bottle's neck reads 'sight potion'.")
tome = tome_class('tome', "the tome!!!!!!!!!!!!!")

inv_potion.pick_room(inv_potion)
sight_potion.pick_room(sight_potion)
tome.pick_room(tome)
