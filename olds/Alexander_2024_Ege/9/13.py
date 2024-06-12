l=[sorted([int(d) for d in x.split()]) for x in open("13.txt")]
c=0
print(l)
for x in l:
    if x[-1]<x[0]+x[1]+x[2]:
        if x[0]+x[-1]==x[1]+x[2]:
            c+=1
            print(x)
print(c)