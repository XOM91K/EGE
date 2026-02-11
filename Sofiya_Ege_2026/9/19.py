l=[[int(d) for d in x.split()]for x in open(r'C:\Users\Zarif\Downloads\1424_1 (10).csv')]
stb1 = [x[0] for x in l]
stb6 = [x[-1] for x in l]
ct=0
for x in l:
    povt3=[a for a in x if x.count(a)==3]
    nepovt=[a for a in x if x.count(a)==1]
    if len(povt3)==3 and len(set(x))==4:
        if stb1.count(povt3[0])==337 or stb6.count(nepovt[0])==337 or stb6.count(nepovt[1])==337 or stb6.count(nepovt[2])==337:
            ct+=1
print(ct)