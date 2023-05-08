# Fight The Troll
import random
import classes
import time

troll = classes.Troll('The Cave Troll', 400, 1, 0.10, 0)
adventurer = classes.Adventurer(input ('What is your Adventurer name?' ), 150, 1, 0.2, 0)
print(f'{adventurer.name}, Your encounter begins, fighting a Troll in the wild!') 
time.sleep(1)

while troll.health > 0 and adventurer.health > 0:
    
    #Troll Turn
    troll_damage = troll.random_action()
    adventurer.health -= troll_damage
    time.sleep(2)

    # Roar
    if random.random() < 0.15 and troll.buff_counter == 0:
        print("The Troll Roars, preparing to crush it's foe")
        troll.buff_counter = 2
        time.sleep(1.5)

    if troll.buff_counter > 0:
        troll.dmg_mult = 1.3
        troll.crit_chance = 0.35
        troll.buff_counter -= 1
        
    else:
        troll.dmg_mult = 1
        troll.crit_chance = 0.2

    #Health Recap 
    
    if adventurer.health > 0:
        print(f'{adventurer.name} HP: {adventurer.health} ')
        print(f'Troll HP: {troll.health}')
    else:
        break
    time.sleep(2)

     #Adventurer Turn
    print('What do you want to do?')
    print('1. Attack')
    print('2. Drink Potion of Healing')
    print('3. Cast Potency of Mana: Lasts 2 Turns')
    print('4. Retreat')
    
    # Buff Counter
    if adventurer.buff_counter > 0:
        adventurer.dmg_mult = 1.3
        adventurer.crit_chance = 0.35
        adventurer.buff_counter -= 1
        
    else:
        adventurer.dmg_mult = 1
        adventurer.crit_chance = 0.2
    
    
    choose_move = input()

    if choose_move == '1':
        adventurer_damage = adventurer.attack()
        troll.health -= adventurer_damage
    elif choose_move == '2':
        adventurer_healing = adventurer.healing()
        adventurer.health += adventurer_healing
        print(f'{adventurer.name} HP: {adventurer.health} ')
    elif choose_move == '3':
        print('Your mana surges, temporarily amplifying the effects of your atacks ')
        adventurer.buff_counter = 2
    else:
        print('You retreat to a nearby town to tend to your wounds')
        break
    time.sleep(1)
    
    
    #Health Recap
    if troll.health > 0:
        print(f'Troll HP: {troll.health}')
        print(f'Adventurer HP:{adventurer.health}')
        time.sleep(1)
    else:
        break

# Time Module found on https://realpython.com/python-sleep/


# Conclusion
if troll.health <= 0:
    print('You have defeated the Troll, Congratulations!')
elif adventurer.health <= 0:
    print('You have been defeated... Care to try again?')

