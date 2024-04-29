def f(num):
    num += 1
    if num == 5:
        return 0
    return f(num) + 1
print(f(2))
#f(2)
#f(3) + 1 = 1 + 1 = 2
#f(4) + 1 => 0 + 1 = 1