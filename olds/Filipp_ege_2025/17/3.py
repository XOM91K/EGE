l = [int(x) for x in open('3.txt')]
mi = [x for x in l if x % 52 == 0]
mi = min(mi)
ans = []
for x in range(len(l) - 2):
    #l_4 = [len(str(abs(y))) for y in [l[x], l[x + 1], l[x + 2]]]
    if l[x] % 113 + l[x + 1] % 113 + l[x + 2] % 113 == mi:
        ans.append(l[x] + l[x + 1] + l[x + 2])
print(len(ans), max(ans))