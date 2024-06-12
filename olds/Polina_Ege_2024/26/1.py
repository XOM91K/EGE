l = sorted([int(x) for x in open('1.txt')])
s = 8200
ct = 0
last = 0
for x in l:
    if s - x >= 0:
        s -= x
        ct += 1
        last = x
s += last
l = l[::-1]
print(ct)
for x in l:
    if s - x >= 0:
        print(x)
        break
