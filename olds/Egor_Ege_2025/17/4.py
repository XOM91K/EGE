b = []
a = []
cnt = 0
l = [int(x) for x in open('4.txt')]
l_2 = [int(i) for i in l if len(str(abs(i))) == 2]
l_2 = max(l_2)
for x in range(len(l) - 3):
    if str(l[x])[-1] == str(l[x+1])[-1] == str(l[x+2])[-1] == str(l[x+3])[-1]:
        a.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3])
A = max(a)
for x in range(len(l) - 4):
    l_5A = [int(n) for n in [l[x], l[x+1], l[x+2], l[x+3], l[x+4]] if n < A]
    if len(l_5A) == 1 and sum([l[x], l[x+1], l[x+2], l[x+3], l[x+4]]) % l_2 == 0:
        cnt += 1
        b.append(sum([l[x], l[x+1], l[x+2], l[x+3], l[x+4]]))
print(cnt, min(b))