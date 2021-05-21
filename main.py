from tkinter import *
import pandas as pd
import random

# --------------------DATA-------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orig_data = pd.read_csv("data/french_words.csv")
    learn = orig_data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")

# --------------------DEFS-------------------- #

def next_card():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = random.choice(learn)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_img, image=flashcard_front)
    flip_timer = root.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_img, image=flashcard_back)


def know_words():
    learn.remove(current_card)
    data = pd.DataFrame(learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# --------------------UI SETUP-------------------- #

root = Tk()
root.title('English To French Flashcard Game')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = root.after(3000, func=flip_card)

# flashcard
canvas = Canvas(width=800, height=626, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=flashcard_front)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

# Buttons
wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=next_card)
button_wrong.place(x=100, y=560)

right = PhotoImage(file="images/right.png")
button_wrong = Button(image=right, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=know_words)
button_wrong.place(x=560, y=560)

next_card()

# --------------------EOF CODE-------------------- #
root.mainloop()
