l = [int(x) for x in open('4.txt')]
mn = min(l)
mn_pair = []
for x in range(len(l) - 1):
    if l[x] % 111 == mn or l[x + 1] % 111 == mn:
        mn_pair.append(l[x] + l[x + 1])
print(len(mn_pair), min(mn_pair))

#0.985771656036377
#0.03400993347167969