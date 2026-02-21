l = [int(x) for x in open('17.txt')]
srpol = [x for x in l if x > 0]
srpol = sum(srpol) / len(srpol)
mx = []
for x in range(len(l) - 2):
    r = [l[x], l[x + 1], l[x + 2]]
    if max(r) - min(r) < srpol:
        mx.append(sum(r))
print(len(mx), max(mx))