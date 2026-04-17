l = [int(x) for x in open("4.txt")]
ct = []
mx = max([d for d in l if d % 10 == 1])
for x in range(len(l) - 3):
    chet = []
    k = 0
    if l[x] % 2 == 0:
        k += 1
    if l[x + 1] % 2 == 0:
        k += 1
    if l[x + 2] % 2 == 0:
        k += 1
    if l[x + 3] % 2 == 0:
        k += 1
    if k % 2 != 0:
        if l[x] < mx and l[x + 1] < mx and l[x + 2] < mx and l[x + 3] < mx:
            ct.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3])
print(len(ct), min(ct))
