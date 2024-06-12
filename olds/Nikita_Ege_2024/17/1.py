l = open('1.txt').readlines()
mx_2 = 0
ct = 0
mx = 0
for x in range(len(l)):
    l[x] = int(l[x])
    if len(str(l[x])) == 2:
        mx_2 = max(mx_2, l[x])
for x in range(len(l) - 1):
    if ((len(str(l[x])) == 2 and len(str(l[x + 1])) != 2) or (len(str(l[x])) != 2 and len(str(l[x + 1])) == 2)) and ((l[x] + l[x + 1]) % mx_2 == 0):
        ct += 1
        mx = max(l[x] + l[x + 1], mx)
print(ct, mx)