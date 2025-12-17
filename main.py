import playerList
import player
import dice

def add_transaction():
    print("\nAdd Transaction:")
    print("Select the type:")
    print("1. Steal other player")
    print("2. Shop")
    print("3. Gift/Take from void")
    type_choice = input("Enter the number of your choice: ")
    if type_choice not in ['1', '2', '3']:
        print("Invalid choice.")
        return
    print("Select the player:")
    select_player = playerList.PlayerList().select_player()
    if select_player is None:
        return
    if type_choice == '1':
        reason = "Steal other player"
        try:
            amount = int(input("Enter the amount to steal (positive number): "))
            if amount <= 0:
                print("Amount must be positive.")
                return
            print("from whom are you stealing?")
            victim_player = playerList.PlayerList().select_player()
            if victim_player is None:
                return
            if victim_player.get_name() == select_player.get_name():
                print("Cannot steal from oneself.")
                return
            select_player.update_balance(amount, f"Steal from {victim_player.get_name()}")
            victim_player.update_balance(-amount, "Stolen by " + select_player.get_name())
        except ValueError:
            print("Invalid amount.")
            return
    elif type_choice == '2':
        reason = "Shop"
        try:
            amount = int(input("Enter the amount spent (positive number): "))
            if amount <= 0:
                print("Amount must be positive.")
                return
            select_player.update_balance(-amount, reason)
        except ValueError:
            print("Invalid amount.")
            return
    elif type_choice == '3':
        reason = "Gift/Take from void"
        try:
            amount = int(input("Enter the amount gifted: "))
            select_player.update_balance(amount, reason)
        except ValueError:
            print("Invalid amount.")
            return
    else:
        print("Invalid choice.")
        return
    playerList.PlayerList().save()

def main():
    players = playerList.PlayerList()
    if players.get_playerList() == []:
        players.add_player("Matthew",100)
        players.add_player("Kuma",100)
        players.add_player("Takumi",100)
    while True:
        print("\nPlayer Balances:")
        for p in players.get_playerList():
            print(f"{p.get_name()}: {p.get_balance()} mil")
        print("\nSelect an option:")
        print("1. Dice Menu")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("q. Exit")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            dice.dice_menu()
        elif choice == '2':
            add_transaction()
        elif choice == '3':
            selected_player = players.select_player()
            if selected_player is None:
                continue
            print(f"\nTransactions for {selected_player.get_name()}:")
            selected_player.print_transactions()
        elif choice == 'q':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice.")
            continue

if __name__ == "__main__":
    main()