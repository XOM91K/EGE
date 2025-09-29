l = [[int(d) for d in x.split(',')] for x in open('6.txt')]
sm = 0
for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    povt2 = [d for d in x if x.count(d) == 2]
    if len(povt3) == 3 and len(povt2) == 4:
        x = sorted(x)
        ch = x[:4]
        nechet = [d for d in ch if d % 2 != 0]
        chet = [d for d in ch if d % 2 == 0]
        if len(nechet) == 2 and len(chet) == 2:
            sm += sum(x)
print(sm)