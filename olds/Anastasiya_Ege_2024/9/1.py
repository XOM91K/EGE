l = [sorted([int(y) for y in x.split()]) for x in open('1.txt')]
c = 0
for x in l:
    if max(x) - min(x) >= 50:
        pr = 1
        for number in x:
            pr = pr * number
        pr = pr // max(x) // min(x)
        if pr <= 1000:
            c += 1
print(c)