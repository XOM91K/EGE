def f(x, y, k):
    if x>y or k.count('2')>3: return 0
    if x==y: return 1
    if x<y: return f(x+3, y, k+'1')+f(x+4, y, k+'2')+f(x**2, y, k+'3')
print(f(4, 61, ''))