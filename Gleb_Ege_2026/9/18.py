l = [[int(d) for d in x.split()] for x in open('18.txt')]
k = 0
for x in l:
    k += 1
    chet = [d for d in x if d % 2 == 0]
    nechet = [d for d in x if d % 2 != 0]
    if len(chet) == len(nechet):
        x = sorted(x)
        if x[0] + x[-1] == x[1] + x[-2] == x[2] + x[-3]:
            print(k, x)