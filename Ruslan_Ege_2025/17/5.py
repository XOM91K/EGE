l = [int(x) for x in open('5.txt')]
mx1 = max([j for j in l if str(j)[-1] == '1'])
mn = []
for x in range(len(l) - 3):
    ch = [j for j in [l[x], l[x + 1], l[x + 2], l[x + 3]] if j % 2 == 0]
    if len(ch) % 2 != 0:
        if max([l[x], l[x + 1], l[x + 2], l[x + 3]]) < mx1:
            mn.append(sum([l[x], l[x + 1], l[x + 2], l[x + 3]]))
print(len(mn), min(mn))