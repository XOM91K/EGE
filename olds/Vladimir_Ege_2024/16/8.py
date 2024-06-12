def F(n):
    if n >= 2031:
        return 1
    if n < 2031:
        return n + 31 + F(n + 31)
print(F(31) - F(23))