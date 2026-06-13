from turtle import *
speed(1000)
tracer(0)
m = 13
for x in range(8):
    fd(15 * m)
    rt(60)
    fd(10 * m)
    rt(60)

up()
for x in range(-25, 25):
    for y in range(-25, 25):
        goto(x * m, y * m)
        dot(3, 'red')
done()z