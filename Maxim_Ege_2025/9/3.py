l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    x.sort()
    if abs(max(x) - min(x)) ** 3 <= (x[1] + x[2]) ** 2:
        print(x)
        ct += 1
print(ct)