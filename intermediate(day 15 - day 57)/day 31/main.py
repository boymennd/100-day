from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
new_data = {}


def new_word():
    global current_card, timer
    win.after_cancel(timer)
    current_card = random.choice(new_data)
    canvas.itemconfig(can_image, image=image2)
    canvas.itemconfig(leng, text="English")
    canvas.itemconfig(word, text=current_card["English"])
    timer = win.after(3000, answer)


def answer():
    canvas.itemconfig(can_image, image=image1)
    canvas.itemconfig(leng, text="Việt Nam")
    canvas.itemconfig(word, text=current_card["VietNam"])


def is_known():
    new_data.remove(current_card)
    new_dict = pandas.DataFrame(new_data)
    new_dict.to_csv("word_to_learn.csv", index=False)
    print(len(new_dict))
    new_word()


try:
    data = pandas.read_csv("word_to_learn.csv")
    new_data = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data.csv")
    new_data = data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    data = pandas.read_csv("data.csv")
    new_data = data.to_dict(orient="records")

win = Tk()
timer = win.after(3000, answer)
win.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
win.title("Flashy")
image1 = PhotoImage(file="images/card_back.png")
image2 = PhotoImage(file="images/card_front.png")
image3 = PhotoImage(file="images/right.png")
image4 = PhotoImage(file="images/wrong.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
can_image = canvas.create_image(400, 263, image=image2)
leng = canvas.create_text(400, 150, text="Tittle", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)
new_word()
but_wrong = Button(
    image=image4, bg=BACKGROUND_COLOR, highlightthickness=0, command=new_word
)
but_wrong.grid(column=1, row=2)
but_right = Button(
    image=image3, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known
)
but_right.grid(column=2, row=2)


win.mainloop()
