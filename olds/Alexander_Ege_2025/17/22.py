l = [int(x) for x in open('22.txt')]
sr = [x for x in l if x > 0]
sr = sum(sr) / len(sr)
mx = []
for x in range(len(l) - 2):
    if (max(l[x], l[x + 1], l[x + 2]) - min(l[x], l[x + 1], l[x + 2])) < sr:
        mx.append(l[x] + l[x +1] + l[x + 2])
print(len(mx) , max(mx))