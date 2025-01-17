



import time
import random
import threading
import art
class Player:
    def __init__(self, name, HP, attack, money, inventory, playerovertime, potionduration, potentialtimer, BlackFlashTiming):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.money = money
        self.inventory = inventory
        self.playerovertime = playerovertime
        self.potionduration = potionduration
        self.potentialtimer = potentialtimer
        self.BlackFlashTiming = BlackFlashTiming




    def PlayerPunch(self, enemy):
        damage = (self.attack)
        enemy.HP -= damage
        J.HP += self.playerovertime
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        print(art.Ppunch)
        if self.playerovertime < 0:
            print(f"{self.name} lost {self.playerovertime} from Poisoning!")
        elif self.playerovertime > 0:
            print(f"{self.name} gained {self.playerovertime} from their regeneration potion!")
        else:
            print(" ")




    def PlayerKick(self, enemy):
        damage = (self.attack * 2.5)
        J.HP += self.playerovertime
        if self.playerovertime <= 0:
            print(f"{self.name} lost {self.playerovertime} from Poisoning!")
        elif self.playerovertime >= 0:
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


    def PotionDrink(self,HP):
        WhichPotion = random.randint(1,4)
        if WhichPotion == 1:
            self.HP +=50
            print(art.HPDrink)
            print(f"{self.name} drunk a bottle of Combat Stim and will now receive 50 HP ")


        elif WhichPotion == 2:
            self.playerovertime += 2
            print(art.RegenDrink)
            print("You drank a suspicious potion and it turned out to be the Ichor of the Gods. It flows through you and you will now recieve health slowly for the duration of the battle.")


        elif WhichPotion == 3:
            self.playerovertime -= 4
            print(art.PoisonDrink)
            print("You drank a suspicious potion and it turned out to be the Tunnel Asp Venom. It is in your system and will eventually kill you. ")    


        elif WhichPotion == 4:
            print(art.WeaknessDrink)
            print("You drank a weakness potion and your attack is halved for four turns.")
            self.potionduration += 4
            if self.potionduration > 0:
                self.attack = self.attack*0.5




    def BlackFlash(self, enemy):
        damage = self.attack*2.5
        enemy.HP -= damage
        print(f"You have landed a black flash and dealt {damage} damage!")
        print("You have went 120 percent of your potential for 3 turns.")
        print(art.BlackFlash)
        self.potentialtimer += 3






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




    def EnemyCDrop(self):
        return self.cdrop


class Weapon:
    def __init__(self, name, attackboost):
        self.name = name
        self.attackboost = attackboost


class Armor:
    def __init__(self, name, hpboost):
        self.name = name
        self.hpboost = hpboost






class Stage1Boss(Enemy):
    def __init__(self, name, HP, attack, cdrop, itemdrop):
        super().__init__(name, HP, attack, cdrop, itemdrop)




    def check_stage_transition(self):
        if self.HP <= 100:
            print(f"{self.name} is enraged and transforms into a more powerful form!")
            return Stage2Boss(self.name, 200, self.attack * 1.5, self.cdrop, self.itemdrop)
        return self






class Stage2Boss(Stage1Boss):
    def __init__(self, name, HP, attack, cdrop, itemdrop):
        super().__init__(name, HP, attack, cdrop, itemdrop)




    def EnemyPunch(self, player):
        super().EnemyPunch(player)
        player.playerovertime -= 0.5 #this is a poison effect upon hit



Weapon = Weapon("Wooden Sword", 20)
SArmor = Armor("Starter Chestplate", 100)
BArmor = Armor("Light Chainmail Plate", 150)
J = Player("MCHammer", 0, 10, 0, [], 0, 0, 0, 0.60)
J.attack = J.attack + Weapon.attackboost
J.HP = J.HP + SArmor.hpboost
PotentialMult = 0

# from moneygrab import Collector




# merchant = Collector(700, 0, 1000, [
#     "Reversed Cursed Technique in a Nutshell",
#     "A Black Flash in a Bottle",
#     "The Eye of Agamoto"
# ])



# print("\nYou meet a strange Collector. He offers to trade!")
# while True:
#     action = input("\nWhat would you like to do? (1: Buy, 2: Sell, 3: Leave) ").lower()
#     if action in ["1", "buy"]:
#         merchant.sell_item(J)  
#     elif action in ["2", "sell"]:
#         merchant.buy_item(J)
#     elif action in ["3", "leave"]:
#         print("\nYou left the Collector.")
#         break
#     else:
#         print("\nInvalid choice.")






J.name = input("What would you like your name to be? ")
print(art.MapSelection)


game_running = True  # Controls the outer loop
while game_running:
    sprompt = True


    while sprompt == True:
        mapselect = input("Where would you like to go? ").lower()




        if mapselect in ("goblin cave", "1"):
            map = "gcave"
            enemiesfought = 0
            while sprompt == True:
                try:
                    AmountSelect = int(input("How many goblins would you like to fight? "))
                    if AmountSelect <= 0:
                        print("Please enter a valid number greater than 0.")
                        continue  
                    break  
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue  
            aprompt = True
            break




        elif mapselect in ("graveyard", "2"):
            map = "graveyard"
            enemiesfought = 0
            while sprompt == True:
                try:
                    AmountSelect = int(input("How many zombies would you like to fight? "))
                    if AmountSelect <= 0:
                        print("Please enter a valid number greater than 0.")
                        continue  
                    break  
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue  
            aprompt = True
            break
        elif mapselect in ("reaper boss", "5"):
            map = "graveyardarena"
            AmountSelect = 1
            aprompt = True
            enemiesfought = 0
            break




        elif mapselect in ("goblin boss", "4"):
            map = "goblinarena"
            AmountSelect = 1
            aprompt = True
            enemiesfought = 0
            break

        elif mapselect in ("Merchant","collector","c","m","3"):

            from moneygrab import Collector




            merchant = Collector(700, 0, 1000, [
                "Reversed Cursed Technique in a Nutshell",
                "A Black Flash in a Bottle",
                "The Eye of Agamoto"
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
            continue
        
        

        else:
            print("That is not available, try again.")  
            continue  

# game_running = True  # Outer loop control
# while game_running:
#     aprompt = True  # Set to True to start the game loop
#     enemiesfought = 0  # Reset enemy count for a new run

    while aprompt:
        if AmountSelect > 0:
            for i in range(AmountSelect):
                if map == "graveyard":
                    enemy = Enemy("Zombie", 100, 15, 50, ["Zombie Hand", "Zombie Brain", "Rotten Essence"])
                elif map == "gcave":
                    enemy = Enemy("Goblin", 50, 10, 20, ['Goblin Spear', 'Goblin Ear', 'Goblin Eye', "Broken Wooden Handle"])
                elif map == "graveyardarena":
                    enemy = Stage1Boss("Grim Reaper", 300, 50, 200, ["Reaper Scythe", "Reaper Cloak"])
                elif map == "goblinarena":
                    enemy = Stage1Boss("Goblin Lord", 200, 30, 100, ["Goblin Crown", "Goblin Sword"])
                print(f"You have encountered {enemy.name}!")
                enemiesfought += 1
    
                while J.HP > 0 and enemy.HP > 0:
                    SelectionScreen = rf"""
                        {enemy.name}                       = Punch / 1 =                 {J.name}                       Potion Duration: {J.potionduration}
                        HP: {enemy.HP}            = Potion / 2 =              = Kick / 3 =    HP: {J.HP}                   Potential: {J.potentialtimer}
                        Attack: {enemy.attack}                                                      Attack: {J.attack}             Critical Timing: {J.BlackFlashTiming}    
                    """
                    if J.potionduration >= 1:
                        J.potionduration -= 1
                    if J.potentialtimer >= 1:
                        J.potentialtimer -= 1
                    if J.potentialtimer == 0 and PotentialMult == 1:
                        J.attack = J.attack/1.2
                        PotentialMult = 0
                    print(SelectionScreen)
                    if enemy.name in ["Goblin Lord", "Grim Reaper"]:
                        enemy.check_stage_transition()
                    control = input("Your move: ").lower()
    
                    if control in ["punch", "1", "p"]:
                    
                       def timeout():
                           global timed_out
                           timed_out = True
                           print("You were too slow to attack!")
                           print(art.PMissPunch)      
                       timed_out = False      
                       print("Get ready...")
                       time.sleep(random.uniform(1, 1))        
                       key = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                       print(f"Press {key} now!")      
                       timer = threading.Timer(1.5, timeout)
                       timer.start()      
                       start_time = time.time()
                       input_character = input(">>> ").strip().upper()
                       timer.cancel()
                       if not timed_out:
                           reaction_time = time.time() - start_time
                           if input_character == key:
                               if reaction_time > J.BlackFlashTiming and reaction_time < 1:
                                   print(f"Good! Your reaction time: {reaction_time:.2f} seconds")
                                   J.PlayerPunch(enemy)
                               elif reaction_time <= J.BlackFlashTiming:
                                   print(f"Amazing! Your reaction time was {reaction_time:.2f} seconds, you hit a black flash!")
                                   J.BlackFlash(enemy)
                                   if PotentialMult == 0:
                                       PotentialMult = 1
                                       J.attack = J.attack*1.2
                               elif reaction_time > 1:
                                   print(f"Meh, your reaction time was {reaction_time:.2f} seconds")
                                   J.PlayerPunch(enemy)
                    elif control in ["potion","pot","2"]:
                        potioncontrol = input("Would you like to consume a suspicious potion? ").lower()
                        if potioncontrol in ["potion","pot","2", "yes", "y"]:
                            J.PotionDrink(J)
                    elif control in ["kick", "k", "3"]:
                        J.PlayerKick(enemy)
                    elif control == "flee":
                        break  
                    else:
                        print("Invalid move! Please enter one of the selections.")
                        print("Your enemy moved while you messed up!")
    
    
                    if enemy.HP <= 0:
                        print(f"{enemy.name} has been defeated!")
                        cash_gain = enemy.EnemyCDrop()
                        J.money += cash_gain
                        print(f"{J.name} now has {J.money} (+{cash_gain}) dollars!")
                        break
                    
                    
                    EnemySelect = enemy.EnemyAI()
                    if EnemySelect == 1:  
                        enemy.EnemyPunch(J)    
                    if J.HP <= 0:
                        print(f"{J.name} has been defeated!")
                        break
                    
                    
                    
                    
            if J.HP > 0:
                reward = 0
                if map == "gcave":
                    reward = 10
                elif map == 'graveyard':
                    reward = 20
                elif map == "goblinarena":
                    reward = 200
                elif map == "graveyardarena":
                    reward = 300
                print(f"{J.name} has defeated all enemies!")
                print(art.Gdeath)
                print(f"{J.name} has received an additional {enemiesfought*reward} dollars for clearing this!")
                J.money += enemiesfought * reward
                print(f"{J.name} now has {J.money} dollars!")
                sprompt = True
            else:
                print(f"{enemy.name} wins the battle!")
                print(f"{J.name} was robbed by {enemy.name} for {enemy.cdrop} dollars!")
                J.money -= enemy.cdrop
                print(f"{J.name} now has {J.money} (-{enemy.cdrop}) dollars")
                aprompt = False



        restart_choice = input("Do you want to restart the game? (yes/no): ").lower()
        if restart_choice not in ["yes", "y"]:
            game_running = False
            print("Thanks for playing! See you next time!")

