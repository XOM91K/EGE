l=[[int(d) for d in x.split()] for x in open('800.txt')]
ct=0
for x in l:
    povt=[y for y in x if x.count(y)>=3]
    nepovt=[y for y in x if x.count(y)==1]
    povt2 = [y for y in x if x.count(y) == 2]
    if len(povt)>=3 and len(nepovt) >= 1:
        print(povt, nepovt)
        if (sum(povt) + sum(povt2)) /(len(povt) + len(povt2))>sum(nepovt) / len(nepovt):
            ct+=1
print(ct)