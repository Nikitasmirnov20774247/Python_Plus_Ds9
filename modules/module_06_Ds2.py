# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


from random import randint as rd


def get_chessboard():
    chessboard = []

    for x in range(1, 9):
        line = []
        y = rd(1, 8)
        for i in range(1, 9):
            if i != y:
                line.append(0)
            else:
                line.append(1)
        chessboard.append(line)
    return chessboard


def print_chessboard(chessboard):
    for i in chessboard:
        print(i)


def check_chessboard(chessboard):
    x = []
    y = []
    for i in range(0, 8):
        for j in range(0, 8):
            if chessboard[i][j] == 1:
                x.append(i)
                y.append(j)
    for i in range(8):
        for j in range(i + 1, 8):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True


def chessboard_run():
    count = 1
    for i in range(4):
        check = False
        while check == False:
            chessboard = get_chessboard()
            check = check_chessboard(chessboard)
            count += 1
        print(f'Попытка №{count}')
        print_chessboard(chessboard)

if __name__ == '__main__':
    chessboard_run()
