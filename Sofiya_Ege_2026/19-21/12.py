def f(s,m):
    if s>=231: return m%2==0
    if m==0: return 0
    if m%2!=0: #Петя
        h=[f(s+3,m-1),f(s*3,m-1)]
    if m%2==0: #Ваня
        h=[f(s+5,m-1),f(s*3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print([s for s in range(10,121) if not f(s,1) and f(s,2)])
print([s for s in range(10,121) if not f(s,1) and not f(s,2) and  f(s,3)])
print([s for s in range(10,121) if not f(s,2) and f(s,4)])