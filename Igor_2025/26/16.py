l = [[int(d) for d in x.split()] for x in open('16.txt')]
l2 = []
for x in l:
    sm = sum(x[1:])
    plus = sum([i for i in x[1:] if i > 0])
    answers = len([i for i in x[1:] if i != 0])
    l2.append([x[0], sm, plus, answers])
l2 = sorted(l2, key=lambda d: (-d[1], -d[2], -d[3], d[0]))
l2 = [x for x in l2 if x[1] > 0]
l3 = l2[:len(l2) // 3]
l2 = l2[len(l2) // 3:]
elem = 0
for x in l2:
    if x[1:] == l3[-1][1:]:
        l3.append(x)
        elem = x
l2 = l2[l2.index(elem) + 1:]
l3 = l2[:len(l2) // 10]
l2 = l2[len(l2) // 10:]
elem = 0
for x in l2:
    if x[1:] == l3[-1][1:]:
        l3.append(x)
        elem = x
print(l3[0][0], len(l3))