from turtle import *
speed(10000)
tracer(0)
m = 30
left(90)
for x in range(13):
    fd(17 * m)
    lt(90)
    fd(15 * m)
    lt(90)
up()
fd(10 * m)
lt(90)
fd(10 * m)
rt(90)
down()
for x in range(40):
    fd(100 * m)
    rt(90)
    fd(200 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'blue')
done()