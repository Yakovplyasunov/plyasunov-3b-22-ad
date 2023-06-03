try:
    lst = [int(num) for num in input('Введите количество чисел\n\n').split(',')]
    print(min(lst))
except Exception:
    print('Ошибка')
