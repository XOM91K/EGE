def f(x,y):
    if x > y or x == 17 or x == 32 or x == 50:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1 , y) + f(x + 5, y) + f(x ** 2 , y)
print(f(5, 25) * f(25, 45) * f(45, 60))