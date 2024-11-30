d = int(input())
mn = 10 ** 10
for x in range(d):
    h = int(input())
    m = int(input())
    mm = h z* 60 + m
    mn = min(mn, mm)
print(mn // 60, mn % 60)
# print(9 / 5)