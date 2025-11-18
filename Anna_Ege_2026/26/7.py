l = [int(x) for x in open('7.txt')]
l = sorted(l)[::-1]
k = [l[0]]
for x in l:
    if k[-1] - x >= 8:
        k.append(x)
print(len(k), k[-1])