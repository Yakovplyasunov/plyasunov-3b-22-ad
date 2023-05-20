import random

array = []

for _ in range(10):
    number = random.randint(1, 10)
    array.append(number)

print("Массив:", array)

sum_of_elements = sum(array)

print("Сумма всех элементов:", sum_of_elements)
