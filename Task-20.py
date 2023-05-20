import random

array = []

for _ in range(10):
    number = random.randint(1, 100)
    array.append(number)

print("Массив:", array)
max_number = max(array)
min_number = min(array)

print("Максимальное число:", max_number)
print("Минимальное число:", mi
