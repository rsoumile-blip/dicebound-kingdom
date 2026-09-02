import random
from abilities import use_ability


def roll_d20():
    return random.randint(1, 20)


def calculate_damage(attack, defense, critical=False):
    damage = max(1, attack - defense + random.randint(1, 6))

    if critical:
        damage *= 2

    return damage


def enemy_turn(player, enemy):
    if enemy.get("stunned", False):
        print(f"💫 {enemy['name']} is stunned and misses its turn!")
        enemy["stunned"] = False
        return

    roll = roll_d20()

    if roll == 20:
        damage = calculate_damage(enemy["attack"], 0, True)
        player["hp"] -= damage
        print(f"💥 {enemy['name']} lands a CRITICAL HIT for {damage} damage!")

    elif roll == 1:
        print(f"❌ {enemy['name']} completely misses!")

    else:
        damage = calculate_damage(enemy["attack"], player["defense"])
        player["hp"] -= damage
        print(f"👹 {enemy['name']} hits you for {damage} damage.")


def player_attack(player, enemy):
    roll = roll_d20()

    print(f"\n🎲 Attack roll: {roll}")

    if roll == 20:
        damage = calculate_damage(
            player["attack"],
            enemy["defense"],
            True
        )
        enemy["hp"] -= damage
        print(f"⚡ CRITICAL HIT! You deal {damage} damage!")

    elif roll == 1:
        print("💀 Critical failure! Your attack misses.")

    else:
        damage = calculate_damage(
            player["attack"],
            enemy["defense"]
        )
        enemy["hp"] -= damage
        print(f"⚔️ You deal {damage} damage.")


def use_potion(player):
    if "Small Potion" not in player["inventory"]:
        print("❌ You don't have a potion.")
        return False

    if player["hp"] >= player["max_hp"]:
        print("❤️ Your HP is already full.")
        return False

    player["inventory"].remove("Small Potion")

    old_hp = player["hp"]
    player["hp"] = min(player["max_hp"], player["hp"] + 30)

    print(f"🧪 You restored {player['hp'] - old_hp} HP.")
    return True


def combat(player, enemy):
    enemy = enemy.copy()

    print("\n" + "=" * 45)
    print(f"⚔️ BATTLE: {enemy['name']}")
    print("=" * 45)

    while player["hp"] > 0 and enemy["hp"] > 0:

        print(f"\n❤️ {player['name']}: {player['hp']}/{player['max_hp']} HP")
        print(f"👹 {enemy['name']}: {enemy['hp']} HP")

        print("\n1. ⚔️ Attack")
        print("2. 🧪 Potion")
        print("3. ✨ Ability")

        choice = input("> ")

        if choice == "1":
            player_attack(player, enemy)

        elif choice == "2":
            if not use_potion(player):
                continue

        elif choice == "3":
            use_ability(player, enemy)

        else:
            print("Choose 1, 2, or 3.")
            continue

        if enemy["hp"] <= 0:
            break

        enemy_turn(player, enemy)

    if player["hp"] <= 0:
        print("\n💀 You were defeated.")
        return False

    print(f"\n🏆 You defeated {enemy['name']}!")
    print(f"💰 +{enemy['gold']} gold")
    print("✨ +25 XP")

    player["gold"] += enemy["gold"]
    player["xp"] += 25

    return True
