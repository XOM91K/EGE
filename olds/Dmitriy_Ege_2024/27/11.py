k = 165423
l = [int(x) for x in open('11.txt')]
mn = 10 ** 10
mn_l = mn_m = mn_r = 10 ** 10
for i in range(2 * k, len(l)):
    mn_l = min(mn_l, l[i - 2 * k])
    mn_m = min(mn_m, mn_l + l[i - k])
    mn_r = min(mn_r, mn_m + l[i])
print(mn_r)