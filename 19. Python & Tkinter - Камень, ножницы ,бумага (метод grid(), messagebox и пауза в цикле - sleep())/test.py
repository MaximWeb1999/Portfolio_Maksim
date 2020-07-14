from tkinter import *
# Импорт всплывающих окон
from tkinter import messagebox
from random import *
from time import *

# Очки
pc_score = 0
user_score = 0
# Выбор фигуры
pc_figur = ''
user_figur = ''


# Логика кнопки камень
def stone():
    # Глобальная переменная
    global user_figur
    # Окрашиваем кнопку
    k_but['bg'] = 'green'
    n_but['bg'] = 'white'
    b_but['bg'] = 'white'
    # Пользователь выбрал камень
    user_figur = 'камень'
    # Состояние кнопки активна
    pc_but['state'] = 'normal'


# Логика кнопки ножницы
def scissors():
    # Глобальная переменная
    global user_figur
    # Окрашиваем кнопку
    k_but['bg'] = 'white'
    n_but['bg'] = 'green'
    b_but['bg'] = 'white'
    # Пользователь выбрал ножницы
    user_figur = 'ножницы'
    # Состояние кнопки активна
    pc_but['state'] = 'normal'


# Логика кнопки бумага
def paper():
    # Глобальная переменная
    global user_figur
    # Окрашиваем кнопку
    k_but['bg'] = 'white'
    n_but['bg'] = 'white'
    b_but['bg'] = 'green'
    # Пользователь выбрал бумага
    user_figur = 'бумага'
    # Состояние кнопки активна
    pc_but['state'] = 'normal'


def go():
    # Глобальные переменные
    global pc_figur, user_figur, user_score, pc_score
    # Анимация выбора компьютера
    for i in range(30):
        # Генерируем случайное число(1,2,3)
        rand = randint(1, 4)
        # Обработка условия
        if rand == 1:
            pc_figur = 'камень'
        if rand == 2:
            pc_figur = 'ножницы'
        if rand == 3:
            pc_figur = 'бумага'
        # Вывод на экран выбор pc
        t4['text'] = 'выбор pc - ' + pc_figur
        # Обновляем виджет(текст)
        t4.update()
        # Ждем
        sleep(0.1)

    # Ничья
    if pc_figur == user_figur:
        # Вывод на экран сообщение(заголовок,сообщение)
        messagebox.showinfo('result', 'Drow')
    else:
        # Обработка условия
        if pc_figur == 'камень' and user_figur == 'ножницы':
            pc_score += 1
            messagebox.showinfo('result', 'PC Победил')
        if pc_figur == 'камень' and user_figur == 'бумага':
            user_score += 1
            messagebox.showinfo('result', 'user Победил')

        if pc_figur == 'ножницы' and user_figur == 'бумага':
            pc_score += 1
            messagebox.showinfo('result', 'PC Победил')
        if pc_figur == 'ножницы' and user_figur == 'камень':
            user_score += 1
            messagebox.showinfo('result', 'user Победил')

        if pc_figur == 'бумага' and user_figur == 'камень':
            pc_score += 1
            messagebox.showinfo('result', 'PC Победил')
        if pc_figur == 'бумага' and user_figur == 'ножницы':
            user_score += 1
            messagebox.showinfo('result', 'user Победил')
        # вывод на экран
        t5['text'] = 'Игрок - ' + str(user_score)
        t6['text'] = 'PC - ' + str(pc_score)

    pc_but['state'] = 'disabled'

    # Создание интерфейса
    # Создание окна
root = Tk()
# Название окна
root.title('KNB')

# Заголовок программы
t1 = Label(root, text='Камень, ножницы, бумага', fg='red')
# Расположение по строкам и столбцам
t1.grid(row=0, column=1)
t2 = Label(root, text='Выбор игрока', fg='green')
t2.grid(row=1, column=1)

# Кнопки
k_but = Button(root, text='Камень', command=stone)
k_but.grid(row=2, column=0)
n_but = Button(root, text='Ножницы', command=scissors)
n_but.grid(row=2, column=1)
b_but = Button(root, text='Бумага', command=paper)
b_but.grid(row=2, column=2)

# Выбор компьютера
t3 = Label(root, text='Выбор Компьютера', fg='blue')
t3.grid(row=3, column=1)

# Кнопка сгенерировать
pc_but = Button(root, text='Сгенерировать', command=go)
# Состояние кнопки неактивна
pc_but['state'] = 'disabled'
pc_but.grid(row=4, column=1)

# Надписи
t4 = Label(root, text='Выбор pc - 0', fg='red')
t4.grid(row=6, column=1)
t5 = Label(root, text='Игрок - 0', fg='green')
t5.grid(row=7, column=0)
t6 = Label(root, text='PC - 0', fg='blue')
t6.grid(row=7, column=2)

root.mainloop()
