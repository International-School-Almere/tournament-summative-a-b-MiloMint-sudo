from tkinter import *
import tkinter as tk 
import os 
from tkinter import messagebox

def setup_signup_page(parent):
    
    def clicked():
        my_label.config(text=f'You selected event is: {radvar.get()}.')

    radvar = StringVar()
    radvar.set("Basketball")

    sport1 = Radiobutton(parent, text="Basketball", variable=radvar, value="Basketball", command=clicked)
    sport1.grid(pady=10, column=1, padx=5, row=1)

    sport2 = Radiobutton(parent, text="Soccer", variable=radvar, value="Soccer", command=clicked)
    sport2.grid(pady=10, column=2, padx=5, row=1)

    sport3 = Radiobutton(parent, text="Tennis", variable=radvar, value="Tennis", command=clicked)
    sport3.grid(pady=10, column=3, padx=5, row=1)

    my_label = Label(parent, text=" ", font=("Helvetica", 16))
    my_label.grid(pady=10)
