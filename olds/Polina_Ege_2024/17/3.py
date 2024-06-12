l = [int(x) for x in open('17_2.txt')]
mx_md = 0
ct = 0
mx = 0
for x in l:
    if abs(x) % 1001 == 0:
        mx_md = max(mx_md, abs(x))
for x in range(len(l) - 1):
    if (len(str(abs(l[x]))) == 3 or len(str(abs(l[x + 1]))) == 3) and ((l[x] + l[x + 1]) > mx_md):
        ct += 1
        mx = max(mx, l[x] + l[x + 1])
        print(l[x], l[x + 1], l[x] + l[x + 1])
print(ct, mx)