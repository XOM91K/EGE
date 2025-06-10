import math
#из Полякова № 6070
l = [int(x) for x in open(r'C:\Users\Zarif\Downloads\17-360.txt')]
mx42 = max([x for x in l if math.prod(map(int, str(abs(x)))) == 42])
mnn = 10 ** 10
ct = 0
for x in range(len(l) - 2):
    can = False
    mn = 10 ** 10
    for y in range(3):
        for z in range(2):
            if abs(l[x + y]) == abs(l[x + z]) and l[x + y] + l[x + z] == 0:
                mn = min(mn, abs(l[x + y]) * abs(l[x + z]))
                can = True
    if can:
        if l[x] < mx42 and l[x + 1] < mx42 and l[x + 2] < mx42:
            mnn = min(mn, mnn)
            ct += 1
print(ct, mnn)

