from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")
# print(data_dict)
cards_used = []
button_clicked = 0
previous_card = {}


def right_button():
    global previous_card
    print(f"inside right function{previous_card}")
    data_dict.remove(previous_card)
    df = pandas.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    generate_word()



def generate_word():
    # language_choice = data_dict.keys()
    # keys = ('French', 'English')
    # chosen_key = random.choice(keys)
    global flip_timer, cards_used, previous_card
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    previous_card = current_card
    fresh_word = current_card["French"]
    canvas.itemconfig('lang_label', text="French", fill="black")
    canvas.itemconfig('word_label', text=f"{fresh_word}", fill="black")
    flip_timer = window.after(3000, flip_image, current_card)


def flip_image(current_set):
    canvas.itemconfig(card_image, image=back_img)
    english_word = current_set["English"]
    canvas.itemconfig('lang_label', text="English", fill="white")
    canvas.itemconfig('word_label', text=f"{english_word}", fill= "white")
    # print("Image flipped")


window = Tk()
window.title("Flash Cards")
canvas = Canvas(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_image)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400,263,image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, font=("Arial", 40, "italic"), tags='lang_label')
canvas.create_text(400, 263, font=("Arial", 60, "bold"), tags='word_label')
canvas.grid(column=0, row=0, columnspan=2)


right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=right_button)
right_button.grid(column=1, row=1)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)

generate_word()





window.mainloop()

