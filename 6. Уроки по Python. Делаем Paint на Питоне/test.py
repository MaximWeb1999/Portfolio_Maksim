from tkinter import *

canvas_width = 700
canvas_height = 500
bruch_size = 3
color = 'black'


def paint(event):
    global bruch_size
    global color
    x1 = event.x - bruch_size
    x2 = event.x + bruch_size
    y1 = event.y - bruch_size
    y2 = event.y + bruch_size
    w.create_oval(x1, y1, x2, y2,
                  fill=color, outline=color)


def bruch_size_change(new_size):
    global bruch_size
    bruch_size = new_size


def color_change(new_color):
    global color
    color = new_color


root = Tk()
root.title('Paint на Питоне')

w = Canvas(root,
           width=canvas_width,
           height=canvas_height,
           bg='white')
w.bind('<B1-Motion>', paint)

red_btn = Button(text='Красный', width=10,
                 command=lambda: color_change('red'))
blue_btn = Button(text='Синий', width=10,
                  command=lambda: color_change('blue'))
black_btn = Button(text='Чёрный', width=10,
                   command=lambda: color_change('black'))
white_btn = Button(text='Ластик', width=10,
                   command=lambda: color_change('white'))

clear_btn = Button(text='Удалить всё', width=10,
                   command=lambda: w.delete('all'))

two_bth = Button(text='2', width=10,
                 command=lambda: bruch_size_change(2))
five_bth = Button(text='5', width=10,
                  command=lambda: bruch_size_change(5))
ten_bth = Button(text='10', width=10,
                 command=lambda: bruch_size_change(10))
twelve_bth = Button(text='20', width=10,
                    command=lambda: bruch_size_change(20))
forty_bth = Button(text='40', width=10,
                   command=lambda: bruch_size_change(40))


w.grid(row=2, column=0,
       columnspan=7, padx=5,
       pady=5, sticky=E+W+S+N)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

red_btn.grid(row=0, column=2)
blue_btn.grid(row=0, column=3)
black_btn.grid(row=0, column=4)
white_btn.grid(row=0, column=5)
clear_btn.grid(row=0, column=6, sticky=W)

two_bth.grid(row=1, column=2)
five_bth.grid(row=1, column=3)
ten_bth.grid(row=1, column=4)
twelve_bth.grid(row=1, column=5)
forty_bth.grid(row=1, column=6, sticky=W)

root.mainloop()
