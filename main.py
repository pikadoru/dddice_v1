import playerList
import player
import dice

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
            selected_player = players.select_player()
            if selected_player is None:
                continue
            amount = input("Enter the transaction amount (use negative for deduction): ")
            reason = input("Enter the reason for the transaction: ")
            try:
                amount = int(amount)
                selected_player.update_balance(amount, reason)
                players.save()
            except ValueError:
                print("Invalid amount. Please enter a number.")
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