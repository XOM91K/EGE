l = [int(x) for x in open('1.txt')]
o = 0
c = []
y = 0
for i in l:
    if i > o and str(i)[-1] == '1':
        o = i

print(o)
for i in range(len(l) - 3):
    ct = 0
    for z in range(4):
        if l[i + z] % 2 == 0:
            ct += 1
    if ct % 2 != 0:
        if l[i] < o and l[i + 1] < o and l[i + 2] and l[i + 3] < o:
            y += 1
            c.append(l[i] + l[i + 1] + l[i + 2] + l[i + 3])
print(y, min(c))