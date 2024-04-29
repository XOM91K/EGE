def f(a,b):
    if a<b or a == 15:
        return 0
    if a==b:
        return 1
    if a>b:
        return f(a//3, b)+f(a-2, b)+f(a-5, b)
print(f(32, 9))
#47
#29
#36