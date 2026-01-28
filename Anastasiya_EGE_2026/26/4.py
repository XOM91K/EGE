l = sorted([int(x) for x in open('4.txt')])
print(l)
lt = 0
rt = len(l) - 1
mx = 400
cont = 0
mass = 0
while lt < rt:
    if l[lt] + l[rt] <= mx:
        cont += 1
        lt += 1
    elif l[lt] + l[rt] > mx:
        mass += l[rt]
    rt -= 1
print(cont, mass)