def F(n):
    if n > 999:
        return n
    else:
        return 10 + n ** 2 + F(n + 4)
print(F(1111) + F(222))