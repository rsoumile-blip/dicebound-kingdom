from player import create_player
from board import roll_d6, show_location
from combat import combat
from quests import show_quests
from save_system import save_game, load_game


class AndroidGame:
    def __init__(self):
        self.player = None
        self.position = 0
        self.message = "Welcome to The Dicebound Kingdom!"

    def new_game(self, name, class_name):
        self.player = create_player(name, class_name)
        self.position = 0
        self.message = f"Welcome, {name}! You are a {class_name}."

    def roll_and_move(self):
        if not self.player:
            self.message = "Start a new game first."
            return self.message

        roll = roll_d6()
        self.position += roll

        try:
            location = show_location(self.position)
        except Exception:
            location = f"Position {self.position}"

        self.message = f"🎲 You rolled {roll}!\\nYou moved to {location}."
        return self.message

    def quests(self):
        if not self.player:
            return "Start a game first."

        show_quests(self.player)
        return "📜 Quest log opened."

    def save(self):
        if not self.player:
            return "Nothing to save."

        save_game(self.player)
        self.message = "💾 Game saved!"
        return self.message

    def load(self):
        player = load_game()

        if player:
            self.player = player
            self.message = "📂 Game loaded!"
        else:
            self.message = "No save found."

        return self.message
