def f(x,y):
    if x>y or x==16:
        return 0
    if x == y :
        return 1
    if x< y:
        return f(x+2,y)+f(x+3,y)+f(x**2,y)
print(f(2,25)*f(25,42))
