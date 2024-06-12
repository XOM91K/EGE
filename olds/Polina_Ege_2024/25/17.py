def dels(n):
    dels = []
    for x in range(1,int(n**0.5)+1):
        if n%x ==0 and x!= n//x:
            if x % 2 == 0:
                dels.append(x)
            if (n // x) % 2 == 0:
                dels.append(n//x)
        elif n%x ==0 and x%2==0 :
            dels.append(x)

    return sorted(dels)
import fnmatch
for i in range(65001,65000*10):
    if fnmatch.fnmatch(str(i),'6*97*5?' ):
        if len(dels(i)) >= 4:
            print(i,sum(dels(i)))