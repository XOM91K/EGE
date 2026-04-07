l = [int(x) for x in open('16.txt')]
mx67 = max([d for d in l])
mx = []
for x in range(len(l) - 2):
    k = 0
    if '0' not in str(l[x]):
        k += 1
    if '0' not in str(l[x + 1]):
        k += 1
    if '0' not in str(l[x + 2]):
        k += 1
    if k >= 2:
        if (l[x] + l[x + 1] + l[x + 2]) < mx67 / 2:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))