d = 1
l = []
while d != 0:
    d = int(input())
    if d == 0:
        break
    if d % 7 == 0 and str(d)[-1] == '2':
        l.append(d)
print(sum(l))