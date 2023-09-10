import tkinter as tk

#   CONSTANTS
LABELS_FONT = ("arial", 12, "bold")
BG_COLOR = "white"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    # this function saves data of the password to a txt file 'data.txt'
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()
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
generate_button = tk.Button(text="Generate Password", bg=BG_COLOR)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=44, bg=BG_COLOR, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
