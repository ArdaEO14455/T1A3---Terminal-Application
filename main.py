# Fight The Troll
import random
import classes
import time

troll = classes.Troll('Troll', 100, 2, 0.2)
adventurer = classes.Adventurer(input ('What is your Adventurer name?' ), 100, 1, 0.2)
  

while troll.health > 0 and adventurer.health > 0:
    #Troll Turn
    troll_damage = troll.random_action()
    adventurer.health -= troll_damage
    time.sleep(1)
    if adventurer.health > 0:
        print(f'{adventurer.name} HP: {adventurer.health} ')
    else:
        break
     #Adventurer Turn
    print('What do you want to do?')
    print('1. Attack')
    print('2. Heal Yourself')
    print('3. Retreat')
    choose_move = input()
    if choose_move == '1':
        adventurer_damage = adventurer.attack()
        troll.health -= adventurer_damage
    elif choose_move == '2':
        adventurer_healing = adventurer.healing()
        adventurer.health += adventurer_healing
        print(f'{adventurer.name} HP: {adventurer.health} ')
    else:
        break
    time.sleep(1)
    if troll.health > 0:
        print(f'Troll HP: {troll.health}')
    else:
        print('You retreat to a nearby town to tend to your wounds')
        break

# Time Module found on https://realpython.com/python-sleep/


# Conclusion
if troll.health <= 0:
    print('You have defeated the Troll, Congratulations!')
elif adventurer.health <= 0:
    print('You have been defeated... Care to try again?')

