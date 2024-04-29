mn = 10 ** 10
for N in range(11, 10000):
    R = oct(N)[2:]
    if N % 5 == 0:
        R += R[:3]
    else:
        R += bin(N % 5)[2:]
    R = int(R, 8)
    if R >= 35000:
        mn = min(mn, N)
print(mn)