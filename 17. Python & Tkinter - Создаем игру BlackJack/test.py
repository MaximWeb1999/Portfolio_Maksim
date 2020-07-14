from tkinter import *
from random import *

# Колода карт. 4 масти. Вес карт. Количество
pack_of_cards = [2, 3, 4, 5, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз'] * 4

# Тасовка колоды карт
shuffle(pack_of_cards)

# Количество очков
count = 0


# Команда взять карту
def take():
    # глобальные переменные
    global count, pack_of_car

    # Берем случайную карту(первую)
    card = pack_of_cards.pop()

    # Опрделяем цену картам (очки)
    if card == 'Валет' or card == 'Дама' or card == 'Король':
        card = 10

    if card == 'Туз':
        card = 11

    # Увеличиваем количество очков
    count += card

    # Обработка условаия
    if count > 21:
        # Поражение
        text3['text'] = 'Вы проиграли, у Вас ' + str(count) + ' очков'
        text2['text'] = 'Вы проиграли'
    else:
        # Вывод очков на экран
        text2['text'] = 'У Вас ' + str(count) + ' очков'


# Команда хватит
def enough():
    # Глобальная переменная
    global count

    # Обработка условаия
    if count == 21:
        # Победа
        text3['text'] = 'Поздравляем, у Вас 21!'

    if count < 21:
        # Вывод очков
        text3['text'] = 'У Вас ' + str(count) + ' очков'


# Создание интерфейса
root = Tk()
root.geometry('300x140')

text1 = Label(root, text='Игра в Black-Jack', fg='red')
text1.place(x=100, y=0)

text2 = Label(root, text='У вас 0 очков', fg='blue')
text2.place(x=110, y=30)

but1 = Button(root, width='15', text='Взять карту', command=take)
but1.place(x=20, y=60)

but2 = Button(root, width='15', text='Хватит', command=enough)
but2.place(x=160, y=60)

text3 = Label(root, text='Результат игры', fg='red')
text3.place(x=90, y=100)

root.mainloop()
