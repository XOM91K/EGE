def F(n):
    if n >= 10.000:
        return n
    if n < 10.000 and n % 2 == 0:
        return F(n+1) + n**2 - 3*(n-1)
    if n < 10.000 and n % 2 != 0:
        return F(n+2) + 5*n - (n-1)
print(F(90)-F(99))