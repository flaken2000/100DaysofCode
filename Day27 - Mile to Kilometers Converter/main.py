from tkinter import *

window = Tk()
window.title("Mile to Km Converter 3000")
window.minsize(width=200, height=100)
window.config(padx=20, pady=30)

miles = Entry(width=10)
miles.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label_left = Label(text="is equal to")
km_label_left.grid(column=0, row=1)

km_label = Label(text="")
km_label.grid(column=1, row=1)

km_label_right = Label(text="Km")
km_label_right.grid(column=2, row=1)


def button_clicked():
    km_label["text"] = str(round((float(miles.get())) * 1.609344, 1))


calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)

window.mainloop()
