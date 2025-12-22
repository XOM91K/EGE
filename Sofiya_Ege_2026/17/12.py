l = [int(x) for x in open('12.txt')]
d = max([x for x in l if str(abs(x))[0] == '8'])
ans = []
for x in range(len(l) - 2):
    n1 = l[x]
    n2 = l[x + 1]
    n3 = l[x + 2]
    if (str(abs(n1))[0] == '6') + (str(abs(n2))[0] == '6') + (str(abs(n3))[0] == '6') <= 1:
        if (n1 + n2 + n3) >= d:
            ans.append(n1 + n2 + n3)
print(len(ans), min(ans))
