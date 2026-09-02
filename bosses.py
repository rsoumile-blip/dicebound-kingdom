from combat import combat


BOSSES = {
    "Blackwood Guardian": {
        "hp": 100,
        "attack": 16,
        "defense": 8,
        "gold": 50,
        "fragment": "Death",
    },
    "Frost Warden": {
        "hp": 120,
        "attack": 18,
        "defense": 10,
        "gold": 60,
        "fragment": "Ice",
    },
    "Flame Lord": {
        "hp": 130,
        "attack": 20,
        "defense": 9,
        "gold": 70,
        "fragment": "Fire",
    },
    "Chronomancer": {
        "hp": 110,
        "attack": 22,
        "defense": 7,
        "gold": 80,
        "fragment": "Time",
    },
    "King of Six": {
        "hp": 180,
        "attack": 24,
        "defense": 12,
        "gold": 150,
        "fragment": "Chaos",
    },
}


def fight_boss(player, boss_name):
    if boss_name not in BOSSES:
        print("❌ Boss not found.")
        return False

    if boss_name in player["bosses"]:
        print(f"✅ You already defeated {boss_name}.")
        return False

    data = BOSSES[boss_name]

    enemy = {
        "name": boss_name,
        "hp": data["hp"],
        "attack": data["attack"],
        "defense": data["defense"],
        "gold": data["gold"],
    }

    print(f"\n👑 BOSS: {boss_name}")
    print(f"🔥 Fragment reward: {data['fragment']}")

    won = combat(player, enemy)

    if won:
        player["bosses"].append(boss_name)

        if data["fragment"] not in player["fragments"]:
            player["fragments"].append(data["fragment"])

        print(f"\n💎 You obtained the {data['fragment']} Fragment!")

    return won
