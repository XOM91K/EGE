l = [int(x) for x in open('15.txt')]
mx = []
sm_otr = sum([d for d in l if d < 0])
for x in range(len(l) - 2):
    if max(l[x], l[x + 1], l[x + 2]) * min(l[x], l[x + 1], l[x + 2]) > sm_otr:
      mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), abs(max(mx)))