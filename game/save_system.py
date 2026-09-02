import json
import os

SAVE_FILE = "saves/save.json"


def save_game(player):
    os.makedirs("saves", exist_ok=True)

    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(player, file, indent=2)

    print("\n💾 Game saved!")


def load_game():
    if not os.path.exists(SAVE_FILE):
        print("\n❌ No save found.")
        return None

    with open(SAVE_FILE, "r", encoding="utf-8") as file:
        player = json.load(file)

    print("\n📂 Game loaded!")
    return player
