import random

BOARD = {
    0: {
        "name": "Castle Gate",
        "paths": [1, 2],
        "description": "The journey begins. Two roads lead into the unknown."
    },
    1: {
        "name": "Blackwood Road",
        "paths": [3],
        "description": "A dark forest surrounds the road."
    },
    2: {
        "name": "Old King's Road",
        "paths": [3, 4],
        "description": "Ancient stones mark the forgotten royal road."
    },
    3: {
        "name": "Blackwood",
        "paths": [5, 6],
        "description": "Something is watching from between the trees."
    },
    4: {
        "name": "Ruined Village",
        "paths": [6, 7],
        "description": "The village was abandoned long ago."
    },
    5: {
        "name": "Forgotten Altar",
        "paths": [8],
        "description": "A strange altar pulses with ancient magic."
    },
    6: {
        "name": "Crossroads",
        "paths": [8, 9],
        "description": "Three roads once met here. Only two remain."
    },
    7: {
        "name": "Cursed Mine",
        "paths": [9],
        "description": "Cold air escapes from the mine entrance."
    },
    8: {
        "name": "Frozen North",
        "paths": [10],
        "description": "Snow covers everything as the temperature drops."
    },
    9: {
        "name": "Flame Valley",
        "paths": [10],
        "description": "The ground burns beneath your feet."
    },
    10: {
        "name": "Sixfold Citadel",
        "paths": [],
        "description": "The final fortress stands before you."
    },
}


def roll_d6():
    return random.randint(1, 6)


def show_location(position):
    location = BOARD[position]

    print("\n" + "=" * 45)
    print(f"📍 {location['name']}")
    print("=" * 45)
    print(location["description"])

    if location["paths"]:
        print("\nAvailable paths:")
        for number, path in enumerate(location["paths"], 1):
            print(f"{number}. {BOARD[path]['name']}")


def move_player(player):
    roll = roll_d6()

    print(f"\n🎲 You rolled a {roll}!")

    current = player["position"]

    for _ in range(roll):
        paths = BOARD[current]["paths"]

        if not paths:
            break

        if len(paths) == 1:
            current = paths[0]
        else:
            print("\nChoose your path:")
            for number, path in enumerate(paths, 1):
                print(f"{number}. {BOARD[path]['name']}")

            while True:
                choice = input("> ")

                if choice in ("1", "2"):
                    current = paths[int(choice) - 1]
                    break

                print("Choose 1 or 2.")

    player["position"] = current

    print(f"\n➡️ You arrived at: {BOARD[current]['name']}")
