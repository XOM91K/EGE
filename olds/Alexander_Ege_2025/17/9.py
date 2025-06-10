# 155
l = [int(x) for x in open("9.txt")]
mn = []
minchetn = min([i for i in l if i%2==0])
for x in range(len(l)-2):
    if l[x] % 2 != l[x + 2] % 2:
        if l[x + 1] % minchetn == 0:
            mn.append(l[x] + l[x + 2])
print(len(mn), min(mn))
