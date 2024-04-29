from itertools import product
k = 0
for x in product('012345678', repeat=6):
    x = ''.join(x)
    if x[0] != '0':
        x = x.replace('2', '*').replace('4', '*').replace('6', '*').replace('8', '*').replace('0', '*')
        if x.count('*') <= 2 and x[5] == '*':
            k += 1
            print(x)
print(k)
