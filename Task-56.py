import operator

file_name = input('Введите имя файла с раcширением\n\n')
file = open(file_name, 'r')
words = [i.replace('\n', '') for i in file.readlines()]
file_name = file_name
file.close()
word_frequency = {word:words.count(word) for word in words}
print(max(word_frequency.items(), key=operator.itemgetter(1)))
