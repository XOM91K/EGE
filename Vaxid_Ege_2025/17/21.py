l = [int(x) for x in open('21.txt')]
ct3 = len([x for x in l if x % 3 == 0]) ** 2
mx = []
for x in range(len(l) - 2):
    k = 0
    if l[x] < 0:
        k += 1
    if l[x + 1] < 0:
        k += 1
    if l[x + 2] < 0:
        k += 1
    if k == 1:
        if abs(l[x] * l[x + 1] * l[x + 2]) < ct3:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))