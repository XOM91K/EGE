r = []
for N in range(1, 100000):
    R = oct(N)[2:]
    if sum(map(int, R)) % 2 == 0:
        R = R + oct(sum(map(int, R)))[2:]
    else:
        R = oct(sum(map(int, R)))[2:] + R
    R = int(R, 8)
    if N > 482:
        r.append(R)
print(min(r))