a = int(input())
mx = 0
yes = 'NO'
for i in range(a):
    d = int(input())
    if d > mx:
        mx = d
    if d == 0:
        yes = 'YES'
print(mx)
print(yes)