# Fight The Troll

#Module Imports

from fight_mechanics import *
from time import sleep

troll = Troll('The Cave Troll', 400, 1.5, 0.10, 0)
adventurer = Adventurer(input ('What is your Adventurer name?' ), 150, 1, 0.1, 0)
#Program Interface Start


print(f'{adventurer.name}, Your encounter begins, fighting a Troll in the wild!') 
sleep(1)
    
while adventurer.health > 0 and troll.health > 0:
    
    try:
        Troll.troll_turn(troll, adventurer)
        if adventurer.health > 0 :
            recap(troll, adventurer)
        else:
            print('You have been defeated... Care to try again?')
            break
        Adventurer.adventurer_turn(adventurer, troll)
        if troll.health > 0 :
            recap(troll, adventurer)
        else:
            print('You have defeated the Troll, Congratulations!')
            break

    except KeyboardInterrupt:
         raise SystemExit
    
                



    

