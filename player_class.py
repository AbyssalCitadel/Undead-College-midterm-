# This file complains a lot, but it works perfectly
# Never thought I'd relate to a file

from items_class import inv_potion, sight_potion
from location_class import transition_rooms, transition_room
from random import randrange, choice
from enemies_class import wanderer
# Player class, for player location, inventory, and stealth bar
# Stealth bar is what triggers a "Game Over" It goes down if the player is in the same room as an enemy
#Player level keeps track of what level the player is on, mostly so the player can be tracked by hunters
class player:
    def __init__ (self, location, stealth_bar, inventory):
        self.location = location
        self.stealth_bar = stealth_bar
        self.inventory = inventory

        

    # For when the player is in a search room, and is not dealing with an enemy
    def search_action (self, current_location, level):
        # There was a bug where the player could "Search" rooms without typing "search". This is to fix that
        action = "none"
        #If the user doesn't enter a word associated with any action, the search code loops until it does
        valid_input = False
        while valid_input == False:
            # Input 
            action = input(f"Would you like to search this current location, leave to search somewhere else, or use a potion?\nPlease type 'search', 'leave', or 'use sight potion' or 'use invisibility potion'\n")
            # If the tome and player is in the same location, and the player chooses search, the exit is added to the list of locations
            if action.lower() == 'search':
                valid_input = True
                
                if current_location.items != []:
                    potion = current_location.items.pop()
                    print(f"Embers finds {potion.discription}")
                    Embers.inventory.append(potion)
                    
                else:
                    #Searching a room that doesn't have anything depleates the stealth bar a bit
                    print(f"You search the {current_location.name}... you find nothing!\n")
                    self.stealth_bar = self.stealth_bar - 5
                    
            elif action.lower() == 'leave':
            # if the user chooses leave, just bring them back to the last transition room the were in
                valid_input = True
                Embers.location = transition_rooms[level]
                print(f"Embers leaves and returns to {transition_rooms[level].name}\n")
                return
            
            elif action.lower() == 'use invisibility potion':
                if inv_potion in Embers.inventory:
                    inv_potion.use(Embers)
                    Embers.inventory.remove(inv_potion)
                else:
                    print("Embers doesn't have that!")

            elif action.lower() == 'use sight potion':
                if sight_potion in Embers.inventory:
                    sight_potion.use()
                    Embers.inventory.remove(sight_potion)
                else:
                    print("Embers doesn't have that!")
                
            else:
                print("Please enter a valid action")
        
    # Code for transition rooms! Displays the search rooms associated with the transition room the player is on, then asks the player which they want to go to
    def move_action (self, current_floor):
                    
                    print(f"\nHere's the locations on the current floor you can check!\n")
                    for x in current_floor:
                        print (x.name)
                    valid_input = False
                    # Again with the valid input loop
                    while valid_input == False:
                        target_room = input("Please enter the room you want to go into!\n")

                        # So, since I need Embers' location saved as the object itself, this counter tracks which loop the while loop is on, using that to set Embers' location
                        loop_count = 0
                        for x in current_floor:
                            # loops though the list of the current transition room's search rooms, looking for if the player typed the name of one of them
                            # If so, send them to that room

            
                            if target_room.lower() == x.name.lower():
                                valid_input = True
                                Embers.location = current_floor[loop_count]
                                return
                            else:
                                # Waits until the last search room has been checked, then tells the player
                                if x.name == current_floor[-1].name:
                                 print("Please enter a valid room\n")

                            loop_count = loop_count + 1
                    
    # If the player is in the same search room as an enemy, this asks the player if they want to try running (for a higher stealth bar depletion), or hiding (lower stealth bar depletion, but the stealth bar depletion can run several times if the undead stays in the room)
    def hide_intro (self, current_threat, player_level):
        print(f"It seems like Embers's movement attracted something! Embers turns to look and sees {current_threat.description}")
        valid_input = False
        while valid_input == False:
            flee_check = input(f"Would you like to try to escape the room and risk the undead seeing you, or hide and hope that the undead goes away?\n Please type 'escape' or 'hide' ")
            if flee_check.lower() == 'escape':
                valid_input = True
                Embers.stealth_bar = Embers.stealth_bar - randrange(30, 45)
                Embers.location = transition_rooms[player_level]
            elif flee_check.lower() == 'hide':
                valid_input = True
                threat_present = True
                while threat_present == True:
                    flee_roll = randrange(1, 5)
                    if flee_roll == 3:
                        threat_present = False
                        print("Seems like the undead left")
                        if type(current_threat) == wanderer:
                            current_threat.location = choice(current_threat.level)
                        else:
                            current_threat.location = current_threat.room_scramble
                    else:
                        Embers.stealth_bar = Embers.stealth_bar - randrange(5, 10) 
                        print("It's still here...")
            else:
                print("Please enter a vaild action")

    # This is for switching from transition room to transition room. Displays the avalible rooms, then asked the player which they want to swap to
    def level_switch (self):
        print(f"\nHere's the floors you can move to!")

        for x in transition_rooms:
            print(x.name)
        level_valid_input = False
        while level_valid_input == False:
            target_level = input("\nWhich floor would you like to switch to?\n")
             # same loop counter trick for keeping track of Embers' location as an object
            loop_counter = 0
            # Uses the same "Loop though list" as the transition room to search room
            for x in transition_rooms:
                if target_level.lower() == x.name.lower():
                    level_valid_input = True
                    self.location = transition_rooms[loop_counter]
                    return
                else: 
                    if x.name == transition_rooms[-1].name:
                        print(target_level)
                        print("Please enter a valid room\n")
                loop_counter = loop_counter + 1


Embers = player(transition_rooms[0], 100, [])