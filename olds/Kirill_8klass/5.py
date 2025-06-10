def F(x, A):
    return ((x % 2 == 0) <= (x % 13 != 0)) or (x + A >= 1000)
for A in range(1, 1000):
    if all([F(x, A) for x in range(1, 1000)]):
        print(A)
        break