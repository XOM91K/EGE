s = 8200
l = sorted([int(x) for x in open('1.txt')])
ct = 0
i = 0
while s - l[i] > 0:
    s -= l[i]
    ct += 1
    i += 1
print(ct)
s += l[i - 1]
i = -1
while True:
    if s - l[i] > 0:
        print(l[i])
        break
    i -= 1
