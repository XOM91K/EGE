l = [[int(d) for d in x.split()] for x in open('7.txt')]
c = []
for x in l:
    m = sorted([i for i in x if x.count(i) >= 2])
    if min(x)**2 in x:
        if not(len(m)>6 or (len(m)==6 and m.count(m[0]) != 3)):
            c.append(sum(x))
    else:
        if len(m)>6 or (len(m)==6 and m.count(m[0]) != 3):
            c.append(sum(x))
print(min(c))
