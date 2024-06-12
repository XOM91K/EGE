l = sorted([int(x) for x in open('4.txt')])
print(l)
v = 99062
ctposilok = 0
for x in range(len(l)):
    if v - l[x] >= 0:
        v = v - l[x]
        ctposilok += 1
        print(l[x])
print(v)
print(l)
print(ctposilok)
