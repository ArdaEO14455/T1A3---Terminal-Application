import random
#Troll Class (self, name, health, damage multiplier, critical chance)
class Troll:
    def __init__(self, name, health, dmg_mult, crit_chance):
        self.name = name
        self.health = health
        self.dmg_mult = dmg_mult
        self.crit_chance = crit_chance

    #Troll Move Randomizer
    def random_action(self):
        move_set = ['Throw Stone', 'Kick', 'Ground-Slam']
        move = random.choice(move_set)
    
    # def attack(self, move):
        if move == 'Throw Stone':
            damage = random.randint(10,20) * self.dmg_mult
            print(f'{self.name} Threw a stone, inflicting {damage} damage')
        elif move == 'Ground-Slam':
            damage = random.randint(10,20) * self.dmg_mult
            print(f'{self.name} Slammed the ground around them, Upheaving the earth beneath and dealing {damage} damage')
        elif move == 'Kick':
            damage = random.randint(10,20) * self.dmg_mult
            print(f'{self.name} Swings his tree-trunk leg at you, inflicting {damage} damage')

        return damage
    


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
    def __init__(self, name, health, dmg_mult, crit_chance):
        self.name = name
        self.health = health
        self.dmg_mult = dmg_mult
        self.crit_chance = crit_chance
    
    def choose_move(self):
        print('What would you like to do?')
        print('1. Cast Fireball')
        print('2. Cast another Fireball')
        print('3. Cast Yeet-Fireball')
        move = input()
        if move == '1' :
            print('I cast fireball')
            damage = random.randint(10,20) * self.dmg_mult
            print(f'You inflict {damage} damage on your enemy')
        elif move == '2' :
            damage = random.randint(15,30) * self.dmg_mult
            print(' Oh look, another spell slot. I cast fireball')
            print(f'Your enemy is engulfed in flame, dealing {damage} damage on your enemy')
        elif move == '3' :
            damage = random.randint(40,60) * self.dmg_mult
            print(' I didnt ask how big the room is, I said, I yeet a big-ass fireball')
            print(f'you deal {damage} damage to your enemy. There is no sign remaining of your enemy')
        
        return damage
    
   
        # damage = 10 * self.dmg_mult


# Def Basic Attack 1 - Basic Attack
    # print ("adventurer attacked the troll")

    # Def Attack 2 - Damage Over time (if applicable) 
    # print ("adventurer applied DoT to the troll")

    # Def Buff (potion of strength)
    # Print('Adventurer Drank potion of strength)
    # Print('Your attacks hit harder for two turns)

    # Def Healing Potion
    # Print('Adventurer Drank potion of healing, revitalising them))
        

    # def battle(self, other):
         
    #     print(f'dealing {Character.attack.damage} damage')

    
            
    



