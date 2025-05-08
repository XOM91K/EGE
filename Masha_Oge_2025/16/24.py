a = int(input())
mn_time = []
for i in range(a):
    p = input().split(' ') # 1:59 7  => ['1:30', '1']
    t = p[0].split(':')  # ['1', '59']
    h = int(p[1])
    M = int(t[0])
    S = int(t[1])
    res = M * 60 + S
    res += h * 2
    mn_time.append(res)
mn_time = min(mn_time)
print(f'{mn_time // 60}:{mn_time % 60}')

# t = '2:59'
# print(int(t[0]))
# print(int(t[-2] + t[-1]))