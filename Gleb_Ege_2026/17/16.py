l = [int(x) for x in open('16.txt')]
w = []
for s in l:
    if s % 1000 == 102 and s > 0:
        w.append(s)
f = min(w)
q = []
for x in range(len(l) - 2):
    for y in range(x + 1, len(l) - 1):
        for z in range(y + 1, len(l)):
            k = 0
            if len(str(abs(l[x]))) == 5 and l[x] % 3 == 0 and l[x] > 0:
                k +=1
            if len(str(abs(l[y]))) == 5 and l[y] % 3 == 0 and l[y] > 0:
                k += 1
            if len(str(abs(l[z]))) == 5 and l[z] % 3 == 0 and l[z] > 0:
                k += 1
            if k == 2:
                if (l[x] ** 2 + l[y] ** 2 + l[z] ** 2) % f == 0:
                    q.append((l[x] + l[y] + l[z]) // 3)
print(len(q), min(q))