l = [[int(d) for d in x.split()] for x in open('11.txt')]
k = 0
for x in l:
    k += 1
    # [22, 22, 45, 41]
    if x == sorted(x):
        ch = [y for y in x if sum(map(int, str(y))) % 2 == 0]
        if len(ch) > 0:
            print(k)