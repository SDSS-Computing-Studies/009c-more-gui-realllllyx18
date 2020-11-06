#!python3
import tkinter as tk
from tkinter import *
import math

window = tk.Tk()
window.title("tk")
window.geometry("500x400")

eoutput = StringVar()
eoutput.set("Here goes thr output")

def function():
    a = aentry.get()
    b = bentry.get()
    c = centry.get()
    h = hentry.get()
    a = float(a)
    b = float(b)
    c = float(c)
    h = float(h)

    if h != "":
        if b != "":
           area = b*h/2
           A = str(area)
           output.set("The area of the triangle is: " + A)
        elif a != "" and c != "":
            b = math.sqrt(a**2-h**2) + math.sqrt(c**2-h**2)
            area = b*h/2
            A = str(area)
            output.set("The area of the triangle is: " + A)
        else:
            output.set("Cannot be calculated.\nPlease try again.")
    else:
        if a != "" and b != "" and c != "":
            s = (a+b+c)/2
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            A = str(area)
            output.set("The area of the triangle is: " + A)
        else:
            output.set("Cannot be calculated.\nPlease try again.")

button1 = tk.Button(window, text="Calculate", command=function)
triangle = PhotoImage(file="triangle.png")
label1 = tk.Label(window, image=triangle)
aentry = tk.Entry(window, width=5)
bentry = tk.Entry(window, width=5)
centry = tk.Entry(window, width=5)
hentry = tk.Entry(window, width=5)

output = StringVar()
instruction = "Enter in as much information about the\n triangle shown and I will calcualte the area"
output.set(instruction)
entry1 = tk.Entry(window, textvariable=output, width=len(instruction))

label1.place(x=0,y=0)
entry1.place(x=0,y=300)
button1.place(x=300,y=350)
aentry.place(x=100,y=150)
hentry.place(x=300,y=150)
centry.place(x=400,y=150)
bentry.place(x=300,y=250)

window.mainloop()
