from tkinter import *
from tkinter import messagebox

# Рисуем окно
root = Tk()
# Название окна
root.title('Викторина')
# Размеры окна
root.geometry('300x300')
# Запускаем
# Создание функции


def que_one():
    # Вопрос задаем
    question = Label(root, text='Висит груша и ее нельзя скушать, что это?')
    # Ввод для ответа
    answer = Entry()
    # Кнопка ответить
    btn = Button(root, text='ответить', command=lambda: game1(que_two))
    # Размещение кнопки
    question.grid()
    answer.grid()
    btn.grid()

    # Создание функции для проверки ответа
    def game1(que_two):
        if answer.get().lower() == 'лампочка':
            que_two()
        else:
            messagebox.showerror('Ошибка!', 'Попробуй еще раз!')


def que_two():
    question_2 = Label(root, text='Зимой и летом одного цвета?')
    answer_2 = Entry()
    btn_2 = Button(root, text='Ответить!', command=lambda: game2(que_two))
    question_2.grid()
    answer_2.grid()
    btn_2.grid()

    def game2(que_two):
        if answer_2.get().lower() == 'ёлка':
            messagebox.showinfo('Победа!', 'ты молодец!')
        else:
            messagebox.showerror('Ошибка!', "Попробуй еще раз!")


que_one()

root.mainloop()
