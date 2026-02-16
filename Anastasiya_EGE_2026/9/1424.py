l = [[int(d) for d in x.split()] for x in open('1424.txt')]
c = 0
stb1 = [x[0] for x in l]
stb6 = [x[-1] for x in l]
for x in l:
    povt = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt) == 3 and len(nepovt) == 3:
        if stb1.count(povt[0]) == 337 or stb6.count(nepovt[0]) == 337 or stb6.count(nepovt[1]) == 337 or stb6.count(nepovt[2]) == 337:
                c += 1
print(c)
