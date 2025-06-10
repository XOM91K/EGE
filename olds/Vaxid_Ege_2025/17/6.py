l = [int(x) for x in open('6.txt')]
sr = sum(l) / len(l)
ct = 0
d = []
for x in range(len(l) - 1):
    if l[x] < sr and l[x+1] < sr:
        if str(l[x])[-1] == '9' or str(l[x+1])[-1] == '9':
            d.append(l[x] + l[x+1])
            ct = ct +1
print(ct)
print(max(d))