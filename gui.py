import random
import string
import tkinter as tk


def generate_password(length):
    # define the possible characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate a random password by choosing characters randomly from the above list
    password = ''.join(random.choice(characters) for i in range(length))

    return password


def generate():
    length_text = length_entry.get()
    if length_text == '':
        password_label.config(text="Please enter a password length.")
    else:
        length = int(length_text)
        password = generate_password(length)
        password_label.config(text=password)


# create the main window
window = tk.Tk()
window.title("Password Generator")

# create a label for the password length
length_label = tk.Label(text="Password Length:")
length_label.pack()

# create an entry box for the password length
length_entry = tk.Entry()
length_entry.pack()

# create a button to generate the password
generate_button = tk.Button(text="Generate Password", command=generate)
generate_button.pack()

# create a label to display the generated password
password_label = tk.Label(text="")
password_label.pack()

# start the GUI
window.mainloop()
