l = [int(x) for x in open('3.txt')]
mx17 = max([d for d in l if d % 17 == 0])
mx = 0
ct = 0
for x in range(len(l) - 1):
    if (l[x] + l[x + 1]) > mx17:
        ct += 1
        mx = max(mx, l[x] + l[x + 1])
print(ct, mx)