a = 0
mx = 0
mn = 10 ** 10
while a != 99999:
    a = int(input())
    mx = max(mx, a)
    mn = min(mn, a)
print(mx, mn)