l=[[int(d) for d in x.split()] for x in open('7.txt')]
ct=0
for x in l:
    povt=[m for m in x if x.count(m) >= 2]
    if len(povt) > 0:
        if x.count(min(x)) == 1:
            if (max(x) + min(x)) < sum(povt):
                ct+=1
print(ct)