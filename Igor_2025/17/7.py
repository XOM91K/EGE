l = [int(x) for x in open('7.txt')]
pt43 = max([y for y in l if len(str(abs(y))) == 5 and str(y)[-2:] == '43'])
ct = 0
mn = []
for x in range(len(l) - 2):
    if len([y for y in [l[x], l[x + 1], l[x + 2]] if len(str(abs(y))) == 5 and str(y)[-2:] == '43']) >= 1:
        if sum([l[x] ** 2, l[x + 1] ** 2, l[x + 2] ** 2]) <= pt43 ** 2:

            ct += 1
            mn.append(sum([l[x] ** 2, l[x + 1] ** 2, l[x + 2] ** 2]))
print(ct, min(mn))