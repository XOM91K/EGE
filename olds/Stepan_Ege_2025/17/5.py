l = [int(x) for x in open('5.txt')]
mx19 = max([y for y in l if str(y)[-2:] == '19'])
mx = []
for x in range(len(l) - 2):
    ch = [y for y in [l[x], l[x + 1], l[x + 2]] if len(str(abs(y))) == 4]
    if len(ch) == 2:
        if l[x] % 3 == 0 or l[x + 1] % 3 == 0 or l[x + 2] % 3 == 0:
            if l[x] + l[x + 1] + l[x + 2] > mx19:
                mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))