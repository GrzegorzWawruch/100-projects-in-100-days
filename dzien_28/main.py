import tkinter
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    checkmarks.config(text="")
    timer_text.config(text="Timer", fg = GREEN)
    canvas.itemconfig(timer_text_canvas, text = "00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0 and reps < 8:
        count_down(short_break_sec)
        timer_text.config(text='Break', fg = PINK)
    elif reps % 2 == 1 and reps < 8:
        count_down(work_sec)
        timer_text.config(text='Work', fg = GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        timer_text.config(text='Long Break', fg = RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    if count % 60 == 0 or 10 > count % 60 > 0:
        canvas.itemconfig(timer_text_canvas, text = f'{count // 60}:0{count % 60}')
    else:
        canvas.itemconfig(timer_text_canvas, text=f'{count // 60}:{count % 60}')
    if count >0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = reps // 2
        for i in range(work_sessions):
            mark += "✓"
        checkmarks.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

canvas = tkinter.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_image)
timer_text_canvas = canvas.create_text(100, 130, text = "00:00" ,font = (FONT_NAME, 30, "bold"), fill = "white")
canvas.grid(column = 1, row = 1)

start_button = tkinter.Button(text = "Start", font = (FONT_NAME, 14), command=start_timer)
start_button.grid(column = 0, row = 2)

reset_button = tkinter.Button(text = "Reset", font = (FONT_NAME, 14), command = reset_timer)
reset_button.grid(column = 2, row = 2)

timer_text = tkinter.Label(text = "Timer", font = (FONT_NAME, 45, "bold"), fg = GREEN, bg = YELLOW, highlightthickness = 0)
timer_text.grid(column = 1, row = 0)

checkmarks = tkinter.Label(font = (FONT_NAME, 14, "bold"), fg = GREEN, bg = YELLOW, highlightthickness = 0)
checkmarks.grid(column = 1, row = 3)

window.mainloop()