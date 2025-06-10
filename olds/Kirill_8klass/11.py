def F(n):
    if n >= 2022:
        return n
    if n < 2022:
        return F(n + 5) + 7
print(F(45) - F(49))