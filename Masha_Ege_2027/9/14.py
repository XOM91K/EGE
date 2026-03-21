l = [[int(d) for d in x.split()] for x in open('14.txt')]
ct = 0
for x in l:
    x = sorted(x)
    if 2 * (x[-1] + x[-2]) > 3 * (sum(x) - x[-1] - x[-2]):
        c5 = [y for y in x if str(y)[-1] == '5']

        if len(c5) >= 2:
            ct += 1
print(ct)