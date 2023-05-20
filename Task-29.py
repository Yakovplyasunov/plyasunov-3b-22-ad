def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

input_string = input("Введите строку: ")

reversed_string = reverse_string(input_string)

print("Строка в обратном порядке:", reversed_string)
