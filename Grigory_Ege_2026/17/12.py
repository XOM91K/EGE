l = [int(d) for d in open('12.txt')]
m = max([y for y in l if len(str(abs(y))) == 5 and abs(y) % 100 == 43])
ms = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5 and abs(l[x]) % 100 == 43 or \
            len(str(abs(l[x+1]))) == 5 and abs(l[x+1]) % 100 == 43 or \
            len(str(abs(l[x+2]))) == 5 and abs(l[x+2]) % 100 == 43 :
        if l[x]**2 + l[x+1]**2 + l[x+2]**2 <= m ** 2 :
            ms.append(l[x]**2 + l[x+1]**2 + l[x+2]**2)
print(len(ms),min(ms))
