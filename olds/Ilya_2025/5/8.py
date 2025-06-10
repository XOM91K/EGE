l = []
for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += '010'
    else:
        R += bin(N % 3 * 5)[2:]
    if int(R, 2) > 300 and int(R, 2) % 2 == 0:
        l.append([int(R, 2), N])
print(sorted(l))