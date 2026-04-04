l = [int(x) for x in open('1.txt')]
sr = sum(l) / len(l)
ct = 0
mx = []
for x in range(0, len(l) - 1):
    if l[x] < sr and l[x + 1] < sr:
        if str(l[x])[-1] == '9' or str(l[x + 1])[-1] == '9':
            ct += 1
            mx.append(l[x] + l[x + 1])
print(ct, max(mx))
print(len(mx), max(mx))