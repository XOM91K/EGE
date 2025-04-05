l = [[int(d) for d in x.split()] for x in open('16.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4 and (x.count(x[0]) == 3 or x.count(x[1]) == 3 or x.count(x[2]) == 3 or x.count(x[3]) == 3):
        povt = [y for y in x if x.count(y) == 3]
        nepovt = [y for y in x if x.count(y) == 1]
        if sum(povt) ** 2 > sum(nepovt) ** 2:
            ct += 1

print(ct)