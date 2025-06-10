ct = 0
mx = 0
mn = 10001
for i in range(2000):
    a = int(input())
    if -100 <= a <= 10000:
        if a % 6 == 0 or str(a)[-1] == '1':
            ct += 1
            mx = max(mx, a)
            mn = min(mn, a)
print(ct, mx, mn)