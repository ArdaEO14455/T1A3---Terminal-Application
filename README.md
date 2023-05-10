# Encounter: Fight The Troll #

Hi and Welcome to the Troll Fight! In this game, you'll play a wizard in an encounter against a troll! This is a turn-based game, whereby you and the troll will take turns in making moves against each other. 

You have a number of moves that you can make that will the fight, whether its directly attacking the troll or casting spells to improve your capabilities. if you find yourself cornered, you also have the option during your turn to retreat and exit the game. 

## Instructions to run the game ##

1- To begin playing, first open up your terminal.
2- if you already have python installed, you can skip this step. if not, this game will require a quick installation to enable the interpreter for the program to work. enter the following command.

    sudo apt-get install python -y

3- Next, we'll activate the virtual environment in the file and run the program within the environment. there is a script already ready to do this for you, just enter the following command:

    bash ./troll_fight.sh

4- That should begin the program with a prompt for you to enter your adventurer name, and begin the fight, Good Luck!


## Troubleshooting ##:

* if ever you want to exit, during your turn you can opt to retreat, which will in turn end the program.

* if you find that you select a valid move and you are given an error, please look through the testing portion of this file

## Features ##

* Turn based fight-mechanic: The game runs on a back and forth between the troll making its move automatically and you selecting yours. After each turn, you'll see your updated hit points (HP). If at any stage either you or the troll have your HP reduced to zero, the fight will end, hopefully with you as the victor!

* Character Stats: other than HP, both you and the troll have a number of stats that will impact the flow of the fight:
        *

* Move-Options: 



##Testing##

in your terminal, enter the appropriate command depending on your OS:

Windows:    py -m pip install
Unix/MacOS:     pip3 install pytest

then, run the following command:

pip3 install pytest

this will install a testing package that will allow you to run some tests built into the program

once the package is installed, input the following command:

pytest src/input_testing.py

this will run some tests to see if the functions within the program are working properly

