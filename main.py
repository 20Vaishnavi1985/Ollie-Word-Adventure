import tkinter as tk


from PIL import Image, ImageTk
from tkinter import messagebox
from _pyrepl import commands
from mimetypes import guess_type
from operator import length_hint
from pydoc import text
from textwrap import fill
import pygame as pg
import random
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for PyInstaller and development."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



import os

def get_save_path(filename):
    folder = os.path.join(os.path.expanduser("~"), "Documents", "OlliesAdventure")

    os.makedirs(folder, exist_ok=True)

    return os.path.join(folder, filename)

pg.mixer.init()
from unicodedata import category

from game_logic import prepare_new_game
from game_statistics import load_statistics, save_statistics
import game_logic
#####sound effects
win_sound = pg.mixer.Sound(resource_path("sound/win_short.mp3"))
lose_sound = pg.mixer.Sound(resource_path("sound/lose.mp3"))
wrong_sound = pg.mixer.Sound(resource_path("sound/wrong_guess.mp3"))
correct_sound = pg.mixer.Sound(resource_path("sound/correct_guess.mp3"))
button_sound = pg.mixer.Sound(resource_path("sound/button.mp3"))
error_sound = pg.mixer.Sound(resource_path("sound/error.mp3"))
######colors

WINDOW_BG = "#87CEEB"      # Sky Blue
FRAME_BG = "#FFF9C4"       # Light Yellow
TEXT_COLOR = "#243B73"    # Dark Blue

GREEN_BTN = "#4CAF50"      # Play / Guess
BLUE_BTN = "#42A5F5"       # Home
ORANGE_BTN = "#FFA726"     # Restart / Play Again
RED_BTN = "#EF5350"        # Exit

ENTRY_BG = "#FFFFFF"
ENTRY_FG = "#000000"
START_BTN_COLOR_1 = "#00ADB5"
START_BTN_COLOR_2 = "#26C6DA"

###fonts
TITLE_FONT = ("Comic Sans MS", 24, "bold")
HEADING_FONT = ("Comic Sans MS", 18, "bold")
NORMAL_FONT = ("Comic Sans MS", 14, "bold")
BUTTON_FONT = ("Comic Sans MS", 14, "bold")
WORD_FONT = ("Comic Sans MS", 24, "bold")

######loading statics

statistics = load_statistics()
games_played = statistics["games_played"]
games_won = statistics["games_won"]
games_lost = statistics["games_lost"]

def update_statistics():
    data = {
        "games_played": games_played,
        "games_won": games_won,
        "games_lost": games_lost
    }

    save_statistics(data)

######hobber effect
def on_enter(event):
    event.widget.config(
        relief="raised",

    )

def on_leave(event):
    event.widget.config(
        relief="raised",

    )


score=0
#####opening best score file with file handling
def load_best_score():
    try:
        with open(get_save_path("best_score.txt")) as file:
            return int(file.read())
    except:
        return 0
best_score = load_best_score()


###window creation
win = tk.Tk()
pg.mixer.music.load(resource_path("sound/background.mp3"))
pg.mixer.music.set_volume(0.15)
pg.mixer.music.play(-1)
win.iconbitmap(resource_path("game_icon.ico"))
win.title("Ollie's Adventure")
win.geometry("800x700")
win.attributes("-alpha",1)
win.configure(bg=WINDOW_BG)

home_content = tk.Frame(
    win,
    bg="#87CEEB",
    highlightthickness=0,
    bd=0,
    padx=40,
    pady=30
)
home_content.pack( expand=True)
hero_frame = tk.Frame(
    home_content,
    bg=WINDOW_BG
)

hero_frame.pack(pady=(20, 10))


#####adding owl image
owl_image = Image.open(resource_path("Images/owl.png"))
owl_image = owl_image.resize((120, 120))
owl_photo = ImageTk.PhotoImage(owl_image)

owl2_image = Image.open(resource_path("Images/icons/owl2.png"))
owl2_image = owl2_image.resize((90, 90))
owl2_photo = ImageTk.PhotoImage(owl2_image)

owl3_image = Image.open(resource_path("Images/icons/owl3.png"))
owl3_image = owl3_image.resize((32, 32))
owl3_photo = ImageTk.PhotoImage(owl3_image)

#instruction
instruction_image = Image.open(resource_path("Images/icons/instruction.png"))
instruction_image = instruction_image.resize((50, 50))
instruction_icon = ImageTk.PhotoImage(instruction_image)
#analysis chart
analysis_image = Image.open(resource_path("Images/icons/analysis.png"))
analysis_image = analysis_image.resize((50, 50))
analysis_icon = ImageTk.PhotoImage(analysis_image)

###about image
about_image = Image.open(resource_path("Images/icons/about.png"))
about_image = about_image.resize((50, 50))
about_icon = ImageTk.PhotoImage(about_image)
##party popup
party1_image =  Image.open(resource_path("Images/icons/party_popup.png"))
party1_image = party1_image.resize((50, 50))
party1_icon = ImageTk.PhotoImage(party1_image)

difficulty1_image = Image.open(resource_path("Images/icons/game_screen icon/difficulties.png"))
difficulty1_image = difficulty1_image.resize((50, 50))
difficulty_icon1 = ImageTk.PhotoImage(difficulty1_image)


# ===========================
#  ICONS LOADING FUNCTION
# ===========================
from PIL import Image, ImageTk

def load_icon(path, size=(32, 32)):
    img = Image.open(resource_path(path)).convert("RGBA")

    bbox = img.getbbox()
    img = img.crop(bbox)

    img.thumbnail(size, Image.LANCZOS)

    canvas = Image.new("RGBA", size, (0, 0, 0, 0))

    x = (size[0] - img.width) // 2
    y = (size[1] - img.height) // 2

    canvas.paste(img, (x, y), img)

    return ImageTk.PhotoImage(canvas)


rocket_photo = load_icon("Images/icons/rocket.png")
book_photo = load_icon("Images/icons/book.png")
chart_photo = load_icon("Images/icons/chart.png")
info_photo = load_icon("Images/icons/info.png")
exit_photo = load_icon("Images/icons/exit.png")
easy_photo=load_icon("Images/icons/easy.png")
medium_photo = load_icon("Images/icons/medium.png")
hard_photo = load_icon("Images/icons/hard.png")
goal_icon=load_icon("Images/goal.png")
sparkle_icon=load_icon("Images/Sparkle.png")
star_icon=load_icon("Images/icons/star.png")
medal_icon=load_icon("Images/icons/medal.png")
##uploading game screen icon
category_icon=load_icon("Images/icons/game_screen icon/categeory.png")
difficulties_icon=load_icon("Images/icons/game_screen icon/difficulties.png")
guess_icon=load_icon("Images/icons/game_screen icon/guess.png")
home_icon=load_icon("Images/icons/game_screen icon/home.png")
lives_icon=load_icon("Images/icons/game_screen icon/lives.png")
restart_icon=load_icon("Images/icons/game_screen icon/restart.png")
word_icon=load_icon("Images/icons/game_screen icon/word.png")
play_icon=load_icon("Images/icons/game_screen icon/play.png")
wrong_icon=load_icon("Images/icons/wrong.png")
party_icon=load_icon("Images/icons/party_popup.png")
bulb_icon=load_icon("Images/icons/bulb.png")
crown_icon=load_icon("Images/icons/crown.png")
pen_icon=load_icon("Images/icons/pen.png")

###statistic icons
game_icon=load_icon("Images/icons/statistic logo/game.png")
sad_icon=load_icon("Images/icons/statistic logo/sad.png")
star1_icon=load_icon("Images/icons/statistic logo/star.png")
trophy_icon=load_icon("Images/icons/statistic logo/trophy.png")
win_rate_icon=load_icon("Images/icons/statistic logo/win_rate.png")

# ===========================
#     OWL LABEL
# ===========================
owl_label = tk.Label(
    home_content,
    image=owl_photo,
    bg=WINDOW_BG
)

owl_label.pack(
    in_=hero_frame,
    pady=(0, 10)
)


title_label = tk.Label(
    home_content,
    text=" Ollie Owl's Word Adventure",
    image=owl2_photo,
    compound="left",
    font= ("Comic Sans MS", 32, "bold"),
    bg=WINDOW_BG,
    fg = TEXT_COLOR
)
title_label.pack(
    in_=hero_frame,
    pady=(0, 5)
)

game_subtitle =tk.Label(
    home_content,
    text="Help Ollie Discover the Hidden Word!",
    image=sparkle_icon,
    compound="left",
    font=("Helvetica", 14, "bold"),
    fg=TEXT_COLOR,
    bg=WINDOW_BG
)
game_subtitle.pack(
    in_=hero_frame,
    pady=(0, 20)
)

# ===========================
#     EXIT FUNCTION
# ===========================
def exit_game():
    button_sound.play()
    win.destroy()


selected_difficulty=None
# ===========================
#  GLOWING BUTTON ANIMATION
# ===========================
glow_state = True
def animate_start_button():
    global glow_state

    if glow_state:
        start_btn.config(bg=START_BTN_COLOR_2)
    else:
        start_btn.config(bg=START_BTN_COLOR_1)

    glow_state = not glow_state

    win.after(1200, animate_start_button)



# ===========================
# SELECT DIFFICULTIES FUNCTION
# ===========================
def select_difficulty(level):
    button_sound.play(),
    global selected_difficulty
    selected_difficulty = level

# ===========================
# START FUNCTION CALLING FUNCTION
# ===========================

def start_button_clicked():
    if selected_difficulty is None:
        error_sound.play()
        messagebox.showwarning(
            "Difficulty Required",
            "Please select a difficulty first."
        )

    else:
        start_game(selected_difficulty)


# ===============================
#  MAIN GAME LOGIC
# ===============================
def start_game(difficulty):
    button_sound.play()
    global category
    global secret_word
    global display_list
    global chances
    global guessed_letters
    global max_chances
    global score
    score=0

    category, secret_word, display_list, chances, guessed_letters = prepare_new_game(difficulty)

    max_chances=chances
    category_label.config(text=f" Category: {category}")
    chance_level.config(text=f" Chances: {chances}")
    word_level.config(text=" ".join(display_list))
    difficulty_label.config(text=f" Difficulty: {difficulty}")
    score_label.config(text=f" score: {score}")

    home_content.pack_forget()
    game_frame.pack(fill="both", expand=True)
    draw_hangman_stage(0)
    win.update_idletasks()


# ===============================
#  CORRECT GUESS FLASH ANIMATION
# ===============================
def flash_correct():
    word_level.config(fg="#2ECC71")   # Bright Green

    win.after(
        250,
        lambda: word_level.config(fg=TEXT_COLOR)
    )

# ===============================
#  WRONG GUESS FLASH ANIMATION
# ===============================
def flash_wrong():
    word_level.config(fg="#E53935" )   # Bright Green

    win.after(
        300,
        lambda: word_level.config(fg=TEXT_COLOR)
    )

# ===============================
#  SHOW STATISTIC FUNCTION
# ===============================
def show_statistics():
    button_sound.play()

    if games_played == 0:
        win_rate = 0
    else:
        win_rate = round((games_won / games_played) * 100)

    games_played_label.config(
        text=f" Games Played : {games_played}"
    )

    games_won_label.config(
        text=f"Games Won : {games_won}"
    )

    games_lost_label.config(
        text=f" Games Lost : {games_lost}"
    )

    win_rate_label.config(
        text=f"Win Rate : {win_rate}%"
    )

    highest_score_label.config(
        text=f" Highest Score : {best_score}"
    )

    home_content.pack_forget()
    game_frame.pack_forget()

    statistics_frame.pack(fill="both", expand=True)

###-------------------###
     #process game
###-------------------###
def process_game():
    button_sound.play(),
    global chances
    global score


    player_guess = guess_entry.get()
    upper_guess = player_guess.upper()

    if len(upper_guess) != 1 or not upper_guess.isalpha():
        error_sound.play()
        messagebox.showinfo("Hey....","please Enter one letter at a time ")
        guess_entry.delete(0, tk.END)
        guess_entry.focus_set()
        return


    if upper_guess in guessed_letters:
        error_sound.play()
        messagebox.showinfo("oh ho..","you already guessed this letter")
        guess_entry.delete(0, tk.END)
        guess_entry.focus_set()
        return

    guessed_letters.append(upper_guess)


    found = False

    for index, letter in enumerate(secret_word.upper()):
        if letter == upper_guess:
            display_list[index] = upper_guess
            correct_sound.play()
            flash_correct()
            show_encouragement()
            score += 10
            score_label.config(text=f"  score: {score}")
            found = True
        word_level.config(text=" ".join(display_list))
    if "_" not in display_list:
        player_won()

    if not found:
        wrong_sound.play()
        flash_wrong()
        chances -= 1

        chance_level.config(text=f"Chances: {chances}")



        wrong_guesses = max_chances - chances

        if max_chances == 8:
            stage = wrong_guesses

        elif max_chances == 6:
            stage = round((wrong_guesses / 6) * 8)

        elif max_chances == 4:
            stage = round((wrong_guesses / 4) * 8)

        draw_hangman_stage(stage)

    if chances == 0:
        player_lost()
    guess_entry.delete(0, tk.END)
    guess_entry.focus_set()
    guess_entry.selection_range(0, tk.END)
    guess_entry.icursor(tk.END)


# ===============================
#  WINNING FUNCTION
# ===============================

def player_won():
        global score
        global best_score
        ###statistics
        global games_played
        global games_won

        games_played += 1
        games_won += 1

        update_statistics()
        win_sound.play()
        guess_btn.config(state="disabled")
        guess_entry.config(state="disabled")
        word_result_label.config(
            text=f" The Hidden Word\n{secret_word.upper()}"
        )
        score_result_label.config(
            text=f" Score : {score}"
        )

        best_result_label.config(
            text=f" Best Score : {best_score}"
        )

        category_result_label.config(
            text=f" Category : {category}"
        )

        difficulty_result_label.config(
            text=f"Difficulty : {difficulty_label.cget('text').replace(' Difficulty: ', '')}"
        )

        win_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=500,
            height=700
        )
        score += 50
        score_label.config(text=f" Score : {score}")


        if score > best_score:
            best_score = score

            best_score_label.config(
                text=f" Best : {best_score}"
            )

            save_best_score()

            best_result_label.config(
                text=f" NEW HIGH SCORE : {best_score}",
                fg="#00C853"
            )
        ###clear entry box
        guess_entry.delete(0, tk.END)

        # Enable controls again
        guess_btn.config(state="normal")
        guess_entry.config(state="normal")

        win_frame.lift()


# ===============================
#  LOSSING FUNCTION
# ===============================

def player_lost():
    global games_played
    global games_lost

    games_played += 1
    games_lost += 1

    update_statistics()
    lose_sound.play()
    guess_btn.config(state="disabled")
    guess_entry.config(state="disabled")


    word_result_label2.config(
        text=f"The Hidden Word\n{secret_word.upper()}"
    )
    score_result_label2.config(
        text=f" Score : {score}"
    )

    best_result_label2.config(
        text=f" Best Score : {best_score}"
    )

    category_result_label2.config(
        text=f" Category : {category}"
    )

    difficulty_result_label2.config(
        text=f" Difficulty : {difficulty_label.cget('text').replace('🎯 Difficulty: ', '')}"
    )
    lose_frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center",
        width=500,
        height=700
    )
    ###clear entry box
    guess_entry.delete(0, tk.END)

    # Enable controls again
    guess_btn.config(state="normal")
    guess_entry.config(state="normal")

    lose_frame.lift()



# ===============================
# RESTART GAME FUNCTION
# ===============================
def restart_game():
    win_sound.stop()
    lose_sound.stop()
    button_sound.play()
    win_frame.place_forget()
    lose_frame.place_forget()
    global category
    global secret_word
    global display_list
    global chances
    global guessed_letters

    # Create a fresh game using current difficulty
    category, secret_word, display_list, chances, guessed_letters = prepare_new_game(selected_difficulty)

    # Update labels
    category_label.config(text=f" Category: {category}")
    difficulty_label.config(text=f" Difficulty: {selected_difficulty}")
    chance_level.config(text=f" Chances: {chances}")
    word_level.config(text=" ".join(display_list))

    # Clear entry box
    guess_entry.delete(0, tk.END)

    # Enable controls again
    guess_btn.config(state="normal")
    guess_entry.config(state="normal")
    draw_hangman_stage(0)



def play_again():
    button_sound.play()
    win_frame.place_forget()
    lose_frame.place_forget()
    restart_game()


#####saving best score function
def save_best_score():
    with open(get_save_path("best_score.txt"), "w") as file:
        file.write(str(best_score))

####show about function
def show_about():

    button_sound.play()

    home_content.pack_forget()
    game_frame.pack_forget()
    instructions_frame.pack_forget()
    statistics_frame.pack_forget()
    win_frame.place_forget()
    lose_frame.place_forget()

    about_frame.pack(fill="both", expand=True)



# Difficulty Title
difficulty_label = tk.Label(
    home_content,
    text="Choose Your Challenge",
    image=goal_icon,
    compound="left",
    font=HEADING_FONT,
    bg=WINDOW_BG,
    fg =TEXT_COLOR

)
difficulty_label.pack(pady=(10, 10))


# Frame to hold difficulty buttons
difficulty_frame = tk.Frame(
    home_content,
    bg=WINDOW_BG
)
difficulty_frame.pack()


# Easy Button
easy_btn = tk.Button(
    difficulty_frame,
    text="Easy",
    image=easy_photo,
    compound="left",
    padx=45,
    pady=1,
    font=BUTTON_FONT,
    bg="#6FCF70",  # Light Green
    fg = "white",
    activebackground = "#81E784",
    activeforeground="white",
    relief="raised",
    bd=4,
    cursor="hand2",
    command=lambda: select_difficulty("Easy")

)
easy_btn.grid(row=0, column=0, padx=15)
easy_btn.bind("<Enter>", on_enter)
easy_btn.bind("<Leave>", on_leave)


# Medium Button
medium_btn = tk.Button(
    difficulty_frame,
    text=" Medium",
    image=medium_photo,
    compound="left",
    padx=43,
    pady=1,
    font=BUTTON_FONT,
    bg="#F9A825",# Orange
    fg = "white",
    activebackground = "#FFCA28" ,
    activeforeground="white",
    relief="raised",
    bd=4,
    cursor="hand2",
    command=lambda: select_difficulty("Medium")
)
medium_btn.grid(row=0, column=1, padx=15)
medium_btn.bind("<Enter>", on_enter)
medium_btn.bind("<Leave>", on_leave)


# Hard Button
hard_btn = tk.Button(
    difficulty_frame,
    text=" Hard",
    image=hard_photo,
    compound="left",
    padx=43,
    pady=1,
    font=BUTTON_FONT,
    bg="#E53935",# Red
    fg="white",
    activebackground = "#EF5350"      ,
    activeforeground="white",
    relief="raised",
    bd=4,
    cursor="hand2",
    command=lambda: select_difficulty("Hard")
)
hard_btn.grid(row=0, column=2, padx=15)
hard_btn.bind("<Leave>", on_leave)
hard_btn.bind("<Enter>", on_enter)


def show_instructions():
    button_sound.play(),
    home_content.pack_forget()
    # start_btn.pack_forget()
    # instruction_btn.pack_forget()
    # Exit_btn.pack_forget()
    instructions_frame.pack(fill="both", expand=True)

# making a button
start_btn=tk.Button(
    home_content,
    text=" Start Adventure",
    image=rocket_photo,
    compound="left",
    font=("Comic Sans MS", 16, "bold"),
    bg=START_BTN_COLOR_1,
    fg="white",

    activebackground=START_BTN_COLOR_2,
    activeforeground="white",

    relief="raised",
    bd=4,

    padx=25,
    pady=4,

    cursor="hand2",
    command=start_button_clicked
)
start_btn.pack( pady=6)
start_btn.bind("<Enter>", on_enter)
start_btn.bind("<Leave>", on_leave)

#### bottom frame to store 4 buttons
bottom_menu_frame = tk.Frame(
    home_content,
    bg=WINDOW_BG
)

bottom_menu_frame.pack(pady=20)

instruction_btn=tk.Button(
    text=" How to Play",
    image=book_photo,
    compound="left",
    bg="#42A5F5",
    fg = "white",
    font = BUTTON_FONT,
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    padx=12,
    pady=5,
    cursor="hand2",
    command=show_instructions
)
instruction_btn.grid(
    in_=bottom_menu_frame,
    row=0,
    column=0,
    padx=10,
    pady=8
)
instruction_btn.bind("<Enter>", on_enter)
instruction_btn.bind("<Leave>", on_leave)
statistics_btn = tk.Button(
    home_content,
    text="Statistics",
    image=chart_photo,
    compound="left",
    padx=25,
    pady=5,
    font=BUTTON_FONT,
    bg=GREEN_BTN,
    fg="white",
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    command=show_statistics
)

statistics_btn.grid(
    in_=bottom_menu_frame,
    row=0,
    column=1,
    padx=14,
    pady=12
)

statistics_btn.bind("<Enter>", on_enter)
statistics_btn.bind("<Leave>", on_leave)
about_btn = tk.Button(
    home_content,
    text=" About",
    image=info_photo,
    compound="left",
    font=BUTTON_FONT,
    bg="#7E57C2",
    fg="white",
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    padx=30,
    pady=5,
    cursor="hand2",
    command=show_about
)

about_btn.grid(
    in_=bottom_menu_frame,
    row=1,
    column=0,
    padx=10,
    pady=8
)

about_btn.bind("<Enter>", on_enter)
about_btn.bind("<Leave>", on_leave)

Exit_btn=tk.Button(
    home_content,
    text=" Exit",
    image=exit_photo,
    compound="left",
    font=BUTTON_FONT,
    bg=RED_BTN,
    fg = "white",
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    padx=38,
    pady=5,
    cursor="hand2",
    command=exit_game
)
Exit_btn.grid(
    in_=bottom_menu_frame,
    row=1,
    column=1,
    padx=10,
    pady=8
)
Exit_btn.bind("<Enter>", on_enter)
Exit_btn.bind("<Leave>", on_leave)

animate_start_button()


#####show home function
def show_home():
    win_sound.stop()
    lose_sound.stop()
    button_sound.play()
    win_frame.place_forget()
    lose_frame.place_forget()
    instructions_frame.pack_forget()
    statistics_frame.pack_forget()
    game_frame.pack_forget()
    about_frame.pack_forget()

    home_content.pack(fill="both", expand=True)




#### instruction frame
instructions_frame = tk.Frame(
    bg=FRAME_BG,

)
instruction_title = tk.Label(
    instructions_frame,
    bg=FRAME_BG,
    text="Instructions",
    image=instruction_icon,
    compound="left",
    font=("Comic Sans MS", 28, "bold"),
    fg=TEXT_COLOR
)
instruction_title.pack(fill="both", expand=True)
instruction_card = tk.Frame(
    instructions_frame,
    bg="white",
    padx=30,
    pady=25,
    highlightbackground="#1A237E",
    highlightthickness=3
)

instruction_card.pack(pady=20)
instruction1 = tk.Label(
    instruction_card,
    text="Guess one letter at a time.",
    image=difficulties_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
    justify="left"
)

instruction1.pack(fill="x", pady=5)
instruction2 = tk.Label(
    instruction_card,
    text="You have chances Acoording to Difficulties   to save Ollie.",
    image=lives_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
    justify="left"
)
instruction2.pack(fill="x", pady=5)
instruction3 = tk.Label(
    instruction_card,
    text="Easy=8,Medium=6,Hard=4.",
    image=difficulties_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
    justify="left"
)
instruction3.pack(fill="x", pady=5)

instruction4 = tk.Label(
    instruction_card,
    text=" Every wrong guess draws part of the hangman.",
    image=wrong_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
    justify="left"
)
instruction4.pack(fill="x", pady=5)

instruction5 = tk.Label(
    instruction_card,
    text="Guess the whole word before Ollie gets stuck!",
    image=owl3_photo,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
    justify="left"
)
instruction5.pack(fill="x", pady=5)

instruction6 = tk.Label(
    instruction_card,
    text="Earn 50 points for every correct word.",
    image=star_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
    justify="left"
)
instruction6.pack(fill="x", pady=5)

instruction7 = tk.Label(
    instruction_card,
    text=" Beat your Best Score by winning more games.",
    image=medal_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
    justify="left"
)
instruction7.pack(fill="x", pady=5)

instruction8 = tk.Label(
    instruction_card,
    text=" Have fun while learning new words!",
    image=party_icon,
    compound="left",
    font=("Comic Sans MS", 14, "bold"),
    fg="#2E7D32",
    bg="white",
    anchor="w",
    justify="left"
)
instruction8.pack(fill="x", pady=(10,5))
back_btn=tk.Button(
    instructions_frame,
    text=" Back",
    image=home_icon,
    compound="left",
    font=("Helvetica", 14, "bold"),
    bg="#00ADB5",
    fg="white",
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    padx=20,
    pady=10,
    cursor="hand2",
    borderwidth=2,
    command=show_home

)
back_btn.pack(pady=20)
back_btn.bind("<Enter>", on_enter)
back_btn.bind("<Leave>", on_leave)

#####main game frame
game_frame=tk.Frame(
    bg=FRAME_BG,



)
center_frame=tk.Frame(
    game_frame,
    bg=FRAME_BG,
)
center_frame.pack()
game_upper_frame=tk.Frame(
    center_frame,
    bg=FRAME_BG,
)
game_upper_frame.pack()
####upper frame right frame
right_panel = tk.Frame(
    game_upper_frame,
    bg=FRAME_BG
)

right_panel.pack(side="right", padx=30)

game_title = tk.Label(
    game_upper_frame,
    text="Ollie's Adventure",
    image=owl2_photo,
    compound="left",
    font= ("Comic Sans MS", 32, "bold"),
    bg=FRAME_BG,
    fg = TEXT_COLOR
)
game_title.pack(pady=(10,5))
game_subtitle =tk.Label(
    game_upper_frame,
    text="Guess the word before Ollie gets stuck!",
    image=sparkle_icon,
    compound="left",
    font=("Helvetica", 14, "bold"),
    fg=TEXT_COLOR,
    bg=FRAME_BG
)
game_subtitle.pack(pady=(0,10))

game_middle_frame=tk.Frame(
    game_frame,
    bg=FRAME_BG,
)
game_middle_frame.pack(fill="x", pady=10)

left_side = tk.Frame(game_middle_frame, bg=FRAME_BG)

left_side.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(30, 20)
)
right_side =tk.Frame(game_middle_frame, bg=FRAME_BG)
right_side.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(20, 30)
)



game_bottom_frame=tk.Frame(
    game_frame,
    bg=FRAME_BG
)

game_bottom_frame.pack(fill="x", pady=(5, 10))

info_frame=tk.Frame(
   game_upper_frame,
    bg=FRAME_BG,
    borderwidth=2,
    padx=20,
    pady=10,
    cursor="hand2",
)

info_frame.pack(
    side="left",
    padx=40,
    anchor="n"
)


hangman_frame = tk.Frame(
    right_panel,
    bg="white",
    padx=15,
    pady=15,
    highlightbackground="#1A237E",
    highlightthickness=2,
    relief="ridge",
    bd=2
)
hangman_frame.pack()
encouragement_frame = tk.Frame(
    right_panel,
    bg=FRAME_BG
)

encouragement_frame.pack(pady=(10,0))


action_frame = tk.Frame(
    game_bottom_frame,
    bg=FRAME_BG,
    padx=20,
    pady=2,
)
action_frame.pack()
#levels start here
difficulty_label=tk.Label(
    info_frame,
    text="Difficulty:",
    image=difficulties_icon,
    compound="left",
    bg=FRAME_BG,
    fg = TEXT_COLOR,
    font=HEADING_FONT,
    pady=20,
    justify="left",
    cursor="hand2",
    borderwidth=2,

)
difficulty_label.pack(fill="x")
chance_level=tk.Label(
    info_frame,
    text="Chance Left:6",
    image=lives_icon,
    compound="left",
    bg=FRAME_BG,
    fg = TEXT_COLOR,
    font=HEADING_FONT,
    padx=20,
    justify="left",
    cursor="hand2",
    borderwidth=2,
)
chance_level.pack(fill="x")
word_level=tk.Label(
    info_frame,
    text="__________",
    image=word_icon,
    compound="left",
    bg=FRAME_BG,
    fg = TEXT_COLOR,
    font=HEADING_FONT,
    pady=20,
    cursor="hand2",
    borderwidth=2,
    justify="center",

)
word_level.pack(fill="x")
category_label = tk.Label(
    info_frame,
    text="Category:",
    image=category_icon,
    compound="left",
    bg=FRAME_BG,
    fg = TEXT_COLOR,
    font=HEADING_FONT,
    pady=20,
    cursor="hand2",
    borderwidth=2,
    justify="left"

)

category_label.pack(fill="x")


guess_level=tk.Label(
    left_side,
    text="Guess a Letter",
    image=guess_icon,
    compound="left",
    bg=FRAME_BG,
    fg = TEXT_COLOR,
    font=NORMAL_FONT,
    pady=20,
    cursor="hand2",
    borderwidth=2,

)
guess_level.pack()
input_frame = tk.Frame(
    left_side,
    bg=FRAME_BG,
    borderwidth=2,
    padx=20,
    pady=10,
)
input_frame.pack(pady=10)
guess_entry = tk.Entry(
    input_frame,
    width=5,
    bg=ENTRY_BG,
    fg=ENTRY_FG,
    font=("Arial", 16),
    justify="center"

)
guess_entry.pack(side="left", padx=10)
guess_entry.bind("<Return>", lambda event: guess_btn.invoke())


guess_btn = tk.Button(
    input_frame,
    text="✅ Guess",
    width=10,
    font=BUTTON_FONT,
    bg=GREEN_BTN,
    fg = "white",
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    command=process_game
)
guess_btn.pack(side="left")
guess_btn.bind("<Enter>", on_enter)
guess_btn.bind("<Leave>", on_leave)



restart_btn = tk.Button(
    action_frame,
    text="Restart",
    image=restart_icon,
    compound="left",
    padx=20,
    pady=10,
    font=BUTTON_FONT,
    bg=ORANGE_BTN,
    fg = "white",
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    command=restart_game

)

restart_btn.pack(side="left", padx=20)
restart_btn.bind("<Leave>", on_leave)
restart_btn.bind("<Enter>", on_enter)

home_btn = tk.Button(
    action_frame,
    text=" Home",
    image=home_icon,
    compound="left",
    padx=20,
    pady=10,
    font=BUTTON_FONT,
    bg=BLUE_BTN,
    fg = "white",
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    command=show_home

)

home_btn.pack(side="left", padx=20)
home_btn.bind("<Enter>", on_enter)
home_btn.bind("<Leave>", on_leave)


#####makin GUI professional


win_frame = tk.Frame(
    game_frame,
    bg=FRAME_BG,
    bd=3,
    relief="ridge"
)
trophy_image =  Image.open(resource_path("Images/trophy.png"))
trophy_image = trophy_image.resize((120,120))
trophy_photo = ImageTk.PhotoImage(trophy_image)
trophy_label = tk.Label(
    win_frame,
    image=trophy_photo,
    bg=FRAME_BG
)
trophy_label.pack(pady=(20,10))
celebration_frame = tk.Frame(
    win_frame,
    bg=FRAME_BG
)

celebration_frame.pack(pady=10)
left_party = tk.Label(
    celebration_frame,
    image=party1_icon,
    bg=FRAME_BG
)
left_party.pack(side="left", padx=10)

title = tk.Label(
    celebration_frame,
    text="Congratulations!\nYou Saved Ollie!",
    font=("Helvetica", 20, "bold"),
    bg=FRAME_BG,
    fg=TEXT_COLOR
)
title.pack(side="left", padx=10)

right_party = tk.Label(
    celebration_frame,
    image=party1_icon,
    bg=FRAME_BG
)
right_party.pack(side="left", padx=10)

ollie_message = tk.Label(
    win_frame,
    text=" Ollie's Champion!",
    image=crown_icon,
    compound="left",
    # fg="#FFD700",
    font=("Comic Sans MS", 18, "bold"),
    bg=FRAME_BG,
    fg="#2E7D32"
)

ollie_message.pack(pady=(5,10))


word_result_label = tk.Label(
    win_frame,
    text="",
    image=difficulty_icon1,
    compound="left",
    font=("Comic Sans MS", 24, "bold"),
    bg=FRAME_BG,
    fg="#1A237E"
)
word_result_label.pack(pady=10)

score_result_label = tk.Label(
    win_frame,
    text="",
    image=star_icon,
    compound="left",
    font=("Comic Sans MS", 14, "bold"),
    bg=FRAME_BG,
    fg="#F57C00"
)
score_result_label.pack(pady=2)

best_result_label = tk.Label(
    win_frame,
    text="",
    image=medal_icon,
    compound="left",
    font=("Comic Sans MS", 14, "bold"),
    bg=FRAME_BG,
    fg="#FFD700"
)
best_result_label.pack(pady=2)

category_result_label = tk.Label(
    win_frame,
    text="",
    image=category_icon,
    compound="left",
    font=("Comic Sans MS", 14, "bold"),
    bg=FRAME_BG,
    fg=TEXT_COLOR
)
category_result_label.pack(pady=2)

difficulty_result_label = tk.Label(
    win_frame,
    text="",
    image=difficulties_icon,
    compound="left",
    font=("Comic Sans MS", 14, "bold"),
    bg=FRAME_BG,
    fg=TEXT_COLOR
)
difficulty_result_label.pack(pady=(2,10))

button_frame = tk.Frame(
    win_frame,
    bg=FRAME_BG
)
button_frame.pack(pady=20)

play_again_button = tk.Button(
    button_frame,
    text="Play Again",
    image=play_icon,
    compound="left",
    font=BUTTON_FONT,
    bg=GREEN_BTN,
    fg = "white",
    padx=15,
    pady=2,
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    command=play_again
)
play_again_button.grid(row=0,column=0,padx=10)
play_again_button.bind("<Enter>", on_enter)
play_again_button.bind("<Leave>", on_leave)


home_button = tk.Button(
    button_frame,
    text=" Home",
    image=home_icon,
    compound="left",
    font=BUTTON_FONT,
    bg=BLUE_BTN,
    fg = "white",
    padx=28,
    pady=2,
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    command=show_home,

)
home_button.grid(row=0,column=1,padx=10)
home_button.bind("<Enter>", on_enter)
home_button.bind("<Leave>", on_leave)


#####lose frame
lose_frame = tk.Frame(
    game_frame,
    bg=FRAME_BG,
    bd=3,
    relief="ridge"
)
sad_image = Image.open(resource_path("Images/sad_image.png"))
sad_image = sad_image.resize((120, 120))
sad_photo = ImageTk.PhotoImage(sad_image)
sad_label = tk.Label(
    lose_frame,
    image=sad_photo,
    bg=FRAME_BG,
)
sad_label.pack(pady=(20,10))

lose_lavel = tk.Label(
    lose_frame,
    text="Better Luck Next Time!",
    image=sad_icon,
    compound="left",
    font=("Comic Sans MS",18,"bold"),
    bg=FRAME_BG,
    fg = "#D32F2F"
)
lose_lavel.pack(pady=5)
ollie_message2 = tk.Label(
    lose_frame,
    text=" Ollie Got Stuck...",
    image=owl3_photo,
    compound="left",
    font=("Comic Sans MS", 18, "bold"),
    bg=FRAME_BG,
    fg="#2E7D32"
)

ollie_message2.pack(pady=(5,10))

word_result_label2 = tk.Label(
    lose_frame,
    text="",
    image=difficulty_icon1,
    compound="left",
    font=("Helvetica",16,"bold"),
    bg=FRAME_BG,
    fg = TEXT_COLOR
)
word_result_label2.pack(pady=10)
score_result_label2 = tk.Label(
    lose_frame,
    text="",
    image=star1_icon,
    compound="left",
    font=("Comic Sans MS", 14, "bold"),
    bg=FRAME_BG,
    fg="#F57C00"
)
score_result_label2.pack(pady=2)

best_result_label2 = tk.Label(
    lose_frame,
    text="",
    image=medal_icon,
    compound="left",
    font=("Comic Sans MS", 14, "bold"),
    bg=FRAME_BG,
    fg="#FFD700"
)
best_result_label2.pack(pady=2)

category_result_label2 = tk.Label(
    lose_frame,
    text="",
    image=category_icon,
    compound="left",
    font=("Comic Sans MS", 14, "bold"),
    bg=FRAME_BG,
    fg=TEXT_COLOR
)
category_result_label2.pack(pady=2)

difficulty_result_label2 = tk.Label(
    lose_frame,
    text="",
    image=difficulties_icon,
    compound="left",
    font=("Comic Sans MS", 14, "bold"),
    bg=FRAME_BG,
    fg=TEXT_COLOR
)
difficulty_result_label2.pack(pady=(2,10))
try_again_label = tk.Label(
    lose_frame,
    text="Every mistake is a chance to learn!",
    image=bulb_icon,
    compound="left",
    font=("Comic Sans MS", 14, "bold"),
    bg=FRAME_BG,
    fg="#2E7D32"
)

try_again_label.pack(pady=(10,15))

button_frame = tk.Frame(
    lose_frame,
    bg=FRAME_BG
)
button_frame.pack(pady=20)

play_again_button = tk.Button(
    button_frame,
    text="Try Again",
    image=play_icon,
    compound="left",
    font=BUTTON_FONT,
    bg=GREEN_BTN,
    fg = "white",
    padx=20,
    pady=5,
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    command=play_again
)
play_again_button.grid(row=0,column=0,padx=10)
play_again_button.bind("<Enter>", on_enter)
play_again_button.bind("<Leave>", on_leave)

home_button = tk.Button(
    button_frame,
    text="Home",
    image=home_icon,
    compound="left",
    font=BUTTON_FONT,
    bg=BLUE_BTN,
    fg = "white",
    padx=35,
    pady=5,
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    command=show_home
)
home_button.grid(row=0,column=1,padx=10)
home_button.bind("<Enter>", on_enter)
home_button.bind("<Leave>", on_leave)


statistics_frame = tk.Frame(
    bg=FRAME_BG
)
statistics_frame.pack(fill="both", expand=True)
statistics_frame.pack_forget()
###stastics label
statistics_title = tk.Label(
    statistics_frame,
    text=" Game Statistics",
    image=analysis_icon,
    compound="left",
    font=("Comic Sans MS", 28, "bold"),
    bg=FRAME_BG,
    fg=TEXT_COLOR
)

statistics_title.pack(pady=(30,20))
statistics_card = tk.Frame(
    statistics_frame,
    bg="white",
    padx=30,
    pady=25,
    highlightbackground="#1A237E",
    highlightthickness=3
)


statistics_card.pack(pady=20)
statistics_box = tk.Frame(
    statistics_frame,
    bg="white",
    padx=30,
    pady=25,
    highlightbackground="#1A237E",
    highlightthickness=3
)

statistics_box.pack(pady=20)
games_played_label = tk.Label(
    statistics_box,
    text="",
    image=game_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
)
games_played_label.pack(anchor="w", pady=5)

games_won_label = tk.Label(
    statistics_box,
    text="",
    image=trophy_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
)
games_won_label.pack(anchor="w", pady=5)

games_lost_label = tk.Label(
    statistics_box,
    text="",
    image=sad_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
)
games_lost_label.pack(anchor="w", pady=5)

win_rate_label = tk.Label(
    statistics_box,
    text="",
    image=win_rate_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
)
win_rate_label.pack(anchor="w", pady=5)

highest_score_label = tk.Label(
    statistics_box,
    text="",
    image=star1_icon,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    anchor="w",
)
highest_score_label.pack(anchor="w", pady=5)

statistics_home_btn = tk.Button(
    statistics_frame,
    text="Home",
    image=home_icon,
    compound="left",
    padx=20,
    pady=5,
    font=BUTTON_FONT,
    bg=BLUE_BTN,
    fg="white",
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    command=show_home

)

statistics_home_btn.pack(pady=20)

statistics_home_btn.bind("<Enter>", on_enter)
statistics_home_btn.bind("<Leave>", on_leave)
#####hangman title lavel
hangman_title = tk.Label(
    hangman_frame,
    text=" Hangman",
    image=pen_icon,
    compound="left",
    font=("Comic Sans MS", 16, "bold"),
    bg="white",
    fg=TEXT_COLOR
)
hangman_title.pack(pady=(0, 10))

#####making the canvas
canvas = tk.Canvas(
    hangman_frame,
    width=250,
    height=300,
    bg="#2A2A2A",
    highlightbackground="white",
    highlightthickness=2
)
canvas.pack()

def draw_hangman_stage(stage):
    canvas.delete("all")
    if stage >= 1:
        canvas.create_line(
            40, 280,
            180, 280,
            fill="white",
            width=4
        )
    if stage >=1:
        canvas.create_line(
            80, 280,
            80, 40,
            fill="white",
            width=4
        )
    if stage >= 2:
        canvas.create_line(
            80, 40,
            170, 40,
            fill="white",
            width=4
        )
    if stage >= 2:
        canvas.create_line(
            170, 40,
            170, 80,
            fill="white",
            width=4
        )
    if stage >= 3:
        canvas.create_oval(
            150, 80,
            190, 120,
            outline="white",
            width=4
        )
    if stage >= 4:
        canvas.create_line(
            170, 120,
            170, 190,
            fill="white",
            width=4
        )
    if stage >= 5:
        canvas.create_line(
            170, 140,
            145, 165,
            fill="white",
            width=4
        )
    if stage >= 6:
        canvas.create_line(
            170, 140,
            195, 165,
            fill="white",
            width=4
        )
    if stage >= 7:
        canvas.create_line(
            170, 190,
            145, 225,
            fill="white",
            width=4
        )
    if stage >= 8:
        canvas.create_line(
            170, 190,
            195, 225,
            fill="white",
            width=4
        )
# draw_hangman_stage(2)

######showing encourasing message

encourage_label = tk.Label(
    encouragement_frame,
    text="",
    font=("Comic Sans MS", 16, "bold"),
    bg=FRAME_BG,
    fg="#4CAF50"
)

encourage_label.pack(pady=10)
encouragements = [
    "🌟 Great Job!",
    "🎉 Awesome!",
    "👏 Nice Guess!",
    "😊 Keep Going!",
    "🦉 Ollie is Happy!",
    "⭐ Excellent!"
]
def show_encouragement():
    message = random.choice(encouragements)

    encourage_label.config(text=message)

    win.after(
        1000,
        lambda: encourage_label.config(text="")
    )
### score system
score_label = tk.Label(
    info_frame,
    text=" Score : 0",
    image=star_icon,
    compound="left",
    font=("Comic Sans MS", 16, "bold"),
    bg=FRAME_BG,
    fg="#FF9800",
    anchor="w"
)

score_label.pack(pady=5)
best_score_label = tk.Label(
    info_frame,
    text=f" Best : {best_score}",
    image=medal_icon,
    compound="left",
    font=("Comic Sans MS", 16, "bold"),
    bg=FRAME_BG,
    fg="#C97A00",
    anchor="w"
)

best_score_label.pack()
####about game screen
about_frame = tk.Frame(
    win,
    bg=FRAME_BG
)
about_title = tk.Label(
    about_frame,
    text=" About",
    image=about_icon,
    compound="left",
    font=("Comic Sans MS", 28, "bold"),
    bg=FRAME_BG,
    fg=TEXT_COLOR
)

about_title.pack(pady=(30,20))
about_card = tk.Frame(
    about_frame,
    bg="white",
    padx=35,
    pady=25,
    highlightbackground="#1A237E",
    highlightthickness=3
)

about_card.pack(pady=20)
about_info = tk.Label(
    about_card,
    text=(
        "Ollie's Adventure\n\n"
        "Version 1.0\n\n"
        "A fun educational Hangman game\n"
        "designed to improve English vocabulary.\n\n"
        "🛠 Built with:\n"
        "Python\n"
        "Tkinter\n"
        "Pygame"
    ),
    image=owl3_photo,
    compound="left",
    font=("Comic Sans MS", 14),
    bg="white",
    justify="center"
)

about_info.pack()
developer_label = tk.Label(
    about_card,
    text=(
        "\n👨‍💻 Developed by:\n"
        "Vaishnavi Dixit\n\n"
        "🎓Btech Student\n"
        "Passionate Python Developer"
    ),
    font=("Comic Sans MS", 13, "bold"),
    bg="white",
    fg="#1A237E",
    justify="center"
)

developer_label.pack(pady=(10,5))
copyright_label = tk.Label(
    about_card,
    text="© 2026 Ollie's Adventure\nAll Rights Reserved",
    font=("Helvetica", 11),
    bg="white",
    fg="gray"
)

copyright_label.pack(pady=(10,5))
about_home_btn = tk.Button(
    about_frame,
    text="Home",
    image=home_icon,
    compound="left",
    padx=20,
    pady=20,
    font=BUTTON_FONT,
    bg=BLUE_BTN,
    fg="white",
    activebackground="#00A8AF",
    activeforeground="white",
    relief="raised",
    bd=4,
    command=show_home
)

about_home_btn.pack(pady=20)

about_home_btn.bind("<Enter>", on_enter)
about_home_btn.bind("<Leave>", on_leave)








win.mainloop()