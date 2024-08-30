import tkinter as tk
from tkinter import *


window = Tk()
window.title("BMI calculater")
window.minsize(width=300, height=300)


def bmi_calculater():
    try:
        num1 = weight_value.get()
        num2 = height_value.get()
        num3 = int(num1)
        num4 = float(num2)
        result.config(text=(num3 // (num4 ** 2)))
    except ValueError:
        result.config(text="Write a number", font="Arial, 11")
        result.place(x=100, y=160)
    if  num3 //(num4 ** 2)< 18.5:
        result2.config(text="You're underweight")
    elif 25 > num3 //(num4 ** 2) > 18.5:
        result2.config(text="You're normal")
    elif 35 > num3 //(num4 ** 2) > 25:
        result2.config(text="You're overweight")
    elif num3 //(num4 ** 2) > 35:
        result2.config(text="You're obese")


main_name = tk.Label(text="BMI Calculater", foreground="black", font="Arial, 24")
main_name.pack()

question_weight = tk.Label(text="Please write your weight (k)", font="Arial, 11")
question_weight.place(x=11, y=70)

question_height = tk.Label(text="Please write your height (m)", font="Arial, 11")
question_height.place(x=11, y=100)

my_button = tk.Button(text="calculate",
                      foreground="black",
                      activebackground="red",
                      activeforeground="white",
                      command=bmi_calculater)

result = tk.Label(text="BMI", font="Arial, 24", width=10)
result.place(x=50, y=140)

result2 = tk.Label(text="Your level", font="Arial, 24", width=10)
result2.place(x=50, y=250)

my_button.config(width=10)
my_button.place(x=110, y=200)

weight_value = tk.Entry(width=10)
weight_value.place(x=195, y=70)

height_value = tk.Entry(width=10)
height_value.place(x=195, y=100)


window.mainloop()
