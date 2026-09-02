import random

from player import create_player, show_player
from board import BOARD, show_location, move_player
from events import trigger_event
from combat import combat
from quests import show_quests, add_quest, complete_quest
from bosses import fight_boss, BOSSES
from endings import show_ending
from save_system import save_game, load_game


def choose_class():
    print("\nChoose your class:")
    print("1. ⚔️ Knight")
    print("2. 🗡️ Rogue")
    print("3. 🔮 Mage")

    classes = {"1": "Knight", "2": "Rogue", "3": "Mage"}

    while True:
        choice = input("> ")
        if choice in classes:
            return classes[choice]
        print("Choose 1, 2, or 3.")


def random_battle(player):
    enemies = [
        {"name": "Goblin Scout", "hp": 35, "attack": 9, "defense": 3, "gold": 8},
        {"name": "Dark Wolf", "hp": 45, "attack": 11, "defense": 4, "gold": 10},
        {"name": "Cursed Knight", "hp": 60, "attack": 13, "defense": 8, "gold": 16},
        {"name": "Void Cultist", "hp": 50, "attack": 15, "defense": 5, "gold": 18},
    ]
    return combat(player, random.choice(enemies))


def explore(player):
    roll = random.randint(1, 12)
    print(f"\n🎲 Exploration D12: {roll}")

    if roll <= 5:
        trigger_event(player)

    elif roll <= 8:
        print("\n⚔️ Enemy encounter!")
        random_battle(player)

    elif roll <= 10:
        gold = random.randint(10, 30)
        player["gold"] += gold
        print(f"\n💰 You found {gold} gold.")

    else:
        print("\n✨ You discovered an ancient secret.")
        player["flags"]["secret_found"] = True


def location_action(player):
    name = BOARD[player["position"]]["name"]

    if name == "Flame Valley":
        fight_boss(player, "Flame Lord")

    elif name == "Frozen North":
        fight_boss(player, "Frost Warden")

    elif name == "Blackwood":
        fight_boss(player, "Blackwood Guardian")

    elif name == "Sixfold Citadel":
        fight_boss(player, "King of Six")

    else:
        explore(player)


def new_game():
    print("\n" + "=" * 45)
    print("       THE DICEBOUND KINGDOM")
    print("              V2.0")
    print("=" * 45)

    name = input("\nEnter your hero's name: ")
    class_name = choose_class()

    player = create_player(name, class_name)

    print(f"\n🔥 Welcome, {name} the {class_name}!")
    return player


def main():
    print("\n" + "=" * 45)
    print("       THE DICEBOUND KINGDOM")
    print("              V2.0")
    print("=" * 45)

    print("\n1. ⚔️ New Game")
    print("2. 📂 Continue")

    while True:
        choice = input("> ")

        if choice == "1":
            player = new_game()
            break

        if choice == "2":
            player = load_game()
            if player is not None:
                break
            print("Starting a new game...")
            player = new_game()
            break

        print("Choose 1 or 2.")

    while player["hp"] > 0:

        print("\n" + "-" * 45)
        print(f"📍 {BOARD[player['position']]['name']}")
        print(f"❤️ HP {player['hp']}/{player['max_hp']}   💰 {player['gold']}")
        print(f"💎 Fragments: {len(player['fragments'])}/6")

        print("\n1. 🎲 Roll & Move")
        print("2. 🔎 Explore")
        print("3. 📊 Character")
        print("4. 🎒 Inventory")
        print("5. 📜 Quests")
        print("6. 💾 Save")
        print("7. 👑 Endings")
        print("8. 🚪 Quit")

        choice = input("> ")

        if choice == "1":
            move_player(player)
            location_action(player)

        elif choice == "2":
            explore(player)

        elif choice == "3":
            show_player(player)

        elif choice == "4":
            print("\n🎒 Inventory:")
            print(", ".join(player["inventory"]))

        elif choice == "5":
            show_quests(player)

            if not player["quests"]:
                add_quest(player, "Explore the Kingdom")

        elif choice == "6":
            save_game(player)

        elif choice == "7":
            show_ending(player)

        elif choice == "8":
            save_game(player)
            print("\n👋 Goodbye.")
            break

        else:
            print("Choose 1-8.")

    if player["hp"] <= 0:
        print("\n💀 Your hero has fallen.")
        show_ending(player)


if __name__ == "__main__":
    main()
