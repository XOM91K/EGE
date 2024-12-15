cnt = 0
l = [int(x) for x in open('5.txt')]
l_7 = max([int(i) for i in l if str(i)[-1] == '7'])
s = set()
for x in range(len(l) - 3):
    a = [j for j in [l[x], l[x+1], l[x+2]] if j % 2 != 0]
    b = [d for d in [l[x], l[x+1], l[x+2]] if d > l_7]
    if len(a) == 2 and len(b) == 1:
        cnt += 1
        s.add(l[x])
        s.add(l[x + 1])
        s.add(l[x + 2])
print(cnt, sum(s) / len(s))