l = [[int(d) for d in x.split()] for x in open('9.txt')]
k = 0
for x in l:
    k += 1
    if sorted(x) == x:
        if len(set(x)) < 5:
            print(k, x)
