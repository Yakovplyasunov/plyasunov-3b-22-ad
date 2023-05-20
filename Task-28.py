def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: Деление на ноль недопустимо.")
            return
    else:
        print("Ошибка: Неподдерживаемая операция.")
        return

    print("Результат:", result)

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operator = input("Введите операцию (+, -, *, /): ")
