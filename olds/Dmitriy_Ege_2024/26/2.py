s = 8200
l = sorted([int(x) for x in open('2.txt')])
mx_users = 0
x = 0
while s - l[x] > 0:
    s -= l[x]
    mx_users += 1
    x += 1

s += l[x - 1]
for x in range(len(l) - 1, -1, -1):
    if s - l[x] > 0:
        print(l[x])
        break
print(mx_users)