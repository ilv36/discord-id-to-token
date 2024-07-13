import base64
import threading
import time
import tkinter as tk
from tkinter import messagebox
from colorama import Fore, init, Style

init(autoreset=True)

rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def rainbow_text(text):
    colored_text = ""
    color_index = 0
    for char in text:
        if char != " ":
            colored_text += rainbow_colors[color_index % len(rainbow_colors)] + char
            color_index += 1
        else:
            colored_text += " "
    return colored_text

root = tk.Tk()
root.title("ilv")

def toggle_title():
    while True:
        root.title("ilv")
        time.sleep(1)
        root.title("ilv36")
        time.sleep(1)

def encode_id():
    userid = entry.get()
    if userid:
        encodedBytes = base64.b64encode(userid.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        messagebox.showinfo("Token", f'TOKEN FIRST PART: {encodedStr} 🔒')
    else:
        messagebox.showwarning("Warning", "Please enter a user ID")

banner_text = """
╔════════════════════════════════════════╗
║                                        ║
║          ID to Token Converter         ║
║               by ilv                   ║
║                                        ║
╚════════════════════════════════════════╝
"""
banner = tk.Label(root, text=banner_text, font=("Consolas", 12), fg="blue")
banner.pack(pady=10)

label = tk.Label(root, text="USER ID:", font=("Consolas", 12))
label.pack(pady=5)

entry = tk.Entry(root, font=("Consolas", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Convert", command=encode_id, font=("Consolas", 12))
button.pack(pady=20)

title_thread = threading.Thread(target=toggle_title, daemon=True)
title_thread.start()

root.mainloop()
