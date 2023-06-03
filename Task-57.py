import os
dir_name = input('Введите путь к директории\n')
ex_name = input('Введите расширение в формате \'.txt\'\n')
try:
    for root, dirs, files in os.walk(dir_name):
        for filename in files:
            if ex_name in filename:
                print(filename)
except Exception:
    print('Ошибка')
