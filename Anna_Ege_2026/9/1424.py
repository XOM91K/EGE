l = [[int(d) for d in x.split()] for x in open('1424.txt')]
stb1 = [x[0] for x in l]
stb6 = [x[-1] for x in l]
ct = 0
for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt3) == 3 and len(povt1) == 3:
        if stb1.count(povt3[0]) == 337 or stb6.count(povt1[0]) == 337 or stb6.count(povt1[1]) == 337 or stb6.count(povt1[2]) == 337:
            ct += 1
print(ct)