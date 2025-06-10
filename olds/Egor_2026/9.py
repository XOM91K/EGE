def tr(number):
    ost = ''
    while number > 0:
        ost = ost + str(number % 3)
        number = number // 3
    ost = ost[::-1]
    return ost
d = 14
print(tr(d))