import random
from art import art 
PotionDuration = 0
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
        print(Ppunch)








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
            print(Pkick)
        elif kickchance < 8:
            enemy.HP -= 0
            print(PMisskick)
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








# Standing = r"""
#                                             O                                 <O> /
#                                            /|\                                /|\/
#                                            / \                                / X
# """
# Standingclose = r"""
#                                                     O                   <O> /
#                                                    /|\                  /|\/
#                                                    / \                  / X
# """
# Standingclose2 = r"""
#                                                            O    <O> /
#                                                           /|\   /|\/
#                                                           / \   / X
# """
# PreGstrike = r"""
#                                                            O  <-<O>.--
#                                                           /|\   /|'
#                                                           / \   / \
# """
# Gstrike = r"""
#                                                            O<---<O>.-
#                                                           /|\  --|'
#                                                           / \   / \
# """








# Ppunch = r"""        
#                                                            O    <O> /
#                                                           /|--- /|\/
#                                                           / \   / X """
# Pkick = r"""
#                                                           O __  <O> /
#                                                           |\___ /|\/
#                                                            |    / X
# """
                   
# PPshieldGstrike = r"""                                  O  \   <-<O>.--
#                                                        /|\[|     /|'
#                                                        / \ /     / \                                    
# """
# SelectionScreen = r"""
#                                                           = Attack / 1 =
#                                             = Potion / 2 =              = Gadget / 3 =
#                                                            = Flee / 4 =
# """
# Gdeath = r"""
#                                                         \O/    
#                                                          |    <O>__
#                                                         / \      | L
# """








# HeartD = r"""                                                                            ¶¶
#                                                                                     ¶1¶1111111¶      
#                                                              ¶¶111¶               ¶¶¶¶111111111¶¶¶1
#                                                           ¶1¶¶¶¶¶111111¶       ¶¶¶1¶¶¶11111111¶1¶¶
#                                                        ¶¶¶1¶1111111111¶¶1    ¶¶1¶¶¶1111111111111¶¶¶
#                                                        ¶¶1¶¶1111111111111¶¶  ¶¶¶1¶¶¶¶1111111111111¶
#                                                        ¶¶_¶1111111111111111¶¶ ¶¶¶¶¶¶11¶111111111111¶
#                                                        11_¶11111111111111111¶¶   ¶¶¶¶  ¶111111111111¶¶
#                                                        ¶¶¶¶1111111111111111¶¶¶¶  1¶¶  11111111111111¶¶
#                                                        ¶¶¶¶11111111111¶¶¶¶¶¶¶  1¶1¶¶11111111111111¶1
#                                                        ¶¶1¶1111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111111¶¶
#                                                        ¶¶11111111111111111111111¶¶  ¶¶¶¶¶¶1111111111¶¶¶
#                                                         1¶111111111111111111¶¶¶¶¶¶  ¶¶¶¶11111111111¶1
#                                                          ¶¶11111111111111111¶¶¶  ¶¶¶1111111111111¶1
#                                                           ¶¶¶111111111111¶1¶¶¶  1¶¶111¶1111111¶11¶1
#                                                            1¶¶¶11111111111¶¶¶¶111¶¶¶111111111¶11¶¶¶
#                                                             ¶¶¶¶1111111111111¶¶¶¶1¶¶¶¶¶¶¶¶11¶11¶¶
#                                                              ¶¶¶¶¶11111111111¶111¶  ¶¶¶111¶1¶¶¶
#                                                               ¶¶¶¶¶¶111111111111¶  ¶¶¶111¶¶¶1
#                                                                 1¶¶¶¶¶11111111¶¶  ¶¶¶¶111¶¶
#                                                                  ¶¶¶¶¶¶¶1111111  ¶¶¶11¶¶1
#                                                                    1¶¶¶¶¶¶1111¶¶¶1¶¶¶¶
#                                                                       ¶¶¶¶¶1¶¶¶¶¶1¶
#                                                                          ¶1¶¶¶1¶¶¶
#                                                                            11¶











# """
# PdeathG = r"""
#                                                         _________
#                                                           \<O>/  
#                                                             |
#                                                 ‗/‾‾|o     / \
# """
# PMisskick = r"""
#                                                           O __  <O> /
#                                                           |\___--|\/
#                                                            |    / X


#                                                         O___/‾‾\<O> /
#                                                        /|   |    |\/
#                                                                 / X      
       

#                                                       .   _    \<O> /
#                                                      O⊥__/       |\/
#                                                                 / X


#                                                                __<O> /
#                                                                   |\/
#                                                     ‗‗O___/\     / X


#                                                           O     <O> /
#                                                          /\_    /|\/
#                                                        _」‾‾|   / X

# """




# RegenDrink = r"""
#                                                            O  <O>    \
#                                                            |==-|/     \
#                                                           / \ / /      v


#                                                         O︿                   <O>
#                                                         |--♁                  _/\
#                                                        / \                  |‾‾ |_                                    

                         
#                                            O ⸧>   +                    <O> /
#                                     .  +  /|                           /|\/
#                                           / \     +                    / X








# """
# WeaknessDrink = r"""
#                                                            O  <O>    \
#                                                            |==-|/     \
#                                                           / \ / /      v


#                                                         O︿                   <O>
#                                                         |--♁                  _/\
#                                                        / \                  |‾‾ |_                                    


                        
#                                            O ⸧>  ⇓                     <O> /
#                                 .      ⇓  /|                           /|\/
#                                           / \   ⇓                      / X

# """
# PoisonDrink = r"""
#                                                            O  <O>    \
#                                                            |==-|/     \
#                                                           / \ / /      v


#                                                         O︿                   <O>
#                                                         |--♁                  _/\
#                                                        / \                  |‾‾ |_                                    


                        
#                                            O ⸧>  ☠                    <O> /
#                                    .  ☠   /|                          /|\/
#                                           / \ ☠                       / X


# """
# HPDrink = r"""
#                                                            O  <O>    \
#                                                            |==-|/     \
#                                                           / \ / /      v


#                                                         O︿                   <O>
#                                                         |--♁                  _/\
#                                                        / \                  |‾‾ |_                                    


                        
#                                            O ⸧> ↑                      <O> /
#                                     . ↑   /|                           /|\/
#                                           / \     ↑                    / X


# """







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


        print(SelectionScreen)
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
        print(Gdeath)
        print(f"{J.name} wins the battle!")
        cash_gain = enemy.EnemyCDrop()
        J.money += cash_gain
        print(f"{J.name} now has {J.money} (+{cash_gain}) dollars!")
    else:
        print(f"{enemy.name} wins the battle!")


