import tkinter as tk
from tkinter import *
import random
root=Tk()
root.geometry("700x450")
root.resizable(False,False)
root.configure(bg="black")
root.title("Pasha_Pheko")
label=Label(root,text="Ab hoga naga nach",font=("times",260))
def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()
button=Button(root,text="Roll the Dice",width=40,height=5,font=3,bg="blue",bd=8,command=roll)
button.pack(padx=10,pady=10)
root.mainloop()