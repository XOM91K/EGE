l = [[int(d) for d in x.split()] for x in open('9.txt')]
sm = 0
k = 0
for x in l:
    k += 1
    povt4 = [d for d in x if x.count(d) == 4]
    if len(set(x)) == 4 and len(povt4) == 4:
        if sorted(x) == x:
            sm += k
print(sm)