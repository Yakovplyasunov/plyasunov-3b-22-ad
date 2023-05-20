def fibonacci(n):
    fib_series = []
    a, b = 0, 1

    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

n = int(input("Введите количество чисел ряда Фибоначчи: "))

fib_numbers = fibonacci(n)

print("Числа ряда Фибоначчи:")
for number in fib_numbers:
    print(number)
