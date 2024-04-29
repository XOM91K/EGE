n = 12 ** 34 + 7 * 12 ** 26 - 3 * 12 ** 16 + 2 * 12 ** 5 + 552
l = []
while n > 0:
    l.append(n % 12)
    n //= 12
print(len(set(l[::-1])))