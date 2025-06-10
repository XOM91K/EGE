l = [int(x) for x in open('2.txt')]
ct = 0
mx = []
sr = sum(l) / len(l)
for x in range(len(l) - 1):
    if l[x] > sr and l[x + 1] > sr:
        if str(l[x] + l[x + 1])[-2:] == '31':
            ct += 1
            mx.append(l[x] + l[x + 1])
print(ct, max(mx), len(mx))