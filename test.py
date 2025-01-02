import random
class Player:
    def __init__(self, name, HP, minattack, maxattack, money, inventory):
        self.name = name
        self.HP = HP
        self.minattack = minattack
        self.maxattack = maxattack
        self.money = money
        self.inventory = inventory
 #for the constant do under map selcet 
    def PotionDrink(self,HP,inventory,maxattack):
        WhichPotion = random.randint(1,4)
        if WhichPotion = 1:
            self.HP +=50
            print(f"{self.name} attacks {enemy.name} for {damage} damage!"}")
        elif WhichPotion = 2:
            self.HP 


    def PlayerPunch(self, enemy):
        damage = random.randint(self.minattack, self.maxattack)
        enemy.HP -= damage  
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        print(Ppunch)


    def PlayerKick(self, enemy):
        damage = (self.maxattack + self.minattack * 2.5)
        kickchance = random.randint(1,10)
        if kickchance >= 8:
            enemy.HP -= damage
            print(f"{self.name} kicks {enemy.name} for {damage} damage!")
            print(Pkick)
        elif kickchance < 8:
            enemy.HP -= 0
            print(PMisskick)
            print(f"{self.name} missed the kick!")

    


    def PGuard(self):
        print(f"{self.name} is guarding!")


"""
    def PGadget(self, inventory):
       
    def PFlee(self):
       
    def PPotion(self, inventory): """
       


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
    def __init__(self, name, minattackboost, maxattackboost):
        self.name = name
        self.minattackboost = minattackboost
        self.maxattackboost = maxattackboost
"""
class Merchant:
    def __init__(self, money, gadget):
        self.money = money
        self.gadget = gadget
    def PlayerSell(self, money, player, gadget): """






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
                                                          / \   / X """
Pkick = r"""
                                                          O __  <O> /
                                                          |\___ /|\/
                                                           |    / X
"""
                   
PPshieldGstrike = r"""                                  O  \   <-<O>.--
                                                       /|\[|     /|'
                                                       / \ /     / \                                    
"""
SelectionScreen = r"""
                                                          = Attack / 1 =
                                            = Potion / 2 =              = Gadget / 3 =
                                                           = Flee / 4 =
"""
Gdeath = r"""
                                                        \O/    
                                                         |    <O>__
                                                        / \      | L
"""


HeartD = r"""                                                                            ¶¶
                                                                                    ¶1¶1111111¶      
                                                             ¶¶111¶               ¶¶¶¶111111111¶¶¶1
                                                          ¶1¶¶¶¶¶111111¶       ¶¶¶1¶¶¶11111111¶1¶¶
                                                       ¶¶¶1¶1111111111¶¶1    ¶¶1¶¶¶1111111111111¶¶¶
                                                       ¶¶1¶¶1111111111111¶¶  ¶¶¶1¶¶¶¶1111111111111¶
                                                       ¶¶_¶1111111111111111¶¶ ¶¶¶¶¶¶11¶111111111111¶
                                                       11_¶11111111111111111¶¶   ¶¶¶¶  ¶111111111111¶¶
                                                       ¶¶¶¶1111111111111111¶¶¶¶  1¶¶  11111111111111¶¶
                                                       ¶¶¶¶11111111111¶¶¶¶¶¶¶  1¶1¶¶11111111111111¶1
                                                       ¶¶1¶1111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111111¶¶
                                                       ¶¶11111111111111111111111¶¶  ¶¶¶¶¶¶1111111111¶¶¶
                                                        1¶111111111111111111¶¶¶¶¶¶  ¶¶¶¶11111111111¶1
                                                         ¶¶11111111111111111¶¶¶  ¶¶¶1111111111111¶1
                                                          ¶¶¶111111111111¶1¶¶¶  1¶¶111¶1111111¶11¶1
                                                           1¶¶¶11111111111¶¶¶¶111¶¶¶111111111¶11¶¶¶
                                                            ¶¶¶¶1111111111111¶¶¶¶1¶¶¶¶¶¶¶¶11¶11¶¶
                                                             ¶¶¶¶¶11111111111¶111¶  ¶¶¶111¶1¶¶¶
                                                              ¶¶¶¶¶¶111111111111¶  ¶¶¶111¶¶¶1
                                                                1¶¶¶¶¶11111111¶¶  ¶¶¶¶111¶¶
                                                                 ¶¶¶¶¶¶¶1111111  ¶¶¶11¶¶1
                                                                   1¶¶¶¶¶¶1111¶¶¶1¶¶¶¶
                                                                      ¶¶¶¶¶1¶¶¶¶¶1¶
                                                                         ¶1¶¶¶1¶¶¶
                                                                           11¶






"""
PdeathG = r"""
                                                        _________
                                                          \<O>/  
                                                            |
                                                ‗/‾‾|o     / \
"""
PMisskick = r"""
                                                          O __  <O> /
                                                          |\___--|\/
                                                           |    / X




                                                        O___/‾‾\<O> /
                                                       /|   |    |\/
                                                                / X      
       
                                                      .   _    \<O> /
                                                     O⊥__/       |\/
                                                                / X




                                                               __<O> /
                                                                  |\/
                                                    ‗‗O___/\     / X




                                                          O     <O> /
                                                         /\_    /|\/
                                                       _」‾‾|   / X




"""




J = Player("MCHammer", 100, 250, 10, 0, [])
Sword = Weapon("Goblin Spear", 50, 50)
J.minattack = Sword.minattackboost + J.minattack
J.maxattack = Sword.maxattackboost + J.maxattack
GameRunning = False
MatchRunning = False
GoblinCave = False




start = input("Would you like to begin? ").lower()
if start in ("yes", "y", "1"):
    J.name = input("What would you like your name to be?")
    GameRunning = True
    mapselect = input("Where would you like to go? ").lower()
   
    while GameRunning == True:
        if mapselect in ("goblin cave", "1"):
            GoblinCave = True
            enemy = Enemy("Goblin", 50, 10, 20, ['Goblin Spear', 'Goblin Ear', 'Goblin Eye', "Broken Wooden Handle"])
            print(f'You have encountered {enemy.name}')
            print(Standing)
            if enemy.HP == 0:
                GoblinCave = False
            if GoblinCave == False:
                print("You have cleared the Goblin Cave!")
                print(f"{J.name} has gained 100 dollars as a reward!")
                cash_gain = 100
                J.money += cash_gain
                print(f"{J.name} now has {J.money} (+{cash_gain}) dollars!")
                break


               


        if mapselect in ("graveyard", "2"):
            enemy = Enemy("Zombie", 100, 15, 50, ["Zombie Hand", "Zombie Brain", "Rotten Essence"])


        while J.HP > 0 and enemy.HP > 0:
            print(SelectionScreen)
            control = input("Your move: ").lower()


            if control in ["potion","p","1"]:

                potioncontrol = input("Would you like to consume a suspicious potion?").lower()
                if potioncontrol in ["potion","p","1"]:
                    J.PotionDrink(J) 


            if control in ["attack", "a", "1"]:


                attackcontrol = input("What attack would you like to do? ").lower()
                if attackcontrol in ["punch", "1", "p"]:
                    J.PlayerPunch(enemy)


                elif control in ["kick", "k", "2"]:
                    J.PlayerKick(enemy)


            elif control == "flee":
                break


            else:
                print("Invalid move! Please enter punch or guard.")
   
            if enemy.HP <= 0:
                break
           
            # Enemy's turn (based on AI)
            EnemySelect = enemy.EnemyAI()
   
            if EnemySelect == 1:  # Enemy chooses to punch
                enemy.EnemyPunch(J)  # Enemy punches if player is not guarding


            if J.HP <= 0:
                break
           
        if J.HP > 0:
            print(f"{enemy.name} has been defeated!")
            print(Gdeath)
            print(f"{J.name} wins the battle!")
            cash_gain = enemy.EnemyCDrop()
            J.money += cash_gain
            print(f"{J.name} now has {J.money} (+{cash_gain}) dollars!")
        else:
            print(f"{enemy.name} wins the battle!")
            GameRunning = False







