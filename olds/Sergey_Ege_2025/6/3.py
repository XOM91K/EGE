from turtle import *
m = 10
speed(1000)
tracer(0)
lt(90)
up()
for x in range(9):
    fd(15 * m)
    rt(90)
    fd(25 * m)
    rt(90)
up()
bk(10 * m)
rt(90)
pd()
for x in range(8):
    fd(15 * m)
    lt(90)
    fd(25 * m)
    lt(90)
up()
fd(6 * m)
lt(90)
pd()
for x in range(7):
    fd(15 * m)
    rt(90)
    fd(25 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'blue')
done()