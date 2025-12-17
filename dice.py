from time import sleep
import player
import playerList
import random

def roll_kuma_die(player):
    sevenChanceOneOver = 8888
    sixChanceOneOver = 32
    count = 0
    print(str(player.get_name()) + " is using Kuma's special die!")
    while True:
        count += 1
        if player is not None:
            sleep(1)
        result = random.randint(1, sevenChanceOneOver)
        if result == sevenChanceOneOver:
            print(str(count) + ". " + str(player.get_name()) + " rolled a 7! WTF!")
            return count,True
        result = random.randint(1, sixChanceOneOver)
        if result == sixChanceOneOver:
            print(str(count) + ". " + str(player.get_name()) + " rolled a 6!")
            return count,False
        result = random.randint(1, 5)
        print(str(count) + ". " + str(player.get_name()) + " rolled a " + str(result))
        if count%20 == 0:
            print(str(player.get_name()) + " rolled "+ str(count) +" times without rolling a 6, Oh Dawg it.")

def roll_normal_die(player):
    sevenChanceOneOver = 6666
    sixChanceOneOver = 24
    count = 0
    print(str(player.get_name()) + " is using a normal die.")
    while True:
        count += 1
        if player is not None:
            sleep(1)
        result = random.randint(1, sevenChanceOneOver)
        if result == sevenChanceOneOver:
            print(str(count) + ". " + str(player.get_name()) + " rolled a 7! WTF!")
            return count,True
        result = random.randint(1, sixChanceOneOver)
        if result == sixChanceOneOver:
            print(str(count) + ". " + str(player.get_name()) + " rolled a 6!")
            return count,False
        result = random.randint(1, 5)
        print(str(count) + ". " + str(player.get_name()) + " rolled a " + str(result))
        if count%20 == 0:
            print(str(player.get_name()) + " rolled "+ str(count) +" times without rolling a 6, Oh Dawg it.")
        
def roll_normal_die_menu():
    costPerRoll = 1
    earning = 20
    print("Select the player:")
    select_player = playerList.PlayerList().select_player()
    if select_player is None:
        return
    if select_player.get_name() == "Kuma":
        count,isSeven = roll_kuma_die(select_player)
    else:
        count,isSeven = roll_normal_die(select_player)
    if isSeven:
        earning = 0
    sum = earning - count * costPerRoll
    print(f"{select_player.get_name()} took {count} rolls to finish.")
    if sum >= 0:
        print(f"{select_player.get_name()} earned ${sum} mil.")
    elif sum < 0:
        print(f"{select_player.get_name()} lost ${-sum} mil.")
    if isSeven:
        print(f"Congratulations {select_player.get_name()}! You rolled a 7 and you obtain a special item!")
    sleep(3)
    select_player.update_balance(sum, "Solo die roll")
    playerList.PlayerList().save()

def roll_vs_die(player1, player2):
    sevenChanceOneOver = 666
    sixChanceOneOver = 24
    count1 = 0
    count2 = 0
    print(f"{player1.get_name()} vs {player2.get_name()}!")
    while True:
        count1 += 1
        sleep(1)
        result = random.randint(1, sevenChanceOneOver)
        if result == sevenChanceOneOver:
            print(str(count1) + ". " + str(player1.get_name()) + " rolled a 7! WTF!")
            return count1,count2,True,1
        result = random.randint(1, sixChanceOneOver)
        if result == sixChanceOneOver:
            print(str(count1) + ". " + str(player1.get_name()) + " rolled a 6!")
            return count1,count2,False,1
        result = random.randint(1, 5)
        print(str(count1) + ". " + str(player1.get_name()) + " rolled a " + str(result))
        count2 += 1
        sleep(1)
        result = random.randint(1, sevenChanceOneOver)
        if result == sevenChanceOneOver:
            print(str(count2) + ". " + str(player2.get_name()) + " rolled a 7! WTF!")
            return count1,count2,True,2
        result = random.randint(1, sixChanceOneOver)
        if result == sixChanceOneOver:
            print(str(count2) + ". " + str(player2.get_name()) + " rolled a 6!")
            return count1,count2,False,2
        result = random.randint(1, 5)
        print(str(count2) + ". " + str(player2.get_name()) + " rolled a " + str(result))
        if count2%10 == 0:
            print("They rolled "+ str(count2) +" times without rolling a 6, Oh Dawg it.")
        

def roll_vs_die_menu():
    costPerRoll = 5
    earning = 100
    print("Select the player 1:")
    select_player1 = playerList.PlayerList().select_player()
    if select_player1 is None:
        return
    print("Select the player 2:")
    select_player2 = playerList.PlayerList().select_player()
    if select_player2 is None:  
        return
    if select_player1.get_name() == select_player2.get_name():
        print("Cannot select the same player for both sides.")
        return
    count1,count2,isSeven,win = roll_vs_die(select_player1,select_player2)
    sleep(1)
    if isSeven:
        earning = 0
    if win == 1:
        sum_win = earning - count1 * costPerRoll
        sum_lose = - count2 * costPerRoll
        print(f"{select_player1.get_name()} took {count1} rolls to finish and won!")
        if sum_win >= 0:
            print(f"{select_player1.get_name()} earned ${sum_win} mil.")
        elif sum_win < 0:
            print(f"{select_player1.get_name()} lost ${-sum_win} mil.")
        if sum_lose >= 0:
            print(f"{select_player2.get_name()} earned ${sum_lose} mil.")
        elif sum_lose < 0:
            print(f"{select_player2.get_name()} lost ${-sum_lose} mil.")
        select_player1.update_balance(sum_win, f"VS {select_player2.get_name()}")
        select_player2.update_balance(sum_lose, f"VS {select_player1.get_name()}")
        playerList.PlayerList().save()
        sleep(3)
    elif win == 2:
        sum_win = earning - count2 * costPerRoll
        sum_lose = - count1 * costPerRoll
        print(f"{select_player2.get_name()} took {count2} rolls to finish and won!")
        if sum_win >= 0:
            print(f"{select_player2.get_name()} earned ${sum_win} mil.")
        elif sum_win < 0:
            print(f"{select_player2.get_name()} lost ${-sum_win} mil.")
        if sum_lose >= 0:
            print(f"{select_player1.get_name()} earned ${sum_lose} mil.")
        elif sum_lose < 0:
            print(f"{select_player1.get_name()} lost ${-sum_lose} mil.")
        select_player2.update_balance(sum_win, f"VS {select_player1.get_name()}")
        select_player1.update_balance(sum_lose, f"VS {select_player2.get_name()}")
        playerList.PlayerList().save()
        sleep(3)
    else:
        print("Error in determining winner.")
        return


def test_menu():
    costPerRoll = 1
    earning = 20
    print("Testing Menu:")
    print("1. Roll normal die")
    print("2. Roll Kuma's die")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        grandTotal = 0
        sevencount = 0
        maxrolls = 0
        for i in range(1000):
            count,isSeven = roll_normal_die(player = None)
            if count > maxrolls:
                maxrolls = count
            sum = earning - count * costPerRoll
            if isSeven:
                sum = 0
                sevencount += 1
            grandTotal += sum
            print(f"Test {i+1}: Took {count} rolls. Earnings: ${sum} mil. Rolled 7: {isSeven}")
        average = grandTotal / 1000
        print(f"Average earnings over 1000 tests: ${average} mil.")
        print(f"Total number of 7s rolled: {sevencount}")
        print(f"Maximum rolls in a single test: {maxrolls}")
    elif choice == '2':
        grandTotal = 0
        sevencount = 0
        maxrolls = 0
        for i in range(1000):
            count,isSeven = roll_kuma_die(player = None)
            if count > maxrolls:
                maxrolls = count
            sum = earning - count * costPerRoll
            if isSeven:
                sum = 0
                sevencount += 1
            grandTotal += sum
            print(f"Test {i+1}: Took {count} rolls. Earnings: ${sum} mil. Rolled 7: {isSeven}")
        average = grandTotal / 1000
        print(f"Average earnings over 1000 tests: ${average} mil.")
        print(f"Total number of 7s rolled: {sevencount}")
        print(f"Maximum rolls in a single test: {maxrolls}")
    else:
        print("Invalid choice.")
        return

def dice_menu():
    print("\nSelect a die to roll:")
    print("1. Solo")
    print("2. VS")
    print("3. testing")
    print("q. Quit")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        roll_normal_die_menu()
    elif choice == '2':
        roll_vs_die_menu()
    elif choice == '3':
        test_menu()
    elif choice == 'q':
        print("Exiting the program.")
        return
    else:
        print("Invalid choice.")
        return
