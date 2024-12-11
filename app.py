import random

class Player:
    def __init__(self, name, HP, attack):
        self.name = name
        self.HP = HP
        self.attack = attack

    def PlayerPunch(self, enemy):
        damage = random.randint(1, self.attack) 
        enemy.HP -= damage  
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        if enemy.HP <= 0:
            print(f"{enemy.name} has been defeated!")

    def PGuard(self):
        print(f"{self.name} is guarding!")

class Enemy:
    def __init__(self, name, HP, attack):
        self.name = name
        self.HP = HP
        self.attack = attack

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
# Example setup: Player vs Enemy
J = Player("MCHammer", 100, 10)
enemy = Enemy("Bub", 50, 10)

PlayerGuard = False
EnemyGuard = False

while J.HP > 0 and enemy.HP > 0:
    control = input("Move? ").lower()
    enemy.EnemyAI()
    # Player attacks first
    if control == "punch":
        J.PlayerPunch(enemy)
        PlayerGuard = False
    elif control == "guard":
        J.PGuard()
        PlayerGuard = True
        print(f"{enemy.name} could not attack!")
    if enemy.HP <= 0:
        break
    EnemySelect = enemy.EnemyAI()
    if PlayerGuard == False:
        if EnemySelect == 1:
            enemy.EnemyPunch(J)
    if EnemySelect == 2:
        enemy.EGuard()
        EnemyGuard = True
        print(f"{J.name} could not attack!")  
    if J.HP <= 0:
        break  

if J.HP > 0:
    print(f"{J.name} wins the battle!")
else:
    print(f"{enemy.name} wins the battle!")


