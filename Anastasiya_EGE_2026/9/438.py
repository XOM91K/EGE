import math #zadaha iz dz
l=[[int(d) for d in x.split()] for x in open('438.txt')]
sm = 0
k=0
for x in l:
    k+=1
    if (x[0]%2==0 and x[2]%2==0 and x[4]%2==0 and x[6]%2==0 and x[1]%2!=0 and x[3]%2!=0 and x[5]%2!=0) or (x[0]%2!=0 and x[2]%2!=0 and x[4]%2!=0 and x[6]%2!=0 and x[1]%2==0 and x[3]%2==0 and x[5]%2==0):
        povt = [d for d in x if x.count(d) >= 2]
        nepovt = [d for d in x if x.count(d) == 1]
        if sum(nepovt) * 3 >= math.prod(povt):
            sm += k
print(sm)