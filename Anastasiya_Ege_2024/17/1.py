l = [int(x) for x in open('1.txt')]
ct = 0
m = []
for x in range(len(l) - 1):
    if l[x] % 3 == 0 or l[x + 1] % 3 == 0:
        ct += 1
        m.append(l[x] + l[x + 1])
print(ct)
print(max(m))