l = [[int(d) for d in x.split()] for x in open('17.txt')]
l = sorted(l, key=lambda d: sum(d))
time_end = 0
ct = 0
for x in l:
    if x[0] >= time_end:
        time_end = sum(x)
        ct += 1
print(ct)