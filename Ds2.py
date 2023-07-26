# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса


import random
from modules import guess, get_circle_riddles_2, show_results, check_date, check_year, chessboard_run, func, guess_game


print(guess(10, 100, 9))
print()


riddles_ = {"Сидит дед в сто шуб одет, кто его раздевет, тот слёзы проливает": ['лук', 'onion'],
                "Висит груша нельзя скушать": ["лампочка", "лампа", "light bulb"]}
get_circle_riddles_2(riddles_)
show_results()
print()


print(check_date("22.11.1980"))
print(check_year("14.11.1980"))
print()


chessboard_run()
print()


func(10,25, a=1, b=2)
print()


guess_game(200, random.randint(1, 10))
