# Import required libraries
import tkinter as tk
from tkinter import *  # Import all tkinter components
import pyttsx3  # Text-to-speech conversion library

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to handle text-to-speech conversion
def spk():
    engine.say(Text.get())  # Convert text to speech
    engine.runAndWait()     # Wait until speech is complete
    engine.stop()           # Stop the engine

# Create the main window
root = Tk()

# Create a StringVar to store the input text
Text = StringVar()

# Create a LabelFrame container with title
obj = LabelFrame(root, text="Text to Speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

# Create and pack the label for text entry
lbl = Label(obj, text="Enter Text", font=30)
lbl.pack(side=tk.LEFT, padx=5)

# Create and pack the text entry field
text = Entry(obj, textvariable=Text, font=30, width=18, bd=5)
text.pack(side=tk.LEFT, padx=10)

# Create and pack the button that triggers speech
btn = Button(obj, text="Very_Well", font=10, bg="black", fg="white", command=spk)
btn.pack(side=tk.LEFT, padx=10)

# Configure the main window
root.title("Text to Speech")          # Set window title
root.geometry("510x200")             # Set window size
root.resizable(False, False)         # Disable window resizing

# Start the main event loop
root.mainloop()

