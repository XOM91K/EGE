l = [int(x) for x in open('10.txt')]
c = []
for x in range(len(l) - 2):
    t = [l[x], l[x + 1], l[x + 2]]
    h = [i for i in t if str(i)[0] == str(i)[-1]]
    g = [i for i in t if len(str(i)) == 5 and str(i)[1] == '7']
    if len(g) == 2 and len(h) == 1:
        c.append(max(t))
print(len(c), sum(c))
