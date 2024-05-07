import math
l = sorted([int(x) for x in open('11.txt')])
s50 = []
for x in l:
    if x <= 50:
        s50.append(x)
l1 = []
for x in l:
    if x > 50:
        l1.append(x)
s_l = []
for x in range(len(l1) // 2):
    s_l.append(l1[-(x + 1)])
    s_l.append(l1[x])
if len(l1) % 2 != 0:
    s_l.append(l1[len(l1) // 2])
print(s_l)
sm = 0
sm_skidka = 0
mx_skidka = 0
for x in range(len(s_l)):
    if x % 2 != 0:
        sm_skidka += (s_l[x] - (s_l[x] * 0.25))
        mx_skidka = max(mx_skidka, s_l[x])
    else:
        sm += s_l[x]
sm_skidka = math.ceil(sm_skidka)
sm = sm + sm_skidka + sum(s50)
print(sm)
print(mx_skidka)