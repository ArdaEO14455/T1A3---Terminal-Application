# Shared Stats:
class Stats:
    def __init__(self, dmgmult, critchance):
        self.dmgmult = dmgmult
        self.critchance = critchance
    # HP
    # damage multiplier
    # crit chance


class Character:
    def __init__(self, hp, name):
        self.name = name
        self.hp = hp
        self.stats = Stats(0, 0)
        
     
#     def __init__(self, name,):
#             self.name = name
#             self.stats = Stats(0, 0, 0)
    def attack1(self, damage):
        self.damage = damage

    # def set(self, hp, dmgmult, critchance):
    #     self.hp = hp
    #     self.dmgmult = dmgmult
    #     self.critchance = critchance

    def attack(self, other):
        print(f'{self.name} does attack 1 at {other.name}')
        Character.attack1.damage = 10 * (self.stats[0])
        print(f'{other.name} takes {Character.attack1.damage} Damage')
        

    # def battle(self, other):
         
    #     print(f'dealing {Character.attack.damage} damage')

    
            
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
    # Def Basic Attack 1 - Basic Attack
    # print ("adventurer attacked the troll")

    # Def Attack 2 - Damage Over time (if applicable) 
    # print ("adventurer applied DoT to the troll")

    # Def Buff (potion of strength)
    # Print('Adventurer Drank potion of strength)
    # Print('Your attacks hit harder for two turns)

    # Def Healing Potion
    # Print('Adventurer Drank potion of healing, revitalising them))

