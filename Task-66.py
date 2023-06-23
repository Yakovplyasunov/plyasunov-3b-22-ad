# Написать программу, которая принимает на вход строку и выводит на экран количество различных подстрок строки, начинающихся и заканчивающихся одним и тем же символом.

def count_substrings(s):
    count = 0
    char_freq = {}

    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    for freq in char_freq.values():
        count += (freq * (freq - 1)) // 2

    return count

# Пример использования
input_string = "abcab"
result = count_substrings(input_string)
print(result)
