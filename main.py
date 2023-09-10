import tkinter as tk
import tkinter.messagebox as mb
import pyperclip
import random

#   CONSTANTS
LABELS_FONT = ("arial", 12, "bold")
BG_COLOR = "white"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = []
    for i in range(ord('a'), ord('z') + 1):
        letters.append(chr(i))
        letters.append(chr(i - 32))

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(random.choice(letters))
     for _ in range(random.randint(8, 10))]
    [password_list.append(random.choice(symbols))
     for _ in range(random.randint(2, 4))]
    [password_list.append(random.choice(numbers))
     for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password_input.delete(0, tk.END)
    p = "".join(password_list)
    pyperclip.copy(p)
    password_input.insert(0, p)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    # this function saves data of the password to a txt file 'data.txt'
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()

    if not (website and user and password):
        mb.showinfo(title="Error", message="Fill all fields!")
    else:
        confirmed = mb.askyesno(title="Confirmation Message",
                                message=f"Website: {website}\nUser: {user}\nPassword: {password}\n\nDo You Want to Confirm?")

        if confirmed:
            with open("data.txt", 'a') as f:
                f.write(f"{website} | {user} | {password}\n")
            website_input.delete(0, tk.END)
            password_input.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
#   Window Setup
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)

#   Canvas Setup
canvas = tk.Canvas(width=200, height=200, bg=BG_COLOR,
                   highlightbackground=BG_COLOR)
img = tk.PhotoImage(file="E:/python projects/password_manager/logo.png")
canvas.create_image(100, 100, image=img)

canvas.grid(row=0, column=1)

#   Labels
website_label = tk.Label(text="Website:", font=LABELS_FONT, bg=BG_COLOR)
website_label.grid(column=0, row=1)

user_label = tk.Label(text="Email/Username:", font=LABELS_FONT, bg=BG_COLOR)
user_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:", font=LABELS_FONT, bg=BG_COLOR)
password_label.grid(column=0, row=3)

#   Input Fields
website_input = tk.Entry(width=50)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

user_input = tk.Entry(width=50)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "omar@mail.com")

password_input = tk.Entry(width=31)
password_input.grid(column=1, row=3)

# Buttons
generate_button = tk.Button(
    text="Generate Password", bg=BG_COLOR, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=44, bg=BG_COLOR, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
