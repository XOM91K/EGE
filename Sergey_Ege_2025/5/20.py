def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
d = []
for N in range(1, 10000):
    R = v3(N)
    if sum(map(int, str(R))) % 2 == 0:
        R = '1' + R + '2'
    else:
        R = '2' + R + '0'
    R = int(R, 3)
    if R > 100:
        d.append(R)
print(min(d))