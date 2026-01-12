# import sys
# sys.setrecursionlimit(1000000)
# def g(n):
#     if n<25: return n
#     if n>=25: return (n-5)*g(n-6)
# print((g(60_000)-315*g(59994))/g(59998))
def f(s, m):
    if s>=77: return m%2==0
    if m==0: return 0
    h=[f(s+1, m-1), f(s+4, m-1), f(s*2, m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print('19', [s for s in range(1, 77) if not f(s, 1) and f(s, 2)])
print('20', [s for s in range(1, 77) if not f(s, 1) and f(s, 3)])
print('21', [s for s in range(1, 77) if not f(s, 2) and f(s, 4)])