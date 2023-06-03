first_lst = [24, 36, 48, 60]
second_lst = [12, 18, 24, 36, 72]
first_lst.extend(second_lst)
nod = 1
for i in range(2, max(first_lst) + 1):
    cnt = 0
    for elem in first_lst:
        if elem % i == 0:
            cnt += 1
    if cnt == len(first_lst):
        nod = i
print(nod)
