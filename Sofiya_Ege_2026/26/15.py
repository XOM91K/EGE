l = [[int(d) for d in x.split()] for x in open('15.txt')]
l = sorted(l)
yach = [-1] * 210 # [-1, -1]
ct = 0
for x in l:
    for y in range(len(yach)):
        if x[0] > yach[y]:
            yach[y] = x[1]
            print(y + 1)
            ct += 1
            break

print(ct)