# возможными вариантами отгадок и количество
# попыток на угадывание.
# ✔ Программа возвращает номер попытки, с которой
# была отгадана загадка или ноль, если попытки
# исчерпаны.


def riddle_game(quest, answers: list, attempts):
    print(f'Загадка: {quest}')
    count = 0
    while count < attempts:
        answer = input('Введите свой ответ: ')
        if answer.lower() in map(str.lower, answers):
            return count + 1
        count += 1
    return 0


# ✔ Добавьте в модуль с загадками функцию, которая
# хранит словарь списков.
# ✔ Ключ словаря - загадка, значение - список с
# отгадками.
# ✔ Функция в цикле вызывает загадывающую функцию,
# чтобы передать ей все свои загадки.


def get_circle_riddles_1(riddles: dict):
    for question, answers in riddles.items():
        result = riddle_game(question, answers, 3)
        print(f"Вы угадали с {result} попытки\n" if result != 0 else "Вы не угадали\n")


if __name__ == '__main__':
    riddles_ = {"Сидит дед в сто шуб одет, кто его раздевет, тот слёзы проливает": ['лук', 'onion'],
                "Висит груша нельзя скушать": ["лампочка", "лампа", "light bulb"]}
    get_circle_riddles_1(riddles_)


# ✔ Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число
# (номер попытки, с которой она угадана).
# ✔ Функция формирует словарь с информацией о
# результатах отгадывания.
# ✔ Для хранения используйте защищённый словарь
# уровня модуля.
# ✔ Отдельно напишите функцию, которая выводит
# результаты угадывания из защищённого словаря в
# удобном для чтения виде.
# ✔ Для формирования результатов используйте
# генераторное выражение.


_results = dict()


def get_circle_riddles_2(riddles: dict):
    global _results
    for question, answers in riddles.items():
        _results[question] = riddle_game(question, answers, 3)
        print()
    return _results


def show_results():
    global _results
    for question, result, in _results.items():
        print(f"С загадкой: {question}")
        print("Ваш результат: ", end="")
        print(f"Вы угадали с {result} попытки\n" if result != 0 else "Вы не угадали\n")


if __name__ == '__main__':
    riddles_ = {"Сидит дед в сто шуб одет, кто его раздевет, тот слёзы проливает": ['лук', 'onion'],
                "Висит груша нельзя скушать": ["лампочка", "лампа", "light bulb"]}
    get_circle_riddles_2(riddles_)
    show_results()