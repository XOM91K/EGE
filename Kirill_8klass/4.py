def F(x, A):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)
for A in range(1, 1000):
    if all([F(x, A) for x in range(1, 1000)]):
        print(A)
        break