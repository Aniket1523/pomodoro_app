from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_mins = math.floor(count / 60)
    count_secs = count % 60

    if count_secs <10:
        count_secs = f"0{count_secs}"


    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(115, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold'))
label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 10, 'bold'), width=11, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, 'bold'), width=11)
reset_button.grid(row=2, column=3)

check_marks = Label(text="✔️", bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
