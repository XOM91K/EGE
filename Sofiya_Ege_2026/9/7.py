l=[[int(d) for d in x.split()] for x in open('7.txt')]
k = 0
for x in l:
    k += 1
    x=sorted(x)
    if x[0]<=x[1]<=x[2]<=x[3]<=x[4]:
        if len(set(x))<=4:
            povt = [sum(map(int, str(d))) % 2 for d in x if x.count(d) > 1]
            if povt.count(0) > 0:
                print(k)