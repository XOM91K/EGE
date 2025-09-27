l = [[int(d)for d in x.split()]for x in open('439.txt')]
sm = 0
for x in l:
    c1 = [y for y in x if x.count(y)==3]
    c2 = [y for y in x if x.count(y)==2]
    x = sorted(x)
    if len(c1) == 3 and len(c2) == 4:
        ch = [d for d in x[:4] if d % 2 == 0]
        nch = [d for d in x[:4] if d % 2 != 0]
        if len(ch) == 2 and len(nch) == 2:
            sm += sum(x)
print(sm)