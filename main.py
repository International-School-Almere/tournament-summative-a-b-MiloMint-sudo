#main file for the Tournament App.
import tkinter as tk 
import os 
from tkinter import messagebox
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

screen.mainloop() 