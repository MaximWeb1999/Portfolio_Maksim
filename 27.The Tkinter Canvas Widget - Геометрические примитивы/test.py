from tkinter import *

# Создание виджета - полотно для рисования
cvs = Canvas(width=140, height=200)
cvs.pack()

# Создание линии
cvs.create_line(20, 100, 80, 20, fill='red', width=10)

# Создание прямоугольника
cvs.create_rectangle(80, 60, 140, 100, fill='blue', outline='red')

# Создание овала
cvs.create_oval(30, 130, 110, 190, fill='blue', outline='red')

mainloop()
