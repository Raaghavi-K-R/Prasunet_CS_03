import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[@$!%*?&]', password))
    
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    if criteria_met == 5:
        return "Very Strong"
    elif criteria_met == 4:
        return "Strong"
    elif criteria_met == 3:
        return "Moderate"
    elif criteria_met == 2:
        return "Weak"
    else:
        return "Very Weak"

def check_password():
    password = entry_password.get()
    if not password:
        messagebox.showerror("Invalid Input", "Password cannot be empty")
        return
    
    strength = assess_password_strength(password)
    label_result.config(text=f"Password Strength: {strength}")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
label_instruction = tk.Label(root, text="Enter a password to assess its strength:")
label_instruction.pack(pady=10)

entry_password = tk.Entry(root, width=40)  # Removed show="*"
entry_password.pack(pady=10)

button_check = tk.Button(root, text="Check Strength", command=check_password)
button_check.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Run the application
root.mainloop()
