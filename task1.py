import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")

eoutput = StringVar()
eoutput.set("Here goes thr output")

def function():
    




button1 = tk.Button(window, text="Calculate")
entry1 = tk.Entry(window, width=10)
triangle = PhotoImage(file="triangle.png")
entry2 = tk.Entry(window, width=10)
entry3 = tk.Entry(window, width=10)
label1 = tk.Label(window, text="Enter in as much information about the\n triangle shown and I will calcualte the area")

button1.grid(row=1, column=1)
entry1.grid(row=1, column=1)
triangle.grid(row=1, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=1, column=1)
lable1.grid(row=1, column=1)

window.mainloop()