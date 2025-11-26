def f(st,fn):
    if st<fn:
        return 0
    elif st==fn:
        return 1
    return f(st-sum(map(int,str(st))), fn) + f(st - int(str(st**2)[0]), fn)
print(f(32,1))