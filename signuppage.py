from tkinter import *
import tkinter as tk 
import os 
from tkinter import messagebox

#-------------GUI-------------
screen = tk.Tk()
screen.title("Ron's College Tournament App")
screen.geometry("1450x900")
screen.minsize(800, 500)

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
       