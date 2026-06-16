def f(st,fn,s):
    if st>fn or s[:1] == 'A' or s[:1] == 'C':
        return 0
    elif st==fn and s[-1] not in 'AC':
        return 1
    return f(st+5,fn,s+'A') + f(st+10, fn, s+'B') + f(st*3,fn,s+'C')
print(f(5,165,''))