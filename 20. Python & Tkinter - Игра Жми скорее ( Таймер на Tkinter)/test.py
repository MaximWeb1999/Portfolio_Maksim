from tkinter import*

# Количество секунд
sec = 0


# Кнопка старт
def start():
    # глобальная переменная
    global sec
    # Делаем кнопку активной
    b1['state'] = 'normal'
    # Увеличиваем количество секунд на 1
    sec += 1
    # Обработка условия
    if sec < 10:
        # Запускает функцию старт через 1 секунду
        root.after(1000, start)
        # Вывод количество секунд
        t1.config(text=str(sec))
    else:
        # Делаем кнопку неактивной
        b1['state'] = 'disable'
        # Вывод на экран результат
        t1.config(text='За ' + str(sec)+' секунд '+str(count)+' нажатий')


# Количество кликов
count = 0


# Логика кнопки жми
def click():
    global count
    count += 1
    b1.config(text='Нажатий - ' + str(count))


# Интерфейс
root = Tk()
root.geometry('150x80')

t1 = Label(root, text='Нажмините старт для начала')
t1.pack()

b1 = Button(root, text='Жми', command=click)
b1.pack()
b1['state'] = 'disabled'

b2 = Button(root, text='старт', command=start)
b2.pack()

root.mainloop()
