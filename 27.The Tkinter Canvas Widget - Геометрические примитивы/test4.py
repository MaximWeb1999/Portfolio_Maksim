from tkinter import *

cvs = Canvas(width=200, height=330)
cvs.pack()

# Рисование светофора
cvs.create_rectangle(50, 25, 150, 330, fill='white', outline='black', width=5)
cvs.create_oval(55, 230, 145, 330, fill='green', width=5)
cvs.create_oval(55, 130, 145, 230, fill='yellow', width=5)
cvs.create_oval(55, 30, 145, 130, fill='red', width=5)
