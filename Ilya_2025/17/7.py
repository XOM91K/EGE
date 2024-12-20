cnt = 0
d = []
l = [int(x) for x in open('7.txt')]
a = max([y for y in l if str(abs(y))[0] == '8'])
for x in range(len(l) - 2):
    b = [i for i in [l[x], l[x+1], l[x+2]] if str(abs(i))[0] == '6']
    if len(b) <= 1:
        if sum([l[x], l[x+1], l[x+2]]) >= a:
            cnt += 1
            d.append(sum([l[x], l[x+1], l[x+2]]))
print(cnt, min(d))