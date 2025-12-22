l = [[int(d) for d in x.split()] for x in open('15.txt')]
ct = 0
for x in l:
    x = sorted(x)
    ch = [d for d in x if d % 2 == 0]
    n = [d for d in x if d % 2 != 0]
    if x[-1] < (x[0] + x[1] + x[2]):
        if sum(ch) == sum(n):
            ct += 1
print(ct)
