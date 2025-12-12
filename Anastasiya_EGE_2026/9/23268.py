l = [[int(d) for d in x.split()] for x in open('23268.txt')]
k=0
for x in l:
    k+=1
    povt=[y for y in x if x.count(y)==2]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt)==4 and len(nepovt)==3:
        if sum(povt)/len(povt) < sum(nepovt):
            print(k, x)
