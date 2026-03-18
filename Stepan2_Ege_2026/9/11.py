l = [[int(d) for d in x.split()] for x in open('11.txt')]
sm = 0
for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    if len(povt3) == 3:
        povt2 = [d for d in x if x.count(d) == 2]
        if len(povt2) == 4:
            x = sorted(x)
            chetiri = x[:4]
            ch = [d for d in chetiri if d % 2 == 0]
            if len(ch) == 2:
                sm += sum(x)
print(sm)