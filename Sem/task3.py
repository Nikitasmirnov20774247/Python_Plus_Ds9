# ✔ Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# ✔ Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# ✔ Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# ✔ Имя файла должно совпадать с именем декорируемой
# функции.


import json
import os.path
from os.path import isfile


def save_to_json(func):
    def wrapper(*args, **kwargs):
        if isfile(f'{func.__name__}.json'):
            with open(f'{func.__name__}.json', encoding='UTF-8') as f:
                data = json.load(f)
        else:
            data = []
        result = func(*args, **kwargs)
        data.append({'args': args, 'kwargs': kwargs, 'result': result})
        with open(f'{func.__name__}.json', 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=2)
    return wrapper


@save_to_json
def func(*args, **kwargs):
    # print(*args, **kwargs)
    return sum(args)


func(10,25, a=1, b=2)
