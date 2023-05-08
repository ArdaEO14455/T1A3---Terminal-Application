import random
import time
#Troll Class (self, name, health, damage multiplier, critical chance)
class Troll:
    def __init__(self, name, health, dmg_mult, crit_chance, buff_counter):
        self.name = name
        self.health = health
        self.dmg_mult = dmg_mult
        self.crit_chance = crit_chance
        self.buff_counter = buff_counter

    #Troll Move Randomizer
    def random_action(self):
        move_set = ['Throw Stone', 'Kick', 'Ground-Slam',]
        move = random.choice(move_set)
    
        if move == 'Throw Stone':
            damage = random.randint(20,30) * self.dmg_mult         
            print(f'{self.name} Hurls a nearby stone at you!')
        elif move == 'Ground-Slam':
            damage = random.randint(15,30) * self.dmg_mult
            print(f'{self.name} Slams the ground around them, Upheaving the earth beneath you')
        elif move == 'Kick':
            damage = random.randint(25,35) * self.dmg_mult
            print(f'{self.name} Swings his leg at you!')
        

        if random.random() < self.crit_chance:
                damage *= 1.8
                print('Critical Hit!')
                time.sleep(1)
                
        print(f'{self.name} deals {int(damage)} damage')
        return int(damage)
    
    
    


    # def attack2(self, other):
    #     damage = random.randint(10, 20) * self.dmg_mult
    #     print(f'{self.name} Attack2 {other.name} and does {damage} damage')
    #     return damage
    
    # def attack3(self, other):
    #     damage = random.randint(10, 20) * self.dmg_mult
    #     print(f'{self.name} Attack3 {other.name} and does {damage} damage')
    #     return damage
    
    # def moves [attack1, attack2, attack3]
        # damage = 10 * self.dmg_mult
# def attack2(self, dmg):
    #     pass

        # Def Basic Attack 1
        # 15 dmg
        # print("troll did attack 1 at the Adventurer")
    
        # Def ttack 2 - Damage Over time (if applicable)
        # 5 dmg per turn
        # print("troll applied attack 2 DoT at the Adventurer")
    
        # Def Buff (Roar)
        # + x to damage multiplier, + x% to crit chance for x turns
        # print("troll roared, preparing to fight harder")
        # priint()

        
# Adventurer Class(Self, HP (60), Damage multiplier, crit chance)
    
class Adventurer:
    def __init__(self, name, health, dmg_mult, crit_chance, buff_counter):
        self.name = name
        self.health = health
        self.dmg_mult = dmg_mult
        self.crit_chance = crit_chance
        self.buff_counter = buff_counter
    
    def attack(self):
        print('How would you like to attack?')
        time.sleep(1.5)
        print('1. Cast Fireball: 65 - 80 Fire Damage')
        print('2. Cast Lightning Tendrils: 60 - 90 Lightning Damage')
        print('3. Life Drain: 60 - 80 Dark Magic Damage')
        global move
        global damage
        move = input()
        if move == '1' :
            print(f'{self.name} Casts fireball, englufing their enemy in flames')
            damage = random.randint(65,80) * self.dmg_mult
            
        elif move == '2' :
            print('Lighting reaches down from the heavens, broadly striking the area around your enemy')
            damage = random.randint(60,90) * self.dmg_mult
            
        elif move == '3' :
            print(f'Channeling more desperate, darker methods, {self.name} shaves off the life of their enemy, adding to their own')
            damage = random.randint(60,80) * self.dmg_mult
              
           
            
        
        if random.random() < self.crit_chance:
                damage *= 1.8
                print('Critical Hit!')
        time.sleep(1.5)
        
        print(f'You deal {int(damage)} damage')
        time.sleep(1)
        
        return int(damage)
        

    def leech(self):
        if move == '3':
            healing = damage * 0.2
            print(f'You heal yourself for {int(healing)} health')
        else:
            healing = 0
        return int(healing)
            


    def selfheal (self):
        healing = random.randint(40,60)
        print(f'You heal yourself for {healing} health')
        time.sleep(1)
        return healing
        

    
            
    



