l = [int(x) for x in open('14.txt')]
k = 0
ct = 0
ct2 = 0
mn = 10**100
for x in l:
    if str(abs(x))[-2:] == '28':
        k+=1
        ct+=x
srarf = ct / k
for x in range(len(l)-2):
    if len(str(abs(l[x]))) == 4 or len(str(abs(l[x+1]))) == 4 or len(str(abs(l[x+2]))) == 4:
        if (str(l[x])[-2:] == '11' and str(l[x+1])[-2:] == '11' and str(l[x+2])[-2:] != '11') or (str(l[x+2])[-2:] == '11' and str(l[x])[-2:] == '11' and str(l[x+1])[-2:] != '11') or (str(l[x+2])[-2:] == '11' and str(l[x+1])[-2:] == '11' and str(l[x])[-2:] != '11') :
            print(l[x], l[x + 1], l[x + 2])
            if l[x]>srarf and l[x+1] > srarf and l[x+2] > srarf:
                ct2+=1
                mn = min(mn,l[x]+l[x+1]+l[x+2])
print(ct2,mn)