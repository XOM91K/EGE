l = [int(x) for x in open('8.txt')]
mn6 = min([x for x in l if abs(x) % 10 == 6 and len(str(abs(x))) == 4 and x > 0])

mx = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and abs(l[x]) % 10 == 6:
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and abs(l[x + 1]) % 10 == 6:
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and abs(l[x + 2]) % 10 == 6:
        k += 1
    if k == 1:
        if l[x] + l[x + 1] + l[x + 2] <= mn6:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))