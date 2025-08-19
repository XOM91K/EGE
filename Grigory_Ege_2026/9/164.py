l = [[int(d) for d in x.split()] for x in open('164.txt')]
k = 0
for x in l :
    k+=1
    if x == sorted(x):
        povt = [y for y in x if x.count(y)>=2 and sum(map(int, str(y))) % 2 == 0]
        #if sum(povt)%2 == 0:
        if len(povt) > 0:
            print(k)