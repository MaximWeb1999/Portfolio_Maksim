from tkinter import *

c = Canvas(width=300, height=200, bg='white')
# Фокусируем внимание клавиатуры на окно
c.focus_set()
c.pack()

# Шарик
ball = c.create_oval(50, 100, 90, 140, fill='red')


def control(event):
    # Проверка ключей клавиш
    if event.keysym == 'Left':
        c.move(ball, -5, 0)
    if event.keysym == 'Right':
        c.move(ball, 5, 0)
    if event.keysym == 'Up':
        c.move(ball, 0, -5)
    if event.keysym == 'Down':
        c.move(ball, 0, 5)


# Приявязка к любой клавише клавиатуры
c.bind('<Key>', control)

mainloop()
