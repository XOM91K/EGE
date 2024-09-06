for N in range(1, 6):
    print(N)
def N(start, end):
    print(start)
    if start < end:
        return N(start + 1, end)

N(1, 5)