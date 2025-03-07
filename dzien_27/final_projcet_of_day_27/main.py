from tkinter import *

app_window = Tk()
app_window.title("Mile to Km Converter")


miles = Entry(width=30)
miles.grid(column=1, row=0)

miles_text = Label(text="Miles", font = ("Arial", 24, "bold"))
miles_text.grid(column=2, row=0)

equal_text = Label(text="Is equal to", font = ("Arial", 24, "bold"))
equal_text.grid(column=0, row=1)

km_text = Label(text="Km", font = ("Arial", 24, "bold"))
km_text.grid(column=2, row=1)

result = Label(text = 0, font = ("Arial", 24, "bold"))
result.grid(column=1, row=1)

def calculate_bottom():
    int_miles = int(miles.get())
    result_int = round(int_miles * 1.6, 2)
    result.config(text = result_int)

calculate_bottom = Button(app_window, text="Calculate", command=calculate_bottom, height=2, width=10)
calculate_bottom.grid(column=1, row=2)

app_window.mainloop()
