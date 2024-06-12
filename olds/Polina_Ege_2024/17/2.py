l = open('17_1.txt').readlines()
ct = 0
for x in range(len(l)):
    l[x] = int(l[x])
print(l)
for x in range(len(l) - 2):
    d = sorted([l[x], l[x + 1], l[x + 2]])
    if d[-1] ** 2 == d[0] ** 2 + d[1] ** 2:
        ct += 1
print(ct)