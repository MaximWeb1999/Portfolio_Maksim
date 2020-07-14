from tkinter import *

cvs = Canvas(width=200, height=400)
cvs.pack()

# Рисование прямоугольников
cvs.create_rectangle(0, 400, 200, 300, fill='blue')
cvs.create_rectangle(25, 300, 175, 200, fill='red')
cvs.create_rectangle(50, 200, 150, 100, fill='green')
