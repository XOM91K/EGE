d = int(input())
mx = 0
for x in range(d):
    a = int(input())
    if a % 5 == 0:
        mx = max(mx, a)
print(mx)