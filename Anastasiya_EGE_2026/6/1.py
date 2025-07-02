from turtle import *
shape('turtle')
tracer(0)
lt(90)
m = 25
for x in range(2):
    fd(7 * m)
    rt(90)
    fd(4 * m)
    rt(90)
up()
fd(2 * m)
rt(90)
fd(5 * m)
lt(90)
down()
for x in range(2):
    fd(3 * m)
    rt(90)
    fd(4 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(8, 'red')

done()