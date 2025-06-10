f = [int(n) for n in open('17.txt')]



min4 = 10**100
for x in f:
    if x >0:
        if (len(str(abs(x)))==4 and str(x)[-1]=='6'):
            min4 = min(x, min4)

cnt = 0
mx_sm = 0
for i in range(len(f)-2):
    l = [f[i], f[i+1], f[i+2]]
    if sum([int((len(str(abs(n)))==4 and str(n)[-1]=='6')) for n in l])==1:
        if sum(l) <= min4:
            mx_sm = max(sum(l), mx_sm)
            cnt += 1
print(cnt, mx_sm)