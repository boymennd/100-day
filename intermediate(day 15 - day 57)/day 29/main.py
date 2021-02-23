from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
blue = "#155ee9"


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
    new_data = {
        website.get(): {
            "email": user.get(),
            "password": password.get(),
        }
    }
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
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
            website.delete(0, END)
            password.delete(0, END)


def get_search():
    with open("data.json", "r") as file:
        data = json.load(file)
    try:
        data_file = data[website.get()]
        messagebox.showinfo(
            title=website.get(),
            message=f"Email:{data_file['email']}\nPassword:{data_file['password']}",
        )
    except KeyError:
        messagebox.showerror(
            title="Error", message=f"These is no website called {website.get()}"
        )


window = Tk()

window.title("Password Manager")
window.config(padx=100, pady=100)
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
website = Entry(width=35)
website.grid(column=2, row=2)
search = Button(text="Search", width=15, command=get_search, activebackground=blue)
search.grid(column=3, row=2)
user = Entry(width=55)
user.insert(END, string="congk59uet@gmail.com")
user_get = user.get()
user.grid(column=2, row=3, columnspan=2)
password = Entry(width=35)
password.grid(column=2, row=4)
but = Button(text="Generate Password", command=get_pass, activebackground=blue)
but.grid(column=3, row=4)
but1 = Button(text="Add", width=46, command=add, activebackground=blue)
but1.grid(column=2, row=5, columnspan=2)


window.mainloop()
