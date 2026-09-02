import json
from pathlib import Path

CONTENT_DIR = Path(__file__).parent / "content"


def load_content(filename):
    path = CONTENT_DIR / filename

    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_all_content():
    return {
        "enemies": load_content("enemies.json"),
        "items": load_content("items.json"),
        "quests": load_content("quests.json"),
        "bosses": load_content("bosses.json"),
        "regions": load_content("regions.json"),
        "events": load_content("events.json")
    }
