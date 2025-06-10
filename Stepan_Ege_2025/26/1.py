a = sorted([[int(j) for j in i.split()]for i in open("1.txt")], key=lambda d: (d[0], -d[1]))
p = []
s = 0
count = 0
for i in a:
    s += i[0] * i[1] / i[1]
cr = s
for i in a:
    if i[0] > cr > 1.5:
        p.append(i)
#m = min(p, key=lambda x: (x[0], -x[1]))

for x in a[:85000]:
    print(x, x[0] * 1.5)
print(cr)
# print(m[0] * m[1])
# k = 0
# for i in p:
#     if i[0] == m[0]:
#         k += i[1]
# print(k)
