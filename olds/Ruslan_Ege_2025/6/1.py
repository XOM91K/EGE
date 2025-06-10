from turtle import *
m = 20
speed(1000)
pendown()
lt(90)
for x in range(2):
    fd(10 * m)
    rt(90)
    fd(4 * m)
    rt(90)
penup()
fd(3 * m)
rt(90)
fd(6 * m)
lt(90)
pendown()
for x in range(2):
    fd(8 * m)
    rt(90)
    fd(6 * m)
    rt(90)
for x in range(-15, 15):
    for y in range(-15, 15):
        goto(x * m, y * m)
        dot(6, 'red')
done()