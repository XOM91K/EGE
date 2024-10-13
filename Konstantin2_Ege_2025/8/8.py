from itertools import product
k = 0
for i in product('01234567', repeat=5):
    s = ''.join(i)
    if s.count('3') <= 1 and s[0] != '0':
        s = s.replace('5', '1').replace('7', '1').replace('3', '1')
        if '11' not in s:
            k += 1
            print(k, s)