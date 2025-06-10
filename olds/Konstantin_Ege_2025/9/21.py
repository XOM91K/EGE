l = [[int(d) for d in x.split()] for x in open('21.txt')]
# [0, 2, 3, 4, 5, 10] # возрастания
# [0, 2, 3, 3, 5, 10] # не убывания
ct = 0
for x in l:
    if x[0] < x[1] < x[2] < x[3] < x[4] < x[5] < x[6]:
        if (x[0] + x[6]) / 2 > (x[1] + x[2] + x[3] + x[4] + x[5]) / 5:
            ct += 1
print(ct)