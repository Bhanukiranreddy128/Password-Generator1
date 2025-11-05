import secrets
import string
import tkinter as tk
from tkinter import ttk, messagebox
try:
    import pyperclip
    CLIP_AVAILABLE = True
except Exception:
    CLIP_AVAILABLE = False

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    if not (use_upper or use_lower or use_digits or use_symbols):
        raise ValueError("At least one character set must be selected.")
    alphabet = ""
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_lower:
        alphabet += string.ascii_lowercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation
    # Use secrets.choice for cryptographic randomness
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def on_generate():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError
    except Exception:
        messagebox.showerror("Invalid input", "Please enter a valid positive integer for length.")
        return
    try:
        pwd = generate_password(length, upper_var.get(), lower_var.get(), digit_var.get(), symbol_var.get())
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return
    result_var.set(pwd)

def on_copy():
    pwd = result_var.get()
    if not pwd:
        return
    if CLIP_AVAILABLE:
        pyperclip.copy(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        # Fallback using tkinter clipboard
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard (tkinter).")

root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("420x300")
root.resizable(False, False)

frame = ttk.Frame(root, padding=12)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Password Length:").grid(column=0, row=0, sticky="w")
length_var = tk.StringVar(value="16")
length_entry = ttk.Entry(frame, textvariable=length_var, width=10)
length_entry.grid(column=1, row=0, sticky="w")

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=False)

ttk.Checkbutton(frame, text="Uppercase (A-Z)", variable=upper_var).grid(column=0, row=1, sticky="w")
ttk.Checkbutton(frame, text="Lowercase (a-z)", variable=lower_var).grid(column=1, row=1, sticky="w")
ttk.Checkbutton(frame, text="Digits (0-9)", variable=digit_var).grid(column=0, row=2, sticky="w")
ttk.Checkbutton(frame, text="Symbols (!@#...)", variable=symbol_var).grid(column=1, row=2, sticky="w")

gen_btn = ttk.Button(frame, text="Generate", command=on_generate)
gen_btn.grid(column=0, row=3, pady=10)

copy_btn = ttk.Button(frame, text="Copy to Clipboard", command=on_copy)
copy_btn.grid(column=1, row=3, pady=10)

result_var = tk.StringVar()
result_entry = ttk.Entry(frame, textvariable=result_var, width=40)
result_entry.grid(column=0, row=4, columnspan=2, pady=10)

ttk.Label(frame, text="Note: Uses Python's secrets module for cryptographic randomness.").grid(column=0, row=5, columnspan=2, sticky="w")

root.mainloop()
