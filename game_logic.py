import csv
import random
import os
import sys
def resource_path(relative_path):
    """Get absolute path to resource."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

from unicodedata import category


def prepare_new_game(difficulty):
    difficulty_mapping = {
        "Easy": "Easy_words.csv",
        "Medium": "Medium_words.csv",
        "Hard": "Hard_words.csv"
    }

    csv_file = resource_path(difficulty_mapping[difficulty])
    rows = []

    with open(csv_file, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            rows.append(row)


    selected_row=random.choice(rows)


    category=selected_row[0]
    possible_words=selected_row[1:]


    secret_word = random.choice(possible_words)


    display_list=['_']*len(secret_word)


    Chances={'Easy':8,'Medium':6,'Hard':4}
    chances = Chances[difficulty]

    guessed_letters = []


    return category, secret_word, display_list,chances, guessed_letters
