l = sorted([[int(d) for d in x.split()]for x in open('378.txt')])
l = sorted(l, key=lambda d: (d[0] + d[1]))
fight = [l[0]]
for x in l:
    if (fight[-1][0] + fight[-1][-1]) <= x[0]:
        fight.append(x)
print(len(fight))
for x in fight:
    print(x)
print('----')
for x in l:
    if x[0] > 1384:
        print(x)
print(1397-1364)