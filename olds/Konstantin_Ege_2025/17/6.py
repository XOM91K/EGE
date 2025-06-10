l = [int(x) for x in open('6.txt')]
mn = []
mx = []
ct = 0
for x in range(len(l)):
    if abs(l[x]) % 10 == 1:
        mn.append(l[x])
mn = min(mn)
for x in range(len(l) - 1):
    if abs(min(l[x], l[x + 1])) % 10 == 4:
        if l[x] ** 2 + l[x + 1] ** 2 < mn ** 2:
            ct += 1
            mx.append(l[x] ** 2 + l[x + 1] ** 2)
print(ct, max(mx))