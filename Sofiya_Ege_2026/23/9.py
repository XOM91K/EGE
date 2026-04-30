def f(x, y):
    if x>y or x==32: return 0
    if x==y: return 1
    if x<y: return f(x+1, y)+f(x+2, y)+f(x+4, y)+f(x+8, y)
print(f(16, 24)*f(24, 48))
def f(x, y):
    if x>y or x==24: return 0
    if x==y: return 1
    if x<y: return f(x+1, y)+f(x+2, y)+f(x+4, y)+f(x+8, y)
print(f(16, 32)*f(32, 48))
print(11428032 + 11253585)