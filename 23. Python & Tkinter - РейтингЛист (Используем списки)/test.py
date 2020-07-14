from tkinter import *

# Оценки
marks = []

# Функции
def upload():
    # Глобальная переменная
    global marks
    # Пустой список lis
    lis = []
    # Получаем символы с пробелами
    s = edit1.get()
    # В пустой список lis попадут все символы без пробелов
    lis = s.split(' ')
    # Временная переменная
    temp = ''
    # Проходим по списку lis
    for val in lis:
        # Обработка условия
        if int(val) < 13:
            # Добавляем в список marks
            marks.append(int(val))
            # Добавляем все элементы lis + пробелы
            temp += val + ' '
    # Вывод строки temp на экран
    text11['text'] = 'Список загружен ' + temp


def mean():
    global marks
    mark = 0
    summ = 0
    for value in marks:
        summ += value
    mark = summ / len(marks)
    text2['text'] = str(mark)


def maximum():
    global marks
    big = marks[0]
    for value in marks:
        if value > big:
            big = value
    text3['text'] = str(big)


def minimum():
    global marks
    small = marks[0]
    for value in marks:
        if value < small:
            small = value
    text4['text'] = str(small)


def ten():
    global marks
    count = 0
    for value in marks:
        if value == 10:
            count += 1
    text5['text'] = str(count)


# Интрефейс
root = Tk()
root.geometry('300x250')

text1 = Label(root, text='Введите оценки через пробел', fg='red')
text1.place(x=70, y=0)

but1 = Button(root, text='Загрузить', command=upload)
but1.place(x=20, y=30)

edit1 = Entry(root, width=30)
edit1.place(x=100, y=33)

text11 = Label(root, text='Список не загружен', fg='green')
text11.place(x=40, y=60)

but2 = Button(root, width=10, text='Средний бал', command=mean)
but2.place(x=20, y=90)
text2 = Label(root, text='Средний бал')
text2.place(x=120, y=93)

but3 = Button(root, width=10, text='Максимум', command=maximum)
but3.place(x=20, y=120)
text3 = Label(root, text='Максимальный бал')
text3.place(x=120, y=123)

but4 = Button(root, width=10, text='Минимум', command=minimum)
but4.place(x=20, y=150)
text4 = Label(root, text='Минимальный бал')
text4.place(x=120, y=153)

but5 = Button(root, width=10, text='10', command=ten)
but5.place(x=20, y=180)
text5 = Label(root, text="Количество 10")
text5.place(x=120, y=183)
