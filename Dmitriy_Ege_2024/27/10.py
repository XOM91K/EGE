l = [int(x) for x in open(r'C:\Users\Zarif\Downloads\27_B_7627.txt')]
k = 1000_000
mx_l = 0
mx_r = 0
for i in range(k, len(l)):
    mx_l = max(mx_l, l[i - k])
    mx_r = max(mx_r, mx_l + l[i])
print(mx_r)

