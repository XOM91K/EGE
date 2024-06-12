k = 10000
t = 100000
l = [[int(d) for d in x.split()] for x in open(r'C:\Users\Zarif\Downloads\27-B_11895.txt')]
mn_left = 10 ** 1000
mx_right = 0
for x in range(len(l) - t):
    mn_left = min(mn_left, l[x][0])
    mx_right = max(mx_right, l[x + t][1])
print(((k // mn_left) * mx_right) - (mn_left * (k // mn_left)))