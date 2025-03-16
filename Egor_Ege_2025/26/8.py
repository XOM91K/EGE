l = [[int(d) for d in x.split()] for x in open('8.txt')]
otl = l.copy()
otl = sorted([x for x in otl if x[1:].count(2) == 0], key=lambda d: (-(sum(d[1:])/4), d[0]))
otl2 = otl[:len(otl) // 4 + 1]
print(otl2[-1][1:])
print(otl)
otl = [x[0] for x in otl if sum(x[1:]) == sum(otl2[-1][1:])]
print(max(otl))
dv = l.copy()
dv = sorted([x for x in dv if 2 in x[1:]], key=lambda d: (d[1:].count(2), d[0]))
dv = [x for x in dv if x[1:].count(2) > 2]

print(dv[0][0])