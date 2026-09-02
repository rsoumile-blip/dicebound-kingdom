from data import CLASSES


def create_player(name, class_name):
    stats = CLASSES[class_name]

    return {
        "name": name,
        "class": class_name,
        "level": 1,
        "xp": 0,
        "hp": stats["max_hp"],
        "max_hp": stats["max_hp"],
        "attack": stats["attack"],
        "defense": stats["defense"],
        "luck": stats["luck"],
        "gold": 25,
        "position": 0,
        "inventory": ["Small Potion"],
        "fragments": [],
        "quests": [],
        "completed_quests": [],
        "bosses": [],
        "flags": {},
    }


def show_player(player):
    print("\n" + "=" * 35)
    print(f"  {player['name']} — Level {player['level']}")
    print("=" * 35)
    print(f"Class:   {player['class']}")
    print(f"HP:      {player['hp']}/{player['max_hp']}")
    print(f"Attack:  {player['attack']}")
    print(f"Defense: {player['defense']}")
    print(f"Luck:    {player['luck']}")
    print(f"Gold:    {player['gold']}")
    print(f"XP:      {player['xp']}")
    print(f"Fragments: {', '.join(player['fragments']) or 'None'}")
    print("=" * 35)
