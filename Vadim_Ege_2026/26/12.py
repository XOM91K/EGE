l = [[int(d) for d in x.split()] for x in open('12.txt')]
pr = [0] * 44640
l = sorted(l, key=lambda d: (d[0], d[1]))
for m in range(44640):
    for y in l:
        if y[0] <= m < y[1]:
            pr[m] = 1
            break
print(sum(pr))
pr = ''.join(map(str, pr))
print(len(max(pr.split('0'), key=len)))