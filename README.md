# Encounter: Fight The Troll #

Hi and Welcome to the Troll Fight! In this game, you'll play a wizard in an encounter against a troll! This is a turn-based game, whereby you and the troll will take turns in making moves against each other. 

You have a number of moves that you can make that will the fight, whether its directly attacking the troll or casting spells to improve your capabilities. however, be wary. the troll has a chance to apply a buff or heal at random each turn on top of attacking!

if you find yourself cornered, you also have the option during your turn to retreat and exit the game. 

## Instructions to run the game ##

1- To begin playing, first open up your terminal.

2- Navigate to the root file ArdaErincOguz_T1A3

2- if you already have python installed, you can skip this step. if not, this game will require a quick installation to enable the interpreter for the program to work. enter the following command.

    sudo apt-get install python -y

3- Next, we'll activate the virtual environment in the file and run the program within the environment. there is a script already ready to do this for you, just enter the following command:

    bash ./battle.sh

4- That should begin the program with a prompt for you to enter your adventurer name, and begin the fight, Good Luck!

* if you have trouble running the script, input the following commands:

    * source .venv/bin/activate 
        this will activate the virtual environment
    * python3 src/battle.py
        this will start the program in the virtual environment


* The application should run smoothly with most operating systems or hardware, no minimum requirement for device specifications.

* The program runs utilizes a number of modules within the python library to ensure the program and its testing works appropriately:
    * 'time' module
    * 'random' module
    * 'sys' module
    * 'io' module
    * 'pytest' module


## Troubleshooting ##:

* if ever you want to exit, during your turn you can opt to retreat, or simply press Ctrl + C which will in turn end the program.

* if you find that you select a valid move and you are given an error, please look through the testing portion of this file


## Features ##

* Turn based fight-mechanic: The game runs on a back and forth mechanic between the troll making its move automatically and you selecting yours. After each turn, you'll see your updated hit points (HP). If at any stage either you or the troll have your HP reduced to zero, the fight will end, hopefully with you as the victor!

* Character Stats: other than HP, both you and the troll have a number of invisible stats that will impact the flow of the fight:
    * Damage multiplier: This stat will increases the damage done by attacks
    * Critical Chance: This is a character's chance to land a critical hit when attacking, greatly increasing the damage done by that attack
    * Buff-Counter: This is a counter that counts down each turn when a buff has applied, enabling buff expiry after it reaches zero.

* Move-Options: While the troll's moves are automatic and based on chance, you as the adventurer are smarter and pick your actions with strategy. Be wary though, you can only make one move each turn, so make it count and think ahead:
    * On your turn, you can choose to make an attack, which will give you the option out of 3 abilities to deal damage to the troll.
    * you can also choose to take a beat and drink a healing potion, allowing you to stay in the fight longer.
    * if you want to play the long game, you can also opt to cast a buff on yourself, temporarily increasing your damage done and your critical chance for 3 turns.
    * if you are feeling cornered, you can opt to retreat, which will exit the game and give you a chance to strategize and tackle the troll next game.




## Testing ##


to conduct testing you'll need to install a module manager. To begin with, make sure your command line is prefixed with the  - pip. but make sure your virtual environment is active, enter the following command:

source .venv/bin/activate 

check for the (.venv) prefix to your terminal input, as below:

ACtivated Virtual Environment ![Active_.Venv] (docs/virtual.png)

then, install the package manager pip using the link below:

https://bootstrap.pypa.io/get-pip.py

in your terminal, enter the appropriate command depending on your OS:

Windows:    py -m pip install
Unix/MacOS:     pip3 install pytest

pip3 install pytest

this will install a testing package that will allow you to run some tests built into the program

once the package is installed, input the following commands:

* to test the inputs for correct functioning: pytest src/input_testing.py
* to test the functions in the program for correct functioning: pytest src/function.py

this will run some tests to see if the functions within the program are working properly. if tests fail, reinstall the program from scratch.


## Additional Information ##

* Link to GitHub repository: https://github.com/ArdaEO14455/T1A3---Terminal-Application

### Implementation Plan ###

1. I started with creating classes for both the troll and the adventurer, including their HP and other stats.
Object Creation Task: ![Object_Creation_Card] (/docs/object_creation.png)

2. create a simple attack function that would impact the health parameter of instances, printing the remaining health
Basic Attack Task: ![basic_attack_card] (docs/basic_attack.png)

3. in another file, i created instances of each class, and implement a while loop that would cycle between the troll and the adventurer attacking one another, ensuring that the program ended when one reached 0 HP
Loop Creation Task ![Loop_task] (docs/Loop.png)

4. after creating additional copies of the simple attack, implement automation of the troll's attack, while implementing a choice-selection prompt, then integrate damage multiplier and critical chance into the attacks.
Moves & Stats ![Moves+Stats] (docs/Loop.png)

5. Additional Moves: added heal and a buff move for both troll and adventurer, automated for the former, selectable for the latter. add a buff counter that would count down once each turn if the buff counter is set to a higher-than-zero value. Also add a life-leech move for the adventurer

Aditional Moves ![Add.Moves] (docs/additional_implementations.png)

6. Add a retreat function to exit the game on adventurer turn.

7. Housekeeping: give unique descriptions for each move, health recaps after each turn, and pauses after descriptions to prevent a flurry of outputs

Housekeeping ![Housekeeping] (docs/Housekeeping.png)


### Broader Implementation Task Tracking ###

Trello Board ![Trello_Board] docs/Trello_Board.png
Overall Features Cards:

![Overall_Battle_Loop] docs/Battle Feature.png
![Class_Features] docs/object_classes_feature.png
![Mechanics] docs/Battle_Mechanics.png



