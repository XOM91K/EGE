l = [[int(d) for d in x.split()] for x in open('99.txt')]
ct = 0
for x in l:
    if len(set(x)) == 2 or (len(set(x)) == 1):
        if (x[0]+x[1]+x[2]+x[3]) == 360 :
            if (x[0] == x[1] and x[2] == x [3] and x[0] == 180 - x[2]) or (x[0] == x[2] and x[1] == x [3] and x[0] == 180 - x[3]) or (x[0] == x[3] and x[2] == x [1] and x[0] == 180 - x[2]) or (x[2] == x[1] and x[0] == x [3] and x[2] == 180 - x[3]) or(x[3] == x[1] and x[2] == x [0] and x[1] == 180 - x[2]):
                ct+=1

print(ct)