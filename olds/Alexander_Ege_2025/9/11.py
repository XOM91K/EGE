# 164
l = [[int(d) for d in x.split()] for x in open("11.txt")]
k = 0
for x in l:
    k += 1
    # if x[0]<=x[1] and x[1]<=x[2] and x[2]<=x[3] and x[3]<=x[4]:
    if x == sorted(x):
        povt = []
        for y in x:
            if x.count(y) > 1:
                povt.append(y)

        if len(povt) > 0:
            print(k, x, povt)
    # if sum(map(int, x))
