from random import choice, randrange
from enemies_class import enemy_list, hunter
from location_class import outside_rooms, upper_floor_rooms, lower_floor_rooms, transition_rooms
from player_class import Embers



# Dank Dungeon

# 10/12/24

# ¯\_(ツ)_/¯

# This game consists of the player character, Embers, searching a abandoned Necromancers' school for a powerful tome while sneaking past the undead that were left to rot



# Print intro
print (f"To recover the all-powerful tome, a young wizard named Embers needs to venture into the abandoned necromancer's school! \nBut that's not all! Since the necromacer's school is strictly forbidden, to avoid anyone knowing Embers was there, \nthey must find the tome without killing a single undead, or letting any undead see them!")
print (f"\nHow to play: Go from room to room to search for the tome, if one of the undead find you, your stealth bar will go down. If your stealth bar reaches zero, you lose!")
print (f"\nEmbers enters the freezing cold building, a half-rotten sign reads 'Lower Central Hall'\n")

# So, "last location" is for, when a player goes from a transition room into a search room, the level they were on wouldn't get lost. 
last_location = "Lower Central Hall";

# When win = true, the game loop breaks.
win = False
#Turn is how many loops the game has been though, used to for enemies' counters
loops = 0

while True: 
    loops = loops + 1

    # This is how the undead switch rooms, 
    for x in enemy_list:
        if loops%x.counter == 0:
            if type(x) is hunter:
                x.enemy_location = choice(x.target_level(x.target, last_location))
            else:
                x.enemy_location = choice(x.level)

    
    # If the stealth bar is less then one, the game is over. Else, the stealth goes up by two (Because they are away from the enemies sight or something)
    if Embers.stealth_bar < 1:
        print("Now Everyone knows you've been here \nGame over!")
        break
    elif Embers.stealth_bar > 98:
            Embers.stealth_bar = 100
    else:
        Embers.stealth_bar = Embers.stealth_bar + 2
    print(f"Current Stealth: {Embers.stealth_bar}")
    
    #This is all for figuring out which transition room to send the player, for each transition room, the code loops to try to figure out which one the player is susposed to be in
    # Need to find a way to make this less bulky
    for x in transition_rooms:
        if Embers.location.name == x.name: 
            stay_or_move_answer = False
            while stay_or_move_answer == False:
                switch_check = input(f"Would you like to stay at {Embers.location.name}, or switch levels?\nPlease type 'Stay' or 'Switch'\n")
                if switch_check.lower() == 'stay':
                    stay_or_move_answer = True
                    if Embers.location.name.lower() == "lower central hall":
                        last_location = 0
                        Embers.move_action(lower_floor_rooms)
                        break 
                    elif Embers.location.name.lower() == "upper central hall":
                        Embers.move_action(upper_floor_rooms)
                        last_location = 1
                        break 
                    elif Embers.location.name.lower() == "outdoor sidewalk":
                        last_location = 2
                        Embers.move_action(outside_rooms)
                        break 
                if switch_check.lower() == 'switch':
                    #If the player switches levels, this just leads to asking the player which one
                    Embers.stealth_bar = Embers.stealth_bar + randrange(10, 30)
                    Embers.level_switch()
        else:
            #Only check this, ONLY if all possible transition rooms have been checked
            #Checks if any undead is in the room using a list loop check
            if x.name == transition_rooms[-1].name:
                for x in enemy_list:
                    if x.enemy_location == Embers.location:
                        Embers.hide_intro(x, last_location) 

                        break
            else:
                Embers.search_action(Embers.location, last_location)
                    
    for x in Embers.inventory:
        if x.name == 'tome':
            print("You win!!!!")
            win = True

    if win == True:
        break
                
            
    

