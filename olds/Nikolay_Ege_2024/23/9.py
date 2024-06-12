def f(x,y,z):
    if x>y or ('BB' in z):
        return 0
    if x ==y:
        return 1
    if x<y:
        return f(x+2,y, z + 'A') + f(x**2,y, z + 'B') + f(x*3,y, z + 'C')
print(f(2, 64, ''))
