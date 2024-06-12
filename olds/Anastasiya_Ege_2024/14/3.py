num = -1 * (18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50)
n = []
while num > 0:
    n.append(num % 49)
    num //= 49
print(n)
print(sum(n))