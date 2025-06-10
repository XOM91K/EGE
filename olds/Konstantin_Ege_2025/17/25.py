l = [int(x) for x in open('25.txt')]
mx = []
mn = min(l)
ct = 0
for x in range(len(l) - 1):
    if l[x] % 77 + l[x + 1] % 77 == mn:
        mx.append(l[x] + l[x + 1])
        ct += 1
print(len(mx), ct, max(mx))