l = []
for N in range(1000, 10000):
    d = oct(N)[2:]
    if len(d) == 4:
        c1 = int(str(N)[0]) + int(str(N)[-1])
        c2 = int(str(N)[1]) + int(str(N)[2])
        if min(c1, c2) == 3 and max(c1, c2) == 17:
            l.append(N)
print(l[0] + l[-1])