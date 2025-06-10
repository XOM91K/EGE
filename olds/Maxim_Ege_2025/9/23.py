l = [[int(d) for d in x.split()] for x in open('23.txt')]
ct = 0
# [22, 19, 18, 18, 2, 1] #не возрастания
# [22, 19, 18, 17, 2, 1]
for x in l:
    #if x[0] > x[1] > x[2] > x[3] > x[4] > x[5] > x[6]:
    if x == sorted(x)[::-1]:
        if (x[0] + x[-1]) / 2 > (x[1] + x[2] + x[3] + x[4] + x[5]) / 5:
            ct += sum(x)
            break
print(ct)