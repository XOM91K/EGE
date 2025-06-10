def func(N):
    R = bin(N)[2:]
    R += bin(N % 4)[2:]
    return int(R, 2)
mx = 0
for N in range(1, 1000):
    l = [int(x) for x in range(N, N + 65)]
    ct = 0
    for i in range(1, 1000):
        if func(i) in l:
            ct += 1
    mx = max(mx, ct)
print(mx)