first_lst = [1, 2, 3, 2, 1]
second_lst = first_lst.copy()
second_lst.reverse()
if first_lst == second_lst:
    print('Массив является палиндромом')
else:
    print('Массив не является палиндромом')
