class Collector:
    def __init__(self, HP, attack, money, shop):
        self.HP = HP
        self.attack = attack
        self.money = money
        self.shop = shop


    def show_shop(self):
       
        print("\nCollector's Shop:")
        for i, item in enumerate(self.shop, start=1):
            print(f"{i}. {item}")
        print(f"\nCollector's Money: {self.money}")


    def sell_item(self, player):
       
        self.show_shop()
        choice = input("\nWhat would you like to buy? (Enter item number or 'exit') ").lower()
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(self.shop):
                item = self.shop.pop(choice)
                if player.money >= 50:  # Assuming all items cost 50 for simplicity.
                    player.money -= 50
                    player.inventory.append(item)
                    self.money += 50
                    print(f"\nYou bought {item} for $50. Remaining money: {player.money}")
                else:
                    print("\nYou don't have enough money!")
            else:
                print("\nInvalid choice.")
        elif choice == "exit":
            print("\nYou left the shop.")
        else:
            print("\nInvalid input.")


    def buy_item(self, player):
       
        print("\nYour Inventory:")
        for i, item in enumerate(player.inventory, start=1):
            print(f"{i}. {item}")
        print(f"\nYour Money: {player.money}")


        choice = input("\nWhat would you like to sell? (Enter item number or 'exit') ").lower()
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(player.inventory):
                item = player.inventory.pop(choice)
                player.money += 25  # Assuming items sell for $25 for simplicity.
                self.money -= 25
                self.shop.append(item)
                print(f"\nYou sold {item} for $25. Your new balance: {player.money}")
            else:
                print("\nInvalid choice.")
        elif choice == "exit":
            print("\nYou left the shop.")
        else:
            print("\nInvalid input.")
































