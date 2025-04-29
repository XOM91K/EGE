l = [int(x) for x in open('3.txt')]
sr = [x for x in l if str(x)[-2:] == '28']
sr = sum(sr) / len(sr)
mn = []
for x in range(len(l) - 2):
    k = [y for y in [l[x], l[x + 1], l[x + 2]] if len(str(abs(y))) == 4]
    if len(k) >= 1:
        k = [y for y in [l[x], l[x + 1], l[x + 2]] if str(abs(y))[-2:] == '11']
        if len(k) == 2:
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                mn.append(l[x] + l[x + 1] + l[x + 2])
print(len(mn), min(mn))