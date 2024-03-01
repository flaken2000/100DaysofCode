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
REPS = 1
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="TIMER", fg=GREEN)
    checkmark.config(text="")
    REPS = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        my_label.config(text="WORK", fg=GREEN)
        count_down(work_seconds)
    elif REPS == 2 or REPS == 4 or REPS == 6:
        my_label.config(text="BREAK", fg=PINK)
        count_down(short_break_seconds)
    elif REPS == 8:
        my_label.config(text="BREAK", fg=RED)
        count_down(long_break_seconds)
    else:
         REPS = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global REPS
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        REPS += 1
        start_timer()
        # Checkmarks
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔️"
        checkmark.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro 3000")
window.config(padx=100, pady=50, bg=YELLOW)
window.eval('tk::PlaceWindow . center')


# Top label
my_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
my_label.grid(column=1, row=0)

# Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
