num = -1
tr = []
sm = 0
while num != 0:
    num = int(input())
    tr.append(num)
    if len(tr) % 3 == 0:
        if (tr[0] + tr[-1]) / 2 == tr[1]:
           sm += sum(tr)
           tr.clear()
print(sm)