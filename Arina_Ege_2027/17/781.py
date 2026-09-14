l = [int(x) for x in open("781.txt")]
mx = []
mx4 = min([x for x in l if x > 0 and str(x)[-1] == "4"])
for i in range(len(l)-2):
    tot1 = sum([int(x) for x in str(abs(l[i]))])
    tot2 = sum([int(x) for x in str(abs(l[i + 1]))])
    tot3 = sum([int(x) for x in str(abs(l[i + 2]))])
    if tot1 + tot2 + tot3 == mx4:
        mx.append(l[i]+l[i+1]+l[i+2])
print(len(mx), max(mx))