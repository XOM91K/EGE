l = [int(x) for x in open('5.txt')]
mix = max([d for d in l if abs(d) % 10 == 7])
ct = 0
sr = []
for x in range(len(l) - 2):
    a = 0
    b = 0
    if l[x]  %2 != 0:
        a += 1
    if l[x+1] % 2 != 0:
        a += 1
    if l[x+2] % 2 != 0:
        a += 1
    if l[x] > mix:
        b += 1
    if l[x+1] > mix:
        b += 1
    if l[x+2] > mix:
        b += 1
    if a == 2 and b == 1:
        ct += 1
        sr.append(l[x])
        sr.append(l[x + 1])
        sr.append(l[x + 2])
print(ct)
print(sum(set(sr)) / len(set(sr)))