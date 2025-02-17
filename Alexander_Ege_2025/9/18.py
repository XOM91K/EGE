l = [sorted([int(d) for d in x.split()]) for x in open('18.txt')]
cnt =0
for x in l:
    if (x[-2] + x[-1]) * 2 > 3 * (x[0] + x[1] + x[2]):
        c5 = [i for i in x if str(i)[-1] == '5']
        if len(c5) >= 2:
            cnt += 1
print(cnt)