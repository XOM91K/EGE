l = sorted([[int(d) for d in x.split()] for x in open('6.txt')])
d = 100000
ct = 0
for x in l:
    if x[1] == 1 and d - (x[0] + 10) >= 0:
        d = d - (x[0]+10)
        ct += 1
print(l)
lst = 0
for x in l:
    if x[1] == 0 and d - (x[0] + 10) >= 0:
        d = d - (x[0] + 10)
        ct += 1
        lst = x[0]
l = l[::-1]
for x in l:
    if lst + d >= x[0]:
        print(x[0])
        break
print(ct)