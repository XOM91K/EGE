def f(x, y):
    if x<y: return 0
    if x==y: return 1
    if x>y: return f(x-int(str(x**2)[0]), y)+ f(x-sum(map(int, str(x))), y)
print(f(32, 1))