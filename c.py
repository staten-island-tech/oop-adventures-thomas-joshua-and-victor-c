import random

class Player:
    def __init__(self, name, HP, attack, money):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.money = money
        self.dodge_turn = random.randint(1, 5)  # Determine when dodge activates
        self.turn_count = 0  # Track the number of turns

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


# Initialize Player and Enemy
J = Player("MCHammer", 100, 10, 0)
enemy = Enemy("Goblin", 50, 10, 20)

PlayerGuard = False
EnemyGuard = False

while J.HP > 0 and enemy.HP > 0:
    # Player's turn
    control = input("Move? (punch/guard): ").lower()

    if control in ["punch", "p", "1"]:
        J.PlayerPunch(enemy)
        PlayerGuard = False
    else:
        print("Invalid move! Please enter punch or guard.")

    if enemy.HP <= 0:
        break

    # Increment the player's turn count
    J.turn_count += 1

    # Enemy's turn
    EnemySelect = enemy.EnemyAI()

    if EnemySelect == 1:  # Enemy chooses to punch
        if J.turn_count == J.dodge_turn:  # Check if it's the dodge turn
            print(f"{J.name} dodges {enemy.name}'s attack!")
            J.dodge_turn += random.randint(1, 5)  # Reset dodge turn
        elif PlayerGuard:
            print(f"{J.name}'s guard blocked {enemy.name}'s attack!")
        else:
            enemy.EnemyPunch(J)

    if J.HP <= 0:
        break

# Outcome of the battle
if J.HP > 0:
    print(f"{J.name} wins the battle!")
    cash_gain = enemy.EnemyDrop()
    J.money += cash_gain
    print(f"{J.name} now has {J.money} (+{cash_gain}) dollars!")
else:
    print(f"{enemy.name} wins the battle!")
