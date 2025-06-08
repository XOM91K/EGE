def f(k,k1,m):
    if k+k1 >= 323:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(k+3,k1,m-1),f(k*2,k1,m-1),f(k,k1+3,m-1),f(k,k1*2,m-1)]
    return any(h) if m%2 != 0 else any(h)
print('19',[s for s in range(1,200) if f(123,s,2)])
print('20',[s for s in range(1,200) if f(123,s,3)])
print('21',[s for s in range(1,200) if f(123,s,4)])