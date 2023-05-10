#Imported Modules
import random
import time


#Troll Class
class Troll:
    def __init__(self, name, health, dmg_mult, crit_chance, buff_counter):
        self.name = name
        self.health = health
        self.dmg_mult = dmg_mult
        self.crit_chance = crit_chance
        self.buff_counter = buff_counter


    #Troll Move Randomizer
    def random_action(self):
        move_set = ['Throw Stone', 'Kick', 'Ground-Slam']
        move = random.choice(move_set)
    #Attack Move-Set
        if move == 'Throw Stone':
            damage = random.randint(20,30) * self.dmg_mult         
            print(f'{self.name} Hurls a nearby stone at you!')
        elif move == 'Ground-Slam':
            damage = random.randint(15,30) * self.dmg_mult
            print(f'{self.name} Slams the ground around them, Upheaving the earth beneath you')
        elif move == 'Kick':
            damage = random.randint(25,35) * self.dmg_mult
            print(f'{self.name} Swings his leg at you!')
        
    #Critical Chance Functionality 
        if random.random() < self.crit_chance:
                time.sleep(1)
                damage *= 1.8
                print('Critical Hit!')
                
    #Damage Output and Return
        time.sleep(1)
        print(f'{self.name} deals {int(damage)} damage')
        return int(damage)
    
class Invalid_Input_Error(Exception):
    pass

#Adventurer Class
class Adventurer:
    def __init__(self, name, health, dmg_mult, crit_chance, buff_counter):
        self.name = name
        self.health = health
        self.dmg_mult = dmg_mult
        self.crit_chance = crit_chance
        self.buff_counter = buff_counter


# Move Select
    def move_select(self):
        print('What do you want to do? (Input selected option number)')
        print('1. Attack')
        print('2. Drink Potion of Healing')
        print('3. Cast Potency of Mana: Lasts 3 Turns')
    
    #Move Selector
        try:
            choose_move = input()
        #Attack - Access to Move-Set 
            if choose_move == '1':
                selected_move = 1
                                   
        #Healing Potion
            elif choose_move == '2':
                selected_move = 2
        #Buff
            elif choose_move == '3':
                print('Your mana surges, temporarily amplifying the effects of your atacks ')
                selected_move = 3
        #Error for invalid option    
            else: raise Invalid_Input_Error
            
        except Invalid_Input_Error:
                print('Invalid Option')
                time.sleep(1)
        finally:
            return selected_move
        


    #Attack Function    
    def attack(self):
        print('How would you like to attack?(Input selected option number)')
        time.sleep(1.5)
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

        except Invalid_Input_Error:
                print("There was a mistake in your casting incantation, causing it to fizzle out")
                time.sleep(1)
          
    #Critical Chance Functionality
        if random.random() < self.crit_chance:
                damage *= 1.8
                print('Critical Hit!')
        time.sleep(1.5)

    #Damage Output and Return
        print(f'You deal {int(damage)} damage')
        time.sleep(1)
        return int(damage)
        
    #Life-steal function for Life-Drain move
    def leech(self):
        if move == '3':
            healing = damage * 0.2
            print(f'You heal yourself for {int(healing)} health')
        else:
            healing = 0
        return int(healing)
            

#Healing Potion
    def selfheal (self):
        healing = random.randint(40,60)
        print(f'You heal yourself for {healing} health')
        time.sleep(1)
        return healing

#Custom Errors





