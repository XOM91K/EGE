from itertools import product
s=product('0123456789abcdefg', repeat=5)
k=0
for x in s:
    x=''.join(x)
    if x[0] != '0' and x.count('1') <= 2:
        for y in '3579bdf':
            x = x.replace(y, '@')
        if '@1' not in x and '1@' not in x and '11' not in x:
            k+=1
print(k)