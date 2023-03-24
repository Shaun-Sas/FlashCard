from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card ={}
to_learn={}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")




def next():
    global current_card, hello
    canvas.itemconfig(canvas_img,image=old_image)
    window.after_cancel(hello)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="Black")
    canvas.itemconfig(card_word,text=current_card["French"] ,fill="Black")
    hello = window.after(3000,english)


def english():
    canvas.itemconfig(canvas_img,image=new_image)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")

    next()




window = Tk()
window.title("Window")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR,highlightthickness=0)
hello = window.after(3000,english)
canvas = Canvas(window, width=800, height=526)
old_image = PhotoImage(file="images/card_front.png")

new_image = PhotoImage(file="images/card_back.png")
canvas_img =canvas.create_image(400, 263, image=old_image, )
card_title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="Word",font=('Ariel',60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

canvas.grid(row=0,column=0,columnspan=2)

cross = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")

wrong_btn = Button(image=cross,bg=BACKGROUND_COLOR,highlightthickness=0,command=next)
wrong_btn.grid(row=1,column=0)

check_btn = Button(image=right,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_known)
check_btn.grid(row=1,column=1)

next()

window.mainloop()

