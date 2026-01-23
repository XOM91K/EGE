import fnmatch
def dels(d):
    l=[]
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
sost=[x for x in range(3, 100000) if len(dels(x))>0]
for x in range(22768, 10**8, 22768):
    if fnmatch.fnmatch(str(x), '1*03*6*'):
        ind = str(x).find('03')
        N = str(x)[1:ind]
        if N != '' and N[0] != '0':
            if int(N) in sost:
                print(x, int(N))
# s = '100'
# print(s.find('03'))