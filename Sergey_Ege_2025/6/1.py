from turtle import *
speed(1000)
color('red', 'red')
m = 10
penup()
lt(90)
for x in range(9):
    fd(15 * m)
    rt(90)
    fd(25 * m)
    rt(90)
penup()
bk(10 * m)
rt(90)
pendown()
for x in range(8):
    fd(15 * m)
    lt(90)
    fd(25 * m)
    lt(90)
penup()
fd(6 * m)
lt(90)
pendown()
for x in range(7):
    fd(15 * m)
    rt(90)
    fd(25 * m)
    rt(90)
speed(10000)

for x in range(-15, 20):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(6, 'blue')
update()
done()