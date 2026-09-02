FRAGMENT_QUESTS = {
    "Fire": "Defeat the Flame Lord.",
    "Ice": "Defeat the Frost Warden.",
    "Death": "Uncover the secret of the Forgotten Altar.",
    "Time": "Find the Chronomancer.",
    "Life": "Save the Fallen Knight.",
    "Chaos": "Discover the truth behind the Six Fragments.",
}


def show_quests(player):
    print("\n📜 QUESTS")

    if not player["quests"]:
        print("No active quests.")
    else:
        for quest in player["quests"]:
            print(f"• {quest}")

    if player["completed_quests"]:
        print("\n✅ COMPLETED")
        for quest in player["completed_quests"]:
            print(f"• {quest}")


def add_quest(player, quest):
    if quest not in player["quests"] and quest not in player["completed_quests"]:
        player["quests"].append(quest)
        print(f"\n📜 New Quest: {quest}")


def complete_quest(player, quest):
    if quest in player["quests"]:
        player["quests"].remove(quest)
        player["completed_quests"].append(quest)
        print(f"\n✅ Quest completed: {quest}")
