l = [[int(d) for d in x.split()] for x in open("8.txt")]
cnt = 0
for x in l:
    chet = []
    nechet = []
    for y in x:
        if int(y) % 2 == 0:
            chet.append(y)
        else:
            nechet.append(y)
    k = 0
    if (len(set(x)) == 4):
        k += 1
    if sum(nechet) > sum(chet):
        k += 1
    if k == 1:
        cnt+=1
print(cnt)