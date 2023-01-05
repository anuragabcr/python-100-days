from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .3
SHORT_BREAK_MIN = .1
LONG_BREAK_MIN = .2
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    sbreak_sec = SHORT_BREAK_MIN * 60
    lbreak_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(lbreak_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(sbreak_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)
        check.config(text=CHECK_MARK * math.ceil(reps / 2))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    canvas.itemconfig(timer_text, text=f"{time // 60}:{time % 60}")
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=100, padx=100, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start = Button(text="Start", font=(FONT_NAME, 15), command=start_timer)
start.grid(row=2, column=0)

check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check.grid(row=2, column=1)

reset = Button(text="Reset", font=(FONT_NAME, 15), command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()
