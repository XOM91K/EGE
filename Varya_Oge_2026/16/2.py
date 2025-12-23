d = int(input())
mx = 0
for x in range(d):
    a = int(input())
    if str(a)[-1] == '9':
        mx = max(mx, a)
print(mx)
# 9121231231239