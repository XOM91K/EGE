l = [int(x) for x in open('10.txt')]
o = 0
c = []
mn = []
for i in l:
    if str(i)[-1] == '7':
        mn.append(i)
mn = min(mn)
for x in range(len(l) - 2):
    if len(str(abs(l[x]))) == 5 or len(str(abs(l[x + 1]))) == 5 or len(str(abs(l[x + 2]))) == 5:
        if (l[x] * l[x + 1] * l[x + 2]) % mn == 0:
            o += 1
            c.append(l[x] * l[x + 1] * l[x + 2])
print(o, max(c))