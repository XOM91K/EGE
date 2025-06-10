N = int(input())
ct = 0
mn_time = 10 ** 10
for n in range(N):
    h = int(input())
    m = int(input())
    mn_time = min(mn_time, h * 60 + m)
print(mn_time // 60, mn_time % 60)