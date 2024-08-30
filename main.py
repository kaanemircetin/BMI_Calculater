import tkinter as tk
from tkinter import *

window = Tk()
window.title("BMI calculater")
window.minsize(width=300, height=300)


def bmi_calculater():
    try:
        num1 = my_entry.get()
        num2 = my_entry1.get()
        num3 = int(num1)
        num4 = float(num2)
        label3.config(text=(num3 // (num4 ** 2)))
    except ValueError:
        label3.config(text="Write a number", font="Arial, 11")
        label3.place(x=100, y=160)


label_main = tk.Label(text="BMI Calculater", foreground="black", font="Arial, 24")
label_main.pack()

label1 = tk.Label(text="Please write your weight (k)", font="Arial, 11")
label1.place(x=11, y=70)

label2 = tk.Label(text="Please write your height (m)", font="Arial, 11")
label2.place(x=11, y=100)

my_button = tk.Button(text="calculate",
                      foreground="black",
                      activebackground="red",
                      activeforeground="white",
                      command=bmi_calculater)

label3 = tk.Label(text="BMI", font="Arial, 24", width=10)
label3.place(x=50, y=140)

my_button.config(width=10)
my_button.place(x=110, y=200)

my_entry = tk.Entry(width=10)
my_entry.place(x=195, y=70)

my_entry1 = tk.Entry(width=10)
my_entry1.place(x=195, y=100)

window.mainloop()
