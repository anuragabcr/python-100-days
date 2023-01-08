from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}


# ---------------------------- show card ------------------------------- #
def front_card():
    global current_word
    canvas.itemconfig(canvas_img, image=front_img)
    current_word = random.choice(df)
    canvas.itemconfig(lang, text='French')
    canvas.itemconfig(word, text=current_word['French'])


def back_card():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(lang, text='English')
    canvas.itemconfig(word, text=current_word['English'])


# ---------------------------- Read Data ------------------------------- #
df = pd.read_csv(r"../data/french_words.csv")
df = df.to_dict(orient='records')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

canvas = Canvas(height=520, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file='card_back.png')
front_img = PhotoImage(file='card_front.png')
canvas_img = canvas.create_image(400, 260, image=front_img)
lang = canvas.create_text(400, 170, font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 350, font=('Ariel', 40, 'italic'))
front_card()
canvas.grid(row=0, column=0, columnspan=2)

right = PhotoImage(file="right.png")
right_button = Button(image=right, background=BACKGROUND_COLOR, borderwidth=0, command=front_card)
right_button.grid(row=1, column=0)

wrong = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong, background=BACKGROUND_COLOR, borderwidth=0, command=back_card)
wrong_button.grid(row=1, column=1)

window.mainloop()
