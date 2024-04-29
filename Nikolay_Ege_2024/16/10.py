def prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
ct=0
a=[]
def f(n):
    if n ==0:
        return 1
    if n>0:
        return 7*(n-1)+f(n-1)

for n in range(2,201):
    if prime(f(n)):
        ct += 1
print(ct)