import sys,functools
sys.setrecursionlimit(1000000000)
#@functools.lru_cache(None)
# def f(n):
#     if n >=10000:
#         return n
#     elif n <10000 and n%2==0:
#         return 1+f(n/2)
#     elif n < 10000 and n %2!=0:
#         return n**n+f(n+2)
# for x in range(10500, 1, -1):
#     f(x)
#     print(f(x))
#print(f(192)-f(9))
dl = [0] * 10003
dl[-1] = 10002
dl[-2] = 10001
dl[-3] = 10000
for x in range(10000, 1, - 1):
    if x % 2 == 0:
        dl[x] = 1 + dl[x // 2]
print(dl[10002])