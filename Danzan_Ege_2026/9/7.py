l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    chet = [d for d in x if d%2 == 0]
    nechet = [d for d in x if d%2 != 0]
    if len(chet) > 0 and len(nechet) > 0:
        if len(chet)%2 == 0 and len(nechet)%2 != 0:
            x = sorted(x)
            if max(chet) %4 == 0:
                ct+=1
print(ct)