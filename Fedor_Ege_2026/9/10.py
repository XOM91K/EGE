l = [[int(d) for d in x.split()] for x in open('10.txt')]
ct = 0
for x in l:
    x.sort()
    d = min(x)
    minpovt = [y for y in x if x.count(y) > 1 and y == d ]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(minpovt) == 2 or len(minpovt) == 3:
        if len(nepovt) == 5 or len(nepovt) == 6:
            f = min(nepovt)
            g = max(nepovt)
            if f**2 + g**2 <= (sum(nepovt) - f - g)**2:
                ct += 1
print(ct)