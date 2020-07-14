from tkinter import *

c = Canvas(width=300, height=200, bg='white')
c.pack()

# Кружок
ball = c.create_oval(50, 100, 90, 140, fill='red')

# Анимация. ДВижение вправо


def motion():
    c.move(ball, 1, 0)
    c.after(100, motion)


motion()

mainloop()
