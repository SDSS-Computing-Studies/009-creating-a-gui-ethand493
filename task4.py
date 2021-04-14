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


label1.place(x=50,y=10)

label2.place(x=120,y=60)

label3.place(x=-1,y=120)





window.mainloop()