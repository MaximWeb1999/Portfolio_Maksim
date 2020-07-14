from tkinter import *


def press_down(event):
    cs.itemconfig(but, width=1)


def press_up(event):
    cs.itemconfig(but, width=5)


cs = Canvas(width=600, height=600)
cs.pack()


but = cs.create_rectangle(250, 50, 300, 75,
                          fill='green', width=5, tag='blue_but')
but_txt = cs.create_text(275, 62, text='press', font='12', tag='blue_but')

cs.tag_bind('blue_but', '<ButtonPress>', press_down)
cs.tag_bind('blue_but', '<ButtonRelease>', press_up)

mainloop()
