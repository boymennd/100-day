from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def get_pass():
    pass_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pass_word_list = pass_symbols + pass_letter + pass_numbers
    random.shuffle(pass_word_list)
    pass_word = "".join(pass_word_list)
    pyperclip.copy(pass_word)
    password.insert(END, string=pass_word)


def add():
    if website.get() == "":
        messagebox.showerror("Error", "Please enter website!")
    elif user.get() == "":
        messagebox.showerror("Error", "Please enter email")
    elif password.get() == "":
        messagebox.showerror("Error", "Please enter password")
    else:
        is_ok = messagebox.askokcancel(
            title=website.get(),
            message=f"There are details entered:\nEmail: "
            f"{user.get()}\nPassword: {password.get()}\n"
            f"It is ok to save?",
        )
        if is_ok:
            with open("data.txt", "a+") as file:
                file.write(f"{website.get()} | {user.get()} | {password.get()}\n")
            website.delete(0, END)
            password.delete(0, END)


window = Tk()

window.title("Password Manager")
window.config(padx=60, pady=100)
image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=image)
canvas.grid(column=2, row=1)
lb = Label(text="Website:", font=2)
lb.grid(column=1, row=2)
lb1 = Label(text="Email/Username:", font=2)
lb1.grid(column=1, row=3)
lb2 = Label(text="Password:", font=2)
lb2.grid(column=1, row=4)
website = Entry(width=55)
website.grid(column=2, row=2, columnspan=2)
user = Entry(width=55)
user.insert(END, string="congk59uet@gmail.com")
user_get = user.get()
user.grid(column=2, row=3, columnspan=2)
password = Entry(width=34)
password.grid(column=2, row=4)
but = Button(text="Generate Password", command=get_pass)
but.grid(column=3, row=4)
but1 = Button(text="Add", width=46, command=add)
but1.grid(column=2, row=5, columnspan=2)


window.mainloop()
