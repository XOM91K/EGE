l = [int(x) for x in open('15.txt')]
min21 = (min([x for x in l if x > 0 and len(str(abs(x))) == 4 and sum(map(int, str(x))) == 21]))**2
ct = 0
mx = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and sum(map(int, str(abs(l[x])))) == 15:
        k+=1
    if len(str(abs(l[x + 1]))) == 4 and sum(map(int, str(abs(l[x + 1])))) == 15:
        k+=1
    if len(str(abs(l[x + 2]))) == 4 and sum(map(int, str(abs(l[x + 2])))) == 15:
        k+=1
    if k == 2:
        if (l[x] + l[x + 1] + l[x + 2]) * 98 >= min21:
            ct += 1
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(ct, max(mx))