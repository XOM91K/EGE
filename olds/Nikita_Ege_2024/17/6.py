def tr3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
l = [int(x) for x in open('6.txt')]
otv = 0
mn = 10**10
mx_3 = max([y for y in l if len(str(abs(y))) == 3 and tr3(y)[::-1] == tr3(y)])
print(mx_3)
for i in range(len(l) - 1):
    if ((len(str(abs(l[i]))) == 4 and len(str(abs(l[i + 1]))) != 4) or
        (len(str(abs(l[i]))) != 4 and len(str(abs(l[i + 1]))) == 4)) and (l[i] ** 2 + l[i + 1] ** 2) % mx_3 == 0:
        otv += 1
        mn = min(mn, l[i] ** 2 + l[i + 1] ** 2)

print(otv, mn)
