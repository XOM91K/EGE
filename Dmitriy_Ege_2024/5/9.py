def alg(N):
    R = bin(N)[2:]
    R += bin(N % 4)[2:]
    return int(R, 2)
dostup_chisla = []
for x in range(1, 10000):
    dostup_chisla.append(alg(x))
mx = 0
for x in range(1, 1000):
    ct = 0
    d = [y for y in range(x, x + 49)]
    for y in d:
        if y in dostup_chisla:
            ct += 1
    mx = max(mx, ct)
print(mx)