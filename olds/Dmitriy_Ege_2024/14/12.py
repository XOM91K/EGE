def v49(n):
    ost = []
    while n > 0:
        ost.append(n % 49)
        n //= 49
    return ost[::-1]
d = 18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50
y = v49(abs(d))
print(sum([int(x) for x in y]))
print(y)