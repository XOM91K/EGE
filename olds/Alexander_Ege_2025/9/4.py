l = [[int(d) for d in x.split()] for x in open('4.txt')]
k = 0
for x in l:
    k += 1
    n3 = []
    n1 = []
    for y in x:
        if x.count(y) == 3:
            n3.append(y)
        if x.count(y) == 1:
            n1.append(y)
    if len(n3) == 6:
        if sum(n3) / 6 < n1[0]:
            print(k, x)
# l = [9, -10, 5]
# for y in l:
#     print(y)