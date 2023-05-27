def first_letters(str1, str2):
    first_letter1 = str1[0].upper()
    first_letter2 = str2[0].upper()

    print(f"Первая буква первой строки: {first_letter1}")
    print(f"Первая буква второй строки: {first_letter2}")

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

first_letters(str1, str2)
