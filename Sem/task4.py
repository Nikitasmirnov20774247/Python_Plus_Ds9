# ✔ Создайте декоратор с параметром.
# ✔ Параметр - целое число, количество запусков декорируемой
# функции.


def run_a_lot(num):
    def run_func(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)

        return wrapper
    
    return run_func


@run_a_lot(5)
def func(*args, **kwargs):
    print(args)
    return sum(args)


func(4, 5)
func(3, 6)
                        