l = [[int(d) for d in x.split()] for x in open('9.txt')]
k = 0
sm = 0
for x in l:
    k += 1
    sr = sum(x) / len(x)
    if sr in x:
        kv = [y for y in x if y ** 0.5 % 1 == 0]
        if len(kv) > 0 and k % 2 == 0:
            sm += k
print(sm)