A=[]
for n in range (3,10001):
    x= '4'+'1'*n
    while '411' in x or '1111' in x :
        if '411' in x:
            x=x.replace('411','14',1)
        if '1111' in x:
            x=x.replace('1111','1',1)
    A.append(x.count('1') + x.count('4') * 4)

print(max(A))