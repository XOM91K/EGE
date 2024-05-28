l = sorted([int(x) for x in open('3.txt')])
s = 99987
ct = 0
last = 0
for x in l:
    if s - x >= 0:
        s -= x
        last = x
        ct += 1
s += last
l = l[::-1]
print(ct)
for x in l:
    if s - x >= 0:
        print(x)
        break