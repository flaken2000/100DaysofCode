from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "arial"
random_entry = ""

# ---------------------------- RANDOM WORD ------------------------------- #


def rand_word():
    global random_entry
    random_entry = random.choice(word_list)

    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfigure(word_text, text=random_entry["French"], fill="black")
    canvas.itemconfigure(title_text, text="French", fill="black")
    window.after(3000, flip_card, random_entry)

# ---------------------------- FLIP CARD ------------------------------- #


def flip_card(random_entry):
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfigure(word_text, text=random_entry["English"], fill="white")
    canvas.itemconfigure(title_text, text="English", fill="white")


# ---------------------------- WRONG BUTTON ------------------------------- #
def dunno():
    rand_word()


# ---------------------------- RIGHT BUTTON ------------------------------- #
def right():
    global random_entry
    word_list.remove(random_entry)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    rand_word()


# ---------------------------- GET WORDS ------------------------------- #

try:
    # Looking to see if words_to_learn.csv exists
    DataFrame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    DataFrame = pandas.read_csv("data/french_words.csv")
finally:
    word_list = DataFrame.to_dict(orient="records")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy 3000")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Dunno Button
dunno_image = PhotoImage(file="images/wrong.png")
dunno_button = Button(image=dunno_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=dunno)
dunno_button.grid(column=0, row=1)

# Right Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=right)
right_button.grid(column=1, row=1)

rand_word()

window.mainloop()
