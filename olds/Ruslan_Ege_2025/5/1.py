b = []
def f5(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n //= 5
    return s
for N in range(5, 10000):
    N5 = f5(N)
    if N % 5 == 0:
        N5 = N5 + N5[-2:]
    else:
        N5 = N5 + f5(N % 5 * 7)
    R = int(N5, 5)
    if R > 200:
        b.append(R)
print(min(b))