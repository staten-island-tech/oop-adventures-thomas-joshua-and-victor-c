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

    def DodgeChance(self):
        dodge = random.randint(1, 10)
        return dodge <= 3

class Enemy:
    def __init__(self, name, HP, attack, drop):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.drop = drop

    def EnemyAI(self):
        return random.randint(1, 2)

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

J = Player("MCHammer", 100, 10, 0)
enemy = Enemy("Goblin", 50, 10, 20)

PlayerGuard = False
EnemyGuard = False

turns = 0
consecutive_guards = 0 

while J.HP > 0 and enemy.HP > 0:
    print(f"\n--- Turn {turns + 1} ---")
    control = input("Move? (punch/guard): ").lower()

    if control in ["punch", "p", "1"]:
        J.PlayerPunch(enemy)
        PlayerGuard = False
        consecutive_guards = 0  
        turns += 1  
    elif control in ["guard", "g", "2"]:
        J.PGuard()
        PlayerGuard = True
        consecutive_guards += 1 
        turns += 1 

        if consecutive_guards >= 3:
            damage_player = random.randint(5, 10)  
            J.HP -= damage_player
            print(f"{J.name} guarded for too long and loses {damage_player} HP!")
            consecutive_guards = 0  # Reset guard counter
    else:
        print("Invalid move! Please enter punch or guard.")
        continue  # Retry the input without incrementing the turn

    if enemy.HP <= 0:
        break

    # Enemy's turn (based on AI)
    EnemySelect = enemy.EnemyAI()

    if EnemySelect == 1:
        if PlayerGuard:
            print(f"{J.name}'s guard blocked {enemy.name}'s attack!")
        else:
            if random.randint(1, 5) == 3 and J.DodgeChance():
                print(f"{J.name} dodged {enemy.name}'s attack!")
            else:
                enemy.EnemyPunch(J)
    else:
        enemy.EGuard()

    if J.HP <= 0:
        break

# Battle result
if J.HP > 0:
    print(f"{J.name} wins the battle!")
    cash_gain = enemy.EnemyDrop()
    J.money += cash_gain
    print(f"{J.name} now has {J.money} (+{cash_gain}) dollars!")
else:
    print(f"{enemy.name} wins the battle!")

""" print()

def PlayerPunch(self, enemy):
    damage = random.randint(1, self.attack)
    enemy.HP -= damage
    print(f"{self.name} attacks {enemy.name} for {damage} damage!")
    print()  # Add a blank line after the attack message
    if enemy.HP <= 0:
        print(f"{enemy.name} has been defeated!")
        print()  # Add a blank line after the defeat message
 """