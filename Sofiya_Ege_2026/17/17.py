l = [int(x) for x in open('17.txt')]
ans = []
mx = max(l)
for x in range(len(l) - 2):
    n1 = l[x]
    n2 = l[x + 1]
    n3 = l[x + 2]
    otri = [a for a in [n1, n2, n3] if a < 0]
    pol = [a for a in [n1, n2, n3] if a > 0]
    if abs(sum(otri)) <= sum(pol):
        if abs(n1 * n2 * n3) % 10 == mx % 10:
            ans.append(abs(n1) * abs(n2) * abs(n3))
print(len(ans), max(ans))
