from turtle import *
speed(1000)
color('red', 'blue')
m = 20
lt(90) #left
rt(30)
begin_fill()
for x in range(10):
    fd(7 * m) #forward
    rt(60) #right
    fd(7 * m)
    rt(120)
end_fill()
ct = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        t = getcanvas().find_overlapping(x * m, y * m, x * m, y * m)
        if len(t) == 1 and t[0] == 5:
            ct += 1
print(ct)
done()
