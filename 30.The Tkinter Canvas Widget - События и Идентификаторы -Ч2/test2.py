from tkinter import *

# Сдвиг для машинки
x = 10


def press_down(event):
    global x
    x += 10
    c.coords(car, 50+x, 200, 100+x, 225)
    c.coords(arrow, 55+x, 212, 95+x, 212)
    c.itemconfig(but, width=1)


def press_up(event):
    c.itemconfig(but, width=2)


c = Canvas(width=600, height=600)
c.pack()

but = c.create_rectangle(
    250, 50, 300, 75, fill='green', width=2, tag='blue_but')
but_txt = c.create_text(275, 62, text='press', font='12', tag='blue_but')

# Прямоугольник со стрелкой
car = c.create_rectangle(50, 200, 100, 225, fill='blue')
arrow = c.create_line(55, 212, 95, 212, fill='white', arrow=LAST)

c.tag_bind('blue_but', '<ButtonPress>', press_down)
c.tag_bind('blue_but', '<ButtonRelease>', press_up)

mainloop()
