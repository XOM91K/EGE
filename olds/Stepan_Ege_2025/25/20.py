def deli(n):
    p = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            p.append(i)
            p.append(n // i)
    return sorted(set(p))
p = []
p1 = []
count = 0
for i in range(1533878, -1, -1):
    d = deli(i)
    if len(d) > 0:
        F = max(d) - min(d)
    else:
        F = 0
    if F > 5000 and F % 1235 == 0:
        count += 1
        p.append([i, F])
    if count == 5:
        break
p = sorted(p)
for i in range(5):
    print(*p[i])