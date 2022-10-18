from tkinter import Y


x = 0
y = 0

# Метод инициализации x и y
def init(a, b):
    global x
    global y
    x = a
    y = b

# Метод складывания
def sum():
    return x+y
