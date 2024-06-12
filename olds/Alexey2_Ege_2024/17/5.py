l = [int(x) for x in open('5.txt')]
sr_ar = 0
sm = 0
ct = 0
for x in l:
    if len(str(x)) == 4:
      sm += x
      ct += 1
sr_ar = sm / ct
ct_pair = 0
sm_pair = 0
for x in range(len(l) - 1):
    if (l[x] + l[x + 1]) not in l:
        if (l[x] + l[x + 1]) < sr_ar:
            ct_pair += 1
            sm_pair = max(sm_pair, sum(map(int, str(l[x]) + str(l[x + 1]))))
print(ct_pair)
print(sm_pair)