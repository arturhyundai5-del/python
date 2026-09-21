from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Приложение на Tkinter")
root.geometry("300x250")

num1 = ttk.Entry(root)
num1.pack()


num2 = ttk.Entry(root)
num2.pack()

result = Text(root, height=5, width=20)
result.pack()


def sum_numbers():
    result.delete("1.0", END)  # очищаем поле
    num1val = int(num1.get())
    num2val = int(num2.get())
    result.insert(END, num1val + num2val)

def minus_numbers():
    result.delete("1.0", END)
    num1val = int(num1.get())
    num2val = int(num2.get())
    result.insert(END, num1val - num2val)

def multiple_numbers():
    result.delete("1.0", END)
    num1val = int(num1.get())
    num2val = int(num2.get())
    result.insert(END, num1val * num2val)

def divide_numbers():
    result.delete("1.0", END)
    num1val = int(num1.get())
    num2val = int(num2.get())
    result.insert(END, num1val / num2val)
    

plus = ttk.Button(root, text="+", command=sum_numbers)
plus.pack()

minus = ttk.Button(root, text="-", command=minus_numbers)
minus.pack()

mult = ttk.Button(root, text="*", command=multiple_numbers)
mult.pack()


div = ttk.Button(root, text="/", command=divide_numbers)
div.pack()


root.mainloop()
