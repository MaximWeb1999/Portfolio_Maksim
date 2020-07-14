from tkinter import *

c = Canvas(width=300, height=200, bg='white')
c.pack()

# Кружок
ball = c.create_oval(50, 100, 90, 140, fill='red')

# Анимация


def motion():
    # Движение вправо
    c.move(ball, 1, 0)
    # Обработка при касания правого края
    if c.coords(ball)[2] > 300:
        c.coords(ball, 50, 100, 90, 140)
    c.after(100, motion)


motion()

mainloop()
