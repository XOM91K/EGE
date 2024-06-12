l = sorted([int(x) for x in open('11.txt')])
min_mas = 1
for i in l:
    if i > min_mas:
        break
    min_mas += i
l = sorted(l, reverse=True)
rem = 0
for i in l:
    if i > min_mas:
        rem += 1
print(rem)
print(min_mas)
