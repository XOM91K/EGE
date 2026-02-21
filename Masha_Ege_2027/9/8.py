l = [[int(d) for d in x.split()] for x in open('8.txt')]
ct = 0
for x in l:
    if x.count(min(x)) == 1:
        povt = [y for y in x if x.count(y) >= 2]
        if max(x) + min(x) < sum(povt):
            ct += 1
print(ct)