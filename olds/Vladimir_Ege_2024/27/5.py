l = [int(x) for x in open('5.txt')]
mn_razn = 10 ** 10
A = l[:1000]
B = l[1000:]
for x in A:
    for y in B:
        mn_razn = min(mn_razn, abs(x - y))
print(mn_razn)