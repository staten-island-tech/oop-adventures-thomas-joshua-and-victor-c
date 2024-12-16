import random

class Player:
    def __init__(self, name, HP, attack, money):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.money = money

    def PlayerPunch(self, enemy):
        damage = random.randint(1, self.attack) 
        enemy.HP -= damage  
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        if enemy.HP <= 0:
            print(f"{enemy.name} has been defeated!")

    def PGuard(self):
        print(f"{self.name} is guarding!")

class Enemy:
    def __init__(self, name, HP, attack, drop):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.drop = drop

    def EnemyAI(self):
        return random.randint(1, 1)

    def EnemyPunch(self, player): 
        damage = random.randint(1, self.attack)  
        player.HP -= damage 
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        if player.HP <= 0:
            print(f"{player.name} has been defeated!")
    def EGuard(self):
        print(f"{self.name} is guarding!")

    def EnemyDrop(self):
        return self.drop

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
Ppunch = r"""
                                                           O    <O> /
                                                          /|--- /|\/
                                                          / \   / X
"""
Pkick = r"""
                                                          O __  <O> /
                                                          |\___ /|\/
                                                           |    / X
"""
PPshieldGstrike = r"""
                                             
                                                        O  \   <-<O>.--
                                                       /|\[|     /|'
                                                       / \ /     / \
                                           
"""
SelectionScreen = r"""
                                                          = Attack = 
                                                 = Potion =          = Gadget = 
                                                           = Flee =
"""

PlayerGuard = False
PlayerAttack = False
EnemyGuard = False

start = input("Would you like to begin? ").lower()

if start == "yes":
    J = Player("MCHammer", 100, 10, 0)
    enemy = Enemy("Goblin", 50, 10, 20)
    print(f'You have encountered {enemy.name}')
    print(Standing)

while J.HP > 0 and enemy.HP > 0:
    print(SelectionScreen)
    control = input("Move? (punch/guard): ").lower()

    # Player's turn
    if control in ["punch", "p", "1"]:
        print(Ppunch)
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
            print(Gstrike)
            enemy.EnemyPunch(J)  # Enemy punches if player is not guarding
    if J.HP <= 0:
        break

if J.HP > 0:
    print(f"{J.name} wins the battle!")
    cash_gain = enemy.EnemyDrop()
    J.money += cash_gain
    print(f"{J.name} now has {J.money} (+{cash_gain}) dollars!")
else:
    print(f"{enemy.name} wins the battle!")


