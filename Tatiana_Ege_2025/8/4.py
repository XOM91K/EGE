import itertools
r = itertools.product('01234567', repeat=5)
f = 0
s = []
for i in r:
    i = ''.join(i)
    s.append(i)
for i in s:
    p = 0
    for j in range(len(i) - 1):
        if int(i[j]) % 2 == 1 and int(i[j + 1]) % 2 == 1:
            p += 1
    if p == 0 and i.count('3') <= 1 and i[0] != '0':
        print(i)
        f += 1
print(f)