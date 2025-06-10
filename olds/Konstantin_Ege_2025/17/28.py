l = [int(x) for x in open('28.txt')]
mx4 = max([x for x in l if len(str(abs(x))) == 4 and abs(x) % 10 == 4])
mx = []
ct = 0
for x in range(len(l) - 1):
    k = 0
    if len(str(abs(l[x]))) == 4 and abs(l[x]) % 10 == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and abs(l[x + 1]) % 10 == 4:
        k += 1
    if k == 1:
        if l[x] + l[x + 1] < mx4:
            mx.append(l[x] + l[x + 1])
            ct += 1
print(ct, max(mx))