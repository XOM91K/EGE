l = [int(x) for x in open('10.txt')]
dv = sum([x for x in l if (len(str(abs(x))) == 2 and x % 2 == 0)])
mn = []
for x in range(len(l) - 1):
    n1 = l[x]
    n2 = l[x + 1]
    if sum([n1 % dv == 0, n2 % dv == 0]) == 1:
        mn.append(n1 * n2)
print(len(mn), abs(min(mn)))