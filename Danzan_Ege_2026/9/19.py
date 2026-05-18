l = [[int(d) for d in x.split()] for x in open('19.txt')]
for x in l:
    x = sorted(x)
    if (x[-2]) ** 2 > (x[0] * x[-1]):
        if sum(x) % 2 == 0:
            sm = []
            for i in x:
                if i < 90:
                    sm.append(i)
            if str(sum(sm))[-1] == '4':
                print(x, sum(x))