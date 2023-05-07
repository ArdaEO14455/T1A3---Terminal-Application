# Fight The Troll
import random
import classes

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



troll = classes.Character('Troll', 100)
troll.stats = (2, 0.1) 

print(troll.__dict__)

adventurer = classes.Character(
    input ('What is your Adventurer name?' ), 100) 
adventurer.stats = (1, 0.1)
print (adventurer.__dict__)

troll.attack(adventurer)
print (adventurer.__dict__)
