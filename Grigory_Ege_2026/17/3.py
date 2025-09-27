l = [int(x) for x in open('3.txt')]
mn25 = min([y for y in l if abs(y) % 100 == 25]) ** 2
mx = []
for x in range(len(l) - 2):
    ch = [y for y in [l[x], l[x + 1], l[x + 2]] if len(str(abs(y))) == 4]
    if len(ch) >= 2:
        if l[x] * l[x + 1] * l[x + 2] <= mn25:
            mx.append(l[x] * l[x + 1] * l[x + 2])
print(len(mx), max(mx))