# ✔ Создайте модуль с функцией внутри.
# ✔ Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
# ✔ Внутри генерируется случайное число в указанных
# границах и пользователь должен угадать его за
# заданное число попыток.
# ✔ Функция выводит подсказки “больше” и “меньше”.
# ✔ Если число угадано, возвращается истина, а если
# попытки исчерпаны - ложь.


from random import randint as rd
import sys


def guess(down, up, tries):
    if down > up:
        up, down = down, up
    aim = rd(down, up)
    count = 0
    while count<tries:
        try:
            tmp = int(input('Введите целое число: '))
        except:
            print('Нужно ввести ЦЕЛОЕ число')
            count += 1
            continue
        if tmp < aim:
            print('Число больше')
        elif tmp > aim:
            print('Число меньше')
        else:
            print('Молодец! угадал')
            return True
        count += 1
    return False


if __name__ == '__main__':
    print(guess(10, 100, 9))


# из модуля в командной строке терминала.
# ✔ Строка должна принимать от 1 до 3 аргументов:
# параметры вызова функции.
# ✔ Для преобразования строковых аргументов
# командной строки в числовые параметры
# используйте генераторное выражение.


def guess_2(down = 10, up = 100, tries = 10):
    if down > up:
        up, down = down, up
    aim = rd(down, up)
    count = 0
    while count<tries:
        try:
            tmp = int(input('Введите целое число: '))
        except:
            print('Нужно ввести ЦЕЛОЕ число')
            count += 1
            continue
        if tmp < aim:
            print('Число больше')
        elif tmp > aim:
            print('Число меньше')
        else:
            return True
        count += 1
    return False


if __name__ == '__main__':
    if len(sys.argv) == 2:
        tries = int(sys.argv[1])
        print(guess_2(tries=tries))
    elif len(sys.argv) == 4:
        up, down, tries = (int(i) for i in sys.argv[1:])
        print(guess_2(up, down, tries))
    else:
        print('Неверное количество аргументов')
