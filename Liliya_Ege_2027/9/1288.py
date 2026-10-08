l = [[int(d) for d in x.split()] for x in open('1288.txt')]
ct = 0
for x in l:
    # 33 33 33 9 9 9 8
    tr = [d for d in x if x.count(d) == 3]
    if len(tr) == 6:
        if max(tr) > sum(x) - sum(tr):
            ct += 1
print(ct)