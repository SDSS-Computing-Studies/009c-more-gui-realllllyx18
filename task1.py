import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")

eoutput = StringVar()
eoutput.set("Here goes thr output")

def function():
    a = float(a)
    b = float(b)
    c = float(c)
    h = float(h)
    s = float(s)
    A = float(A)
    if a > 0 and b > 0 and c > 0:
        s = (a+b+c)/2
        A = math.sqrt(s(s-a)*(s-b)*(s-c))
    else:
        A = b*h/2

button1 = tk.Button(window, text="Calculate")
entry1 = tk.Entry(window, width=15)
triangle = PhotoImage(file="triangle.png")
entry2 = tk.Entry(window, width=15)
entry3 = tk.Entry(window, width=15)
label1 = tk.Label(window, text="Enter in as much information about the\n triangle shown and I will calcualte the area")
label2 = tk.Label(window, image=triangle)

label2.grid(row=1, column=1, rowspan=1)
button1.grid(row=5, column=1)
entry1.grid(row=1, column=0)
entry2.grid(row=2, column=1)
entry3.grid(row=3, column=1)
label1.grid(row=4, column=1)

window.mainloop()