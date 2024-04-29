l =  [int(x) for x in open('4.txt')]
mx = 0
otv = 0
otv_max = 0
for i in range(len(l)):
    if ((l[i] > mx) and (l[i]%100==39) and (l[i]>999) and (l[i]<10000)):
        mx = l[i]
for i in range(len(l)-1):
    if (len(str(abs(l[i]))) == 4 and len(str(abs(l[i + 1]))) != 4) or (len(str(abs(l[i]))) != 4 and len(str(abs(l[i + 1]))) == 4):
        if ((l[i] + l[i+1])**2 <= mx**2):
            otv +=1
            if (otv_max < (l[i] + l[i+1])):
                otv_max = l[i] + l[i+1]
print(otv, otv_max)