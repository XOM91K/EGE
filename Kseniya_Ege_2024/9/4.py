l = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
k = 0
sm = 0
for x in l:
    k += 1
    if len(set(x)) == 5 and (x.count(x[2]) == 3 or x.count(x[4]) == 3):
        povt = (sum(x) - sum(set(x))) // 2
        if povt != x[0] and povt != x[-1]:
            print(x)
            sm += k
print(sm)