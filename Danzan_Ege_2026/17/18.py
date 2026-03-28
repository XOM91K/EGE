l = [int(x) for x in open('18.txt')]
mx = []
ln3 = len([d for d in l if len(str(abs(d))) == 4 and str(d)[-1] == '3']) ** 2
for x in range(len(l) - 2):
    r = sorted([l[x], l[x + 1], l[x + 2]])
    smb = r[1] + r[2]
    if smb > ln3:
        mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), abs(max(mx)))
# 7236 286698