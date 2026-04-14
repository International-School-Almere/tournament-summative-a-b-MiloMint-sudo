#main file for the Tournament App.
import tkinter as tk 
import os 
from tkinter import Label, Radiobutton, StringVar, messagebox
#-------------GUI-------------
screen = tk.Tk()
screen.title("Ron's College Tournament App")
screen.geometry("1450x900")
screen.minsize(800, 500)

#-------------School name / logo------------
school_name_label = tk.Label(screen, text="Ron's College", font=("Helvetica", 16))
school_name_label.grid(pady=20, column=0, padx=25, sticky="nw")

container = tk.Frame(screen)
container.configure(bg="white")
container.grid(row=1, column=0, columnspan=6, sticky="nsew")

def show_home_page():
    for widget in container.winfo_children():
        widget.destroy()
    container.columnconfigure(0, weight=1)

    Home_page_title = tk.Label(container, text="Ron's college 2026 Sports and Academic Tournament", font=("Helvetica", 20))
    Home_page_title.grid(pady=20, column=0, columnspan=4, padx=25)
    Home_page_title.config(anchor="center")

    rules_text_title = tk.Label(container, text="Tournament Rules", font=("Helvetica", 21))
    rules_text_title.grid(row=1, column=2, pady=10, padx=10, sticky="w")

    rules_text = "1. Respect all participants\n2. Follow the rules\n3. Have fun!"
    rules_display = tk.Label(container, text=rules_text, font=("Helvetica", 16), justify="left", wraplength=200)
    rules_display.grid(row=2, pady=5, column=2, padx=15, sticky="n")

    game_play_title = tk.Label(container, text="How the games will work", font=("Helvetica", 21), wraplength=170)
    game_play_title.grid(row=1, column=3, pady=10, padx=10, sticky="w")

    game_play = "blah blah blah"
    game_play_display = tk.Label(container, text=game_play, font=("Helvetica", 16), justify="left", wraplength=200)
    game_play_display.grid(row=2, pady=5, column=3, padx=15, sticky="n")

def show_leaderboard_page():
    for widget in container.winfo_children():
        widget.destroy()
    container.columnconfigure(0, weight=1)

    Leaderboard_page = tk.Label(container, text="Leaderboard", font=("Helvetica", 20))
    Leaderboard_page.grid(pady=20, column=1, padx=25, sticky="n")
    Leaderboard_page.config(anchor="center")

def show_participant_page():
    for widget in container.winfo_children():
        widget.destroy()
    container.columnconfigure(0, weight=1)

    participant_page = tk.Label(container, text="Participants", font=("Helvetica", 20))
    participant_page.grid(pady=20, column=1, padx=25, sticky="n")
    participant_page.config(anchor="center")

def show_sign_up_page():
    for widget in container.winfo_children():
        widget.destroy()
    container.grid(row=1, column=0, columnspan=6, sticky="nsew")
    container.columnconfigure(0, weight=1)

    sign_up_page = tk.Label(container, text="Sign Up", font=("Helvetica", 20))
    sign_up_page.grid(pady=20, column=1, padx=25, sticky="n")
    sign_up_page.config(anchor="center")

    def clicked():
        my_label.config(text=f'You selected event is: {radvar.get()}.')

    radvar = StringVar()
    radvar.set("Basketball")

    sport1 = Radiobutton(container, text="Basketball", variable=radvar, value="Basketball", command=clicked)
    sport1.grid(pady=10, column=1, padx=5, row=1)

    sport2 = Radiobutton(container, text="Soccer", variable=radvar, value="Soccer", command=clicked)
    sport2.grid(pady=10, column=2, padx=5, row=1)

    sport3 = Radiobutton(container, text="Tennis", variable=radvar, value="Tennis", command=clicked)
    sport3.grid(pady=10, column=3, padx=5, row=1)

    my_label = Label(container, text=" ", font=("Helvetica", 16))
    my_label.grid(pady=10)

#-------------Buttons-------------
home_button = tk.Button(screen, text="Home", command = show_home_page)
leaderboard_button = tk.Button(screen, text="Leaderboard", command=show_leaderboard_page)
participant_button = tk.Button(screen, text="Participants", command=show_participant_page)
sign_up_button = tk.Button(screen, text="Sign Up", command=show_sign_up_page)

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

show_home_page()

screen.mainloop()