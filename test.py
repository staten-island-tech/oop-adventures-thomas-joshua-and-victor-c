# import random
# import sys
# # Assign the stickman art to a varia


# class Player:
#     def __init__(self, name, HP, attack, money, inventory):
#         self.name = name
#         self.HP = HP
#         self.attack = attack
#         self.money = money
#         self.inventory = inventory


#     def PlayerPunch(self, enemy):
#         damage = random.randint(1, self.attack)
#         enemy.HP -= damage  
#         print(f"{self.name} attacks {enemy.name} for {damage} damage!")
#         print(Ppunch)
#         if enemy.HP <= 0:
#             print(f"{enemy.name} has been defeated!")
#             print(Gdeath)
#     def PlayerKick(self, enemy):
#         damage = random.randint(1,self.attack + self.attack*0.5)
#         if damage <=self.attack*1.3:
#             enemy.HP -= 0
#         elif damage > self.attack*1.3:
#             enemy.HP -= damage


#     def PGuard(self):
#         print(f"{self.name} is guarding!")
# """ 

#     def PGadget(self, inventory):


#     def PFlee(self):


#     def PPotion(self, inventory):
#         """


# class Enemy:
#     def __init__(self, name, HP, attack, drop):
#         self.name = name
#         self.HP = HP
#         self.attack = attack
#         self.drop = drop


#     def EnemyAI(self):
#         return random.randint(1, 1)


#     def EnemyPunch(self, player):
#         damage = random.randint(1, self.attack)  
#         player.HP -= damage
#         print(f"{self.name} attacks {player.name} for {damage} damage!")
#         print(PreGstrike)
#         print(Gstrike)
#         print(PreGstrike)
#         if player.HP <= 0:
#             print(f"{player.name} has been defeated!")
#             print(PdeathG)
#     def EGuard(self):
#         print(f"{self.name} is guarding!")


#     def EnemyCDrop(self):
#         return self.drop

# """ 
# class Merchant:
#     def __init__(self, money, gadget):
#         self.money = money
#         self.gadget = gadget
#     def PlayerSell(self, money, player, gadget): """


# SelectionScreen = r"""
#                                                           = Attack =
#                                                  = Potion =          = Gadget =
#                                                            = Flee =
# """

# HeartD = r"""
#                                                                                         ¶¶
#                                                                                     ¶1¶1111111¶       
#                                                              ¶¶111¶               ¶¶¶¶111111111¶¶¶1
#                                                           ¶1¶¶¶¶¶111111¶       ¶¶¶1¶¶¶11111111¶1¶¶
#                                                        ¶¶¶1¶1111111111¶¶1    ¶¶1¶¶¶1111111111111¶¶¶
#                                                        ¶¶1¶¶1111111111111¶¶  ¶¶¶1¶¶¶¶1111111111111¶
#                                                        ¶¶_¶1111111111111111¶¶ ¶¶¶¶¶¶11¶111111111111¶
#                                                        11_¶11111111111111111¶¶   ¶¶¶¶  ¶111111111111¶¶
#                                                        ¶¶¶¶1111111111111111¶¶¶¶  1¶¶  11111111111111¶¶
#                                                        ¶¶¶¶11111111111¶¶¶¶¶¶¶  1¶1¶¶11111111111111¶1
#                                                        ¶¶1¶1111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111111¶¶
#                                                        ¶¶11111111111111111111111¶¶  ¶¶¶¶¶¶1111111111¶¶¶
#                                                         1¶111111111111111111¶¶¶¶¶¶  ¶¶¶¶11111111111¶1
#                                                          ¶¶11111111111111111¶¶¶  ¶¶¶1111111111111¶1
#                                                           ¶¶¶111111111111¶1¶¶¶  1¶¶111¶1111111¶11¶1
#                                                            1¶¶¶11111111111¶¶¶¶111¶¶¶111111111¶11¶¶¶
#                                                             ¶¶¶¶1111111111111¶¶¶¶1¶¶¶¶¶¶¶¶11¶11¶¶
#                                                              ¶¶¶¶¶11111111111¶111¶  ¶¶¶111¶1¶¶¶
#                                                               ¶¶¶¶¶¶111111111111¶  ¶¶¶111¶¶¶1
#                                                                 1¶¶¶¶¶11111111¶¶  ¶¶¶¶111¶¶
#                                                                  ¶¶¶¶¶¶¶1111111  ¶¶¶11¶¶1
#                                                                    1¶¶¶¶¶¶1111¶¶¶1¶¶¶¶
#                                                                       ¶¶¶¶¶1¶¶¶¶¶1¶
#                                                                          ¶1¶¶¶1¶¶¶
#                                                                            11¶

# """
# PdeathG = r"""
#                                                         _________
#                                                           \<O>/  
#                                                             |
#                                                 ‗/‾‾|o     / \
# """
# Gdeath = r"""
#                                                         \O/     
#                                                          |    <O>__
#                                                         / \     |  L
# """
# Standing = r"""
#                                             O                                 <O> /
#                                            /|\                                /|\/
#                                            / \                                / X
# """
# Standingclose = r"""
#                                                     O                   <O> /
#                                                    /|\                  /|\/
#                                                    / \                  / X
# """
# Standingclose2 = r"""
#                                                            O    <O> /
#                                                           /|\   /|\/
#                                                           / \   / X
# """
# PreGstrike = r"""
#                                                            O  <-<O>.-- 
#                                                           /|\   /|'
#                                                           / \   / \
# """
# Gstrike = r"""
#                                                            O<---<O>.- 
#                                                           /|\  --|'
#                                                           / \   / \
# """
# Ppunch = r"""
#                                                            O    <O> /
#                                                           /|--- /|\/
#                                                           / \   / X
# """
# Pkick = r"""
#                                                           O __  <O> /
#                                                           |\___ /|\/
#                                                            |    / X
# """
# PPshieldGstrike = r"""
                                              
#                                                         O  \   <-<O>.--
#                                                        /|\[|     /|'
#                                                        / \ /     / \
                                           
# """


# PlayerGuard = False
# PlayerAttack = False
# EnemyGuard = False


# start = input("Would you like to begin? ").lower()


# if start == "yes":
#     J = Player("MCHammer", 100, 10, 0, [])
#     enemy = Enemy("Goblin", 50, 10, 20)
#     print(f'You have encountered {enemy.name}')
#     print(Standing)
# else:
#     print(" ......ok. Tell me when I guess. Why would You even play this game or start it if u dont want to play. I only understand yes bc of my primitive language")
    

# while J.HP > 0 and enemy.HP > 0:
#     print(SelectionScreen)
#     control = input("Move? (punch/guard): ").lower()


#     # Player's turn
#     if control in ["punch", "p", "1"]:
#         J.PlayerPunch(enemy)
#         PlayerGuard = False
#     if control in ["kick","k","2"]:
#         J.PlayerKick(enemy)
        
#     else:
#         print("Invalid move! Please enter punch or guard.")


#     if enemy.HP <= 0:
#         break


#     # Enemy's turn (based on AI)
#     EnemySelect = enemy.EnemyAI()


#     if EnemySelect == 1:  # Enemy chooses to punch
#         if PlayerGuard:
#             print(f"{J.name}'s guard blocked {enemy.name}'s attack!")
#         else:
#             enemy.EnemyPunch(J)  # Enemy punches if player is not guarding
#     if J.HP <= 0:
#         break


# if J.HP > 0:
#     print(f"{J.name} wins the battle!")
#     cash_gain = enemy.EnemyCDrop()
#     J.money += cash_gain
#     print(f"{J.name} now has {J.money} (+{cash_gain}) dollars!")
# else:
#     print(f"{enemy.name} wins the battle!")

import random


class Player:
    def __init__(self, name, HP, attack, money, inventory):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.money = money
        self.inventory = inventory


    def PlayerPunch(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.HP -= damage  
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        print(Ppunch)
        if enemy.HP <= 0:
            print(f"{enemy.name} has been defeated!")
            print(Gdeath)


    def PGuard(self):
        print(f"{self.name} is guarding!")


"""
    def PGadget(self, inventory):
       
    def PFlee(self):
       
    def PPotion(self, inventory): """
       


class Enemy:
    def __init__(self, name, HP, attack, cdrop, itemdrop):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.cdrop = cdrop
        self.itemdrop = itemdrop


    def EnemyAI(self):
        return random.randint(1, 1)


    def EnemyPunch(self, player):
        damage = random.randint(1, self.attack)  
        player.HP -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        print(PreGstrike)
        print(Gstrike)
        if player.HP <= 0:
            print(f"{player.name} has been defeated!")
            print(PdeathG)
            print(HeartD)
    def EGuard(self):
        print(f"{self.name} is guarding!")


    def EnemyCDrop(self):
        return self.cdrop
"""
class Merchant:
    def __init__(self, money, gadget):
        self.money = money
        self.gadget = gadget
    def PlayerSell(self, money, player, gadget): """






Standing = r"""
                                            O                                 <O> /
                                           /|\                                /|\/
                                           / \                                / X
"""
Standingclose = r"""
                                                    O                   <O> /
                                                   /|\                  /|\/
                                                   / \                  / X
"""
Standingclose2 = r"""
                                                           O    <O> /
                                                          /|\   /|\/
                                                          / \   / X
"""
PreGstrike = r"""
                                                           O  <-<O>.--
                                                          /|\   /|'
                                                          / \   / \
"""
Gstrike = r"""
                                                           O<---<O>.-
                                                          /|\  --|'
                                                          / \   / \
"""

PrePpunch = r"""
                                                           O/‾  <O> /
                                                          /|    /|\/
                                                          / \   / X 
"""
PrePkick = r"""
                                                          O __  <O> /
                                                          |\/\  /|\/
                                                           |    / X
"""



Ppunch = r"""        
                                                           O    <O> /
                                                          /|--- /|\/
                                                          / \   / X """
Pkick = r"""
                                                          O __  <O> /
                                                          |\___ /|\/
                                                           |    / X
"""
PMisskick = r"""
                                                          O __  <O> /
                                                          |\___--|\/
                                                           |    / X

                                                        O___/‾‾\<O> /
                                                       /|   |    |\/
                                                                / X       
        
                                                      .   _    \<O> /
                                                     O⊥__/       |\/
                                                                / X 

                                                               __<O> /
                                                                  |\/
                                                    ‗‗O___/\     / X

                                                          O     <O> /
                                                         /\_    /|\/
                                                       _」‾‾|   / X

"""                   
PPshieldGstrike = r"""                                  O  \   <-<O>.--
                                                       /|\[|     /|'
                                                       / \ /     / \                                    
"""
SelectionScreen = r"""
                                                          = Attack / 1 =
                                            = Potion / 2 =              = Gadget / 3 =
                                                           = Flee / 4 =
"""
Gdeath = r"""
                                                        \O/    
                                                         |    <O>__
                                                        / \      | L
"""


HeartD = r"""                                                                            ¶¶
                                                                                    ¶1¶1111111¶      
                                                             ¶¶111¶               ¶¶¶¶111111111¶¶¶1
                                                          ¶1¶¶¶¶¶111111¶       ¶¶¶1¶¶¶11111111¶1¶¶
                                                       ¶¶¶1¶1111111111¶¶1    ¶¶1¶¶¶1111111111111¶¶¶
                                                       ¶¶1¶¶1111111111111¶¶  ¶¶¶1¶¶¶¶1111111111111¶
                                                       ¶¶_¶1111111111111111¶¶ ¶¶¶¶¶¶11¶111111111111¶
                                                       11_¶11111111111111111¶¶   ¶¶¶¶  ¶111111111111¶¶
                                                       ¶¶¶¶1111111111111111¶¶¶¶  1¶¶  11111111111111¶¶
                                                       ¶¶¶¶11111111111¶¶¶¶¶¶¶  1¶1¶¶11111111111111¶1
                                                       ¶¶1¶1111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111111¶¶
                                                       ¶¶11111111111111111111111¶¶  ¶¶¶¶¶¶1111111111¶¶¶
                                                        1¶111111111111111111¶¶¶¶¶¶  ¶¶¶¶11111111111¶1
                                                         ¶¶11111111111111111¶¶¶  ¶¶¶1111111111111¶1
                                                          ¶¶¶111111111111¶1¶¶¶  1¶¶111¶1111111¶11¶1
                                                           1¶¶¶11111111111¶¶¶¶111¶¶¶111111111¶11¶¶¶
                                                            ¶¶¶¶1111111111111¶¶¶¶1¶¶¶¶¶¶¶¶11¶11¶¶
                                                             ¶¶¶¶¶11111111111¶111¶  ¶¶¶111¶1¶¶¶
                                                              ¶¶¶¶¶¶111111111111¶  ¶¶¶111¶¶¶1
                                                                1¶¶¶¶¶11111111¶¶  ¶¶¶¶111¶¶
                                                                 ¶¶¶¶¶¶¶1111111  ¶¶¶11¶¶1
                                                                   1¶¶¶¶¶¶1111¶¶¶1¶¶¶¶
                                                                      ¶¶¶¶¶1¶¶¶¶¶1¶
                                                                         ¶1¶¶¶1¶¶¶
                                                                           11¶






"""
PdeathG = r"""
                                                        _________
                                                          \<O>/  
                                                            |
                                                ‗/‾‾|o     / \
"""




PlayerGuard = False
PlayerAttack = False
EnemyGuard = False
J = Player("MCHammer", 100, 10, 0, [])


start = input("Would you like to begin? ").lower()
if start in ("yes", "y", "1"):
    mapselect = input("Where would you like to go? ").lower()


    if mapselect in ("goblin cave", "1"):
        enemy = Enemy("Goblin", 50, 10, 20, ['Goblin Spear', 'Goblin Ear', 'Goblin Eye', "Broken Wooden Handle"])
        print(f'You have encountered {enemy.name}')
        print(Standing)




    if mapselect in ("graveyard", "2"):
        enemy = Enemy("Zombie", 100, 15, 50, ["Zombie Hand", "Zombie Brain", "Rotten Essence"])


while J.HP > 0 and enemy.HP > 0:
    print(SelectionScreen)
    control = input("Move? (punch/guard): ").lower()


    # Player's turn
    if control in ["punch", "p", "1"]:
        J.PlayerPunch(enemy)
        PlayerGuard = False
    else:
        print("Invalid move! Please enter punch or guard.")


    if enemy.HP <= 0:
        break
   
    # Enemy's turn (based on AI)
    EnemySelect = enemy.EnemyAI()


    if EnemySelect == 1:  # Enemy chooses to punch
        if PlayerGuard:
            print(f"{J.name}'s guard blocked {enemy.name}'s attack!")
        else:
            enemy.EnemyPunch(J)  # Enemy punches if player is not guarding
    if J.HP <= 0:
        break
   
if J.HP > 0:
    print(f"{J.name} wins the battle!")
    cash_gain = enemy.EnemyCDrop()
    J.money += cash_gain
    print(f"{J.name} now has {J.money} (+{cash_gain}) dollars!")
else:
    print(f"{enemy.name} wins the battle!")




