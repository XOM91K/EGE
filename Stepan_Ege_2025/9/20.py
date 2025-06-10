l = [[int(d) for d in x.split()] for x in open('20.txt')]
k = 0
for x in l:
    k += 1
    ch = [1 for i in x if i % 2 == 0]
    nch = [1 for i in x if i % 2 != 0]
    if sum(ch) == sum(nch):
        x.sort()
        if x[0] + x[-1] == x[1] + x[-2] == x[2] + x[-3]:
            print(k, x)