dst = {}
for N in range(1, 10_000_000):
    R = bin(N)[2:]
    R += bin(N % 4)[2:]
    R = int(R, 2)
    if N not in dst:
        dst[N] = 0
    dst[N] = R
print('---')
mx = 0
for x in range(1000000, 1010000):
    ct = 0
    for y in (x, x + 65):
        if y in dst:
            if dst[y] != 0:
                ct += 1
    mx = max(mx, ct)
print(mx)