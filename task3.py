#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
nF = Frame()

dogphoto = PhotoImage(file="dog.png")

label1 = tk.Label(window, image=dogphoto, borderwidth=3)

label2 = tk.Label(window, text="Pochancco!")

label3 = Label(window,text="A cuddly little puppy! This is from the same\n creators that brought you Keropi and Kero Kero", background="#aaffff")

label1.grid(row = 1, column = 2)

label2.grid(row = 1, column = 3)

label3.grid(row = 2, column = 1, columnspan = 4)





window.mainloop()