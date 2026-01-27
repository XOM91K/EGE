l = [int(x)for x in open('14.txt')]
s = []
sr = [x for x in l if x > 0]
sr = sum(sr) / len(sr)
for x in range(len(l) - 2):
        if (max([l[x], l[x + 1], l[x + 2]]) - min([l[x], l[x + 1], l[x + 2]])) < sr:
            s.append(l[x] + l[x+1] + l[x+2])
print(len(s), max(s))