l = [int(x) for x in open('4.txt')]
q = 28442
mx_left = mx_middle = mx_right = 0
for x in range(2 * q, len(l)):
    mx_left = max(mx_left, l[x - 2 * q])
    mx_middle = max(mx_middle, mx_left * l[x - q])
    mx_right = max(mx_right, mx_middle * l[x])
print(mx_right % (10 ** 6 + 1))
