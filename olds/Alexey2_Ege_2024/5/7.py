s = set()
for N in range(2, 10000):
    R = bin(N)[3:]
    s.add(int(R, 2) - N)
print(len(s))

