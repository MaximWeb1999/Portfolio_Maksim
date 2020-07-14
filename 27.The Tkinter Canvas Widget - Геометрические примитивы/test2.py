from tkinter import *

cvs = Canvas(width=200, height=400)
cvs.pack()

# Создание крестика
cvs.create_line(0, 0, 200, 400, fill='red', width=10)
cvs.create_line(200, 0, 0, 400, fill='blue', width=10)

mainloop()
