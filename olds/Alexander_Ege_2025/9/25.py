ct=0
l = [sorted([int(d) for d in x.split()])for x in open("25.txt")]
for x in l:
    if x[-1] < x[0] + x[1] + x[2]:
        if len(set(x)) == 3:
            ct+=1
            print(x)
print(ct)