# ✔ Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.


import json
from os.path import isfile
import random
from functools import wraps


def save_to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if isfile(f'{func.__name__}.json'):
            with open(f'{func.__name__}.json', encoding='UTF-8') as f:
                data = json.load(f)
        else:
            data = []
        result = func(*args, **kwargs)
        data.append({'args': args, 'kwargs': kwargs, 'result': result})
        with open(f'{func.__name__}.json', 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=4)
            
    return wrapper


def check_data(func):
    @wraps(func)
    def wrapper(answer, attempts):
        if not (1 <= answer <= 100):
            answer = random.randint(1, 100)
        if not (1 <= attempts <= 10):
            attempts = random.randint(1, 10)
        func(answer, attempts)
        
    return wrapper


def run_a_lot(num):
    def run_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)

        return wrapper
    
    return run_func


@run_a_lot(2)
@save_to_json
@check_data
def guess_game(answer, attempts):

    for _ in range(attempts):
        guess = int(input('Введите число: '))
        if guess == answer:
            print('Вы угадали число!')
            return
        elif guess < answer:
            print('Число больше')
        else:
            print('Число меньше')
    print('Попытки закончились!')

    return guess_game()


guess_game(200, random.randint(1, 10))
help(guess_game)
