l=[[int(d) for d in x.split()] for x in open('7.txt')]
l=sorted(l)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
for x in sl:
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 12:
            print(x, sl[x][y] + 1)
            break
# mx=[]
# for x in l:
# print(l)