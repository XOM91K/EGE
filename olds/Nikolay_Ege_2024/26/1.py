l = sorted([int(x) for x in open('1.txt')])
print(l)
s = 1000000
ct = 0
last = 0
for x in l:
    if s - x >= 0:
        s -= x
        last = x
        ct += 1
print(ct)
s += last
for x in range(len(l) - 1, -1, -1):
    if s - l[x] >= 0:
        print(l[x])
        break
