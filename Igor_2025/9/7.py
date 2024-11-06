cnt = 0
l = [sorted([int(d) for d in x.split()]) for x in open("7.txt")]
for x in l:
    if x.count(x[0]) == 1:
        
        for y in x:
            if x.count(y) > 1:
                if x[0]+x[-1] < (x[1]+x[2]+x[3]+x[4]) / 2:
                    cnt +=1
                    break
print(cnt)