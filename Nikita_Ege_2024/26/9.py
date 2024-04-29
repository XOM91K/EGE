sm = 99062
l = sorted([int(x) for x in open('9.txt')])
i = 0
ct = 0
while sm - l[i] >= 0:
    sm -= l[i]
    ct += 1
    i += 1
print(ct)
print(sm + l[i - 1])
i = -1
while True:
    if l[i] <= 101:
        print(l[i])
        break
    i -= 1