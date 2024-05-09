l = [int(x) for x in open('8.txt')]
mn1 = 10 ** 10
mn2 = 10 ** 10
mn3 = 10 ** 10
sm = 0
k = 165423
for i in range(len(l) - 2 * k):
    mn1 = min(mn1, l[i])
    mn2 = min(mn2, mn1 + l[i + k])
    mn3 = min(mn3, mn2 + l[i + 2 * k])
print(mn3)