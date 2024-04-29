def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
r = []
for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R = '10' + R[:-3]
    else:
        R += v3(R.count('1') + R.count('2') * 2)
    R = int(R, 3)
    if R > 453:
        r.append(R)
print(min(r))