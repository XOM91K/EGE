l = [int(x) for x in open('2.txt')]
mn52 = min([x for x in l if x % 52 == 0])
ct = 0
mx = []
for x in range(len(l) - 2):
    if l[x] % 113 + l[x + 1] % 113 + l[x + 2] % 113 == mn52:
        ct += 1
        mx.append(l[x] + l[x + 1] + l[x + 2])
print(ct, max(mx))