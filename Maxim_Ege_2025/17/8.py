l = [int(x) for x in open('8.txt')]
k = 0
su = []
ma7 = []
for x in l:
    if str(x)[-1] == '7':
        ma7.append(x)
ma7 = max(ma7)
print(ma7)
for x in range(len(l)-1):
    if str(l[x])[0] == str(l[x+1])[0]:
        na7 = 0
        if str(l[x])[-1] == '7' and len(str(abs(l[x]))) == 3:
            na7 += 1
        if str(l[x + 1])[-1] == '7' and len(str(abs(l[x + 1]))) == 3:
            na7 += 1
        if na7 >= 1:
            if (l[x] + l[x + 1]) < ma7:
                k += 1
                su.append((l[x] + l[x + 1]))
print(k,max(su))
