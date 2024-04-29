l=[[int(d)for d in x.split()]for x in open('11.txt')]
ob=0
for x in l:
    mn = min(x)
    x.remove(max(x))
    x.remove(min(x))
    if sum(x) % mn == 0:
        ob += 1

print(ob)