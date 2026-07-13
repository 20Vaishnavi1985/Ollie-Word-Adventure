import json
import os
import sys

def get_save_path(filename):
    folder = os.path.join(os.path.expanduser("~"), "Documents", "OlliesAdventure")

    os.makedirs(folder, exist_ok=True)

    return os.path.join(folder, filename)

STATISTICS_FILE = get_save_path("statistics.json")




def load_statistics():
    if os.path.exists(STATISTICS_FILE):
        with open(STATISTICS_FILE, "r") as file:
            return json.load(file)

    return {
        "games_played": 0,
        "games_won": 0,
        "games_lost": 0
    }


def save_statistics(data):
    with open(STATISTICS_FILE, "w") as file:
        json.dump(data, file, indent=4)