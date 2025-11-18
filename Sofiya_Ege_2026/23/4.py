def f(x, y, s):
    if x>y or 'ab' in s: return 0
    if x==y: return 1
    if x<y: return f(x+3, y, s + 'a')+f(x*5, y, s + 'b')+f(x*7, y, s + 'c')
print(f(1, 1000, ''))