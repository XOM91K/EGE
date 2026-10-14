s = [int(x) for x in open('1255.txt')] # 32 64 1 2 3
ln32 = len([x for x in s if x % 32 == 0])
ans = 0
mx = []
for i in range(len(s) - 1):
    if s[i] < 0 or s[i + 1] < 0:
        summa = s[i] + s[i + 1]
        if summa < ln32:
            ans += 1
            mx.append(summa)

print(ans, max(mx))