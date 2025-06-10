def f(x,y,s):
    if x > y or s.count('b') > 3:
        return 0
    if x == y and s[-1] != 'a':
        return 0
    if x == y and s[-1] == 'a':
        return 1
    if x < y:
        return f(x+3,y,s +'a') + f(x+4,y,s + 'b') + f(x**2,y,s + 'c')
print(f(4,64,''))