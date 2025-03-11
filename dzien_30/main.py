import tkinter
import pandas

BACKGROUND_COLOR = "#B1DDC6"
app_window = tkinter.Tk()
app_window.title("Flashy")
app_window.configure(background=BACKGROUND_COLOR)
app_window.geometry("1000x750")

#-----------------------download word from csv file-------------------------#
words_to_learn = pandas.read_csv("./data/french_words.csv")

#------------------------------Functions------------------------------------#
def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(word_label, text= current_word["English"], fill = "white")

def next_word():
    global current_word
    current_word = words_to_learn.sample(n=1).iloc[0]
    canvas.itemconfig(card_image, image = card_front)
    canvas.itemconfig(word_label, text = current_word["French"], fill = "black")
    app_window.after(3000, flip_card)

def move_card_to_known_word():
    global known_words, current_word, words_to_learn
    known_words = pandas.concat([known_words, current_word.to_frame().T], ignore_index=True)
    words_to_learn = words_to_learn[words_to_learn.French != current_word.French]
    next_word()

#------------------------------Create GUI-----------------------------------#
canvas = tkinter.Canvas(app_window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
canvas.place(x=100, y=50)
word_label = canvas.create_text(400, 263, text="", font = ("Arial", 40, "bold"), fill = "black")

right_button_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(app_window, image=right_button_image, highlightthickness=0, borderwidth=0, command = move_card_to_known_word)
right_button.place(x=600, y=600)

wrong_button_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(app_window, image=wrong_button_image, highlightthickness=0, borderwidth=0, command = next_word)
wrong_button.place(x=300, y=600)

current_word ={}
known_words = pandas.DataFrame()

#--------------------------------main code----------------------------------#
next_word()

app_window.mainloop()
