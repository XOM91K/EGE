def pt(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]
for N in range(5, 10000):
    R = pt(N)
    if N % 5 == 0:
        R += R[-2:]
    else:
        R += pt(N % 5 * 7)
    R = int(R, 5)
    if R > 200:
        print(R)