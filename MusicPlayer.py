import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password():
    try:
        password_length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        return

    if password_length <= 0:
        messagebox.showerror("Error", "Password length must be a positive integer.")
    else:
        random_password = generate_random_password(password_length)
        password_label.config(text="Generated Password: " + random_password)


root = tk.Tk()
root.title("Random Password Generator")


length_label = tk.Label(root, text="Enter the desired password length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()


password_label = tk.Label(root, text="")
password_label.pack()


root.mainloop()

