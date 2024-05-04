S = 95000
#https://kompege.ru/variant?kim=25037848
l = sorted([int(x) for x in open('2.txt')])
buys = []
for x in l:
    if S - x >= 0:
        S -= x
        buys.append(x)
print(l)
print(len(buys))
print(95000 - sum(buys))
#1371
#1370