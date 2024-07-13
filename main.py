import os
import base64
import threading
import time
from colorama import Fore, init, Style

init(autoreset=True)

def toggle_title():
    while True:
        os.system("title ilv")
        time.sleep(1)
        os.system("title ilv36")
        time.sleep(1)

title_thread = threading.Thread(target=toggle_title, daemon=True)
title_thread.start()

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

banner_text = """
╔════════════════════════════════════════╗
║                                        ║
║          ID to Token Converter         ║
║               by ilv                   ║
║                                        ║
╚════════════════════════════════════════╝
"""
banner = rainbow_text(banner_text)
print(Style.BRIGHT + banner)

input_prompt = rainbow_text(" [INPUT] USER ID: ")
userid = input(Style.BRIGHT + input_prompt + Fore.RESET)

encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")

encoded_text = rainbow_text(f'\n [LOGS] TOKEN FIRST PART: {encodedStr} 🔒')
print(Style.BRIGHT + encoded_text)

print(rainbow_text("\nPress any key to exit..."))
os.system('pause >nul')
