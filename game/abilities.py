import random


def roll_d4():
    return random.randint(1, 4)


def use_ability(player, enemy):
    class_name = player["class"]
    roll = roll_d4()

    print(f"\n🎲 Ability roll: {roll}")

    if class_name == "Knight":
        # Shield Bash
        damage = max(5, player["defense"] + roll * 3 - enemy["defense"])
        enemy["hp"] -= damage

        print(f"🛡️ Shield Bash deals {damage} damage!")

        if roll >= 3:
            enemy["stunned"] = True
            print("💫 The enemy is stunned!")

    elif class_name == "Rogue":
        # Shadow Strike
        if roll >= 2:
            damage = max(8, player["attack"] * 2 - enemy["defense"])
            enemy["hp"] -= damage
            print(f"🗡️ Shadow Strike deals {damage} damage!")

            if roll == 4:
                print("🌑 Perfect strike! Extra damage!")
                enemy["hp"] -= 10
        else:
            print("🌑 Shadow Strike failed!")

    elif class_name == "Mage":
        # Arcane Burst
        damage = max(10, player["attack"] + roll * 4)
        enemy["hp"] -= damage

        print(f"🔮 Arcane Burst deals {damage} damage!")

        if roll == 4:
            print("✨ Arcane Surge! Extra 15 damage!")
            enemy["hp"] -= 15

    return roll
