l=[[int(d) for d in x.split()] for x in open('9.txt')]
ct=0
sm = 0
for x in l:
    x=sorted(x)
    povt3 = [d for d in x if x.count(d)==3]
    povt2 = [d for d in x if x.count(d)==2]
    chet = [d for d in x[:4] if d % 2 == 0]
    nechet = [d for d in x[:4] if d % 2 != 0]
    if len(povt3)==3 and len(povt2)==4:
        if len(chet) == 2 and len(nechet) == 2:
            ct+=1
            print(sum(x))
            sm += sum(x)
print(sm)