def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Введите число: "))

if is_prime(number):
    print(f"{number} является простым числом")
else:
    print(f"{number} не является простым числом")
