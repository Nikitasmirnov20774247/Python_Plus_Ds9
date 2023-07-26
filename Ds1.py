# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.


import csv
import json
import math
from random import randint
from os.path import isfile


def save_to_json(func):
    def wrapper(*args):
        filename = f'{func.__name__}.json'
        
        if isfile(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []

        result = func(*args)
        data.append({'coefficients':{'a': args[0], 'b': args[1], 'c': args[2]}, 'result':result})
        
        with open(filename, 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)        
    
    return wrapper


def read_csv(func):
    def wrapper():
        with open('gen_random_result.csv', 'r', newline='', encoding='UTF-8') as reader_file:
            reader = csv.reader(reader_file, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                func(*row)

    return wrapper


@read_csv
@save_to_json
def root_result(a, b, c):
    dis_form = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis_form))
    
    if dis_form > 0:
        x1 = (-b + sqrt_val) /(2 * a)
        x2 = (-b - sqrt_val) /(2 * a)
        return {'x1': x1, 'x2': x2}
    elif dis_form == 0:
        return -b / 2 * a
    else:
        return f'нет действительных корней'


def gen_random_csv(filepath):
    with open(filepath, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        
        for _ in range(randint(100, 1000)):
            row = [randint(-100, 100) for _ in range(3)]
            if row[0] == 0:
                continue
            csv_writer.writerow(row)


if __name__ == '__main__':
    gen_random_csv('gen_random_result.csv')
    root_result()
