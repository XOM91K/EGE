s = 8200
l = sorted([int(x) for x in open('1.txt')])
for x in range(len(l)):
    if s - l[x] > 0:
        s -= l[x]
    else:
        break
s += l[x - 1]
print(x)
for x in range(len(l) - 1, -1, -1):
    if s - l[x] > 0:
        print(l[x])
        break