l = [int(x) for x in open('2.txt')]
ct = 0
mx = []
for x in range(len(l) - 1):
    if l[x] % 3 == 0 or l[x + 1] % 3 == 0:
        ct += 1
        mx.append(l[x] + l[x + 1])
print(ct, max(mx))