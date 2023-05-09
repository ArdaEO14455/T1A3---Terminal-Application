# Fight The Troll

#Module Imports
import random
import classes
# from classes import *
import time

troll = classes.Troll('The Cave Troll', 400, 3, 0.10, 0)
adventurer = classes.Adventurer(input ('What is your Adventurer name?' ), 150, 1, 0.2, 0)
print(f'{adventurer.name}, Your encounter begins, fighting a Troll in the wild!') 
time.sleep(1)
 

#Turn Based Fight
while troll.health > 0 and adventurer.health > 0:
    #Troll Turn
    troll_damage = troll.random_action()
    adventurer.health -= troll_damage

    #Troll -  Roar & Self Heal
    if random.random() < 0.15 and troll.buff_counter == 0:
        print("The Troll Roars, preparing to crush it's foe (Buff Lasts 3 Turns)")
        troll.buff_counter = 3
        time.sleep(1.5)
    elif random.random() < 0.1 and troll.buff_counter > 0:
        troll.health += 50
        time.sleep(1.5)
        print('The troll devours a nearby morsel, restoring some of its health')

    #Troll - Buff Counter
    if troll.buff_counter > 0:
        troll.dmg_mult = 1.3
        troll.crit_chance = 0.35
        troll.buff_counter -= 1
          
    else:
        troll.dmg_mult = 1
        troll.crit_chance = 0.2

    if troll.health > 0 and adventurer.health > 0:
        print(f'Troll HP: {troll.health}')
        print(f'Adventurer HP:{adventurer.health}')
        time.sleep(1)
    else:
        break

   
    #Adventurer Turn:

    selected_move = adventurer.move_select()
    try:
        if selected_move == '1':
            adventurer_damage = adventurer.attack()
            troll.health -= adventurer_damage
            adventurer_healing = adventurer.leech()
            adventurer.health += adventurer_healing
        elif selected_move == '2':
            adventurer_healing = adventurer.selfheal()
            adventurer.health += adventurer_healing
        elif selected_move == '3':
            adventurer.buff_counter = 3
            time.sleep(1)
        else: 
            raise Exception
    
    except Exception:
        # print('That is not a valid option')
        print("You missed your chance to make a move")
        time.sleep(1)



    if troll.health > 0 and adventurer.health > 0:
        print(f'Troll HP: {troll.health}')
        print(f'Adventurer HP:{adventurer.health}')
        time.sleep(1)
    else:
        break






    
    
    
if troll.health <= 0:
    print('You have defeated the Troll, Congratulations!')
elif adventurer.health <= 0:
    print('You have been defeated... Care to try again?')

