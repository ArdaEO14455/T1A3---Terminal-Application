import random
#Troll Class (self, name, health, damage multiplier, critical chance)
class Troll:
    def __init__(self, name, health, dmg_mult, crit_chance):
        self.name = name
        self.health = health
        self.dmg_mult = dmg_mult
        self.crit_chance = crit_chance
    def attack(self, other):
        damage = random.randint(10, 20) * self.dmg_mult
        print(f'{self.name} Attacks {other.name} and does {damage} damage')
        return damage
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
    def attack(self, other):
        damage = random.randint(10, 20) * self.dmg_mult
        print(f'{self.name} Attacks {other.name} and does {damage} damage')
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

    
            
    



