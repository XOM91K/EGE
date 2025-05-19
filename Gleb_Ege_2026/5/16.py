l = []
for N in range(11, 1000):
    R = oct(N)[2:]
    if N % 5 == 0:
        R = R + R[:2]
    else:
        a = bin(N % 5)[2:]
        R = R + a
    R = int(R, 8)
    if R >= 35000:
        l.append(N)
print(min(l))