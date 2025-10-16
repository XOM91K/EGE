l = [int(x) for x in open('7.txt')]
min1 = min([x for x in l if x>0 and x%10==4])
d = []
for x in range(len(l) - 2):
    if sum(map(int, str(abs(l[x])) + str(abs(l[x + 1])) + str(abs(l[x + 2]))))==min1:
        d.append(l[x]+l[x+1]+l[x+2])
print(len(d), max(d))