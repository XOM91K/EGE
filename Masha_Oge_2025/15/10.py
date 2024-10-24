A = int(input())
mx=0
for x in range(A):
    x=int(input())
    if x % 10 == 9:
        mx=max(mx,x)
print(mx)