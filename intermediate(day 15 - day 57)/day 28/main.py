from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = []
timer = None


def reset_timer():
    global reps, check_mark
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00.00")
    label.config(text="Timer", fg=GREEN)
    checkbutton.config(text="")
    reps = 0
    check_mark = []


def start_timer():
    global reps
    reps += 1

    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps > 8:
        reset_timer()
    elif reps % 8 == 0:
        check_mark.append("✓")
        checkbutton.config(
            text=check_mark,
            fg=GREEN,
            font=("arial", 20, "bold"),
            bg=YELLOW,
            highlightthickness=0,
        )
        count_down(long_break_min)
        label.config(
            text="Break", fg=RED, font=("arial", 35), bg=YELLOW, highlightthickness=0
        )
    elif reps % 2 == 0:
        check_mark.append("✓")
        checkbutton.config(
            text=check_mark,
            fg=GREEN,
            font=("arial", 20, "bold"),
            bg=YELLOW,
            highlightthickness=0,
        )
        count_down(short_break_min)
        label.config(
            text="Break", fg=PINK, font=("arial", 35), bg=YELLOW, highlightthickness=0
        )
    else:
        count_down(work_min)
        label.config(
            text="Work", fg=GREEN, font=("arial", 35), bg=YELLOW, highlightthickness=0
        )


def count_down(count):
    minute = math.floor(count / 60)
    seconds = count % 60
    if 0 <= seconds <= 9:
        seconds = f"0{seconds}"
    if 0 <= minute <= 9:
        minute = f"0{minute}"
    canvas.itemconfig(timer_text, text=f"{minute}.{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)

timer_text = canvas.create_text(
    102, 130, text="00.00", fill="white", font=(FONT_NAME, 30, "bold")
)
canvas.grid(column=2, row=2)
label = Label(
    text="Timer", fg=GREEN, font=("arial", 35), bg=YELLOW, highlightthickness=0
)
label.grid(column=2, row=1)
button_start = Button(text="Start", command=start_timer)
button_start.grid(column=1, row=3)
button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=3, row=3)
checkbutton = Label(
    text=check_mark,
    fg=GREEN,
    font=("arial", 20, "bold"),
    bg=YELLOW,
    highlightthickness=0,
)
checkbutton.grid(column=2, row=4)
window.mainloop()
