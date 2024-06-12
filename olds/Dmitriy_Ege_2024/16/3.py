def F(n):
    if n < 10:
        return n
    if n >= 10:
        return (n % 10) * F(n // 10)
for x in range(1, 1000):
    if F(x) != 0:
        print(x, F(x))
print((9999999999999 - 1000000000000) // 10)
print((9999999999999 - 1000000000000) - 899999999999)