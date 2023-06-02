try:
    with open('test.txt', 'w') as file:
        file.write('Hello, World!')
except OSError:
    print('Ошибка')
