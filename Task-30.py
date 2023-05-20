import calculator

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result_addition = calculator.addition(num1, num2)
result_subtraction = calculator.subtraction(num1, num2)
result_multiplication = calculator.multiplication(num1, num2)
result_division = calculator.division(num1, num2)

print("Результат сложения:", result_addition)
print("Результат вычитания:", result_subtraction)
print("Результат умножения:", result_multiplication)
print("Результат деления:", result_division)
