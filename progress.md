# Progress Journal

> Use this journal to track progress, decisions, problems, and next steps.
> Update it after each work session.
> 
---

# 1. Project Overview

## Project Title
Tournament Summative Crit. B & C

## Project Description
I’m building a scoring app for a college tournament. The college is running this big event with 5 different challenges—everything from sports to academic stuff.

My job is to make a program that keeps track of everyone's points so the judges don't have to do it by hand on a messy spreadsheet.

## Start Date
30 March 2026

## Target End Date
[Unknown / add later]

## File list.

## (Dependencies) API / library / module list.
---


# 2. Progress Log

> Add a new session at the top each time you work.

---
## Session [01]
**Date:** 31st March 2026  
**Time spent:** 15 min  
**Focus:** Initializing the Python Environment and UI Framework.

### Problems / Challenges
- 
- 

### Solutions / Actions Taken
- 
- 

### Evidence
- Added code: 
"import tkinter as tk 
import os 
from tkinter import messagebox
#-------------GUI-------------
screen = tk.Tk()
screen.title("Ron's College Tournament App")
screen.geometry("1450x900")
screen.minsize(800, 500)

#-------------School logo / logo------------

#-------------Pages-------------
home_page = tk.Frame(screen)
leaderboard_page = tk.Frame(screen)
participant_page = tk.Frame(screen)
sign_up_page = tk.Frame(screen)

#-------------Buttons-------------
screen.mainloop()"

- [Updated design] 
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?
- What needs improvement?
- What did I learn?

---

## Session [02]
**Date:** 1st April 2026  
**Time spent:** 45 min  
**Focus:** This code sets up a navigation menu with buttons that allow the user to switch between the different "pages" (frames) of your tournament app using a grid layout and a switching function.

### Problems / Challenges
- At first my buttons were stuck on the left side and refused to go to the center of the app. 
- 

### Solutions / Actions Taken
- I asked Chatgpt to help me and it said I needed to use a "columnconfigure" which fixed part of the problem. (Its not perfectly in the middle but its somewhat in the middle so Im happy.)
- 

### Evidence
- Added code:
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

- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?
    I think I was able to create the buttons and the layout for them really well. Using grid made it much easier to keep the spacing consistent across the top of the app.
- What needs improvement?
    I need to make sure the buttons are up to my standard, so I want to refine the centering. 
- What did I learn?


---
## Session [03]
**Date:** 6 April 2026  
**Time spent:** 2 hours 15 min  
**Focus:** Developing the event selection logic and implementing data validation via radio buttons.

### Problems / Challenges
- Variable scope: I initially had an issue where every radio button had its own variable, allowing the user to select multiple sports at once. This would have broken the tournament rules.
- 

### Solutions / Actions Taken
- Grouping Logic: I assigned all sport buttons to one StringVar (selected_sport) and all academic buttons to another (selected_academic). This automatically makes them "mutually exclusive" (choosing one deselects the others).
- 

### Evidence
- Added code: 
def sign_up():
  
    def clicked():

        sport = selected_sport.get()
        academic = selected_academic.get()

        if sport == "Basketball":
            messagebox.showinfo("Selection", "You chose Basketball.")
        elif sport == "Soccer":
            messagebox.showinfo("Selection", "You chose Soccer.")
        elif sport == "Tennis":
            messagebox.showinfo("Selection", "You chose Tennis.")
        else:
            messagebox.showinfo("Selection", "No sport selected.")

        if academic == "Math":
            messagebox.showinfo("Selection", "You chose Math.")
        elif academic == "Science":
            messagebox.showinfo("Selection", "You chose Science.")
        elif academic == "English":
            messagebox.showinfo("Selection", "You chose English.")
        else:
            messagebox.showinfo("Selection", "No academic subject selected.")

 #----------Create StringVar()----------
    selected_sport = StringVar()
    selected_academic = StringVar()
 #----------Create radio buttons----------
    radio1 = Radiobutton(screen, text="Basketball", variable=selected_sport, value="Basketball", command=clicked)
    radio1.grid()
    radio2 = Radiobutton(screen, text="Soccer", variable=selected_sport, value="Soccer", command=clicked)
    radio2.grid()
    radio3 = Radiobutton(screen, text="Tennis", variable=selected_sport, value="Tennis", command=clicked)
    radio3.grid()

    academic1_radio1 = Radiobutton(screen, text="Math", variable=selected_academic, value="Math", command=clicked)
    academic1_radio1.grid()
    academic2_radio2 = Radiobutton(screen, text="Science", variable=selected_academic, value="Science", command=clicked)
    academic2_radio2.grid()
    academic3_radio3 = Radiobutton(screen, text="English", variable=selected_academic, value="English", command=clicked)
    academic3_radio3.grid()
       
- [Updated design]
- [Created sketch]
- Radio buttons (Basically checkboxes but only can check one off.)
- [Uploaded image/screenshot]

### Reflection
- What went well?
- What needs improvement?
- What did I learn?
    I learnt about radio buttons from a youtube tutorial. 

---

## Session [04]
**Date:** 7 April 2026  
**Time spent:** 30 min  
**Focus:** Designing the Homepage Dashboard and Information Hierarchy.

### Problems / Challenges
- 
- 

### Solutions / Actions Taken
- 
- 

### Evidence
- Added code: 
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

- [Updated design] 
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?
- What needs improvement?
- What did I learn?

## Session [05]
**Date:** 10 April 2026  
**Time spent:** 45 min  
**Focus:** Implement home page layout and sign-up functionality in the tournament app

### Problems / Challenges
- My program did NOT want to put the home screen on display in my main code if I connected one to the other. It refused to do anything.
- 

### Solutions / Actions Taken
- My solution was putting the homepage code into the main code. 
- 

### Evidence
- Added code: The homepage code into the main code (nothing new added)
- [Updated design] 
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?
- What needs improvement?
- What did I learn?

## Session [06]
**Date:** 14 April 2026  
**Time spent:** 1 hour  
**Focus:** Refactor home and sign-up pages: adjust layout, improve alignment, and add participant input fields for first name, last name, and year group.

### Problems / Challenges
- 
- 

### Solutions / Actions Taken
- 
- 

### Evidence
- Added code: 
- [Updated design] 
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?
- What needs improvement?
- What did I learn?

## Session [07]
**Date:** 15 April 2026  
**Time spent:** 1 hour  
**Focus:** Refactor sign-up page: improve layout, add event selection options, and include team name dropdown.

### Problems / Challenges
- 
- 

### Solutions / Actions Taken
- 
- 

### Evidence
- Added code: 
 group_var = StringVar()
    group_var.set("Group")

    group_title = tk.Label(container, text="Group:", font=("Helvetica", 16))
    group_title.grid(row=9, column=0, pady=10, padx=5)

    individual_title = tk.Label(container, text="Individual:", font=("Helvetica", 16))
    individual_title.grid(row=9, column=1, pady=10, padx=5)

    group = Radiobutton(container, text="Group", variable=group_var, value="Group", command=clicked)
    group.grid(row=10, column=0, pady=10, padx=5)

    team_name_label = tk.Label(container, text="Team Name:", font=("Helvetica", 16))
    team_name_label.grid(row=11, column=0, pady=10, padx=5)

    individual = Radiobutton(container, text="Individual", variable=group_var, value="Individual", command=clicked)
    individual.grid(row=10, column=1, pady=10, padx=5)

    teamnames = ["Team name 1", 
                 "Team name 2", 
                 "Team name 3", 
                 "Team name 4"]

    dropdown = tk.OptionMenu(container, group_var, value=teamnames)
    dropdown.grid(row=12, column=0, pady=10, padx=5)

- [Updated design] 
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?
- What needs improvement?
- What did I learn?

## Session [08]
**Date:** 17 April 2026  
**Time spent:** 1 hour  
**Focus:** Add Treeview for participant data display: implement columns for first name, last name, year group, sport, and academic subjects.

### Problems / Challenges
- 
- 

### Solutions / Actions Taken
- 
- 

### Evidence
- Added code: 
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
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5]))
        count += 1

- [Updated design] 
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?
- What needs improvement?
- What did I learn?

## Session [09]
**Date:**  21 April 2026  
**Time spent:** 55 minutes   
**Focus:** Implement participant sign-up functionality: add participant data saving and loading, enhance sign-up page with dropdowns for year group and team name.

### Problems / Challenges
- Didn't know how to put all the data into a json file
- 

### Solutions / Actions Taken
- Youtube tutorial
- 

### Evidence
- Added code: 
PARTICIPANTS_FILE = "participants.json"
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
save_button = tk.Button(container, text="Submit", command=save_signup)
save_button.grid(row=13, column=1, pady=20, padx=5)

- [Updated design] 
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- What went well?
- What needs improvement?
- What did I learn?

# 7. Problems and Fixes

| Problem | Cause | Fix | Status |
|---|---|---|---|
| [Describe issue] | [Why it happened] | [What you did] | Open / Fixed |
| [Describe issue] | [Why it happened] | [What you did] | Open / Fixed |

---

# 11. Final Reflection

> Complete this section at the end of the project.

## What I achieved
- 
- 
- 

## What worked well
- 
- 
- 

## What did not work well
- 
- 
- 

## What I would improve next time
- 
- 
- 

## Final outcome
[Describe the final result]

## Did I meet the success criteria (designspecifications)?
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Final evaluation
[Write a short final judgment of the project]

---
- 
