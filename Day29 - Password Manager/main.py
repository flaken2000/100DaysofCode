from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
label_font = "arial"
label_size = 10
default_email = "email@domain.com"
password_file = "data.json"

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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty fields", message="Please do not leave any empty fields")
    else:
        saved_entry = website + " | " + email + " | " + password + "\n"
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, default_email)
        password_entry.delete(0, END)

        try:
            with open(password_file, mode="r") as passwords:
                # Reading existing data
                data = json.load(passwords)
        except FileNotFoundError:
            with open(password_file, mode="w") as passwords:
                json.dump(new_data, passwords, indent=4)
        else:
            # Updating existing data with new entry
            data.update(new_data)
            with open(password_file, mode="w") as passwords:
                # Saving updated data
                json.dump(data, passwords, indent=4)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    try:
        with open(password_file, mode="r") as passwords:
            # Reading existing data
            data = json.load(passwords)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        try:
            website = website_entry.get()
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showinfo(title="Not found", message="No details for the website exists")
        else:
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")



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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky="EW")
search_pass_button = Button(text="Search", command=search_password)
search_pass_button.grid(column=2, row=1, sticky="EW")
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
