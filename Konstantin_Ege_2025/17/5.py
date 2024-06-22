l = [int(x) for x in open('5.txt')]
mn = min(l)
ct = 0
mx1 = []
for x in range(len(l) - 1):
    if l[x] % 18 + l[x + 1] % 18 == mn:
        ct += 1
        mx1.append(l[x] + l[x + 1])
print(ct)
print(max(mx1))