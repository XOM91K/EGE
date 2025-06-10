l = [sorted([int(d) for d in x.split()]) for x in open('6.txt')]
cnt = 0
for x in l:
    kr3 = [n for n in x if n % 3 == 0]
    if len(kr3) == 3:
        if x[-1] - x[0] <= sum(kr3):
            cnt += 1
print(cnt)







# g = [1, 2, 4, 33, 12, 15, 19]
# e = [a for a in g if a % 3 == 0]
# print(e)
# t = [3 * f for f in g if f > 10]
# print(t)
#f = [-d for d in g] #копирование элементов из списка g
#t = [2*d for d in g]
#print(t)
# g.append(99)
# print(g)
# print(f)