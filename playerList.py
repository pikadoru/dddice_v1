import player
import pickle
class PlayerList:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'players'):
            self.players = list()
            self.load()

    def save(self):
        try:
            with open('players.pkl', 'wb') as f:
                pickle.dump(self.players, f)
        except Exception as e:
            print(f"Error saving players: {e}")

    def load(self):
        try:
            with open('players.pkl', 'rb') as f:
                self.players = pickle.load(f)
        except FileNotFoundError:
            pass  # No file yet, start empty
        except Exception as e:
            print(f"Error loading players: {e}")

    def add_player(self, player_name:str, balance=100):
        """Add a player to the list."""
        for p in self.players:
            if p.get_name() == player_name:
                print(f"Player {player_name} already exists.")
                return
        self.players.append(player.Player(player_name, balance))
        self.save()

    def remove_player(self, player_name):
        """Remove a player from the list."""
        for p in self.players:
            if p.get_name() == player_name:
                self.players.remove(p)
                self.save()
                return
        print(f"Player {player_name} not found.")

    def get_playerList(self):
        return self.players
    
    def select_player(self):
        for idx, p in enumerate(self.players):
            print(f"{idx+1}. {p.get_name()}")
        choice = input("Enter the number of your choice: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.players):
                return self.players[choice - 1]
            else:
                print("Invalid choice.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
        