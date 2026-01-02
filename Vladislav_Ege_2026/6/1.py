from turtle import *
lt(90)
tracer(0)
m = 20
for x in range(2):
    fd(10 * m)
    rt(90)
    fd(4 * m)
    rt(90)
up()
fd(3 * m)
rt(90)
fd(6 * m)
lt(90)
down()
for x in range(2):
    fd(8 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'red')
done()