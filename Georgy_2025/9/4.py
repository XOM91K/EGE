l = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4:
        if (x[-1] + x[0]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
            ct += 1
print(ct)
# a = [1, 2, 3] #list список
# b = (1, 2, 3) #tuple кортеж
# st = 'abracadabra'
# print(set(st)) #set множества
# print(list(st)[2])
# print(tuple(st)[4])