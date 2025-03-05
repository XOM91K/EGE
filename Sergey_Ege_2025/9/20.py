l = [[int(d) for d in x.split()] for x in open('20.txt')]
k = 0
for x in l:
    k += 1
    if x[4] >= x[3] >= x[2] >= x[1] >= x[0]:
        povt_chet = [d for d in x if x.count(d) > 1 and sum(map(int, str(d))) % 2 == 0]
        if len(povt_chet) > 0:
        #if sorted(x) == x:
            print(k, x, povt_chet)
