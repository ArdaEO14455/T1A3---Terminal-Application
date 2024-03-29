#Imported Modules
import random
from time import sleep
from sys import exit


#Custom Errors
class Invalid_Input_Error(Exception):
    pass

#Troll Class
class Troll:
    def __init__(self, name, health, dmg_mult, crit_chance, buff_counter):
        self.name = name
        self.health = health
        self.dmg_mult = dmg_mult
        self.crit_chance = crit_chance
        self.buff_counter = buff_counter
#Troll Turn
    def troll_turn(self, other):
            other.health -= self.random_action()
            sleep(1.5)
            #Troll - Buff Counter
            if self.buff_counter > 0:
                self.dmg_mult = 1.3
                self.crit_chance = 0.35
                self.buff_counter -= 1
                
            else:
                self.dmg_mult = 1
                self.crit_chance = 0.2

#Troll Move Randomizer
    def random_action(self):
        move_set = ['Throw Stone', 'Kick', 'Ground-Slam']
        move = random.choice(move_set)

    #Attack Move-Set
        if move == 'Throw Stone':
            troll_damage = random.randint(20,30) * self.dmg_mult         
            print(f'{self.name} Hurls a nearby stone at you!')
        elif move == 'Ground-Slam':
            troll_damage = random.randint(15,30) * self.dmg_mult
            print(f'{self.name} Slams the ground around them, Upheaving the earth beneath you')
        elif move == 'Kick':
            troll_damage = random.randint(25,35) * self.dmg_mult
            print(f'{self.name} Swings his leg at you!')
        
    #Critical Chance Functionality 
        if random.random() < self.crit_chance:
                sleep(1)
                troll_damage *= 1.8
                print('Critical Hit!')
                
    #Damage Output and Return
        sleep(1)
        print(f'{self.name} deals {int(troll_damage)} damage')
        return int(troll_damage)

#Troll -  Roar & Self Heal
    def buff_heal(self):
        if random.random() < 0.15 and self.buff_counter == 0:
            print("The Troll Roars, preparing to crush it's foe (Buff Lasts 3 Turns)")
            self.buff_counter = 3
            sleep(1.5)
        elif random.random() < 0.1 and self.buff_counter > 0:
            self.health += 50
            sleep(1.5)
            print('The troll devours a nearby morsel, restoring some of its health')

        

    
        



#----------------------------------Adventurer Class--------------------------------------------
class Adventurer:
    def __init__(self, name, health, dmg_mult, crit_chance, buff_counter):
        self.name = name
        self.health = health
        self.dmg_mult = dmg_mult
        self.crit_chance = crit_chance
        self.buff_counter = buff_counter

    def adventurer_turn(self, other):    
        
        # Buff Counter
        if self.buff_counter > 0:
            self.dmg_mult = 1.3
            self.crit_chance = 0.35
            self.buff_counter -= 1

        else:
            self.dmg_mult = 1
            self.crit_chance = 0.2
        #Move Select
        try:
            selected_move = self.move_select()
            if selected_move == '1':
                #Attack
                adventurer_damage = self.attack()
                other.health -= adventurer_damage
                adventurer_healing = self.leech()
                self.health += adventurer_healing
            elif selected_move == '2':
                #Self-Heal
                adventurer_healing = self.selfheal()
                self.health += adventurer_healing
                #Buff
            elif selected_move == '3':
                print('Your mana surges, temporarily amplifying the effects of your atacks ')
                self.buff()
                sleep(1)
                #exit
            elif selected_move == '4':
                print('You narrowly escape into the wilderness')
                exit()
            # else: 
                # print("You missed your chance to make a move")
                # raise AssertionError
        except KeyboardInterrupt:
                self.retreat()
        
        except (AssertionError, UnboundLocalError, NameError):
            print("You missed your chance to make a move")
            sleep(1)

# Move Select
    def move_select(self):
        print('What do you want to do? (Input selected option number)')
        print('1. Attack')
        print('2. Drink Potion of Healing')
        print('3. Cast Potency of Mana: Lasts 3 Turns')
        print('4. Escape')
    
    #Move Selector
        try:
            selected_move = input()
            
        #Attack - Access to Move-Set 
            if selected_move == ('1' or '2' or '3' or '4'):
                return selected_move
                
        #Error for invalid option    
            else: raise Invalid_Input_Error

        except KeyboardInterrupt:
                print(' - You narrowly escape into the wilderness')
                exit()
            
        except Invalid_Input_Error:
                print('Invalid Option')
                sleep(1)
        


    #Attack Function    
    def attack(self):
        print('How would you like to attack?(Input selected option number)')
        sleep(1.5)
        print('1. Cast Fireball: 65 - 80 Base Fire Damage')
        print('2. Cast Lightning Tendrils: 60 - 90 Base Lightning Damage')
        print('3. Cast Life Drain: 60 - 80 Base Dark Magic Damage, Heals Self For 12 - 16 HP')
        global move
        global damage
        try:
            move = input()
    #Attack Moveset
            if move == '1' :
                print(f'{self.name} Casts fireball, englufing their enemy in flames')
                damage = random.randint(65,80) * self.dmg_mult
                
            elif move == '2' :
                print('Lighting reaches down from the heavens, broadly striking the area around your enemy')
                damage = random.randint(60,90) * self.dmg_mult
                
            elif move == '3' :
                print(f'Channeling more desperate, darker methods, {self.name} shaves off the life of their enemy, adding to their own')
                damage = random.randint(60,80) * self.dmg_mult
            #Error for Invalid Option 
            else: raise Invalid_Input_Error

        except KeyboardInterrupt:
                print(' - You narrowly escape into the wilderness')
                exit()
                
        
        except Invalid_Input_Error:
                print("There was a mistake in your casting incantation, causing it to fizzle out")
                sleep(1)
        
          
    #Critical Chance Functionality
        if random.random() < self.crit_chance:
                damage *= 1.8
                print('Critical Hit!')
        sleep(1.5)

    #Damage Output and Return
        print(f'You deal {int(damage)} damage')
        sleep(1)
        return int(damage)
        
    #Life-steal function for Life-Drain move
    def leech(self):
        if move == '3':
            healing = damage * 0.2
            print(f'You heal yourself for {int(healing)} health')
            sleep(1)
        else:
            healing = 0
        return int(healing)
            

#Healing Potion
    def selfheal (self):
        healing = random.randint(40,60)
        print(f'You heal yourself for {healing} health')
        sleep(1)
        return healing

#Buff
    def buff(self):
        self.buff_counter = 3
        sleep(1)
    
#Fight Recap

def recap(self, other):
        print(f'{self.name} HP: {self.health}')
        print(f'{other.name} HP: {other.health}')
        sleep(1)

    