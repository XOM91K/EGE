l = [[int(d) for d in x.split()] for x in open('9.txt')]
k = 0
for x in l:
    k += 1
    if x == sorted(x):
        ch = [d for d in x if x.count(d) > 1 and sum(map(int, str(d))) % 2 == 0]
        if len(ch) > 0:
            print(k, x, ch)