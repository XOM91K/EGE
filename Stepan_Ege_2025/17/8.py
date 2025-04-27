l = [int(x) for x in open('8.txt')]
mx1 = max([y for y in l if str(abs(y))[-1] == '1'])
mn = []
for x in range(len(l) - 3):
    ch = [y for y in [l[x], l[x + 1], l[x + 2], l[x + 3]] if y % 2 == 0]
    if len(ch) % 2 != 0:
        if l[x] < mx1 and l[x + 1] < mx1 and l[x + 2] < mx1 and l[x + 3] < mx1:
            mn.append(sum([l[x], l[x + 1], l[x + 2], l[x + 3]]))
print(len(mn), min(mn))