l = [[int(d) for d in x.split()] for x in open('801.txt')]
ct = 0
# [1, 1, 1, 4, 5, 5]
for x in l:
    povt = [y for y in x if x.count(y) >= 3]
    povt2 = [y for y in x if x.count(y) == 2]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) > 0 and len(nepovt) > 0:
        if (sum(povt) + sum(povt2)) / (len(povt) + len(povt2)) < sum(nepovt) / len(nepovt):
            ct += 1
print(ct)
