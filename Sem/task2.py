# ✔ Дорабатываем задачу 1.
# ✔ Превратите внешнюю функцию в декоратор.
# ✔ Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# ✔ Если не входят, вызывать функцию со случайными числами
# из диапазонов.


import random


def check_data(func):
    def wrapper(answer, attempts):
        if not (1 <= answer <= 100):
            answer = random.randint(1, 100)
        if not (1 <= attempts <= 10):
            attempts = random.randint(1, 10)
        func(answer, attempts)
        
    return wrapper


@check_data
def func(answer, attempts):
    print(answer, attempts)


func(55,50)
