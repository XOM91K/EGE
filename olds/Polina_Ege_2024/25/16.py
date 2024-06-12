def dels(n):
    dels = []
    for x in range(2,int(n**0.5)+1):
        if n%x ==0 and x!= n//x:
            if x % 2 != 0:
                dels.append(x)
            if (n // x) % 2 != 0:
                dels.append(n//x)
        elif n%x ==0 :
            if x % 2 != 0:
                dels.append(x)

    return sorted(dels)

for i in range(18782,18823):
    if len(dels(i)) == 3:
        print(*dels(i))