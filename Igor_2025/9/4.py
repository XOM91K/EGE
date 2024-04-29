l = [[int(d) for d in x.split()] for x in open('4.txt')]
f = []
for x in l:
    for y in x:
        f.append(y)
ct = 0
for x in l:
    for y in x:
        if x.count(y) > 1:
            g = x.count(y)
            if f.count(y) - g > 100:
                ct += 1
                break
print(ct)