from turtle import *
lt(90)
tracer(0)
m = 15
for x in range(2):
    fd(24 * m)
    rt(90)
    fd(10 * m)
    rt(90)
fd(3 * m)
lt(90)
fd(13 * m)
rt(90)
for x in range(2):
    fd(9 * m)
    rt(90)
    fd(32 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'red')

done()