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

class Weapon:
    def __init__(self, name, attackboost):
        self.name = name
        self.attackboost = attackboost

class Dungeon:
    def __init__(self, name, creward, dreward, eamount):
        self.name = name
        self.creward = creward
        self.dreward = dreward
        self.eamount = eamount
    def DungeonClear(name, creward, dreward):
        print(f"Congratulations, you have cleared the {self.name}.")
        print(f"{J.name} has received {self.creward} dollars, and a {self.dreward}!")
        J.money += self.creward
        print(f"{J.name} now has {J.money}")

    def DungeonEnter(name, creward, dreward, enemy):
        print(f"You have entered {self.name}, this dungeon drops {self.creward} dollars, and a {self.dreward}!")
        dstart = input("Would you like to begin the dungeon?").lower()
        if dstart == "yes":
            enemy = Enemy("Goblin", 50, 10, 20, ['Goblin Spear', 'Goblin Ear', 'Goblin Eye', "Broken Wooden Handle"])



GCave = Dungeon("Goblin Cave", 100, "Goblin Helmet", 1)


GCave.DungeonEnter()
print(enemy)