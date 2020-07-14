from tkinter import*


def plus():
    n1 = int(e1.get())
    n2 = int(e2.get())
    result = n1 + n2
    t1.config(text=str(result))


def minus():
    n1 = int(e1.get())
    n2 = int(e2.get())
    result = n1 - n2
    t1.config(text=str(result))


def multiply():
    n1 = int(e1.get())
    n2 = int(e2.get())
    result = n1 * n2
    t1.config(text=str(result))


def division():
    n1 = int(e1.get())
    n2 = int(e2.get())
    result = n1 / n2
    t1.config(text=str(result))


win = Tk()
win.geometry('200x180')
win.title('Calc')

t1 = Label(win, text='Введите два числа')
t1.pack()

e1 = Entry(win, width=20)
e1.pack()

e2 = Entry(win, width=20)
e2.pack()

b1 = Button(win, text='Сложение', command=plus)
b1.pack()

b2 = Button(win, text='Вычитание', command=minus)
b2.pack()

b3 = Button(win, text='Умножение', command=multiply)
b3.pack()

b4 = Button(win, text='Деление', command=division)
b4.pack()

win.mainloop()
