#l = [int(x) for x in open('6.txt')]
#Составление префиксной суммы
l = [3, 4, 10, 3, 2, 8, 1, 1]
pr_l = [0] * (len(l) + 1)
for x in range(len(l)):
    pr_l[x + 1] = pr_l[x] + l[x]
print(pr_l)