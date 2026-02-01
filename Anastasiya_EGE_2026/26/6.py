l=sorted([int(x) for x in open('6.txt')])[::-1]
k=[l[0]]
ct=1
for i in l:
    if k[-1]- i >= 8:
        k.append(i)
        ct+=1
print(ct)
print(k[-1])