import random
import tkinter
from tkinter import *

def natural_note():
    notes = ["C", "D", "E", "F", "G", "A", "B"]
    note = random.choice(notes)
    label.config(text=note)

def any_note():
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note = random.choice(notes)
    label.config(text=note)

root = Tk()
root.geometry("300x200")
root.title("Musical Note Generator")

button_frame = Frame(root)
button_frame.pack(side=tkinter.TOP)

natural_button = Button(button_frame, text="Natural Note", command=natural_note)
natural_button.pack(side=tkinter.LEFT)

any_button = Button(button_frame, text="Any Note", command=any_note)
any_button.pack(side=tkinter.LEFT)

button_frame = Frame(root)
button_frame.pack(side=tkinter.TOP)

label = Label(root, font='Times 22', width=60, height=15)
label.pack()

root.mainloop()