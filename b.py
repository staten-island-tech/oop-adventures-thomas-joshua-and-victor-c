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
        # 30% chance to dodge
        return random.randint(1, 5) == 1  # 1 in 5 chance to dodge


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

PlayerGuard = False
turns = 0  # Track turns

# Main battle loop
while J.HP > 0 and enemy.HP > 0:
    turns += 1  # Increment turn counter
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
        continue  # Retry input

    if enemy.HP <= 0:
        break

    # Enemy's turn
    EnemySelect = enemy.EnemyAI()
    if EnemySelect == 1:  # Enemy chooses to punch
        if PlayerGuard:
            print(f"{J.name}'s guard blocked {enemy.name}'s attack!")
        else:
            # Check for dodge chance
            if J.DodgeChance():
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
