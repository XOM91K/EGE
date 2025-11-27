l = [[int(d) for d in x.split()] for x in open('9.txt')]
mx = []
for x in l: #[33, 33, 44, 33, 1, 2]
    povt3 = [y for y in x if x.count(y) == 3]
    povt2 = [y for y in x if x.count(y) == 2]
    x = sorted(x)
    if (len(povt3) == 3 and len(povt2) == 4) or (x[0] + x[-1]) >= 2 * (x[1] + x[2] + x[3] + x[4] + x[5]):
        mx.append(sum(x))