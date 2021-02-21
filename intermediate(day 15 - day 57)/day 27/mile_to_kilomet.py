from tkinter import *


def start():
    answer = int(int(miles.get()) / 0.61237)
    km.config(text=answer)


window = Tk()
window.title("Miles to Km converter")
window.minsize(width=300, height=150)
window.config(padx=100, pady=50)
label = Label(text="Is equal to", font=3)
label.grid(column=1, row=2)
label1 = Label(text="Miles", font=3)
label1.grid(column=3, row=1)
label2 = Label(text="Km", font=3)
label2.grid(column=3, row=2)
km = Label(text=0, font=3)
km.grid(column=2, row=2)
button = Button(text="Calculate", font=3, command=start)
button.grid(column=2, row=3)
miles = Entry()
miles.grid(column=2, row=1)
window.mainloop()
