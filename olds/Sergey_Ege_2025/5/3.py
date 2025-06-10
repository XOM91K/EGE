l = []
for N in range(1, 1000):
    R = bin(N)[2:] #110100010 010
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin(N % 3 * 3)[2:]
    if int(R, 2) <= 137:
        l.append(int(R, 2))
print(max(l))
