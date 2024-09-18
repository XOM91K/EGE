l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:#[4, 9, 5]
    if min(x) ** 3 > (sum(x) - min(x) - max(x)) * max(x) * 3:
        ct += 1
print(ct)