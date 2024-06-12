arr=[]
for i in range(0,9,2):
    for j in range(1,999):
        if '0' not in str(j) and '2' not in str(j) and '4' not in str(j) and '6' not in str(j) and '8' not in str(j):
            s="1"+str(i)+"2157"+str(j)+"4"
            if int(s) <= 10 ** 10:
                if int(s)%133==0:
                    arr.append([int(s), int(s) // 133])
for x in sorted(arr):
    print(*x)