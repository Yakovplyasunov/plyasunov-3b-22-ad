try:
    n = int(input('Введите целое число\n\n'))
    for i in range(1, n + 1):
        print(i)
except Exception:
    print('Ошибка')
