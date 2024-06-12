def tr(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

ct = 0
mn = 10 ** 10
l = [int(x) for x in open('10.txt')]
mx_3 = max([x for x in l if tr(x)[::-1] == tr(x) and len(str(abs(x))) == 3])
for x in range(len(l) - 1):
    if (len(str(abs(l[x]))) == 4 and len(str(abs(l[x + 1]))) != 4) or (len(str(abs(l[x]))) != 4 and len(str(abs(l[x + 1]))) == 4):
        if (l[x] ** 2 + l[x + 1] ** 2) % mx_3 == 0:
            ct += 1
            mn = min(mn, l[x] ** 2 + l[x + 1] ** 2)
print(ct, mn)