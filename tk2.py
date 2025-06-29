import tkinter as tk
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("400x400")
root.resizable(False,False)
name=StringVar()
res=StringVar()
def salary():

    a =float(name.get())
    s = a + (a * 0.12) + (a * 0.1)
    res.set(f"Total Salary is {s:.2f} Rs")

lbl=Label(root,text="Enter Basic Salary",font=("bold",20),bd=1)
lbl.pack(pady=10)
txt=Entry(root,textvariable=name,font=("bold",15),bd=5)
txt.pack(pady=10)
btn=Button(root,text="Enter",font=10,bg="black",fg="white",command=salary)
btn.pack(pady=10)
lbl1=Label(root,textvariable=res,font=("bold",20),bd=1)
lbl1.pack(pady=10)
root.mainloop()
