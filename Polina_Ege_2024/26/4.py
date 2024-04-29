#На полякове №2645
l = sorted([int(x) for x in open('4.txt')])
l = l[::-1]
s = 100
ct = 0
for x in l:
    if s - x >= 0:
        s -= x
        ct += 1
        print(x)
print(ct)