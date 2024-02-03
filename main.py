# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    pass
# ---------------------------- UI SETUP ------------------------------- #
# NORMAL_FONT = ("Arial", 15, "normal")
# PASSWORD_BTTN_FONT = ("Arial", 12, "normal")

from tkinter import *

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
website_entry = Entry(width=37)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

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
password_entry = Entry(width=21, bg="white")
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", width=12)
password_button.grid(column=2, row=3)

# Row 4
add_button = Button(text="Add", width=35)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
