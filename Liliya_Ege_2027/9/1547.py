l = [[int(d) for d in x.split()] for x in open('1547.txt')]
sm = 0
for x in l:
    if x == sorted(x)[::-1]:
        # 44 44 44 1 2 3
        povt3 = [d for d in x if x.count(d) == 3]
        povt2 = [d for d in x if x.count(d) == 2]
        if len(povt3) == 3 and len(povt2) == 2:
            if min(povt3 + povt2) > sum(x) - sum(povt3) - sum(povt2):
                sm += sum(x)
print(sm)