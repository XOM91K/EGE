l = [[int(d)for d in x.split()]for x in open('10.txt')]
l = sorted(l, key=lambda x: x[1])
print(l)
m = [l[0]]
for x in l:
    if x[0] > m[-1][1] + 20:
        m += [x]
print(m)
print(len(m))
for x in l:
    if x[0] > 1236:
        print(x[0], 1288 - 1236)