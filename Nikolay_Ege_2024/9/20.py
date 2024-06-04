l=[sorted(int(d)for d in x.split())for x in open(r'20.txt')]
print(l)
ct=0
for x in l:
    chet = []
    nechet = []
    for y in x:
        if y%2==0:
            chet.append(y)
        else:
            nechet.append(y)
    if x[-1]%2!=0 and x[0]%2==0 and sum(chet)>sum(nechet):
        ct+=1
print(ct)
