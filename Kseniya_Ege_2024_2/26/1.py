l = sorted(set([int(x) for x in open('1.txt')]))[::-1]
l1 = [9998]
i = 0
for x in range(1, len(l)):
    if l[i] - l[x] >= 8:
        i = x
        l1.append(l[x])
print(len(l1), min(l1))