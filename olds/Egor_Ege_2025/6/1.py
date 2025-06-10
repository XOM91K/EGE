from turtle import *
shape('turtle')
lt(90)
screensize(1920, 1080)
tracer(0)
m = 20
for x in range(3):
    fd(30 * m)
    rt(90)
    fd(10 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(5 * m)
lt(90)
down()
for x in range(4):
    fd(100 * m)
    rt(90)
    fd(90 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')
done()