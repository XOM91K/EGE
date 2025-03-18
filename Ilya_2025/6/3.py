from turtle import *
lt(90) #left
speed(1000)
tracer(0)
m = 7
for x in range(4):
    fd(28 * m) #forward
    rt(90) #right
    fd(26 * m)
    rt(90)
up() #penup
fd(8 * m)
rt(90)
fd(7 * m)
lt(90)
pd() #pendown
for x in range(4):
    fd(67 * m) #forward
    rt(90) #right
    fd(98 * m)
    rt(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(4, 'blue')
done()