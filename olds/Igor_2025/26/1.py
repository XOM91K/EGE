s = 8200
l = sorted([int(x) for x in open('1.txt')])
ct_users = 0
mx_file = 0
for x in l:
    if s - x >= 0:
        s -= x
        mx_file = x
        ct_users += 1
s += mx_file
for x in l[::-1]:
    if s - x >= 0:
        print(x)
        break
print(ct_users)
