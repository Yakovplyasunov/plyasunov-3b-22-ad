lst = [5, 7, 11, 13, 15, 20, 25]
new_lst = [elem for elem in lst if elem > 10]
avg = sum(new_lst) / len(new_lst)
print(avg)
