l = sorted([int(x) for x in open('2.txt')])[::-1]
print(l)
s = 100000
ct = 0
last = 0
for x in l:
    if s - x >= 0:
        s -= x
        last = x
        ct += 1
print(ct, last)
print(s)