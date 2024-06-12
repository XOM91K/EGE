#дорешать 
l = sorted([[int(d) for d in x.split()] for x in open('10.txt')])
sl = {}
mesta = [[0, 0] for x in range(3)]
# print(mesta)
# for x in range(10):
#     sl[x + 1] = []
ct_pas = 0
for x in l:
    for y in range(len(mesta)):
        if x[0] >= mesta[y][1]:
            mesta[y][0] = x[0]
            mesta[y][1] = x[1]
            ct_pas += 1
            break
    else:
        for y in range(len(mesta)):
            if x[0] == mesta[y][0]:
                mesta[y][0] = x[0]
                mesta[y][1] = max(mesta[y][1], x[1])
                break
print(ct_pas)