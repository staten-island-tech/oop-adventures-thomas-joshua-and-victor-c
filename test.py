import random
import art#fixed the art prob. All goodie, just had to stop defining it, let it be. 
import moneygrab
PotionDuration = 0
RoundDuration = 0
class Player:
    def __init__(self, name, HP, attack, money, inventory,playerovertime, potionduration):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.money = money
        self.inventory = inventory
        self.playerovertime = playerovertime
        self.potionduration = potionduration
 #for the constant do under map selcet
    def PotionDrink(self,HP):#do inventory here
        WhichPotion = random.randint(1,4)
        if WhichPotion == 1:
            self.HP +=50
            print(f"{self.name} drunk a bottle of Combat Stim and will now  receive 50 HP ")
        elif WhichPotion == 2:
            self.playerovertime += 2
            print("You drank a suspicious potion and it turned out to be the Ichor of the Gods.It flows through you and you will now receive health slowly for the duration of the battle.")
        elif WhichPotion == 3:
            self.playerovertime -= 4
            print("You drank a suspicious potion and it turned out to be the Tunnel Asp Venom. It is in your system and will eventually kill you. ")    
        elif WhichPotion == 4:
            self.potionduration += 4
            if self.potionduration > 0:
                self.attack = self.attack*0.5
            print("You drank a weakness potion and your attack is halved.This effect lasts for four turns. ")
           
    def PlayerPunch(self, enemy):
        damage = (self.attack + self.attack - 30)
        enemy.HP -= damage
        J.HP += self.playerovertime
        if self.playerovertime < 0:
            print(f"{self.name} lost {self.playerovertime} from Poisoning!")
        elif self.playerovertime > 0:
            print(f"{self.name} gained {self.playerovertime} from their regeneration potion!")
        else:
            print(" ")
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        print(art.Ppunch)
















    def PlayerKick(self, enemy):
        damage = (self.attack * 2.5)
        J.HP += self.playerovertime
        if self.playerovertime < 0:
            print(f"{self.name} lost {self.playerovertime} from Poisoning!")
        elif self.playerovertime > 0:
            print(f"{self.name} gained {self.playerovertime} from their regeneration potion!")
        else:
            print(" ")
        kickchance = random.randint(1,10)
        if kickchance >= 8:
            enemy.HP -= damage
            print(f"{self.name} kicks {enemy.name} for {damage} damage!")
            print(art.Pkick)
        elif kickchance < 8:
            enemy.HP -= 0
            print(art.PMisskick)
            print(f"{self.name} missed the kick!")




    def PGuard(self):
        print(f"{self.name} is guarding!")
        self.HP += damage
       


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
        print(art.PreGstrike)
        print(art.Gstrike)
        if player.HP <= 0:
            print(f"{player.name} has been defeated!")
            print(art.PdeathG)
            print(art.HeartD)
    def EGuard(self):
        print(f"{self.name} is guarding!")


    def EnemyCDrop(self):
        return self.cdrop


class Stage1:
    def __init__(self, name, HP, attack, cdrop, itemdrop):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.cdrop = cdrop
        self.itemdrop = itemdrop
class Stage2(Stage1):
    def __init__(self, name, HP, attack, cdrop, itemdrop, defense ):
        super().__init__(HP, attack, cdrop, itemdrop)
        self.defense = defense
        self.name = name
class Weapon:
    def __init__(self, name, attackboost):
        self.name = name
        self.attackboost = attackboost



from moneygrab import Collector

merchant = Collector(700, 0, 1000, [
    "Reversed Cursed Technique in a Nutshell",
    "A Black Flash in a Bottle",
    "The Eye of Agamoto",
    "Armed And Dangerous + Again⁶",
    "Armed And Dangerous + Again³",
    "Armed And Dangerous + Again¹³",
])


print("\nYou meet a strange Collector. He offers to trade!")
while True:
    action = input("\nWhat would you like to do? (1: Buy, 2: Sell, 3: Leave) ").lower()
    if action in ["1", "buy"]:
        merchant.sell_item(J)  
    elif action in ["2", "sell"]:
        merchant.buy_item(J)
    elif action in ["3", "leave"]:
        print("\nYou left the Collector.")
        break
    else:
        print("\nInvalid choice.")

class Dungeon:
    def __init__(self, name, creward, dreward,eamount):
        self.name = name
        self.creward = creward
        self.dreward = dreward
        self.eamount = eamount
    def DungeonClear(name, creward, dreward):
        print(f"Congratulations, you have cleared the {self.name}.")
        print(f"{J.name} has received {self.creward} dollars, and a {self.dreward}!")
        J.money += self.creward
        print(f"{J.name} now has {J.money}")








    def DungeonEnter(self, player):
        print(f"You have entered {self.name}, this dungeon drops {self.creward} dollars, and a {self.dreward}!")
        dstart = input("Would you like to begin the dungeon? ").lower()
        if dstart in ["yes", "y", "1"]:
            for i in range(self.eamount):
                enemy = Enemy("Goblin", 50, 10, 20, ['Goblin Spear', 'Goblin Ear', 'Goblin Eye', "Broken Wooden Handle"])
            self.DungeonClear(J, self.dreward)




"""
class Merchant:
    def __init__(self, money, gadget):
        self.money = money
        self.gadget = gadget
    def PlayerSell(self, money, player, gadget): """
















Weapon = Weapon("Goblin Spear", 20 )
GCave = Dungeon("Goblin Cave", 100, "Goblin Helmet",5)
J = Player("MCHammer", 100, 10, 0, [], 0, 0)
J.attack = J.attack + Weapon.attackboost


from moneygrab import Collector

merchant = Collector(700, 0, 1000, [
    "Reversed Cursed Technique in a Nutshell",
    "A Black Flash in a Bottle",
    "The Eye of Agamoto",
    "Armed And Dangerous + Again⁶",
    "Armed And Dangerous + Again³",
    "Armed And Dangerous + Again¹³",
])


print("\nYou meet a strange Collector. He offers to trade!")
while True:
    action = input("\nWhat would you like to do? (1: Buy, 2: Sell, 3: Leave) ").lower()
    if action in ["1", "buy"]:
        merchant.sell_item(J)  
    elif action in ["2", "sell"]:
        merchant.buy_item(J)
    elif action in ["3", "leave"]:
        print("\nYou left the Collector.")
        break
    else:
        print("\nInvalid choice.")



start = input("Would you like to begin? ").lower()
if start in ("yes", "y", "1"):
    J.name = input("What would you like your name to be? ")
    mapselect = input("Where would you like to go? ").lower()
   
    if mapselect in ("goblin cave", "1"):
        GCave.DungeonEnter(Enemy)
        if enemy.HP == 0:
            GCave.DungeonClear






    if mapselect in ("graveyard", "2"):
        enemy = Enemy("Zombie", 100, 15, 50, ["Zombie Hand", "Zombie Brain", "Rotten Essence"])




    while J.HP > 0 and enemy.HP > 0:
        SelectionScreen = rf"""
               {enemy.name}                           = Attack / 1 =                               {J.name}                     Potion Duration:
               HP: {enemy.HP}            = Potion / 2 =              = Gadget / 3 =                HP: {J.HP}                  {J.potionduration}
               Attack: {enemy.attack}                      = Flee / 4 =                            Attack: {J.attack}
        """
        PotionDuration -= 1
        RoundDuration += 1




        print(art.SelectionScreen)
        control = input("Your move: ").lower()
        if control in ["punch", "1", "p"]:
                J.PlayerPunch(enemy)    
        elif control in ["potion","pot","2"]:








            potioncontrol = input("Would you like to consume a suspicious potion?").lower()
            if potioncontrol in ["potion","pot","2", "yes", "y"]:
                J.PotionDrink(J)
        elif control in ["gaurd","g","5"]:
                J.PGaurd(J)
        elif control in ["kick", "k", "3"]:
                J.PlayerKick(enemy)
       








        elif control == "flee":
            break  




        else:
            print("Invalid move! Please enter punch or guard.")
   








        if enemy.HP <= 0:
            continue
       
       
        EnemySelect = enemy.EnemyAI()






        if EnemySelect == 1:  
            enemy.EnemyPunch(J)    
        if J.HP <= 0:
            break
       
    if J.HP > 0:
        print(f"{enemy.name} has been defeated!")
        print(art.Gdeath)
        print(f"{J.name} wins the battle!")
        cash_gain = enemy.EnemyCDrop()
        J.money += cash_gain
        print(f"{J.name} now has {J.money} (+{cash_gain}) dollars!")
    else:
        print(f"{enemy.name} wins the battle!")


