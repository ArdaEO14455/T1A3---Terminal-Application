# Fight The Troll
import random
import classes
import time

#Start with Introduction + Ask for Character Name
# While Loop to create back and forth between troll and adventurer until one reaches 0 hp
# While Troll HP > 0 and Adventurer HP > 0:
    # Adventurer Turn
    # Print Action
    # Print Result
    # 1s delay

    # Troll Turn
    # Print Action
    # Print Result
    # 1s delay



troll = classes.Troll('Troll', 100, 2, 0.2)
adventurer = classes.Adventurer(input ('What is your Adventurer name?' ), 100, 1, 0.2)
  
print(troll.__dict__)

print (adventurer.__dict__)

while troll.health > 0 and adventurer.health > 0:
    troll.random_action()
    time.sleep(1)
    adventurer.choose_move()
# Time Module found on https://realpython.com/python-sleep/
    # adventurer.attack(troll)
    if troll.health <= 0:
        print('You have defeated the Troll, Congratulations!')
    elif adventurer.health <= 0:
        print('You have been defeated... Care to try again?')

