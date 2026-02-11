l = [[int(d) for d in x.split()] for x in open('4.txt')]
ct = 0
for x in l:
    # [1, 1, 2, 2, 3, 3]
    povt2 = [d for d in x if x.count(d) == 2]
    if len(povt2) == 2:
        x = sorted(x)
        pol = [d for d in x if d > 0]
        otr = [d for d in x if d < 0]
        if abs(sum(otr)) > sum(pol):
            ct += 1
print(ct)
