from random import *

print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    if n.isdigit() and 0 < int(n) <= 100:
        return True
    return False


def game():
    n = int(input('До какого числа хотите угадать? (от 1 и до ...): '))
    r_n = randint(1, n + 1)
    count = 0
    while True:
        user = input('Введите число от 1 до'+ ' ' + str(n) + ': ')
        if is_valid(user):
            user = int(user)
        else:
            print('А может быть все таки введем целое число от 1 до'+' ' + n)
            continue
        # if is_valid(user):
        if user < r_n:
            print('Ваше число меньше загаданного, попробуйте еще раз')
            count += 1
        elif user > r_n:
            print('Ваше число больше загаданного, попробуйте еще раз')
            count += 1
        elif user == r_n:
            print('Вы угадали число за {} попыток, поздравляем!'.format(count))
            answer = input('Еще хотите испытать удачу?!: ').lower()
            if answer == 'да':
                print('Отлично! Погнали')
                game()
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся!)')
        # else:
        #     print('А может быть все таки введем целое число от 1 до' + ' ' + n)


game()
