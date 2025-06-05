l = [[int(d) for d in x.split()] for x in open('9.txt')]
cnt = 0

for x in l:
    k = 0
    p = [j for j in x if x.count(j) == 3]
    n = [j for j in x if x.count(j) == 1]
    if len(p) == 3 and len(n) == 3:
        for i in l:
            if i[0] == p[0]:
                k += 1
        for i in n:
            j = 0
            for r in l:
                if r[-1] == i:
                    j += 1
            if j == 337:
                break
        if j == 337 or k == 337:
            cnt += 1
print(cnt)