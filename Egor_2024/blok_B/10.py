ct = 0
mx = 0
while ct < 30:
    N = int(input())
    if -100 <= N <= 100:
        ct += 1
        mx = max(mx, N)
print(mx)