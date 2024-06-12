l = sorted([int(x) for x in open('5.txt')], reverse=True)
m = 400
# {63, 61}, {60, 59}, {55, 57} и {54, 52}, а товары {81} и {83}
i = 0
j = len(l) - 1
knt = 0
od = 0
while i < j:
    if l[i] + l[j] <= m:
        i += 1
        j -= 1
        knt += 1
    else:
        od += l[i]
        i += 1
print(knt, od)