def get_ending(player):
    fragments = set(player["fragments"])
    completed = len(player["completed_quests"])

    if len(fragments) == 6:
        return (
            "TRUE ENDING",
            "You collected all six Fragments and discovered the truth "
            "behind the Kingdom."
        )

    if "Chaos" in fragments and "Death" in fragments:
        return (
            "CHAOS ENDING",
            "The power of the Fragments consumes the Kingdom."
        )

    if "Life" in fragments and "Ice" in fragments:
        return (
            "GUARDIAN ENDING",
            "You become the protector of the Kingdom."
        )

    if completed >= 3:
        return (
            "HERO ENDING",
            "Your choices save the Kingdom, even without every Fragment."
        )

    return (
        "WANDERER ENDING",
        "The Kingdom survives, but its greatest secrets remain hidden."
    )


def show_ending(player):
    title, text = get_ending(player)

    print("\n" + "=" * 50)
    print(f"👑 {title}")
    print("=" * 50)
    print(text)
    print(f"\n💎 Fragments: {len(player['fragments'])}/6")
