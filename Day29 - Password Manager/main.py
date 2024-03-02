from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
label_font = "arial"
label_size = 10
default_email = "email@domain.com"
password_file = "data.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty fields", message="Please do not leave any empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}\n Password: {password}\n Is it ok to save?")
        if is_ok:
            saved_entry = website + " | " + email + " | " + password + "\n"
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, default_email)
            password_entry.delete(0, END)
            with open(password_file, mode="a") as passwords:
                passwords.write(saved_entry)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager 3000")
window.config(padx=50, pady=50)
window.eval('tk::PlaceWindow . center')

# Image
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:", font=(label_font, label_size, "normal"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

# Email/Username
email_label = Label(text="Email/Username:", font=(label_font, label_size, "normal"))
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "email@domain.com")

# Password
password_label = Label(text="Password:", font=(label_font, label_size, "normal"))
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")
gen_pass_button = Button(text="Generate Password", command=gen_password)
gen_pass_button.grid(column=2, row=3, sticky="EW")

# Save password
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")




window.mainloop()
