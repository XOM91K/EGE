l = [int(x) for x in open('1.txt')]
l.sort(reverse=True)
l = sorted(l)[::-1]
mat = [l[0]]
for x in l:
    if mat[-1] - x >= 9:
        mat.append(x)
print(len(mat), min(mat), mat[-1])