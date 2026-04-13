#main file for the Tournament App.
import tkinter as tk 
import os 
from tkinter import messagebox
from sign_up_page import setup_signup_page
#-------------GUI-------------
screen = tk.Tk()
screen.title("Ron's College Tournament App")
screen.geometry("1450x900")
screen.minsize(800, 500)

#-------------School name / logo------------
school_name_label = tk.Label(screen, text="Ron's College", font=("Helvetica", 16))
school_name_label.grid(pady=20, column=0, padx=25, sticky="nw")

#-------------Pages-------------
home_page = tk.Frame(screen)
leaderboard_page = tk.Frame(screen)
participant_page = tk.Frame(screen)
sign_up_page = tk.Frame(screen)

#-------------Buttons-------------
home_button = tk.Button(screen, text="Home")
leaderboard_button = tk.Button(screen, text="Leaderboard")
participant_button = tk.Button(screen, text="Participants")
sign_up_button = tk.Button(screen, text="Sign Up")

screen.columnconfigure(0, weight=1)
screen.columnconfigure(1, weight=0)
screen.columnconfigure(2, weight=0)
screen.columnconfigure(3, weight=0)
screen.columnconfigure(4, weight=0)
screen.columnconfigure(5, weight=1)

home_button.grid(row=0, column=1, padx=10, pady=10)
leaderboard_button.grid(row=0, column=2, padx=10, pady=10)
participant_button.grid(row=0, column=3, padx=10, pady=10)
sign_up_button.grid(row=0, column=4, padx=10, pady=10)

container = tk.Frame(screen)
container.configure(bg="white")
container.grid(row=1, column=0, columnspan=6, sticky="nsew")

def show_home_page():
    for widget in container.winfo_children():
        widget.destroy()
    container.grid(row=1, column=0, columnspan=6, sticky="nsew")

    school_name_label = tk.Label(container, text="Ron's College", font=("Helvetica", 16))
    school_name_label.grid(pady=20, column=0, padx=25, sticky="nw")

    Home_page_title = tk.Label(container, text="Ron's college 2026 Sports and Academic Tournament", font=("Helvetica", 20))
    Home_page_title.grid(pady=20, column=1, padx=25, sticky="n")

    rules_text_title = tk.Label(container, text="Tournament Rules", font=("Helvetica", 16))
    rules_text_title.grid(row=1, column=2, pady=10, padx=10, sticky="w")

    rules_text = "1. Respect all participants\n2. Follow the rules\n3. Have fun!"
    rules_display = tk.Label(container, text=rules_text, font=("Helvetica", 13), justify="left", wraplength=200)
    rules_display.grid(row=2, pady=5, column=2, padx=15, sticky="n")

    game_play_title = tk.Label(container, text="How the games will work", font=("Helvetica", 16), wraplength=170)
    game_play_title.grid(row=1, column=3, pady=10, padx=10, sticky="w")

    game_play = "blah blah blah"
    game_play_display = tk.Label(container, text=game_play, font=("Helvetica", 13), justify="left", wraplength=200)
    game_play_display.grid(row=2, pady=5, column=3, padx=15, sticky="n")
        

def show_frame(frame):
    frame.tkraise()
    home_button.config(command=lambda: show_frame(home_page))
    leaderboard_button.config(command=lambda: show_frame(leaderboard_page))
    participant_button.config(command=lambda: show_frame(participant_page))
    sign_up_button.config(command=lambda: show_frame(sign_up_page))

    tk.Label(home_page, text="Home").grid()
    tk.Label(leaderboard_page, text="Leaderboard").grid()
    tk.Label(participant_page, text="Participants").grid()
    tk.Label(sign_up_page, text="Sign Up").grid() 


setup_signup_page(sign_up_page)
show_home_page()
screen.mainloop()