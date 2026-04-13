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
