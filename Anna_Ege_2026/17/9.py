l = [int(x) for x in open('9.txt')]
mx3 = sorted(l)[-3]
mx = []
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 == 0:
        k += 1
    if l[x + 1] % 2 == 0:
        k += 1
    if l[x + 2] % 2 == 0:
        k += 1
    if k <= 2:
        if l[x] + l[x + 1] + l[x + 2] <= mx3:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))