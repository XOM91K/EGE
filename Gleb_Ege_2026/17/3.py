l = [int(x) for x in open('3.txt')]
mx = max(l)
mx2 = []
for x in range(len(l) - 2):
    k = 0
    if '0' not in str(l[x]):
        k += 1
    if '0' not in str(l[x + 1]):
        k += 1
    if '0' not in str(l[x + 2]):
        k += 1
    if k >= 2:
        if l[x] + l[x + 1] + l[x + 2] < mx / 2:
            mx2.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx2), max(mx2))