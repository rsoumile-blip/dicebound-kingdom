import random

EVENTS = [
    ("Healing Spring", "You find a magical spring.", 1),
    ("Goblin Ambush", "Enemies leap from the shadows!", 2),
    ("Treasure Chest", "You discover a forgotten chest.", 3),
    ("Mysterious Traveler", "A strange traveler offers you a choice.", 4),
    ("Ancient Shrine", "An ancient shrine reacts to your presence.", 5),
    ("Fallen Knight", "A wounded knight asks for help.", 6),
    ("Cursed Ground", "Dark energy surrounds you.", 7),
    ("Merchant", "A traveling merchant appears.", 8),
    ("Lost Child", "You find someone lost on the road.", 9),
    ("Magic Rift", "Reality briefly tears open.", 10),
    ("Rare Treasure", "You discover something extremely valuable.", 11),
    ("Fragment Vision", "You glimpse one of the Six Fragments.", 12),
]


def trigger_event(player):
    roll = random.randint(1, 12)
    name, description, _ = EVENTS[roll - 1]

    print("\n" + "=" * 45)
    print(f"🎲 D12 EVENT: {roll}")
    print(f"✨ {name}")
    print("=" * 45)
    print(description)

    if roll == 1:
        healing = 25
        player["hp"] = min(player["max_hp"], player["hp"] + healing)
        print(f"❤️ You recover {healing} HP.")

    elif roll == 2:
        print("⚔️ A battle is about to begin.")

    elif roll == 3:
        player["gold"] += 30
        print("💰 You found 30 gold.")

    elif roll == 4:
        print("❓ The traveler asks: 'Do you trust fate?'")

    elif roll == 5:
        print("🔮 The shrine seems connected to the Six Fragments.")

    elif roll == 6:
        player["flags"]["helped_knight"] = True
        print("🛡️ You agree to help the knight.")

    elif roll == 7:
        damage = 10
        player["hp"] = max(1, player["hp"] - damage)
        print(f"💀 Dark energy deals {damage} damage.")

    elif roll == 8:
        print("🛒 A merchant waits nearby.")

    elif roll == 9:
        player["flags"]["found_child"] = True
        print("🌟 A new quest may have appeared.")

    elif roll == 10:
        print("🌀 The rift disappears as quickly as it appeared.")

    elif roll == 11:
        player["gold"] += 75
        print("💎 You found 75 gold!")

    elif roll == 12:
        print("👁️ You see a vision of a Fragment...")
        player["flags"]["fragment_vision"] = True

    return roll
