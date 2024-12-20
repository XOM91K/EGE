def su(a):
    return sum([int(x) for x in str(abs(a))])


l = [int(x) for x in open('6.txt')]
mi = [x for x in l if x >= 0 and str(x)[-1] == "4"]
mi = min(mi)
ans = []
for x in range(len(l) - 2):
    if int(su(l[x])) + int(su(l[x+1])) + int(su(l[x+2])) == int(mi):
        ans.append(l[x] + l[x+1] + l[x+2])
print(len(ans), max(ans))