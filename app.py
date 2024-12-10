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

    def Guard(self):
        print(f"{self.name} is guarding!")
        Guard = True

class Enemy:
    def __init__(self, name, HP, attack):
        self.name = name
        self.HP = HP
        self.attack = attack

    def EnemyPunch(self, player): 
        damage = random.randint(1, self.attack)  
        player.HP -= damage 
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        if player.HP <= 0:
            print(f"{player.name} has been defeated!")

# Example setup: Player vs Enemy
J = Player("MCHammer", 100, 10)
enemy = Enemy("Bub", 100, 10)
# Simple battle loop
while J.HP > 0 and enemy.HP > 0:
    control = input("Move? ")
    # Player attacks first
    if control == "punch":
        J.PlayerPunch(enemy)
    elif control == "guard":
        J.Guard()
        Guard = True
    if enemy.HP <= 0:
        break  

    # Enemy attacks
    if not Guard:
        enemy.EnemyPunch(J)
    if J.HP <= 0:
        break  


if J.HP > 0:
    print(f"{J.name} wins the battle!")
else:
    print(f"{enemy.name} wins the battle!")




