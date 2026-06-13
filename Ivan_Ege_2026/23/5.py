import itertools
ct = 0
l = []
for x in itertools.product('ABC', repeat=6):
    x = ''.join(x)
    start = 2
    for y in x:
        if y == 'A':
            start += 5
        elif y == 'B':
            start -= 3
        else:
            start += 1
    l.append(start)
print(len(set(l)))