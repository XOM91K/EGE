l = [[int(d) for d in x.split()] for x in open('9.txt')]
ct = 0
for x in l:
    chet = [d for d in x if d % 2 == 0]
    nechet = [d for d in x if d % 2 != 0]
    if len(chet) > 0 and len(nechet) > 0:
        if len(chet) % 2 == 0 and len(nechet) % 2 != 0:
            if max(chet) % 4 == 0:
                ct += 1
print(ct)
# if (x[2]-x[1]) != 0 and ([-1]-x[0])%(x[2]-x[1])==0x: