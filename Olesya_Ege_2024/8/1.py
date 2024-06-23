from itertools import product
lst = []
for i in product('01234567', repeat=5):
    i = ''.join(i)
    if i[0] not in '01357' and i[-1] not in '26' and i.count('7') <= 2:
        print(i)
        lst.append(i)
print(len(lst))