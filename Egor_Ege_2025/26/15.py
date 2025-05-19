l = [[int(d) for d in x.split()] for x in open('15.txt')]
# 1) сумма – общее количество набранных баллов;
# 2) плюсы – сумма баллов без учёта неверных ответов;
# 3) ответы – общее количество сданных ответов (верных и неверных).
l = sorted(l, key=lambda d: (-sum(d[1:]), -sum([x for x in d[1:] if x > 0]), d[1:].count(0), d[0]))
print(len(l))
zach = l[:len(l) // 3]
ct = 0
for x in l:
    ct += 1
    print(ct, x, sum(x[1:]), sum([y for y in x[1:] if y > 0]), x[1:].count(0))