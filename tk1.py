import tkinter as tk
from tkinter import *
import pyttsx3
engine =pyttsx3.init()
# Import all tkinter components
# Import required libraries
root=Tk()
root.title("GUI")
root.geometry("400x400")
root.config(bg="lightblue")
root.resizable(False,False)
# Create a StringVar to store the name input
name=StringVar()
res=StringVar()
# Function to display greeting message
def dis():
    a = name.get()
    res.set("Welcome "+ a+"!")
    engine.say(res.get())
    engine.runAndWait()
    engine.stop()
# Create a LabelFrame container with title
lbl=Label(root, text="Enter name", font=("Georgia", 30, "bold"), fg="Red",bg="lightblue", bd=1)
lbl.pack(pady=10)
# Create and pack the label for name entry
txt=Entry(root, textvariable=name, font=("Georgia", 15, "bold"), bd=5)
txt.pack(pady=10)
# create and pack the button that triggers the greeting
btn=Button(root, text="Enter", font=("Georgia", 15, "bold"), bg="black", fg="white", command=dis)
btn.pack(pady=10)
# Create and pack the label to display the greeting message
lbl1=Label(root, textvariable=res, font=("Georgia", 20, "bold"), fg="black", bg="lightblue", bd=1)
lbl1.pack(pady=10)
# Configure the main window
root.mainloop()