l = sorted([int(x) for x in open('20.txt')])
s = 9800
x = 0
ct = 0
print(l)
while s - l[x] >= 0:
    s -= l[x]
    x += 1
    ct += 1
s += l[x - 1]
for x in range(len(l) - 1, -1, -1):
    if s - l[x] >= 0:
        print(l[x])
        break
print(ct)