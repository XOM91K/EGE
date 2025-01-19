l = [[int(d) for d in x.split()] for x in open('7.txt')]
k = 0
for x in l:
    k += 1
    povt = []
    nepovt = 0
    for y in x:
        if x.count(y) == 3:
            povt.append(y)
    nepovt = sum(x) - sum(povt)
    if len(povt) == 6:
        if sum(povt) / 6 > nepovt:
            print(k)
# d = [44, 59, 100, -103]
# for y in d:
#     print(y)