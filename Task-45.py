name = str(input('Введите имя файла: '))
try:
    with open(name, 'r') as file:
        inner = file.read()
        print(inner)
except FileNotFoundError:
    print('Ошибка')
except OSError:
    print('Ошибка')
