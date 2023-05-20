def find_two_smallest(numbers):
    if len(numbers) < 2:
        print("Ошибка: список должен содержать хотя бы два элемента")
        return

    smallest1 = min(numbers)
    numbers.remove(smallest1)
    smallest2 = min(numbers)

    print("Наименьшие значения:")
    print(smallest1)
    print(smallest2)

numbers = input("Введите список чисел через пробел: ").split()

numbers = [int(num) for num in numbers]

find_two_smallest(numbers)
