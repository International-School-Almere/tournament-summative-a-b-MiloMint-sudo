#main file for the Tournament App.
import tkinter as tk 
import tkinter as ttk 
import os 
from tkinter import Label, Radiobutton, StringVar, messagebox
import json
PARTICIPANTS_FILE = "participants.json"
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
container.grid(row=1, column=0, columnspan=6)

def show_home_page():
    for widget in container.winfo_children():
        widget.destroy()
    container.columnconfigure(0, weight=1)

    Home_page_title = tk.Label(container, text="Ron's college 2026 Sports and Academic Tournament", font=("Helvetica", 20))
    Home_page_title.grid(pady=15, column=0, columnspan=4, padx=25)
    Home_page_title.config(anchor="center")

    rules_text_title = tk.Label(container, text="Tournament Rules", font=("Helvetica", 21))
    rules_text_title.grid(row=1, column=1, pady=10, padx=10)
    rules_text_title.config(anchor="center")

    rules_text = "1. Respect all participants\n2. Follow the rules\n3. Have fun!"
    rules_display = tk.Label(container, text=rules_text, font=("Helvetica", 16), justify="left", wraplength=200)
    rules_display.grid(row=2, pady=5, column=1, padx=15)
    rules_display.config(anchor="center")

    game_play_title = tk.Label(container, text="How the games will work", font=("Helvetica", 21), wraplength=170)
    game_play_title.grid(row=1, column=2, pady=10, padx=10)
    game_play_title.config(anchor="center")

    game_play = "blah blah blah"
    game_play_display = tk.Label(container, text=game_play, font=("Helvetica", 16), justify="left", wraplength=200)
    game_play_display.grid(row=2, pady=5, column=2, padx=15)
    game_play_display.config(anchor="center")

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

    #------Treeview------
    my_tree = ttk.Treeview(container)

    #Define our columns 
    my_tree['Columns'] = ("First Name", "Last Name", "Year Group", "Sport", "Academic")
    
    #Formate our columns
    my_tree.column("#0", width=0, stretch=tk.NO)
    my_tree.column("First Name", anchor="w")
    my_tree.column("Last Name", anchor="w")
    my_tree.column("Year Group", anchor="center")
    my_tree.column("Sport", anchor="w")
    my_tree.column("Academic", anchor="w")

    #Create headings
    my_tree.heading("#0", text="", anchor="w")
    my_tree.heading("First Name", text="First Name", anchor="w")
    my_tree.heading("Last Name", text="Last Name", anchor="w")
    my_tree.heading("Year Group", text="Year Group", anchor="center")
    my_tree.heading("Sport", text="Sport", anchor="w")
    my_tree.heading("Academic", text="Academic", anchor="w")

    #Add data
    
    data = [
        ('John', 'Smith', 'Year 10', 'Basketball', ''),
        ('Jane', 'Doe', 'Year 11', 'Soccer', ''),
        ('Jim', 'Beam', 'Year 12', '', 'Maths'),
        ('Lana', 'Joens', 'Year 4', '', 'Physics')
    ]

    count=0 
    for record in data: 
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4]))
        count += 1


def show_sign_up_page():
    
    def clicked():
        my_label.config(text=f'You selected event is: {event_var.get()}.')

    def load_participants():
        if os.path.exists(PARTICIPANTS_FILE):
            try: 
                with open(PARTICIPANTS_FILE, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
            return []

    def save_participants(participants_data):
        participants = load_participants()
        participants.extend(participants_data)
        with open(PARTICIPANTS_FILE, "w") as file:
            json.dump(participants, file)

    def save_signup():
        participant_data = {
            "year_group": year_group_entry.get().strip(),
            "first_name": name_entry.get().strip(),
            "last_name": last_name_entry.get().strip(),
            "event": event_var.get(),
            "entry_type": participation_var.get(),
            "team_name": team_var.get() if participation_var.get() == "Group" else ""
        }

        if not participant_data["year_group"] or not participant_data["first_name"] or not participant_data["last_name"] or not participant_data["event"]:
            messagebox.showerror("Error", "Please fill in the year group, first name, last name, and event.")
            return

        if participant_data["entry_type"] == "Group" and not participant_data["team_name"]:
            messagebox.showerror("Error", "Please select a team.")
            return

        save_participants([participant_data])
        messagebox.showinfo("Saved", "Participant saved successfully.")

    for widget in container.winfo_children():
        widget.destroy()
    container.columnconfigure(0, weight=1)

    sign_up_page = tk.Label(container, text="Sign Up", font=("Helvetica", 20))
    sign_up_page.grid(pady=20, column=1, padx=25,)
    sign_up_page.config(anchor="center")


    participant_year_group = ["MYP 1a","MYP 1b","MYP 1c", 
                              "MYP 2a","MYP 2b","MYP 2c", 
                              "MYP 3a","MYP 3b","MYP 3c", 
                              "MYP 4a","MYP 4b","MYP 4c", 
                              "MYP 5a","MYP 5b","MYP 5c", 
                              "DP1", "DP2", "CP1", "CP2"]

    participant_year_group_var = StringVar()
    participant_year_group_var.set(participant_year_group[0])

    participant_year_group_title = tk.Label(container, text="Year Group:", font=("Helvetica", 16))
    participant_year_group_title.grid(row=1, column=0, pady=10, padx=5)

    year_group_dropdown = tk.OptionMenu(container, participant_year_group_var, *participant_year_group)
    year_group_dropdown.grid(row=1, column=1, pady=10, padx=5)

    participant_name = tk.Label(container, text="First Name:", font=("Helvetica", 16))
    participant_name.grid(row=2, column=0, pady=10, padx=5)
    name_entry = tk.Entry(container, font=("Helvetica", 16))
    name_entry.grid(row=2, column=1, pady=10, padx=5)

    participant_last_name = tk.Label(container, text="Last Name:", font=("Helvetica", 16))
    participant_last_name.grid(row=3, column=0, pady=10, padx=5)
    last_name_entry = tk.Entry(container, font=("Helvetica", 16))
    last_name_entry.grid(row=3, column=1, pady=10, padx=5)

    #------Event type------
    event_var = StringVar()
    event_var.set("Basketball")

    sports_title = tk.Label(container, text="Select a sport:", font=("Helvetica", 16))
    sports_title.grid(row=4, column=0, pady=10, padx=5)

    sport1 = Radiobutton(container, text="Basketball", variable=event_var, value="Basketball", command=clicked)
    sport1.grid(pady=10, column=0, padx=5, row=5)

    sport2 = Radiobutton(container, text="Soccer", variable=event_var, value="Soccer", command=clicked)
    sport2.grid(pady=10, column=0, padx=5, row=6)

    sport3 = Radiobutton(container, text="Tennis", variable=event_var, value="Tennis", command=clicked)
    sport3.grid(pady=10, column=0, padx=5, row=7)

    academic_title = tk.Label(container, text="Select an academic event:", font=("Helvetica", 16))
    academic_title.grid(row=4, column=1, pady=10, padx=5)

    academic1 = Radiobutton(container, text="Maths", variable=event_var, value="Maths", command=clicked)
    academic1.grid(pady=10, column=1, padx=5, row=5)

    academic2 = Radiobutton(container, text="Physics", variable=event_var, value="Physics", command=clicked)
    academic2.grid(pady=10, column=1, padx=5, row=6)

    academic3 = Radiobutton(container, text="History", variable=event_var, value="History", command=clicked)
    academic3.grid(pady=10, column=1, padx=5, row=7)

    my_label = Label(container, text="", font=("Helvetica", 16))
    my_label.grid(row=8, column=1, pady=10)

    #-------Participation Type--------
    participation_var = StringVar()
    participation_var.set("Group")

    group_title = tk.Label(container, text="Group:", font=("Helvetica", 16))
    group_title.grid(row=9, column=0, pady=10, padx=5)

    individual_title = tk.Label(container, text="Individual:", font=("Helvetica", 16))
    individual_title.grid(row=9, column=1, pady=10, padx=5)

    group = Radiobutton(container, text="Group", variable=participation_var, value="Group", command=clicked)
    group.grid(row=10, column=0, pady=10, padx=5)

    team_name_label = tk.Label(container, text="Team Name:", font=("Helvetica", 16))
    team_name_label.grid(row=11, column=0, pady=10, padx=5)

    individual = Radiobutton(container, text="Individual", variable=participation_var, value="Individual", command=clicked)
    individual.grid(row=10, column=1, pady=10, padx=5)

    #------Teams------
    teamnames = ["Team name 1", "Team name 2", "Team name 3", "Team name 4"]

    team_var = StringVar()
    team_var.set(teamnames[0])

    dropdown = tk.OptionMenu(container, team_var, *teamnames)
    dropdown.grid(row=12, column=0, pady=10, padx=5)

    save_button = tk.Button(container, text="Submit", command=save_signup)
    save_button.grid(row=13, column=1, pady=20, padx=5)

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