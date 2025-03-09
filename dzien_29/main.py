import tkinter
import random

def password_generator():
    low_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    up_letters = [letter.upper() for letter in low_letters]
    numbers = [number for number in range(0,11)]
    special_characters = ["!","@","#","$","%","^","&"]
    password_list = []
    for i in range(21):
        choose = random.randint(1,4)
        if choose == 1:
            password_list.append(random.choice(up_letters))
        elif choose == 2:
            password_list.append(random.choice(low_letters))
        elif choose == 3:
            password_list.append(str(random.choice(numbers)))
        elif choose == 4:
            password_list.append(str(random.choice(special_characters)))
    password = "".join(password_list)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

def empty_popup():
    empty_pole = tkinter.Tk()
    empty_pole.title("Oops")
    empty_pole_label = tkinter.Label(empty_pole, text="Please don't leave any fields empty!")
    empty_pole_label.pack()
    close_button = tkinter.Button(empty_pole, text = "Ok", command = empty_pole.destroy)
    close_button.pack()

def write_data_to_db():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(f"{website} | {email} | {password}\n")

def correct_data_popup():
    correct_data_pole = tkinter.Tk()
    correct_data_pole.title("AppBrewery")
    correct_data_label = tkinter.Label(correct_data_pole, text=f"Email: {email_username_entry.get()} \nPassword: {password_entry.get()} \n Is this ok?")
    correct_data_label.pack()
    no_button = tkinter.Button(correct_data_pole, text = "No", command = correct_data_label.destroy)
    no_button.pack()
    yes_button = tkinter.Button(correct_data_pole, text = "Yes", command = write_data_to_db)
    yes_button.pack()

def add_button_logic():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_username_entry.get()) == 0:
        empty_popup()
    else:
        correct_data_popup()

app_window = tkinter.Tk()
app_window.title("Password Manager")
app_window.config(padx=10, pady=10)
app_window.columnconfigure(0, weight=1)

canvas = tkinter.Canvas(app_window)
padlock_image = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(200, 95, image = padlock_image)
canvas.grid(column=1, row=0)

website_text = tkinter.Label(app_window, text="Website:", font=("Arial", 16, "bold"))
website_text.grid(column=0, row=1)

email_username_text = tkinter.Label(app_window, text="Email/Username:", font=("Arial", 16, "bold"))
email_username_text.grid(column=0, row=2)

password_text = tkinter.Label(app_window, text="Password:", font=("Arial", 16, "bold"))
password_text.grid(column=0, row=3)

generate_password_button = tkinter.Button(app_window, text="Generate Password", font=("Arial", 11, "bold"), command=password_generator)
generate_password_button.grid(column=2, row=3, sticky = "ew")

add_button = tkinter.Button(app_window, text="Add", padx= 80, font=("Arial", 11, "bold"), command=add_button_logic)
add_button.grid(column=1, row=4, columnspan=2, sticky = "ew")

website_entry = tkinter.Entry(app_window, width=35, font=("Arial", 14, "bold"))
website_entry.grid(column=1, row=1, columnspan=2, sticky = "ew")

email_username_entry = tkinter.Entry(app_window, width=35, font=("Arial", 14, "bold"))
email_username_entry.grid(column=1, row=2, columnspan=2, sticky = "ew")

password_entry = tkinter.Entry(app_window , font=("Arial", 11, "bold"))
password_entry.grid(column=1, row=3, sticky = "ew")

app_window.mainloop()