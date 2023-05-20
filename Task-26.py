def find_1(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_2(a, b):
    i = find_1(a, b)
    j = (a * b) // i
    return j

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

j = find_2(num1, num2)

print(f"Наименьший общий множитель чисел {num1} и {num2}: {j}")
