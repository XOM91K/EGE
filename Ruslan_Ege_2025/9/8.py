l = [sorted([int(d) for d in x.split(',')]) for x in open('8.txt')]
k = 0
for x in l:
    if len(x) == len(set(x)):
        if (x[-1]+x[-2])*2 >= (x[0]+x[1]+x[2]+x[3])*3:
            k+=1
print(k)