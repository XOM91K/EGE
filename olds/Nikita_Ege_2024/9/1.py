l = [[int(d) for d in x.split()] for x in open('1.txt')]
otv = 0
for i in range(len(l)):
    kolvo_usl = 0
    if (len(l[i])==len(set(l[i]))+1):
        kolvo_usl += 1
    ch = 0
    nch = 0
    for j in l[i]:
        if j % 2 == 0:
            ch += j
        else:
            nch += j
    if nch > ch:
        kolvo_usl += 1
    if kolvo_usl == 1:
        otv += 1
print(otv)