from tkinter import *
import math
import datetime
# Вычисление x и y

# x


def x_coordinate(length, angle):
    return width/2 + length * math.cos(angle * math.pi / 180)

# y


def y_coordinate(length, angle):
    return height / 2 - length * math.sin(angle * math.pi / 180)


# Переменные
width = 400
height = 400
radius = 150
# Окно
root = Tk()
root.title('CLOCK')
# Рисуем окно
canvas = Canvas(root, width=width, height=height)
canvas.pack()
# рисуем круг
canvas.create_oval(width/2-radius, height/2-radius,
                   width/2+radius, height/2+radius)
# Секунданя стрелка
seconds = canvas.create_line(0, 0, 0, 0, fill='red')
# Минутная стрелка
minutes = canvas.create_line(0, 0, 0, 0)
# Часовая стрелка
hours = canvas.create_line(0, 0, 0, 0)

# Отвечает за изменение стрелки


def change_hand(length, time, clock_hand, degree):
    alpha = 90 - time * degree
    x1 = x_coordinate(0, alpha)
    y1 = y_coordinate(0, alpha)
    x2 = x_coordinate(length, alpha)
    y2 = y_coordinate(length, alpha)
    canvas.coords(clock_hand, x1, y1, x2, y2)

# Считает стрелки


def update():
    # Текущее время
    time = str(datetime.datetime.now())
    # Берем секунды
    sec = int(time[17:19])
    # Берем минуты
    min = int(time[14:16])
    # Берем часы
    h = int(time[11:13])
    # Секунданя стрелка
    change_hand(radius-20, sec, seconds, 6)
    # Минутная стрелка
    change_hand(radius-40, min, minutes, 6)
    # Часовая стрелка
    change_hand(radius / 2, h, hours, 30)

    # Вызов через 1 секунду
    root.after(1000, update)


# Размещение цифр
alpha = 60
for i in range(1, 13):
    canvas.create_text(x_coordinate(radius + 20, alpha),
                       y_coordinate(radius + 20, alpha),
                       text=i, fill='darkblue', font='Times 10 italic bold')
    alpha -= 30
# Рисуем стрелочки
for i in range(60):
    x1 = x_coordinate(radius, alpha)
    y1 = y_coordinate(radius, alpha)
    # Удленение стрелочки
    if alpha % 30 == 0:
        x2 = x_coordinate(radius-20, alpha)
        y2 = y_coordinate(radius-20, alpha)
    else:
        x2 = x_coordinate(radius-10, alpha)
        y2 = y_coordinate(radius-10, alpha)
    canvas.create_line(x1, y1, x2, y2)
    alpha += 6
# Запускаем
update()
root.mainloop()
