l = [[int(d) for d in x.split()] for x in open('stg1.txt')]
sm = 0
k = 0
for x in l:
    k += 1
    sr = sum(x) // len(x)
    if sr in x:
        usl2 = [d for d in x if d ** 0.5 % 1 == 0]
        if len(usl2) > 0:
            if k % 2 == 0:
                sm += k
print(sm)