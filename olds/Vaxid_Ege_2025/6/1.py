from turtle import *
pd()
tracer(0)
m = 20
lt(90)
for x in range(8):
    fd(11 * m)
    rt(90)
    fd(25 * m)
    rt(90)
up()
fd(7 * m)
rt(90)
fd(2 * m)
lt(90)
pd()
for x in range(8):
    fd(59 * m)
    rt(90)
    fd(71 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'green')
done()