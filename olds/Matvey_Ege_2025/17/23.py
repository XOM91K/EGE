l = [int(x) for x in open('23.txt')]
sr = [x for x in l if x > 0]
sr = sum(sr) / len(sr)
mx = []
for x in range(len(l) - 2):
    a = [l[x], l[x + 1], l[x + 2]]
    if max(a) - min(a) < sr:
        mx.append(sum(a))
print(len(mx), max(mx))