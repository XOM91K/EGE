l = [[int(d) for d in x.split()] for x in open('4.txt')]
ct = 0
for x in l:
    if max(x) < sum(x) - max(x):
        x.sort()
        if x[0] + x[-1] == x[1] + x[2]:
            print(x)
            ct += 1
print(ct)