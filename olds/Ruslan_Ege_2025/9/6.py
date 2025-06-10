l = [sorted([int(d) for d in x.split()]) for x in open('6.txt')]
k = 0
for x in l:
    m = 1
    if len(set(x)) < 7:
        povt = []
        nepovt = []
        for i in x:
            if x.count(i) > 1:
                povt.append(i)
            else:
                nepovt.append(i)
        for h in povt:
            m *= h
        if (3 * sum(nepovt)) <= m:
            k += 1
print(k)