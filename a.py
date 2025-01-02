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


# Initialize player and enemy
J = Player("MCHammer", 100, 10, 0)
enemy = Enemy("Goblin", 50, 10, 20)

# Flags for guarding and other states
PlayerGuard = False
EnemyGuard = False

# Track turns
turns = 0

# Main battle loop
while J.HP > 0 and enemy.HP > 0:
    turns += 1  # Increment turn count
    print(f"\n--- Turn {turns} ---")
    control = input("Move? (punch/guard): ").lower()

    # Player's turn
    if control in ["punch", "p", "1"]:
        J.PlayerPunch(enemy)
        PlayerGuard = False
    elif control in ["guard", "g", "2"]:
        J.PGuard()
        PlayerGuard = True
    else:
        print("Invalid move! Please enter punch or guard.")
        continue  # Retry the input

    if enemy.HP <= 0:
        break

    # Enemy's turn (based on AI)
    EnemySelect = enemy.EnemyAI()

if EnemySelect == 1: 
    if PlayerGuard:
        print(f"{J.name}'s guard blocked {enemy.name}'s attack!")
    else:
        if turns % random.randint(3, 5) == 0 and J.DodgeChance():
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