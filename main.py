from tkinter import *
from tkinter import messagebox as msb
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    new_password = ''.join(password_list)

    password_entry.insert(END, new_password)

    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        msb.showerror(title="Oops", message="Please don't leave any fields empty!")
        return
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                print(data)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving update data
                json.dump(data, data_file, indent=4)

        finally:
            # Getting fields empty
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -------------------------- FIND PASSWORD ----------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        msb.showerror(title="Oops", message="No data file found!")
    else:
        for dic in data.keys():
            if website == dic:
                email = data[website]["email"]
                password = data[website]["password"]
                msb.showinfo(title=f"{website}", message=f"Website: {website}\n Email: {email}\nPassword: {password}")
                return
            else:
                msb.showerror(title="Oops", message="No details for the website exists!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Row 0
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Row 1
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)

# Row 2
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
user_entry = Entry(width=37)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(END,
                  "user@email.com")  # Method to insert a default text,
# END is a variable to refer the very last character's index

# Row 3
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21, show="*")
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", width=12, command=generate_password)
password_button.grid(column=2, row=3)

# Row 4
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
