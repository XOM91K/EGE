def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
d = []
for N in range(1, 10000):
    R = v3(N)
    if sum([int(x) for x in R]) % 9 == 0:
        R += '2'
    else:
        R += v3(sum([int(x) for x in R]) % 9)
    R = int(R, 3)
    if N > 166:
        d.append(R)
print(min(d))
