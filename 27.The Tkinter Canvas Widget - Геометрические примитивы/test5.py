from tkinter import *

cvs = Canvas(width=240, height=400)
cvs.pack()

cvs.create_rectangle(10, 10, 100, 50)

cvs.create_polygon(60, 60, 80, 60,
                   80, 80, 100, 80,
                   100, 100, 80, 100,
                   80, 120, 60, 120,
                   60, 100, 40, 100,
                   40, 80, 60, 80,
                   60, 60, fill='red')
cvs.create_text(120, 200, text='Hello World,\n Python\n and TK',
                justify=CENTER, font='Verdana 14')

mainloop()
