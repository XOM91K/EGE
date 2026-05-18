l = [[int(d) for d in x.split()] for x in open('14.txt')]
l = sorted(l)
yach = [0] * 230
ct = 0
c = 0
for x in l:
    for y in range(len(yach)):
        if x[0] > yach[y]:
            yach[y] = x[1]
            ct += 1
            c = y + 1
            break
print(ct, c)