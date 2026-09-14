l = [[int(d) for d in x.split()] for x in open("316.txt")] # 1 2 3 4 
ct = 0
for x in l:
    if max(x) < (sum(x) - max(x)):
        x = sorted(x)
        print(x)
        if (x[0] + x[3]) == (x[1] + x[2]):
            ct+=1
print(ct)