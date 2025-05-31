k = 0
l = [[int(d) for d in x.split()]for x in open("29.txt")]
for x in l:
    k += 1
    povt2 = [i for i in x if x.count(i)==2]
    nepovt = [i for i in x if x.count(i)==1]
    if len(povt2)==6:
        if len(nepovt)==2:
            povt2 = sorted(povt2)
            if (povt2[-1]-povt2[0])**2>2*(nepovt[0]**2+nepovt[1]**2):
                print(k)