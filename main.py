from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


data = pd.read_csv('./data/french_words.csv')
data_dict = data.to_dict(orient="records")

def next_card():
    random_word = random.choice(data_dict)['French']
    canvas.itemconfig(word_label, text=random_word)
    canvas.itemconfig(title_label, text="French")



# ----------------------------------UI SETUP--------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=60, pady=60, bg= BACKGROUND_COLOR)


canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
title_label = canvas.create_text(400,150, text="Title", font=("Ariel", 40,"italic"))
word_label = canvas.create_text(400,263, text="Word", font=("Ariel", 60,"bold"))  
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()



