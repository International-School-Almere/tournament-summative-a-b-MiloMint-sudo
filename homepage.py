import tkinter as tk 
import os 
from tkinter import messagebox

screen = tk.Tk()
screen.title("Ron's College Tournament App")
screen.geometry("1450x900")
screen.minsize(800, 500)

school_name_label = tk.Label(screen, text="Ron's College", font=("Helvetica", 16))
school_name_label.grid(pady=20, column=0, padx=25, sticky="nw")

Home_page_title = tk.Label(screen, text="Ron's college 2026 Sports and Academic Tournament", font=("Helvetica", 20))
Home_page_title.grid(pady=20, column=1, padx=25, sticky="n")

rules_text_title = tk.Label(screen, text="Tournament Rules", font=("Helvetica", 16))
rules_text_title.grid(row=1, column=2, pady=10, padx=10, sticky="w")

rules_text = "1. Respect all participants\n2. Follow the rules\n3. Have fun!"
rules_display = tk.Label(screen, text=rules_text, font=("Helvetica", 13), justify="left", wraplength=200)
rules_display.grid(row=2, pady=5, column=2, padx=15, sticky="n")

game_play_title = tk.Label(screen, text="How the games will work", font=("Helvetica", 16), wraplength=170)
game_play_title.grid(row=1, column=3, pady=10, padx=10, sticky="w")

game_play = "blah blah blah"
game_play_display = tk.Label(screen, text=game_play, font=("Helvetica", 13), justify="left", wraplength=200)
game_play_display.grid(row=2, pady=5, column=3, padx=15, sticky="n")