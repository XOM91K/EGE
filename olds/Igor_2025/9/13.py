f = [[int(i) for i in z.split()] for z in open('13.txt')]
for i in range(len(f)):
    l = f[i]
    if l == sorted(l):
        povt = [n for n in l if l.count(n)>1]
        nepovt = [y for y in l if l.count(y)==1]
        povt_cnts = [l.count(b) for b in povt]
        print(l, povt, nepovt)
        print(povt_cnts)
        if sorted(set(povt_cnts)) == [2,4] and len(nepovt)==1:
            if max(povt) <= nepovt[0]:
                print(i+1)
                break