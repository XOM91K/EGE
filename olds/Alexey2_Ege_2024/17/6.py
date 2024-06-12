l = [int(x) for x in open('6.txt')]
sr = []
for x in l:
    if x % 37 != 0:
        sr.append(x)
sr = sum(sr) / len(sr)
tr = []
for x in range(len(l) - 2):
    if bin(l[x] + l[x + 1] + l[x + 2])[2:] == bin(l[x] + l[x + 1] + l[x + 2])[2:][::-1]:
        if min(l[x], l[x + 1], l[x + 2]) > sr:
            tr.append(l[x] + l[x + 1] + l[x + 2])
print(len(tr), max(tr))