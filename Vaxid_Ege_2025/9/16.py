#*******************
l = [[int(d) for d in x.split()] for x in open('16.txt')]
k = 0
for x in l:
    k = k + 1
    pov = []
    nepov = []
    for y in x:
        if x.count(y) == 2:
            pov.append(y)
        if x.count(y) == 1:
            nepov.append(y)
    if len(pov) == 6 and len(nepov) == 2:
        if (max(pov) - min(pov)) ** 2 > 2 * (nepov[0] ** 2 + nepov[1] ** 2):
            print(k, x)