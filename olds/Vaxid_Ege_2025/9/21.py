l = [[int(d) for d in x.split()] for x in open('21.txt')]
ct = 0
for x in l:
    sr = sum(x) / len(x)
    if sr % 1 == 0:
        if len(set(x)) == 4:
            povt = sum(x) - sum(set(x))
            if x[0] == povt and x[-1] == povt:
                print(x, povt)
                ct += 1
print(ct)
        #print(x, sr)