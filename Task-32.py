def character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

input_string = input("Введите строку: ")

frequency = character_frequency(input_string)

for char, count in frequency.items():
    print(f"Символ '{char}' встречается {count} раз(а)")
   
