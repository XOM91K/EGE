l = [int(x) for x in open('5.txt')]
mn41 = min([x for x in l if x > 0 and x % 41 == 0])
mx = []
ct = 0
print(l)
for x in range(len(l) - 1):
    if l[x] != l[x + 1] and abs(l[x] - l[x + 1]) % mn41 == 0:
        mx.append(l[x] + l[x + 1])
        ct += 1
print(ct, max(mx))