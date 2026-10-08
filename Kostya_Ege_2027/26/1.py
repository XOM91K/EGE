l = sorted([int(x) for x in open('1.txt')])[::-1]
l2 = [l[0]]
for x in l:
    if l2[-1] - x >= 8:
        l2.append(x)
print(len(l2), l2[-1])