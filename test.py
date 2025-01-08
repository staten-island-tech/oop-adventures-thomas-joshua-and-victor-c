class Dungeon:
    def __init__(self, name, creward, dreward, eamount):
        self.name = name
        self.creward = creward
        self.dreward = dreward
        self.eamount = eamount

    def DungeonClear(self, player):
        print(f"Congratulations, you have cleared the {self.name}.")
        print(f"{player.name} has received {self.creward} dollars, and a {self.dreward}!")
        player.money += self.creward
        print(f"{player.name} now has {player.money}")

    def DungeonEnter(self, player):
        print(f"You have entered {self.name}, this dungeon drops {self.creward} dollars, and a {self.dreward}!")
        dstart = input("Would you like to begin the dungeon?").lower()
        if dstart == "yes":
            for i in range(self.eamount):
                enemy = Enemy("Goblin", 50, 10, 20, ['Goblin Spear', 'Goblin Ear', 'Goblin Eye', "Broken Wooden Handle"])
                print(f"A wild {enemy.name} appeared!")
                while enemy.HP > 0 and player.HP > 0:
                    action = input("What will you do? (Punch/Kick/Potion/Guard) ").lower()
            self.DungeonClear(J)



Weapon = Weapon("Goblin Spear", 20 )
GCave = Dungeon("Goblin Cave", 100, "Goblin Helmet", 5)
J = Player("MCHammer", 100, 10, 0, [], 0, 0)
J.attack = J.attack + Weapon.attackboost


start = input("Would you like to begin? ").lower()
if start in ("yes", "y", "1"):
    J.name = input("What would you like your name to be? ")
    mapselect = input("Where would you like to go? ").lower()  
    if mapselect in ("goblin cave", "1"):
        GCave.DungeonEnter(J)